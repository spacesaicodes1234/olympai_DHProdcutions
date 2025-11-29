# Medical Report Summarizer  
**AI-Powered PDF to Clinical Summary in Seconds**

A beautiful, fully offline, privacy-first web tool that lets you **upload any medical report in PDF format** and instantly generates a **clear, professional, AI-written summary** using the T5 transformer model.

No data leaves your device • Works 100% locally • Export summaries as stunning PDFs

Perfect for doctors, nurses, medical students, researchers, and anyone managing health records.

### Screenshots:

**light mode:**

<img width="1250" height="929" alt="image" src="https://github.com/user-attachments/assets/6a874b82-6e77-4338-8f05-f5a74158a544" />
<img width="1306" height="738" alt="image" src="https://github.com/user-attachments/assets/ae483b89-c156-4613-b0e4-665164938db3" />

**dark mode:**

<img width="1191" height="927" alt="image" src="https://github.com/user-attachments/assets/aaddf408-6650-4fee-b0a8-8d3928a208d2" />
<img width="1259" height="742" alt="image" src="https://github.com/user-attachments/assets/0dbac3c6-6456-497d-9eee-c8ffd59b146a" />





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

### Method 1

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
pip install -r requirements.txt

```

Open your browser → http://127.0.0.1:5000
Upload a medical report → Get AI summary → Download or copy!

### Method 2

**Step 1:** 
Downlaod python from www.python.org

**Step 2:** 
Downlaod zip from github repo
<img width="1691" height="652" alt="image" src="https://github.com/user-attachments/assets/b1e64938-c826-4338-a22f-a219ebaef693" />

**Step 3:** 
Get an idle(Vscode,thonny,pycharm,etc)

- Vscode: https://code.visualstudio.com/ (Install python extension)
- Thonny: https://thonny.org/
- pycharm: https://www.jetbrains.com/pycharm/

**Step 4:** 
Extract zip and open in idle

**Step 5:** 
Run app.py from idle

**Step 6:** 
Open local host: 
http://127.0.0.1:5000

---

### File/Folder,Purpose & Description

| File/Folder | Purpose & Description |
|---|---|
| app.py | Main Flask application. Contains all backend logic: PDF upload, text extraction, T5 summarization, and PDF export generation. This is the only file you run. |
| templates/index.html | Frontend UI (single-page). Beautiful, responsive design with upload form, copy button, and "Download PDF" link. Uses Jinja2 templating to display the summary. |
| templates/credits.html | Credits page |
| requirements.txt | Complete list of Python dependencies with pinned versions for perfect reproducibility. |
| README.md | This file – full project documentation, setup guide, and file descriptions. |
