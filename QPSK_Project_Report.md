# PROJECT REPORT

## QPSK Modulation and Demodulation using MATLAB

**Student:** Hitha Ankam  
**Course/Subject:** Communication Systems / POC Activity  
**Project Repository:** https://github.com/hithaankam/POC-Activity

---

## 1. Abstract

This project demonstrates Quadrature Phase Shift Keying (QPSK), a digital modulation technique that transmits two bits of information per symbol. MATLAB code generates random binary data, maps pairs of bits to QPSK symbols, adds Additive White Gaussian Noise (AWGN), detects the received symbols, and calculates the Bit Error Rate (BER) for different Eb/N0 values.

## 2. Introduction

Digital modulation converts binary information into an analog carrier waveform. In QPSK, the binary stream is divided into pairs and each pair is represented by one of four phase positions. QPSK therefore transmits twice the data rate of BPSK for the same symbol rate and has the same BER as BPSK for equal transmitted energy per bit.

## 3. Objectives

- Generate binary input data.
- Map input bit pairs to QPSK symbols.
- Transmit symbols through an AWGN channel.
- Detect symbols using minimum Euclidean distance.
- Calculate and plot BER against Eb/N0.
- Observe constellation spreading caused by noise.

## 4. QPSK Modulation

For each two-bit pair, a symbol is selected from:

- `00` → `(1 + j)/sqrt(2)`
- `01` → `(-1 + j)/sqrt(2)`
- `10` → `(-1 - j)/sqrt(2)`
- `11` → `(1 - j)/sqrt(2)`

This uses four phases separated by 90 degrees.

## 5. System Block Diagram

```text
Binary Data --> Serial-to-Parallel --> QPSK Mapping --> AWGN Channel
                                                              |
Detected Bits <-- QPSK Detection <-- Received Symbols ---------
``` 

## 6. MATLAB Implementation

The main implementation is in `qpsk_simulation.m`. It performs the following operations:

1. Generates 20,000 random binary bits.
2. Groups bits into pairs.
3. Maps the pairs to complex symbols.
4. Adds controlled Gaussian noise for each Eb/N0 value.
5. Detects received symbols using minimum Euclidean distance.
6. Compares detected and transmitted bits to calculate BER.
7. Saves constellation and BER plots.

## 7. Experimental Procedure

1. Open MATLAB and select the project directory.
2. Run `qpsk_simulation.m`.
3. Observe the QPSK constellation.
4. Observe the BER-versus-Eb/N0 curve.
5. Compare performance as the noise level decreases.

## 8. Expected Results

The received constellation should become more dispersed at low Eb/N0 and more concentrated around the four ideal points at high Eb/N0. BER should decrease rapidly as Eb/N0 increases.

## 9. Applications

- Satellite communication
- Wi-Fi systems
- Digital television broadcasting
- Mobile communication links

## 10. Conclusion

The MATLAB simulation successfully demonstrates QPSK modulation, an AWGN channel, symbol detection, and BER analysis. It provides a clear visual and numerical understanding of digital communication performance.

## Source Code and Repository

The complete project is available at: **https://github.com/hithaankam/POC-Activity**

## References

1. S. Haykin, *Communication Systems*, Wiley.
2. J. G. Proakis and M. Salehi, *Digital Communications*, McGraw-Hill.
3. MATLAB documentation on digital modulation and AWGN channel modeling.
