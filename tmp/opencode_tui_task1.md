# Tugas: Percantik Website Portofolio Skripsi (iterasi 2)

Folder `website/` sudah berisi website portofolio yang JADI dan BERFUNGSI (index.html + css/style.css + js/script.js). Website ini masih kosong identitasnya. **PERBAIKI DAN TAMBAH FITUR di file yang sudah ada — jangan buat ulang dari nol, jangan hapus konten/section yang sudah ada.** Tetap vanilla HTML/CSS/JS murni, tanpa framework/CDN/library eksternal apa pun.

## 1. Identitas pemilik (WAJIB)

- Nama pemilik: **Arthur Reezan** — mahasiswa S1 Manajemen, FEB Universitas Kristen Krida Wacana, konsentrasi Manajemen Keuangan.
- Tambahkan section **profil** baru (letakkan setelah hero / sebelum Tentang) berisi:
  - **Foto profil placeholder**: avatar lingkaran dengan inisial "AR" dibuat murni CSS (gradient hijau + huruf putih besar). JANGAN pakai gambar eksternal. Beri komentar di HTML `<!-- GANTI: foto asli -->` supaya mudah diganti nanti.
  - Nama "Arthur Reezan", "Mahasiswa S1 Manajemen — FEB UKRIDA", tagline singkat: "Tertarik pada keuangan berkelanjutan & riset perbankan Indonesia."
  - Baris info kecil: fokus riset Green Financing · Bank KBMI 4 · Ekonometrika Data Panel.
- Tambahkan link "Profil" di navbar.

## 2. Halaman publikasi terpisah (BARU)

Buat file **`website/publikasi.html`** (halaman kedua, style sama persis — reuse css/style.css):

- Navbar sederhana dengan link kembali ke index.html ("← Kembali").
- Hero kecil: "Publikasi & Dokumen Penelitian".
- Kartu-kartu daftar dokumen penelitian ini, masing-masing dengan judul, deskripsi 1–2 kalimat, badge jenis (Skripsi / Panduan Belajar / Simulasi Sidang), dan tombol/link:
  - Skripsi lengkap (PDF): `../skripsi_ukrida.pdf` (relatif dari folder website/)
  - Pedoman Penyusunan Skripsi FEB UKRIDA 2022: `../Buku Pedoman Penyusunan Skripsi FEB Ukrida 2022.pdf`
  - Panduan Belajar & Penguasaan Materi v2: `../skripsi/PANDUAN_BELAJAR_SKRIPSI_v2.md` (tampilkan sebagai kartu tanpa link langsung jika .md tidak bisa dibuka di browser — tetap tulis path-nya)
  - Bank Soal Latihan, Flashcard Istilah, Pertanyaan Sidang Sulit, Simulasi Dialog Sidang, Ringkasan Per Bab (folder `../skripsi/BELAJAR SKRIPSI SAMPAI BISA/`)
- Footer catatan: dokumen hanya untuk keperluan akademik.
- Tambahkan link "Publikasi" di navbar index.html yang mengarah ke publikasi.html.

## 3. Ganti skema warna (refresh visual)

Sekarang: hijau polos. Ubah menjadi skema **emerald → teal gelap yang lebih premium**:

- Definisikan CSS variables di :root dan PAKAI konsisten: `--primary` (emerald ~ #0d9488 teal-600 atau serupa), `--primary-dark` (~ #134e4a), `--accent` (amber/emerald light untuk highlight), plus netral.
- Hero gradient dari hijau tua ke teal (bukan hijau→hitam).
- Hover states lebih halus: kartu terangkat (transform translateY + shadow), transisi 0.2–0.3s.
- Section Hasil: angka statistik pakai warna accent agar menonjol.
- Scrollbar halus (webkit-scrollbar styling) dan `scroll-behavior: smooth`.

## 4. Polish tambahan

- Tambah tombol back-to-top (muncul setelah scroll 400px, JS).
- Tambah tahun dinamis di footer (`new Date().getFullYear()`).
- Pastikan hamburger mobile tetap bekerja dengan menu item baru.
- Meta description + Open Graph title/description di kedua HTML.

## Verifikasi wajib

1. `node --check website/js/script.js`
2. Semua id anchor navbar ada di index.html; semua href internal resolve (cek path relatif file PDF benar-benar ada: `ls "../skripsi_ukrida.pdf"` dari folder website/, dst).
3. Laporkan ringkasan perubahan per file.
