# 🎓 Sistem Informasi Data Mahasiswa

## Deskripsi

Sistem Informasi Data Mahasiswa merupakan aplikasi berbasis web yang dibuat menggunakan framework Flask. Aplikasi ini digunakan untuk mengelola data mahasiswa dengan fitur login, registrasi, serta pengelolaan data mahasiswa (CRUD).

Project ini dibuat sebagai tugas akhir mata kuliah **Pemrograman Berorientasi Objek (PBO)**.

---

## Teknologi yang Digunakan

- Python 3
- Flask
- Flask SQLAlchemy
- Flask Login
- SQLite
- Bootstrap 5
- HTML
- CSS
- Jinja2

---

## Fitur Aplikasi

- Login User
- Register User
- Logout
- Dashboard
- Menampilkan Data Mahasiswa
- Menambah Data Mahasiswa
- Mengubah Data Mahasiswa
- Menghapus Data Mahasiswa
- Pencarian Data Mahasiswa
- Validasi Username
- Validasi NIM
- Flash Message

---

## Struktur Project

```
PBO-FINAL
│
├── app.py
├── models.py
├── requirements.txt
│
├── instance
│    └── app.db
│
├── templates
│   ├── base.html
│   ├── dashboard.html
│   ├── login.html
│   ├── register.html
│   ├── mahasiswa.html
│   ├── tambah.html
│   └── edit.html
│
└── static
    ├── css
    │    └── style.css
    ├── img
    └── js
```

---

## Cara Menjalankan Program

### 1. Clone Repository

```bash
git clone https://github.com/USERNAME/PBO-FINAL.git
```

### 2. Masuk Folder

```bash
cd PBO-FINAL
```

### 3. Buat Virtual Environment

```bash
python -m venv venv
```

### 4. Aktifkan Virtual Environment

Windows

```bash
venv\Scripts\activate
```

### 5. Install Library

```bash
pip install -r requirements.txt
```

### 6. Jalankan Program

```bash
python app.py
```

### 7. Buka Browser

```
http://127.0.0.1:5000
```

---

## Database

Database menggunakan SQLite dengan nama:

```
instance/app.db
```

---

## Tampilan Aplikasi

- Login
- Register
- Dashboard
- Data Mahasiswa
- Tambah Mahasiswa
- Edit Mahasiswa

*(Tambahkan screenshot aplikasi jika diperlukan.)*

---

## Pengembang

Nama : **Alfina**

Mata Kuliah : **Pemrograman Berorientasi Objek**

Tahun : **2026**

---

## Lisensi

Project ini dibuat untuk keperluan pembelajaran dan tugas kuliah.