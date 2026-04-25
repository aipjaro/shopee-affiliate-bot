import os
import requests
import random

AFFILIATE_ID = "arip113377"

def ambil_produk():
    # Daftar produk (bisa kamu tambah sendiri nanti)
    database = [
        {"nama": "Sepatu Sneakers Xtra", "url": "https://shope.ee"},
        {"nama": "Gamis Laku Keras", "url": "https://shope.ee"}
    ]
    return random.choice(database)

def posting_fb(pesan):
    token = os.getenv("FB_TOKEN")
    page_id = os.getenv("FB_PAGE_ID")
    
    # Ini alamat pintu masuk resmi untuk bot Facebook (Graph API)
    url = f"https://facebook.com{page_id}/feed"
    
    payload = {
        'message': pesan,
        'access_token': token
    }
    
    response = requests.post(url, data=payload)
    return response.json()

if __name__ == "__main__":
    p = ambil_produk()
    # Format pesan iklan
    pesan = f"🔥 PROMO XTRA! 🔥\n\n{p['nama']}\nCek di sini: {p['url']}?smtt=0.0.{AFFILIATE_ID}"
    
    print("Sedang mengirim postingan...")
    hasil = posting_fb(pesan)
    print(hasil)
