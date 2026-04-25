import os
import requests
import random

AFFILIATE_ID = "arip113377"

def ambil_produk():
    database = [
        {"nama": "Sepatu Sneakers Xtra", "url": "https://shope.ee"},
        {"nama": "Gamis Laku Keras", "url": "https://shope.ee"},
        {"nama": "Tas Selempang Pria", "url": "https://shope.ee"}
    ]
    return random.choice(database)

def posting_fb(pesan):
    token = os.getenv("FB_TOKEN")
    page_id = os.getenv("FB_PAGE_ID")
    url = f"https://graph.facebook.com/{page_id}/feed"
    
    payload = {
        'message': pesan,
        'access_token': token
    }
    
    try:
        response = requests.post(url, data=payload)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    p = ambil_produk()
    pesan = (
        f"PROMO XTRA HARI INI! 🔥\n\n"
        f"Produk: {p['nama']}\n"
        f"Cek di sini: {p['url']}?af_id={AFFILIATE_ID}\n\n"
        f"Buruan sebelum kehabisan! 🚀"
    )

    print(f"Sedang memproses postingan untuk: {p['nama']}...")
    hasil = posting_fb(pesan)
    print("Respon dari Facebook:")
    print(hasil)
