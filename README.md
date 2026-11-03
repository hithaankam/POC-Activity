# QPSK Modulation and Demodulation POC

## Objective
Implement a QPSK communication-system simulation in MATLAB and analyze its Bit Error Rate (BER) over an AWGN channel.

## Requirements
- MATLAB R2020b or later
- Communications Toolbox recommended

## How to Run
1. Open MATLAB.
2. Set the current folder to this project directory.
3. Run:

```matlab
qpsk_simulation
```

The generated plots are saved in the `results` folder.

## What the Program Demonstrates
- Random binary data generation
- Bit-pair to QPSK symbol mapping
- Transmission over an AWGN channel
- Minimum-distance symbol detection
- BER calculation for 0–20 dB Eb/N0
- Constellation and BER plots

## Results
The constellation diagram shows ideal and noisy symbols. The BER curve demonstrates improved performance as the signal-to-noise ratio increases.

## Project Report
See `QPSK_Project_Report.md` for the complete report.

## GitHub Repository
GitHub Repository: https://github.com/hithaankam/POC-Activity
