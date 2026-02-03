import requests
from produk.models import Produk, Kategori, Status

URL = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"

PAYLOAD = {
    "username": "tesprogrammer030226C12",
    "password": "1c168003aae0c425a5b0750fad81e54d"
}

def fetch_and_save_produk():
    response = requests.post(URL, data=PAYLOAD)
    data = response.json()

    if data.get("error") == 1:
        print("Login gagal:", data.get("ket"))
        return

    for item in data["data"]:
        kategori_obj, _ = Kategori.objects.get_or_create(
            nama_kategori=item["kategori"]
        )

        status_obj, _ = Status.objects.get_or_create(
            nama_status=item["status"]
        )

        Produk.objects.update_or_create(
            id_produk=item["id_produk"],
            defaults={
                "nama_produk": item["nama_produk"],
                "harga": int(item["harga"]),
                "kategori": kategori_obj,
                "status": status_obj
            }
        )

    print("✅ Data produk berhasil disimpan")
