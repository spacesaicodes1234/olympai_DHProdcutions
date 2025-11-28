# Medical Report Summarizer  
**AI-Powered PDF to Clinical Summary in Seconds**

A beautiful, fully offline, privacy-first web tool that lets you **upload any medical report in PDF format** and instantly generates a **clear, professional, AI-written summary** using the T5 transformer model.

No data leaves your device • Works 100% locally • Export summaries as stunning PDFs

Perfect for doctors, nurses, medical students, researchers, and anyone managing health records.

### Screenshots:
<img width="1057" height="931" alt="image" src="https://github.com/user-attachments/assets/bafa9f18-4eb6-482b-8819-4860247a0121" />
<img width="970" height="722" alt="image" src="https://github.com/user-attachments/assets/e418ce08-a68e-47a7-b544-9ad498731ad3" />
<img width="970" height="722" alt="image" src="https://github.com/user-attachments/assets/abbf3db6-11f9-42ee-8f8b-38b491ebd1b1" />

---

### Features

- Upload any medical PDF (digital or scanned)
- Smart text extraction with PyPDF2
- Abstractive summarization using **T5 (Google/Hugging Face)**
- Adjustable summary length (short, medium, detailed)
- One-click **"Copy to Clipboard"**
- One-click **"Download as Professional PDF"** (with date, filename, disclaimer)
- Modern, responsive, medical-grade UI
- Zero cloud dependency — completely offline after setup

---

### Live Demo (Local)
Run the app and visit:  
http://127.0.0.1:5000

---

### Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/spacesaicodes1234/olympai_DHProdcutions.git
cd olympai_DHProdcutions
cd project

# 2. Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

```

Open your browser → http://127.0.0.1:5000
Upload a medical report → Get AI summary → Download or copy!

### File/Folder,Purpose & Description

| File/Folder | Purpose & Description |
|---|---|
| app.py | Main Flask application. Contains all backend logic: PDF upload, text extraction, T5 summarization, and PDF export generation. This is the only file you run. |
| templates/index.html | Frontend UI (single-page). Beautiful, responsive design with upload form, copy button, and "Download PDF" link. Uses Jinja2 templating to display the summary. |
| templates/credits.html | Credits page |
| requirements.txt | Complete list of Python dependencies with pinned versions for perfect reproducibility. |
| README.md | This file – full project documentation, setup guide, and file descriptions. |
