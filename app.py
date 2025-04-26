from flask import Flask, render_template, request, send_file
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from werkzeug.utils import secure_filename
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from io import BytesIO
import numpy as np
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['PDF_FOLDER'] = 'static/reports'

# Load model
model = load_model('custom_cnn_model.keras')

def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(150, 150))
    img_array = image.img_to_array(img) / 255.0
    return np.expand_dims(img_array, axis=0)

def predict_image(img_path):
    img_array = preprocess_image(img_path)
    prediction = model.predict(img_array)[0][0]
    label = 'Pneumonia' if prediction > 0.5 else 'Normal'
    confidence = prediction if prediction > 0.5 else 1 - prediction
    return label, round(confidence * 100, 2)

def create_pdf_report(data):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    
    # Header
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 750, "Pneumonia Diagnosis Report")
    
    # Patient Info
    c.setFont("Helvetica", 12)
    y_position = 700
    for key, value in data['patient_info'].items():
        c.drawString(50, y_position, f"{key}: {value}")
        y_position -= 20
    
    # Image
    img = ImageReader(data['image_path'])
    c.drawImage(img, 50, 500, width=200, height=200)
    
    # Diagnosis
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, 250, f"Diagnosis: {data['diagnosis']}")
    c.drawString(50, 230, f"Confidence: {data['confidence']}%")
    
    c.save()
    buffer.seek(0)
    return buffer

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Create directories if needed
        for folder in [app.config['UPLOAD_FOLDER'], app.config['PDF_FOLDER']]:
            os.makedirs(folder, exist_ok=True)
            
        # Get patient info
        patient_info = {
            'name': request.form.get('name', ''),
            'age': request.form.get('age', ''),
            'gender': request.form.get('gender', ''),
            'patient_id': request.form.get('patient_id', '')
        }
        
        # Handle file upload
        if 'file' not in request.files:
            return render_template('index.html', error="No file selected.")
        
        file = request.files['file']
        if file.filename == '':
            return render_template('index.html', error="Please upload an image.")
        
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Get prediction
        label, confidence = predict_image(file_path)
        
        # Generate PDF
        pdf_data = {
            'patient_info': patient_info,
            'image_path': file_path,
            'diagnosis': label,
            'confidence': confidence
        }
        
        pdf_buffer = create_pdf_report(pdf_data)
        pdf_filename = f"report_{os.path.splitext(filename)[0]}.pdf"
        pdf_path = os.path.join(app.config['PDF_FOLDER'], pdf_filename)
        with open(pdf_path, 'wb') as f:
            f.write(pdf_buffer.getbuffer())
        
        return render_template('index.html',
                             file_path=file_path,
                             label=label,
                             confidence=confidence,
                             pdf_path=pdf_path,
                             patient_info=patient_info)
    
    return render_template('index.html')

@app.route('/download/<path:filename>')
def download_pdf(filename):
    return send_file(os.path.join(app.config['PDF_FOLDER'], filename),
                     as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)