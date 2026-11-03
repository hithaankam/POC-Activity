%% QPSK Modulation and Demodulation POC
% Demonstrates QPSK transmission over an AWGN channel and calculates BER.
clear; clc; close all;

rng('default');              % Reproducible results
numberOfBits = 20000;
EbN0dB = 0:2:20;

bits = randi([0 1], numberOfBits, 1);

% Convert each pair of bits into one QPSK symbol.
% [b1 b2] mapping: 00 -> +45deg, 01 -> +135deg,
%                  11 -> -135deg, 10 -> -45deg (Gray coding).
if mod(numberOfBits, 2) ~= 0
    bits(end + 1) = 0;
end
bitPairs = reshape(bits, 2, []).';
symbolIndex = bitPairs(:, 1) * 2 + bitPairs(:, 2);

constellation = (1/sqrt(2)) * [ 1+1j  -1+1j  -1-1j  1-1j ];
transmittedSymbols = constellation(symbolIndex + 1).';

BER = zeros(size(EbN0dB));

for k = 1:length(EbN0dB)
    % Each QPSK symbol carries two bits.
    EbN0 = 10^(EbN0dB(k)/10);
    noiseVariance = 1 / (2 * EbN0);
    noise = sqrt(noiseVariance) * ...
        (randn(size(transmittedSymbols)) + 1j*randn(size(transmittedSymbols)));

    receivedSymbols = transmittedSymbols + noise;

    % Detect each received symbol using minimum Euclidean distance.
    distance = abs(receivedSymbols - constellation);
    [~, nearestIndex] = min(distance, [], 2);
    detectedIndex = nearestIndex - 1;

    detectedPairs = [bitget(detectedIndex, 2) bitget(detectedIndex, 1)];
    detectedBits = reshape(detectedPairs.', [], 1);

    BER(k) = sum(detectedBits ~= bits) / length(bits);
end

% QPSK constellation at the noisy received symbols.
scatterNoiseVariance = 1 / 10;
scatterNoise = sqrt(scatterNoiseVariance) * ...
    (randn(size(transmittedSymbols)) + 1j*randn(size(transmittedSymbols)));
receivedAt10dB = transmittedSymbols + scatterNoise;

figure('Name', 'QPSK Constellation');
scatter(real(receivedAt10dB), imag(receivedAt10dB), 12, 'b', 'filled');
hold on;
scatter(real(transmittedSymbols(1:500)), imag(transmittedSymbols(1:500)), ...
    25, 'r', 'LineWidth', 1.5);
axis([-2 2 -2 2]); axis square; grid on;
xlabel('In-phase (I)'); ylabel('Quadrature (Q)');
title('QPSK Constellation after AWGN Channel');
legend('Received symbols', 'Ideal symbols', 'Location', 'northwest');
saveas(gcf, 'results/qpsk_constellation.png');

figure('Name', 'QPSK BER Curve');
semilogy(EbN0dB, BER, '-o', 'LineWidth', 2, 'MarkerFaceColor', 'b');
grid on;
xlabel('Eb/N0 (dB)'); ylabel('Bit Error Rate (BER)');
title('QPSK BER Performance in AWGN Channel');
saveas(gcf, 'results/qpsk_ber_curve.png');

fprintf('Number of transmitted bits: %d\n', length(bits));
fprintf('BER at 20 dB: %.6f\n', BER(end));
