# Medical Report Summarizer  
**AI-Powered PDF to Clinical Summary in Seconds**

A beautiful, fully offline, privacy-first web tool that lets you **upload any medical report in PDF format** and instantly generates a **clear, professional, AI-written summary** using the T5 transformer model.

No data leaves your device • Works 100% locally • Export summaries as stunning PDFs

Perfect for doctors, nurses, medical students, researchers, and anyone managing health records.

### Screenshots:

**light mode:**

<img width="900" height="925" alt="image" src="https://github.com/user-attachments/assets/86febd76-a983-43b8-aab6-e475bc70d90c" />
<img width="937" height="555" alt="image" src="https://github.com/user-attachments/assets/4f23c33f-bc83-4fc8-84e8-486d7ebe486c" />

<br/>
<br/>

**dark mode:**

<img width="887" height="923" alt="image" src="https://github.com/user-attachments/assets/1d94e62c-1a8a-45f5-a4c9-4ac08891a1c9" />
<img width="896" height="567" alt="image" src="https://github.com/user-attachments/assets/e85bf75c-8019-46b8-b2fc-9bfa7c89bdbf" />

---

### Features

- Upload any medical PDF (digital or scanned)
- Smart text extraction with PyPDF2
- Abstractive summarization using **T5 (Google/Hugging Face)**
- Adjustable summary length 
- One-click **"Copy to Clipboard"**
- One-click **"Download as Professional PDF"** (with date, filename, disclaimer)
- Modern, responsive, medical-grade UI
- Zero cloud dependency — completely offline after setup

---

## Proceedure to run the website

### Prerequisites

**Downlaod and install python from www.python.org**

## Method 1

**Quick Start**

```bash
# 1. Clone the repo
git clone https://github.com/spacesaicodes1234/olympai_DHProdcutions.git
cd olympai_DHProdcutions
cd project

# 2. Install dependencies
pip install Flask transformers torch PyPDF2 weasyprint Werkzeug

# 3. Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

python app.py
```

Open your browser → http://127.0.0.1:5000
Upload a medical report → Get AI summary → Download or copy!

## Method 2

**Step 1:** 
Downlaod zip file from the GitHub repository on this website using the highlighted box below:

<img width="1605" height="631" alt="image" src="https://github.com/user-attachments/assets/0624d4bd-deec-44c0-9423-d8d199686f9e" />

**Step 2:** 
Get an idle(Vscode)

- Vscode: https://code.visualstudio.com/ (Install python extension)

**Step 3:** 
Extract zip and open in IDLE(Vscode)

<img width="808" height="728" alt="image" src="https://github.com/user-attachments/assets/b6af7335-677b-4d61-b766-2c31a2cc0389" />


**Step 4:** 
Install dependencies
```bash

# Install dependencies
pip install Flask transformers torch PyPDF2 weasyprint Werkzeug

```
Run in terminal of IDLE.

**Step 5:**

- Go to /project
- Run app.py from IDLE

<img width="1802" height="712" alt="image" src="https://github.com/user-attachments/assets/c31f02e4-ea6a-4614-9a66-68d14d2282fd" />


**Step 6:** 

Open local host: 
http://127.0.0.1:5000

---

### Description of each file and its purpose

| File/Folder | Purpose & Description |
|---|---|
| app.py | Main Flask application. Contains all backend logic: PDF upload, text extraction, T5 summarization, and PDF export generation. This is the only file you run. |
| templates/index.html | Frontend UI (single-page). Beautiful, responsive design with upload form, copy button, and "Download PDF" link. Uses Jinja2 templating to display the summary. |
| templates/credits.html | Credits page |
| requirements.txt | Complete list of Python dependencies with pinned versions for perfect reproducibility. |
| README.md | This file – full project documentation, setup guide, and file descriptions. |

---

### List of AI tools used: 

- T5 (Text-to-Text Transfer Transformer)
- Hugging Face Transformers
- Github Copilot for debugging
