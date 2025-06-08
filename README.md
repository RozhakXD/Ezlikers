# EduPintarIPAS 🤖✨ - **Teman Belajar Cerdas untuk Siswa SD Kelas 6**

**EduPintarIPAS** adalah chatbot edukatif berbasis web yang dikembangkan untuk membantu siswa Sekolah Dasar kelas 6 dalam memahami materi Ilmu Pengetahuan Alam dan Sosial (IPAS). Aplikasi ini hadir sebagai solusi interaktif yang mudah diakses dan ramah anak, khususnya bagi mereka yang berada di daerah 3T (Terdepan, Terluar, Tertinggal) dengan keterbatasan akses terhadap bimbingan belajar berkualitas. EduPintarIPAS memanfaatkan teknologi AI dari Microsoft Azure untuk menyediakan layanan tanya-jawab berbasis kurikulum secara cepat dan tepat.

## 🔗 Live Demo
Coba langsung aplikasinya di sini:
👉 [https://edupintaripas.pythonanywhere.com/](https://edupintaripas.pythonanywhere.com/)

## 🖼️ Tampilan Aplikasi
![Image](https://github.com/user-attachments/assets/a534fcee-0704-4244-957a-271c99e954ab)

## 🚀 Fitur Utama
- **🧠 Chatbot Cerdas:** Menjawab berbagai pertanyaan materi IPAS kelas 6, termasuk topik-topik IPA seperti Sistem Gerak, Energi, Lingkungan, dan Tata Surya, serta IPS seperti Sejarah Kemerdekaan, Geografi Dunia, dan Kerjasama Internasional.
- **📚 Dataset Komprehensif:** Dibuat berdasarkan kurikulum resmi SD, berisi ratusan pasangan pertanyaan-jawaban yang relevan dan akurat.
- **💬 Percakapan Ramah:** Mendukung interaksi dasar dan chit-chat sederhana seperti sapaan, sehingga terasa lebih personal dan menyenangkan.
- **📱 Antarmuka Responsif:** Tampilan bersih, modern, dan optimal di berbagai perangkat mulai dari smartphone hingga desktop.

## 🛠️ Teknologi yang Digunakan
- **Dependencies:** `requests`, `python-dotenv`, `gunicorn`
- **Backend:** Python dengan Flask Framework
- **Frontend:** HTML5 & CSS3
- **AI Service:** Microsoft Azure AI Language – Custom Question Answering
- **Deployment:** PythonAnywhere

## ⚙️ Instalasi dan Menjalankan Secara Lokal
1. **Clone repositori ini:**
    ```bash
    git clone https://github.com/RozhakXD/EduPintarIPAS.git
    cd EduPintarIPAS
    ```

2. **Buat dan aktifkan virtual environment:**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependensi:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Buat file `.env` dan isi dengan kredensial Azure Anda:**
    ```env
    AZURE_QNA_ENDPOINT=<URL_ENDPOINT_ANDA>
    AZURE_QNA_KEY=<KUNCI_API_ANDA>
    CONFIDENCE_THRESHOLD=0.5
    ```

5. **Jalankan aplikasi:**
    ```bash
    flask run
    ```
    Akses aplikasi di browser melalui `http://127.0.0.1:5000`.

## 🗂️ Struktur Proyek  
```
EduPintarIPAS/
├── app/
│   ├── static/          # File CSS, JS, dan gambar
│   ├── templates/       # Template HTML
│   ├── main/            # Blueprint rute utama
│   └── services/        # Logika integrasi ke Azure API
├── datasets/            # Dataset QnA
├── .env                 # File environment lokal
├── config.py            # Konfigurasi global
├── requirements.txt     # Dependensi proyek
└── run.py               # Entry point aplikasi
```

## 📢 Informasi Hackathon  
Proyek ini dikembangkan sebagai bagian dari submission **Microsoft Online Hackathon 2025 – DTS x elevAIte** dengan tema: **Pendidikan Digital Inklusif (SDG 4: Quality Education)**.

## 📄 Lisensi  
Proyek ini dirilis di bawah [Lisensi MIT](LICENSE).
