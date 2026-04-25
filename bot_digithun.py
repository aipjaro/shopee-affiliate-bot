import os
import requests
import random

# Pastikan ID Affiliate sudah benar (Ini akan muncul di teks postingan)
AFFILIATE_ID = "arip113377"

def ambil_produk():
    # Daftar database produk
    # Kamu bisa menambahkan produk baru di bawah dengan format yang sama
    database = [
        {"nama": "Sepatu Sneakers Xtra", "url": "https://shope.ee"},
        {"nama": "Gamis Laku Keras", "url": "https://shope.ee"},
        {"nama": "Tas Selempang Pria", "url": "https://shope.ee"}
    ]
    return random.choice(database)

def posting_fb(pesan):
    # Mengambil token dan ID dari GitHub Secrets
    token = os.getenv("FB_TOKEN")
    page_id = os.getenv("FB_PAGE_ID")
    
    # URL API Facebook yang sudah diperbaiki (PENTING!)
   ...url = f"https://graph.facebook.com/{page_id}/feed"



    payload = {
        'message': pesan,
        'access_token': token
    }
    
    try:
        # Mengirim data ke Facebook
        response = requests.post(url, data=payload)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    # 1. Pilih produk acak
    p = ambil_produk()
    
    # 2. Susun pesan iklan yang rapi
    # Menambahkan kode affiliate di akhir link (opsional, tergantung sistem link kamu)
    pesan = (
        f"PROMO XTRA HARI INI! 🔥\n\n"
        f"Produk: {p['nama']}\n"
        f"Cek di sini: {p['url']}?af_id={AFFILIATE_ID}\n\n"
        f"Buruan sebelum kehabisan! 🚀"
    )

    print(f"Sedang memproses postingan untuk: {p['nama']}...")
    
    # 3. Eksekusi posting
    hasil = posting_fb(pesan)
    
    # Tampilkan hasil di log GitHub
    print("Respon dari Facebook:")
    print(hasil)
