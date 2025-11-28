from flask import Flask, render_template, request, flash
from werkzeug.utils import secure_filename
import os
from PyPDF2 import PdfReader
from transformers import T5ForConditionalGeneration, T5Tokenizer

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "super_secret_key")  # Use environment variable for secret key
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Create uploads folder if not exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load T5 model (use t5-base for better medical summaries)
MODEL_NAME = "t5-base" 
try:
    tokenizer = T5Tokenizer.from_pretrained(MODEL_NAME, legacy=False)
    model = T5ForConditionalGeneration.from_pretrained(MODEL_NAME)
except Exception as e:
    raise RuntimeError(f"Failed to load T5 model: {e}")

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + " "
    except Exception as e:
        return None, str(e)
    return text.strip(), None

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = ''
    extracted_text = ''
    filename = ''
    min_length = 50
    max_length = 200

    if request.method == 'POST':
        if 'pdf_file' not in request.files:
            flash('No file part')
            return render_template('index.html', min_length=min_length, max_length=max_length)

        file = request.files['pdf_file']
        if file.filename == '':
            flash('No file selected')
            return render_template('index.html', min_length=min_length, max_length=max_length)

        if file and file.filename.lower().endswith('.pdf'):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Extract text
            extracted_text, error = extract_text_from_pdf(filepath)
            if error:
                flash(f"Error reading PDF: {error}")
            elif not extracted_text:
                flash("No text could be extracted from the PDF.")
            else:
                try:
                    min_length = int(request.form.get('min_length', 50))
                    max_length = int(request.form.get('max_length', 200))
                    if min_length < 10 or max_length > 500 or min_length >= max_length:
                        raise ValueError("Invalid summary length range.")
                except ValueError:
                    flash("Invalid minimum or maximum length values.")
                    return render_template('index.html', min_length=min_length, max_length=max_length)

                # Clean and prepare text
                input_text = extracted_text.replace("\n", " ").strip()
                if len(input_text.split()) < 20:
                    flash("PDF has too little text to summarize.")
                else:
                    try:
                        # T5 summarization
                        preprocess_text = "summarize: " + input_text
                        inputs = tokenizer(
                            preprocess_text,
                            return_tensors="pt",
                            max_length=1024,
                            truncation=True
                        )

                        outputs = model.generate(
                            inputs["input_ids"],
                            max_length=max_length,
                            min_length=min_length,
                            length_penalty=2.0,
                            num_beams=6,
                            early_stopping=True,
                            no_repeat_ngram_size=3
                        )

                        summary = tokenizer.decode(outputs[0], skip_special_tokens=True)
                    except Exception as e:
                        flash(f"Error generating summary: {e}")

            # Clean up uploaded file
            if os.path.exists(filepath):
                os.remove(filepath)
        else:
            flash('Only PDF files are allowed!')

    return render_template(
        'index.html',
        summary=summary,
        extracted_text=extracted_text[:1000] + "..." if extracted_text and len(extracted_text) > 1000 else extracted_text,
        filename=filename,
        min_length=min_length,
        max_length=max_length
    )

if __name__ == '__main__':

    app.run(debug=True)
