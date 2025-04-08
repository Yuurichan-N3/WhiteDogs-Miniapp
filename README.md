# 🌟 WhiteDogs Bot - Task Automation

Script Python untuk mengotomatiskan penyelesaian tugas di WhiteDogs. Menggunakan multi-threading untuk memproses beberapa akun secara efisien dengan antarmuka CLI yang kaya menggunakan `rich`.

---

## 🚀 Fitur Utama
- Membaca `telegram_id` dari file `data.txt` untuk multiple akun
- Mengotomatiskan penyelesaian tugas dari daftar tugas yang telah ditentukan
- Logging real-time dengan status dan warna
- Tabel hasil untuk setiap akun
- Filter tugas yang belum selesai
- Multi-threading untuk pemrosesan paralel
- Penanganan error yang informatif

---

## 📋 Prasyarat
Sebelum memulai, pastikan Anda memiliki:
- Python (versi 3.7 atau lebih tinggi) terinstal
- Library Python berikut:
  - `requests`
  - `rich`
- File `data.txt` berisi WebAppData dengan `telegram_id` untuk setiap akun

---

## 🛠️ Cara Instalasi
1. **Clone Repository**
   ```bash
   git clone https://github.com/Yuurichan-N3/WhiteDogs-Miniapp.git
   cd WhiteDogs-Miniapp
   ```

2. **Instal Dependensi**
   Jalankan perintah berikut untuk menginstal library yang dibutuhkan:
   ```bash
   pip install requests rich
   ```

3. **Siapkan File `data.txt`**
   - Buat file `data.txt` di direktori yang sama dengan script
   - Masukkan WebAppData dalam format URL-encoded, satu per baris, contoh:
     ```
     user=%7B%22id%22%3A123456789%2C%22first_name%22%3A%22John%22%7D
     user=%7B%22id%22%3A987654321%2C%22first_name%22%3A%22Jane%22%7D
     ```
   - Pastikan setiap baris berisi `id` yang valid

---

## ▶️ Cara Penggunaan
1. **Jalankan Script**
   Dari terminal, ketik:
   ```bash
   python bot.py
   ```

2. **Pantau Output**
   - Script akan menampilkan banner dan memproses semua akun
   - Log akan menunjukkan status setiap tugas (SUCCESS/SKIP/FAILED) dengan timestamp
   - Tabel hasil akan muncul di akhir, menampilkan jumlah tugas yang diselesaikan per akun
   - Contoh output:
     ```
     [10:00:00] INFO: [SUCCESS] Task 149 - Play Path completed
     [10:00:02] INFO: [SKIP] Task 148 - Join Planes already completed
     ```

3. **Hentikan Jika Diperlukan**
   Tekan `Ctrl+C` untuk menghentikan eksekusi kapan saja

---

## 📂 Struktur File
- `bot.py`: Script utama
- `data.txt`: File input berisi WebAppData (harus dibuat manual)
- `README.md`: Dokumentasi ini

---

## ⚠️ Catatan Penting
- Pastikan koneksi internet stabil
- File `data.txt` harus ada dan berisi minimal satu akun valid
- Script menggunakan 3 thread secara default untuk pemrosesan paralel (dapat diubah di kode)
- Delay 2 detik antar tugas untuk mencegah rate limiting
- Jika status 401 muncul, autentikasi mungkin diperlukan (periksa API)

---

## 📜 Lisensi
Script ini didistribusikan untuk keperluan pembelajaran dan pengujian. Penggunaan di luar tanggung jawab pengembang.

Untuk update terbaru, bergabunglah di grup **Telegram**: [Klik di sini](https://t.me/sentineldiscus).

---

## 💡 Disclaimer
Penggunaan bot ini sepenuhnya tanggung jawab pengguna. Kami tidak bertanggung jawab atas penyalahgunaan skrip ini.
