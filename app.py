from flask import Flask, request, jsonify, render_template_string, send_from_directory, redirect
import os
import json
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'static'
PDF_FOLDER = os.path.join(UPLOAD_FOLDER, 'pdfs')
IMG_FOLDER = os.path.join(UPLOAD_FOLDER, 'thumbnails')
DATA_FILE = 'products.json'
UNDO_FILE = 'last_deleted.json'

os.makedirs(PDF_FOLDER, exist_ok=True)
os.makedirs(IMG_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return redirect('/uploader.html')

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
        "pdf": "/" + pdf_path.replace("\\", "/"),
        "thumbnail": "/" + img_path.replace("\\", "/")
    }

    products = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            products = json.load(f)

    existing = next((p for p in products if p['name'] == product), None)
    if existing:
        existing.update(product_entry)
    else:
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

@app.route('/delete-product', methods=['POST'])
def delete_product():
    name = request.form.get('name')
    if not name:
        return jsonify({"success": False, "error": "Missing product name"}), 400

    products = []
    deleted_product = None
    deleted_files = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            products = json.load(f)

        updated_products = []
        for p in products:
            if p['name'] == name:
                deleted_product = p
                pdf_path = p.get('pdf', '').lstrip('/')
                img_path = p.get('thumbnail', '').lstrip('/')
                if os.path.exists(pdf_path):
                    os.remove(pdf_path)
                    deleted_files.append(pdf_path)
                if os.path.exists(img_path):
                    os.remove(img_path)
                    deleted_files.append(img_path)
            else:
                updated_products.append(p)

        with open(DATA_FILE, "w") as f:
            json.dump(updated_products, f, indent=2)

        if deleted_product:
            with open(UNDO_FILE, "w") as f:
                json.dump(deleted_product, f, indent=2)

        return jsonify({"success": True, "deleted_files": deleted_files})

    return jsonify({"success": False, "error": "No data file found"}), 404

@app.route('/undo-delete', methods=['POST'])
def undo_delete():
    if os.path.exists(UNDO_FILE):
        with open(UNDO_FILE, "r") as f:
            product = json.load(f)

        products = []
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                products = json.load(f)

        products.append(product)

        with open(DATA_FILE, "w") as f:
            json.dump(products, f, indent=2)

        os.remove(UNDO_FILE)

        return jsonify({"success": True, "restored": product})

    return jsonify({"success": False, "error": "No recent deletion to undo."})

@app.route('/update-products', methods=['POST'])
def update_products():
    try:
        products = request.get_json()
        with open(DATA_FILE, "w") as f:
            json.dump(products, f, indent=2)
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    app.run(debug=True)
