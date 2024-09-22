from flask import Flask, request, jsonify, render_template, send_from_directory
from PIL import Image
import pytesseract
import cv2
import numpy as np
import os

# Tentukan path instalasi Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

app = Flask(__name__)

# Fungsi untuk membaca teks dari gambar
def read_text_from_image(image):
    np_img = np.frombuffer(image.read(), np.uint8)
    img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray_image)
    return text

# Endpoint untuk halaman HTML
@app.route('/')
def index():
    return send_from_directory('', 'index.html')

# Endpoint untuk upload dan ekstrak teks dari gambar
@app.route('/extract-text', methods=['POST'])
def extract_text():
    if 'image' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    image = request.files['image']
    text = read_text_from_image(image)
    return jsonify({"text": text})

if __name__ == "__main__":
    app.run(debug=True)
