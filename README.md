# Medical Report Summarizer  
**AI-Powered PDF to Clinical Summary in Seconds**

A beautiful, fully offline, privacy-first web tool that lets you **upload any medical report in PDF format** and instantly generates a **clear, professional, AI-written summary** using the T5 transformer model.

No data leaves your device • Works 100% locally • Export summaries as stunning PDFs

Perfect for doctors, nurses, medical students, researchers, and anyone managing health records.

### Screenshots:

**light mode:**

<img width="980" height="877" alt="image" src="https://github.com/user-attachments/assets/bc94c3fe-9d49-4836-a8f5-aef2eb12f4e6" />
<img width="976" height="592" alt="image" src="https://github.com/user-attachments/assets/882ee9dc-7eec-4c6f-bd00-68b6f9316323" />

<br/>
<br/>

**dark mode:**

<img width="948" height="876" alt="image" src="https://github.com/user-attachments/assets/0151b026-0680-4dfb-998c-c9d93a526a5e" />
<img width="989" height="605" alt="image" src="https://github.com/user-attachments/assets/9e3d8951-fbab-4635-a8e8-444bf587b3a3" />

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

# 2. Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

python app.py

# 3. Install dependencies
pip install Flask transformers torch PyPDF2 weasyprint Werkzeug

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
Extract zip and open in idle(Vscode)

<img width="808" height="728" alt="image" src="https://github.com/user-attachments/assets/b6af7335-677b-4d61-b766-2c31a2cc0389" />


**Step 4:** 
Install dependencies
```bash

# Install dependencies
pip install Flask transformers torch PyPDF2 weasyprint Werkzeug

```
Run in terminal of idle.

**Step 5:** 
Run app.py from idle

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
