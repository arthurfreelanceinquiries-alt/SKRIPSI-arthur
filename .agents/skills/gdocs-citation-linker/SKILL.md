---
name: gdocs-citation-linker
description: >
  Menstandarkan dan memulihkan tautan sitasi interaktif (cross-referencing) pada dokumen tesis/skripsi
  lintas platform: Word DOCX (OOXML visible bookmark Ref_*) dan Google Docs Web (native Apps Script
  bookmark #bookmark=<id>). Mencegah sitasi in-text menjadi teks mati setelah konversi DOCX ke Google Docs.
  Gunakan skill ini setiap kali membuat, memodifikasi, mengekspor naskah skripsi, menambahkan sitasi baru,
  atau memulihkan navigasi klik sitasi (Author, Year) menuju DAFTAR PUSTAKA.
---

# Google Docs & DOCX Citation Linker Skill

Skill ini menetapkan protokol standar untuk memastikan seluruh sitasi in-text di dalam naskah skripsi/tesis **BUKAN TEKS MATI**, melainkan tautan interaktif yang dapat diklik langsung untuk melompat ke entri terkait di **DAFTAR PUSTAKA**, baik saat dibuka di **Microsoft Word Desktop** maupun **Google Docs Web**.

---

## 🏗️ Arsitektur Tiga Lapis (3-Layer Cross-Referencing)

Ketika dokumen DOCX yang dihasilkan dari script/LaTeX diunggah ke Google Drive dan dikonversi ke Google Docs via *"Open with Google Docs"*, konverter internal Google **sering membuang `<w:hyperlink w:anchor>` dan bookmark Word** (terutama bookmark tersembunyi berawalan underscore `_Ref_*`).

Untuk menjamin keandalan 100%, sistem menerapkan arsitektur 3 lapis:

```
┌─────────────────────────────────────────────────────────────┐
│ Layer 1: DOCX Native Visible Bookmarks (build_proposal_word)│
│  - Bookmark: Ref_<kunci> (tanpa awalan underscore '_')     │
│  - Hyperlink internal OOXML: <w:hyperlink w:anchor="Ref_*"> │
│  - Navigasi Word Desktop: Ctrl + Klik                       │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ Layer 2: Parity & Invariant Verification Engine             │
│  - verify_docx_typography.py & verify_pdf_docx_parity.py   │
│  - Invariant: 0 anchor yatim, 100% entri DP ter-bookmark    │
│  - Teks paragraf pre/post snapshot identik 100%             │
└──────────────────────────────┬──────────────────────────────┘
                               │ (Saat diunggah ke GDrive & Convert)
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ Layer 3: Google Docs Native Relinker (Apps Script)          │
│  - Script: execution/fix_gdocs_citation_links.gs            │
│  - Bersihkan bookmark lama (idempoten)                      │
│  - Buat Google Docs Bookmarks native di tiap entri DP        │
│  - Tautkan sitasi teks via setLinkUrl('#bookmark=<id>')     │
│  - Navigasi Google Docs Web: Klik Biasa (Single Click)      │
└─────────────────────────────────────────────────────────────┘
```

---

## 📋 Aturan Baku Penulisan Sitasi & Pustaka

Agar parser otomatis dapat mengekstrak nama penulis dan tahun secara deterministik, seluruh sitasi dan entri daftar pustaka **WAJIB** mengikuti format standar:

### 1. Sitasi In-Text
- **Parentetikal:** `(NamaBelakang, Tahun)` atau `(Nama1 & Nama2, Tahun)` atau `(Nama et al., Tahun)`
  - Contoh: `(Barasz et al., 2017)`, `(Statista, 2024)`, `(Arnold & Reynolds, 2003)`
- **Naratif:** `NamaBelakang (Tahun)` atau `Nama1 dan Nama2 (Tahun)` atau `Nama et al. (Tahun)`
  - Contoh: `Barasz et al. (2017)`, `Arnold dan Reynolds (2003)`
- **Dilarang Keras:**
  - Menuliskan gelar akademik pada sitasi (misal: *Dr. Colline (2024)* -> **HARUS** *Colline (2024)*).
  - Menambahkan karakter visual buatan seperti `[🔗]` yang merusak standar baku kampus.
  - Mengubah warna sitasi menjadi biru bergaris bawah di DOCX tubuh (harus tetap hitam *pure black* tanpa *underline*).

### 2. Entri DAFTAR PUSTAKA
- Format APA 7th Edition: `NamaBelakang, Inisial. (Tahun). Judul Artikel...`
  - Contoh: `Barasz, K., John, L. K., Keenan, E. A., & Norton, M. I. (2017). Pseudo-set framing...`
- Penulis Korporat: `Statista. (2024). Pokémon franchise revenue...`
- Heading bab wajib bernama tepat: `DAFTAR PUSTAKA`.

---

## 🛠️ Panduan Operasional Layer 3: Google Docs Apps Script

### Berkas Sumber
Skrip resmi berada di: [`execution/fix_gdocs_citation_links.gs`](file:///d:/Perkuliahan/Skripsi/SKRIPSI-arthur/execution/fix_gdocs_citation_links.gs)

### Langkah Eksekusi di Google Docs Web (2 Menit):
1. **Buka Dokumen di Docs:** Unggah berkas `.docx` ke Google Drive -> Klik Kanan -> *Buka dengan Google Docs (Open with Google Docs)*.
2. **Buka Apps Script:** Pada menu Google Docs, pilih **Ekstensi (*Extensions*)** > **Apps Script**.
3. **Pasang Skrip:**
   - Hapus kode default di file `Code.gs`.
   - Salin seluruh isi dari `execution/fix_gdocs_citation_links.gs`.
   - Simpan (*Save* / Ctrl+S).
4. **Jalankan Relinker:**
   - Pilih fungsi `relinkCitationsToDP` dari dropdown menu.
   - Klik **Jalankan (*Run*)**.
   - Berikan otorisasi izin akses dokumen (*Review Permissions* -> Pilih Akun -> *Advanced* -> *Go to Untitled project (unsafe)* -> *Allow*).
   - Klik **Jalankan (*Run*)** sekali lagi.
5. **Verifikasi:**
   - Dialog konfirmasi akan muncul:
     ```
     Selesai.
     DP ter-bookmark: 55
     Sitasi tertaut: 241
     Dilewati (tak cocok): 0

     Klik sitasi (klik biasa) untuk lompat ke Daftar Pustaka.
     ```
   - Di dokumen Google Docs: Klik sembarang sitasi in-text, misalnya `(Barasz et al., 2017)` — kursor akan langsung melompat mulus ke entri pustaka terkait di DAFTAR PUSTAKA!
6. **(Opsional) Audit Total Tautan:**
   - Jalankan fungsi `verifyCitationLinks` di Apps Script untuk memastikan rasio sitasi ber-link mendekati 100%.

---

## 🔍 Logika Algoritma Pencocokan (`parseDpEntry` & `bestMatch`)

1. **Parser Entri DP (`parseDpEntry`):**
   - Menangkap ekspresi reguler `^(.+?)\(\s*((?:19|20)\d{2}[a-z]?)\s*\)`.
   - Memecah penulis ganda (`dan`, `and`, `&`, `;`).
   - Mengambil nama belakang (*surname*) sebelum tanda koma pertama.
   - Menangani penulis korporat multi-kata (`Statista`, `The Pokémon Company`).
2. **Matcher Sitasi (`bestMatch`):**
   - Mencocokkan tahun publikasi secara presisi.
   - Menghitung skor kemiripan (*similarity score*) kemunculan nama belakang di dalam teks sitasi.
   - Memilih kandidat dengan skor tertinggi (`bestScore > 0`).
3. **Pengurutan Terbalik (*Right-to-Left Replacement*):**
   - Sitasi dalam satu paragraf diurutkan dari posisi indeks akhir ke awal (`b.s - a.s`) sebelum ditautkan.
   - Menjamin indeks pergeseran karakter tidak merusak posisi teks sitasi berikutnya.

---

## ✅ Kriteria Keberhasilan (Quality Checklist)
- [ ] **DOCX Word Desktop:** Seluruh sitasi dapat di-Ctrl+klik menuju DAFTAR PUSTAKA.
- [ ] **Google Docs Web:** Seluruh sitasi dapat diklik biasa (single click) menuju DAFTAR PUSTAKA.
- [ ] **Zero Orphaned Bookmarks:** Tidak ada hyperlink yang mengarah ke target yang tidak ada.
- [ ] **Zero Format Degradation:** Teks sitasi tetap hitam, tidak ada penambahan simbol aneh, dan tidak ada pemenggalan kalimat.
- [ ] **Idempoten:** Skrip aman dijalankan berulang kali tanpa membuat duplikasi bookmark.
