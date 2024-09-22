# Import library yang diperlukan
from PIL import Image
import pytesseract
import cv2

# Tentukan path instalasi Tesseract (sesuaikan dengan lokasi di komputer Anda)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Fungsi untuk membaca teks dari gambar
def read_text_from_image(image_path):
    # Membaca gambar menggunakan OpenCV
    image = cv2.imread(image_path)

    # Konversi gambar ke skala abu-abu
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Menggunakan pytesseract untuk mendeteksi teks dalam gambar
    text = pytesseract.image_to_string(gray_image)

    # Mengembalikan teks yang terdeteksi
    return text

# Fungsi utama
def main():
    # Minta pengguna memasukkan path gambar
    image_path = input("Masukkan path gambar (JPG atau PNG): ")

    # Baca teks dari gambar
    text = read_text_from_image(image_path)

    # Tampilkan teks yang terdeteksi
    print("\nTeks yang terdeteksi:")
    print(text)

if __name__ == "__main__":
    main()
