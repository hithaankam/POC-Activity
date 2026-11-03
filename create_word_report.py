from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

report = Document()
section = report.sections[0]
section.top_margin = Inches(0.75)
section.bottom_margin = Inches(0.75)

styles = report.styles
styles['Normal'].font.name = 'Times New Roman'
styles['Normal'].font.size = Pt(11)

p = report.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run('PROJECT REPORT')
r.bold = True
r.font.size = Pt(18)

p = report.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run('QPSK Modulation and Demodulation using MATLAB')
r.bold = True
r.font.size = Pt(16)

for text in ['Student: Hitha Ankam', 'Subject: Communication Systems / POC Activity', 'Repository: [ADD_GITHUB_REPOSITORY_LINK]']:
    p = report.add_paragraph(text)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER

report.add_page_break()

sections = {
'1. Abstract': 'This project demonstrates Quadrature Phase Shift Keying (QPSK), a digital modulation technique that transmits two bits of information per symbol. MATLAB code generates random binary data, maps pairs of bits to QPSK symbols, adds Additive White Gaussian Noise, detects received symbols, and calculates the Bit Error Rate for different Eb/N0 values.',
'2. Introduction': 'Digital modulation converts binary information into an analog carrier waveform. QPSK divides the binary stream into pairs, with each pair represented by one of four phase positions. It transmits two bits per symbol.',
'3. Objectives': 'Generate binary input data; map input pairs to QPSK symbols; transmit symbols over AWGN; detect symbols using minimum Euclidean distance; calculate and plot BER; and observe constellation spreading.',
'4. QPSK Modulation': '00 → (1+j)/sqrt(2)\n01 → (-1+j)/sqrt(2)\n10 → (-1-j)/sqrt(2)\n11 → (1-j)/sqrt(2)\nThe four points are separated by 90 degrees.',
'5. System Block Diagram': 'Binary Data → Serial-to-Parallel Conversion → QPSK Mapping → AWGN Channel → QPSK Detection → Recovered Binary Data',
'6. MATLAB Implementation': 'The main implementation is in qpsk_simulation.m. It generates 20,000 random bits, groups them into pairs, maps them to complex symbols, adds controlled Gaussian noise, detects symbols using minimum Euclidean distance, calculates BER, and saves plots.',
'7. Experimental Procedure': '1. Open MATLAB and select the project directory.\n2. Run qpsk_simulation.m.\n3. Observe the constellation diagram.\n4. Observe the BER-versus-Eb/N0 curve.\n5. Compare performance as noise decreases.',
'8. Expected Results': 'At low Eb/N0, the received constellation is dispersed. At high Eb/N0, it becomes concentrated near the four ideal points. BER decreases as Eb/N0 increases.',
'9. Applications': 'Satellite communication, Wi-Fi systems, digital television broadcasting, and mobile communication links.',
'10. Conclusion': 'The MATLAB simulation successfully demonstrates QPSK modulation, an AWGN channel, symbol detection, and BER analysis.',
'Source Code and Repository': 'Complete source code repository: [ADD_GITHUB_REPOSITORY_LINK]',
'References': '1. S. Haykin, Communication Systems, Wiley.\n2. J. G. Proakis and M. Salehi, Digital Communications, McGraw-Hill.\n3. MATLAB documentation for digital modulation and AWGN channel modeling.'
}

for heading, body in sections.items():
    report.add_heading(heading, level=1)
    for line in body.split('\n'):
        if line.strip():
            report.add_paragraph(line.strip())

report.save('QPSK_Project_Report.docx')
print('Created QPSK_Project_Report.docx')
