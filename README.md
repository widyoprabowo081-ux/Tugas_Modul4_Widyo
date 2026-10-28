# Sistem Manajemen Perpustakaan

Sistem informasi manajemen perpustakaan berbasis desktop yang dibangun menggunakan Python dan CustomTkinter. Aplikasi ini menerapkan pola arsitektur Model-View-Controller (MVC) dengan fitur keamanan autentikasi (password hashing SHA-256) dan otorisasi berbasis peran (Role-Based Access Control) untuk Admin dan Anggota.

## Struktur Direktori MVC
* `models/` : Berisi logika interaksi dengan basis data MySQL (`buku_model.py`, `user_model.py`).
* `views/` : Berisi antarmuka pengguna GUI CustomTkinter (`login_view.py`, `buku_view.py`).
* `controllers/` : Berisi logika alur aplikasi yang menghubungkan View dan Model (`auth_controller.py`, `buku_controller.py`).

## Panduan Instalasi & Konfigurasi Database MySQL
1. Pastikan aplikasi Laragon (atau XAMPP) telah terinstal dan layanan MySQL berjalan.
2. Buka antarmuka manajemen basis data (seperti HeidiSQL atau terminal MySQL).
3. Buat basis data baru bernama `perpustakaan`.
4. Impor tabel atau jalankan kueri SQL untuk membuat tabel `buku` dan `users` sesuai modul.
5. Sesuaikan parameter koneksi (host, user, password, database) pada file `config/database.py`.

## Cara Menjalankan Aplikasi
* **Menggunakan File Eksekusi (.exe):** Buka folder `dist/` dan jalankan `AplikasiPerpustakaan.exe`.
* **Melalui Source Code:** Buka terminal, aktifkan virtual environment, dan jalankan perintah `python main.py`.