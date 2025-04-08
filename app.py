from flask import Flask, request, jsonify, render_template_string, send_from_directory, redirect
import os
import json
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'static'
PDF_FOLDER = os.path.join(UPLOAD_FOLDER, 'pdfs')
IMG_FOLDER = os.path.join(UPLOAD_FOLDER, 'thumbnails')
DATA_FILE = 'products.json'

os.makedirs(PDF_FOLDER, exist_ok=True)
os.makedirs(IMG_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return redirect('/catalog.html')

@app.route('/upload', methods=['POST'])
def upload():
    product = request.form['product']
    category = request.form['category']
    pdf_file = request.files['pdf']
    img_file = request.files['thumbnail']

    if not (pdf_file and img_file and pdf_file.filename.endswith('.pdf')):
        return "Invalid file(s)."

    pdf_name = secure_filename(pdf_file.filename)
    img_name = secure_filename(img_file.filename)

    pdf_path = os.path.join(PDF_FOLDER, pdf_name)
    img_path = os.path.join(IMG_FOLDER, img_name)

    pdf_file.save(pdf_path)
    img_file.save(img_path)

    product_entry = {
        "name": product,
        "category": category,
        "pdf": f"/{pdf_path.replace('\\\\', '/')}",
        "thumbnail": f"/{img_path.replace('\\\\', '/')}"
    }

    products = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            products = json.load(f)

    products.append(product_entry)
    with open(DATA_FILE, "w") as f:
        json.dump(products, f, indent=2)

    return f"Uploaded! <a href='{product_entry['pdf']}' target='_blank'>View PDF</a>"

@app.route('/products')
def list_products():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return jsonify(json.load(f))
    return jsonify([])

# Serve static files (catalog.html, upload.html, etc.)
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    app.run(debug=True)
