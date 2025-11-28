# Medical Report PDF Summarizer (T5 Transformer)

A beautiful, 100% local, privacy-first web app that turns any medical report PDF into a clear, professional AI summary in seconds — with one-click PDF export.

- No data ever leaves your computer  
- Works completely offline after first download  
- Export summaries as clean, printable PDFs  
- Modern UI with copy & download buttons  

Perfect for doctors, nurses, researchers, medical students, and personal health records.

### Live Demo Screenshot
(Imagine a clean blue-white interface with upload area and a nicely formatted summary card)

### Features
- Upload medical PDFs (digital or scanned)
- Automatic text extraction
- AI abstractive summarization using Google's T5 model
- One-click "Copy to Clipboard"
- One-click "Download Summary as PDF" (with date, filename, disclaimer)
- Responsive, professional medical-style design
- Zero external API calls — fully private


### Quick Start (2 minutes)

1. Save the Python code as `medical_summarizer.py`
2. Open terminal/command prompt in that folder
3. Run these commands:

```bash
# Create virtual environment (recommended)
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install everything
pip install flask transformers torch sentencepiece PyPDF2 weasyprint

# Run the app
python medical_summarizer.py
