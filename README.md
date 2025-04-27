# Product Editor Tool (Flask + HTML)

This tool allows you to:
- Upload products with a name, category, thumbnail (image), and PDF file
- View all uploaded products
- Delete products (and automatically remove their files)
- Undo the last deletion

---

## 📦 Installation Instructions

### 1. Clone or download the project

Download the project ZIP or clone it via Git:

```bash
git clone https://github.com/vortexgello/quad-dimensions
cd quad-dimensions
```

---

### 2. Set up Python environment

Make sure you have **Python 3.8+** installed.

Install `Flask`:

```bash
pip install flask
```

If pip has proxy issues, fix pip settings or manually install Flask.

---

### 3. Run the Flask server

In the project folder, run:

```bash
python app.py
```

You should see output like:

```
 * Running on http://127.0.0.1:5000/
```

Open your browser and go to: [http://localhost:5000](http://localhost:5000)

---

## 🚀 How to Use

### Upload Products
- Open the web page
- Fill in the product name and category
- Upload a PDF file and a thumbnail image
- Click **Upload**

### View Products
- Scroll down to see all uploaded products
- View thumbnails and download linked PDFs

### Delete a Product
- Click the **Delete** button on any product
- It will remove the product and delete its associated files (image + PDF)

### Undo Deletion
- After a deletion, click **Undo Last Delete**
- The last deleted product will be restored into the system

---

## 📁 Project Structure

```
static/
├── pdfs/           # Uploaded PDFs
├── thumbnails/     # Uploaded thumbnails
uploads/            # (if needed for temporary files)
templates/
├── uploader.html   # Main frontend page
products.json       # Database for products
last_deleted.json   # Stores last deleted product for undo
app.py              # Flask backend server
```

---

## ⚙️ APIs

- `POST /upload` — Upload a new product
- `GET /products` — Fetch all products
- `POST /delete-product` — Delete a product by name
- `POST /undo-delete` — Undo the last deleted product

---

## 🛠️ Requirements
- Python 3.8 or higher
- Flask 2.0+

---

## ✨ Future Improvements
- Upload multiple products at once
- Multiple levels of undo
- Admin authentication
- Search/filter products

---

## 👨‍💻 Author

Built with ❤️ by [Your Name]

