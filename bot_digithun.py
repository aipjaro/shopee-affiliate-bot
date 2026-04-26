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
    token = "EAAVRNJlJmosBRURoJNmy6jThNWAbK6NH1IL79OLtpVNOjcl3eMMjSpPd8ZCcge3dvTPwzft56u8ZCqqgewH4l7CQnTZBDe2ZCemK0nEABnjEuHcAqD51ztTxXcvg3mRPsLL91GFJ60mAEADhu7vnlIII2hJIHnE5jRNAJQuVZCQtTtoRZBYjMm0WNnUsX5bLvEVdB4fnrpIiVemM1B4USPo7zNZBgim5jQ1bEoobgwZD"
    page_id = "1133363113184355"
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
