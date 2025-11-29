import os
import io
from flask import Flask, render_template, request, flash, send_file
from werkzeug.utils import secure_filename
from PyPDF2 import PdfReader
from transformers import T5ForConditionalGeneration, T5Tokenizer
from datetime import datetime
from weasyprint import HTML

try:
    gtk_path = r"C:\Program Files\GTK3-Runtime Win64\bin"
    if os.path.exists(gtk_path):
        os.add_dll_directory(gtk_path)
except:
    pass

app = Flask(__name__)
app.secret_key = "medical_summarizer_2025"
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load model
MODEL_NAME = "t5-base" 
tokenizer = T5Tokenizer.from_pretrained(MODEL_NAME, legacy=False)
model = T5ForConditionalGeneration.from_pretrained(MODEL_NAME)

# HEALTH TIPS ENGINE 
def generate_health_tips(text, summary):
    text_lower = text.lower()
    summary_lower = summary.lower()
    tips = []

    # Diabetes / Blood Sugar
    if any(k in text_lower for k in ["diabetes", "hba1c", "glucose", "blood sugar", "dm ", "t2dm"]):
        if any(k in text_lower for k in [">7", ">8", ">9", "high glucose", "poor control"]):
            tips.append("Monitor blood sugar regularly • Aim for HbA1c <7% • Consider low-carb meals • Walk 30 min daily")
        else:
            tips.append("Great job keeping diabetes controlled! • Continue healthy diet • Stay active lifestyle")

    # Hypertension
    if any(k in text_lower for k in ["hypertension", "high blood pressure", "bp ", "htn"]):
        if any(k in text_lower for k in [">140", ">150", ">160", "uncontrolled"]):
            tips.append("Reduce salt intake (<2g/day) • Exercise 150 min/week • Practice stress relief (meditation, sleep)")
        else:
            tips.append("Blood pressure well managed • Keep up the great work!")

    # Cholesterol / Lipids
    if any(k in text_lower for k in ["cholesterol", "ldl", "hdl", "triglyceride", "dyslipidemia"]):
        if any(k in text_lower for k in ["high ldl", "elevated cholesterol", ">200", ">240"]):
            tips.append("Eat more fiber (oats, vegetables) • Include healthy fats (nuts, olive oil, fish) • Avoid trans fats")
        else:
            tips.append("Excellent lipid profile • Maintain heart-healthy habits")

    # Obesity / Weight
    if any(k in text_lower for k in ["obese", "bmi >30", "overweight", "weight concern"]):
        tips.append("Focus on sustainable weight loss (0.5–1 kg/week) • Combine diet + exercise • Consider consulting a dietitian")

    # Thyroid
    if "thyroid" in text_lower:
        if "hypothyroid" in text_lower or "tsh high" in text_lower:
            tips.append("Take thyroid medication on empty stomach • Avoid soy/goitrogens near dose time")
        elif "hyperthyroid" in text_lower:
            tips.append("Stay hydrated • Avoid iodine excess • Follow up regularly")

    # Anemia
    if any(k in text_lower for k in ["anemia", "low hemoglobin", "hb <", "iron deficiency"]):
        tips.append("Include iron-rich foods: spinach, red meat, lentils • Pair with vitamin C for absorption • Avoid tea/coffee with meals")

    # General wellness (always add)
    tips.append("Stay hydrated (2–3L water/day) • Sleep 7–9 hours • Move every hour • Annual health checkups")

    return tips[:5]  # Limit to top 5 most relevant

#  ROUTES 

@app.route('/credits')
def credits():
    return render_template('credits.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = ''
    health_tips = []
    filename = ''
    min_length = 60
    max_length = 180

    if request.method == 'POST':
        file = request.files.get('pdf_file')
        if not file or file.filename == '':
            flash("Please select a PDF file.", "error")
            return render_template('index.html')

        if not file.filename.lower().endswith('.pdf'):
            flash("Only PDF files are allowed.", "error")
            return render_template('index.html')

        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Extract text
        reader = PdfReader(filepath)
        full_text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                full_text += page_text + " "

        if len(full_text.strip()) < 50:
            flash("Not enough text found in PDF. Try a digital/report PDF.", "error")
            os.remove(filepath)
            return render_template('index.html')

        # Generate summary
        try:
            min_length = int(request.form.get('min_length', 60))
            max_length = int(request.form.get('max_length', 180))
            inputs = tokenizer("summarize: " + full_text.replace("\n", " "),
                              return_tensors="pt", max_length=1024, truncation=True)
            outputs = model.generate(
                inputs["input_ids"],
                max_length=max_length,
                min_length=min_length,
                length_penalty=2.0,
                num_beams=6,
                early_stopping=True
            )
            summary = tokenizer.decode(outputs[0], skip_special_tokens=True)

            # Generate personalized health tips
            health_tips = generate_health_tips(full_text, summary)

        except Exception as e:
            flash(f"Error generating summary: {str(e)}", "error")

        finally:
            if os.path.exists(filepath):
                os.remove(filepath)

    return render_template('index.html',
                           summary=summary,
                           health_tips=health_tips,
                           filename=filename,
                           min_length=min_length,
                           max_length=max_length)

# PDF Download with Tips Included
@app.route('/download_summary')
def download_summary():
    summary = request.args.get('summary', '')
    filename = request.args.get('filename', 'Report')
    tips = request.args.get('tips', '').split('|||') if request.args.get('tips') else []

    tip_html = "<ul style='font-size:17px; line-height:1.8;'>"
    for tip in tips:
        tip_html += f"<li>{tip.strip()}</li>"
    tip_html += "</ul>"

    html_content = f"""
    <html><head><meta charset="utf-8"><title>Summary - {filename}</title>
    <style>
        body {{ font-family: 'Segoe UI', sans-serif; margin: 60px; line-height: 1.7; color: #1a1a1a; }}
        .header {{ text-align: center; border-bottom: 4px solid #2563eb; padding-bottom: 20px; }}
        .title {{ font-size: 32px; color: #1e40af; }}
        .info {{ margin: 40px 0; color: #555; }}
        .summary, .tips-box {{ background: #f8f9fc; padding: 30px; border-radius: 10px; margin: 20px 0; }}
        .tips-box {{ border-left: 6px solid #f59e0b; }}
        .footer {{ margin-top: 80px; text-align: center; color: #888; font-size: 13px; }}
    </style></head><body>
        <div class="header"><h1 class="title">AI Medical Report Summary</h1>
        <p>Generated on {datetime.now().strftime("%B %d, %Y")}</p></div>
        <div class="info"><strong>Report:</strong> {filename}</div>
        <div class="summary"><h2>Clinical Summary</h2><p>{summary.replace(chr(10), '<br>')}</p></div>
        <div class="tips-box"><h2>Personal Health Tips</h2>{tip_html}</div>
        <div class="footer">AI-generated • Always consult your doctor before making changes</div>
    </body></html>
    """

    pdf = HTML(string=html_content).write_pdf()
    return send_file(io.BytesIO(pdf),
                     as_attachment=True,
                     download_name=f"Health_Summary_{os.path.splitext(filename)[0]}_{datetime.now().strftime('%Y%m%d')}.pdf",
                     mimetype='application/pdf')

if __name__ == "__main__":
    app.run(debug=True)
