# Test Junior Programmer – Fast Print Indonesia

Repository ini berisi hasil pengerjaan **Seleksi Tahap Pertama – Test Programmer** untuk posisi Junior Programmer di Fast Print Indonesia (Surabaya).

---

## 👤 Informasi Pelamar
| Data | Keterangan |
| :--- | :--- |
| **Nama** | Anggi Aurel Dewanti |
| **Posisi** | Junior Programmer |
| **Framework** | Django |
| **Database** | MySQL |

---

## 🎯 Deskripsi Project
Project ini dibuat untuk memenuhi kebutuhan test dengan ketentuan sebagai berikut:
* Mengambil data produk dari API yang disediakan.
* Menyimpan data ke database MySQL.
* Menampilkan produk dengan status **"bisa dijual"**.
* Menyediakan fitur **CRUD** (Create, Read, Update, Delete).
* Menggunakan validasi input pada form.
* Menyediakan dokumentasi berupa laporan dan video.

---

## 🧩 Fitur Utama
- [x] **Fetch Data:** Mengambil data otomatis dari API Fast Print.
- [x] **Database Sync:** Sinkronisasi data ke MySQL.
- [x] **Relasi Tabel:** Implementasi relasi antara tabel Produk, Kategori, dan Status.
- [x] **Filter Status:** Menampilkan produk yang hanya berstatus "bisa dijual".
- [x] **Full CRUD:** Tambah, edit, dan hapus data produk.
- [x] **Validasi:** Form dengan validasi nama wajib diisi dan harga harus numerik.
- [x] **UX/UI:** Konfirmasi sebelum hapus data & desain responsif dengan **Tailwind CSS & Alpine.js**.

---

## 🛠️ Teknologi yang Digunakan
* **Backend:** Python 3, Django
* **Database:** MySQL
* **Frontend:** Tailwind CSS, Alpine.js
* **Tools:** Postman (API Testing)

---

## 🗂️ Struktur Database
Terdiri dari 3 tabel utama dengan relasi *Foreign Key* untuk menjaga integritas data:
1.  **Produk**: Menyimpan detail item.
2.  **Kategori**: Pengelompokan jenis produk.
3.  **Status**: Status ketersediaan (bisa dijual/tidak).

---

## 🚀 Cara Menjalankan Project

### 1. Clone Repository
```bash
git clone https://github.com/anggiaureldewanti/Fast-Print-API-Test
cd Fast-Print-API-Test
```
### 2. Aktifkan Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Install Dependencies
Konfigurasi Database
Sesuaikan pengaturan database pada file settings.py:
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fastprint',
        'USER': 'root',
        'PASSWORD': 'password_mysql_anda',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```
### 5. Migrasi Database
```bash
python manage.py makemigrations
python manage.py migrate
```
### 6. Ambil Data dari API
Masuk ke Django shell:
```bash
python manage.py shell
```
Lalu Jalankan:
```bash
from produk.fetch_api import fetch_and_save_produk
fetch_and_save_produk()
```
### 7. Jalankan Server
```bash
python manage.py runserver
```
Akses Aplikasi di:
```bash
http://127.0.0.1:8000/
```

---

## 🎥 Video Dokumentasi
📺 Link YouTube:
👉 [https://youtu.be/vGOgiV33h3g]

---

## 📄 Dokumentasi Laporan
Dokumentasi lengkap tersedia dalam bentuk PDF dan dikirimkan melalui email sesuai instruksi test.

---

## 🙏 Penutup
Terima kasih atas kesempatan yang diberikan untuk mengikuti proses seleksi ini.
Saya berharap project ini dapat menjadi bahan pertimbangan untuk tahap selanjutnya.
