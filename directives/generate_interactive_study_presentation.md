# Directive: Generate Interactive Study Web Presentation

> **Tujuan:** Menghasilkan aplikasi web presentasi interaktif dan modul belajar mandiri (*Study Suite*) untuk proposal skripsi S1 Manajemen Keuangan FEB UKRIDA (Topik: Pokémon TCG & Impulsive Buying dengan Moderasi Self-Control).

---

## 1. Input Data
1. `02_Persiapan_Sidang/PANDUAN_BELAJAR_PROPOSAL.md` — Master Study Guide (Bab 1–3, ekosistem Pokémon, grading PSA, operasionalisasi variabel, teori, hipotesis H1–H6, metodologi MRA, dan 15 skenario bimbingan dosen).
2. `02_Persiapan_Sidang/BELAJAR SKRIPSI SAMPAI BISA/01_BANK_SOAL_LATIHAN.md` — Bank soal latihan sidang.
3. `02_Persiapan_Sidang/BELAJAR SKRIPSI SAMPAI BISA/02_FLASHCARD_ISTILAH.md` — Istilah kunci flashcard.
4. `02_Persiapan_Sidang/BELAJAR SKRIPSI SAMPAI BISA/03_PERTANYAAN_SIDANG_SULIT.md` — 10 pertanyaan jebakan sidang sulit.
5. `04_Riset_&_Metodologi/SOURCE_OF_TRUTH.md` — Sumber kanonis variabel dan keputusan terkunci (D01–D13).

---

## 2. Alat Eksekusi (Layer 3)
* **Skrip:** `execution/build_interactive_presentation.py`
* **Lingkungan:** Python 3 standard library (tanpa dependensi eksternal).

---

## 3. Format Output & Deliverables
1. `02_Persiapan_Sidang/presentasi_interaktif/`
   - `index.html`: Berkas HTML utama modular.
   - `style.css`: Desain sistem lengkap (Dark Mode, Glassmorphism, Google Fonts, responsive grid, 3D card flips).
   - `app.js`: Logika presentasi slide, keyboard shortcut handler, flashcard manager, kuis interaktif, defense simulator, dan visualisator model MRA.
2. `02_Persiapan_Sidang/PRESENTASI_PANDUAN_BELAJAR.html`
   - Berkas *all-in-one standalone bundle* yang menyatukan HTML, CSS, dan JS agar mahasiswa dapat langsung membukanya di peramban apa pun (Chrome, Edge, Safari, Firefox) cukup dengan klik dua kali (*double click*).

---

## 4. Alur Kerja (SOP)
1. Periksa ketersediaan berkas sumber di `02_Persiapan_Sidang/`.
2. Jalankan skrip `py execution/build_interactive_presentation.py` (gunakan `py` di Windows).
3. Verifikasi struktur berkas keluaran dan ukuran berkas.
4. Uji tampilan berkas HTML di browser untuk memastikan kelancaran navigasi slide, flip flashcard 3D, dan kuis interaktif.
5. Jika terdapat penambahan soal atau pembaruan materi di `PANDUAN_BELAJAR_PROPOSAL.md`, perbarui data di generator dan jalankan ulang skrip eksekusi.
