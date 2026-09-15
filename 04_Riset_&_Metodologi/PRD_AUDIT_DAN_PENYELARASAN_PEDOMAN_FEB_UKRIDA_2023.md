# PRD: Audit & Penyelarasan Kepatuhan Pedoman Tugas Akhir FEB UKRIDA 2023

> [!SUMMARY] Tujuan & Solusi Catatan Ini
> - **Untuk Apa:** Menjadi dokumen rujukan (*Product Requirements Document*) untuk memastikan naskah proposal skripsi Arthur 100% patuh terhadap seluruh ketentuan Buku Pedoman Penyusunan Tugas Akhir FEB UKRIDA 2023 (SK Dekan No. 350a/SK/UKKW/FEB/D/VI/2023).
> - **Masalah yang Diselesaikan:** Mengeliminasi celah ketidaksesuaian format teknis, memastikan kepatuhan kuota jurnal terindeks SINTA/Internasional, membakukan gaya sitasi dalam teks (in-text citations), serta membersihkan format Daftar Pustaka dari nomor urut dan menyesuaikannya dengan gaya penulisan referensi resmi UKRIDA 2023.
> - **Keputusan/Output:** Panduan audit 7 butir kepatuhan mutlak dan cetak biru standarisasi format pada arsitektur 3-Layer.

---

## 1. Latar Belakang & Landasan Otoritas

Buku Pedoman Penyusunan Tugas Akhir FEB UKRIDA 2023 merupakan otoritas tertinggi yang mengikat seluruh mahasiswa S1 Manajemen FEB UKRIDA. Setiap naskah proposal yang akan diajukan ke seminar proposal wajib melewati audit kepatuhan administratif dan format teknis.

Berdasarkan audit komparatif antara Buku Pedoman 2023 dengan naskah aktif (`Proposal_Arthur_PokemonTCG.pdf`, `Proposal_Arthur_PokemonTCG.docx`, `PROPOSAL_SKRIPSI_POKEMON_TCG.md`, dan `references.bib`), telah diidentifikasi status kepatuhan serta area perbaikan teknis.

---

## 2. Matriks Hasil Audit Komprehensif (Status Kepatuhan)

| No | Ketentuan Pedoman 2023 | Pasal / Halaman | Syarat Minimum | Realisasi Naskah Arthur | Status Audit | Catatan Tindakan |
|:---:|:---|:---:|:---|:---|:---:|:---|
| **1** | **Sitasi Jurnal SINTA / Internasional** | Subbab 1.4.c (hlm. 4) | Minimal **5 artikel** terindeks SINTA dan/atau Internasional | **>15 artikel** terverifikasi (SINTA 1, SINTA 2, SINTA 4, dan 8+ Scopus Q1) | **LULUS MUTLAK (PASS)** | Melampaui kuota minimal 3x lipat |
| **2** | **Sitasi Dosen FEB UKRIDA** | Subbab 1.4.b (hlm. 4) | Wajib mensitasi karya dosen FEB UKRIDA yang relevan | Mengutip Dr. Fredella Colline (2024), *Accounting and Finance Studies* | **LULUS MUTLAK (PASS)** | Disitasi di Bab 1, 2, dan 3 |
| **3** | **Tebal Minimum Halaman** | Subbab 1.4.a (hlm. 4) | TA minimal 50 halaman (Bab 1–5) | Naskah proposal Bab 1–3 sudah **54 halaman** | **LULUS (PASS)** | Melebihi standar minimum proposal |
| **4** | **Jumlah Referensi Kepustakaan** | Subbab 1.5.b.1 (hlm. 5) & 3.7 (hlm. 21) | Minimal **20 referensi** mutakhir (5 tahun terakhir untuk empiris) | **51 referensi** (10 empiris 2021–2025 + teori seminal) | **LULUS (PASS)** | 100% bebas dari referensi skripsi |
| **5** | **Tata Letak & Tipografi Fisik** | Subbab 3.1 & 3.2 (hlm. 15–16) | Margin 4-3-3-3 cm, TNR 12pt, Spasi 1.5, Justify, Pure Black #000000 | 100% terstandarisasi di XeLaTeX dan Word OMML | **LULUS (PASS)** | Skrip verifikasi tipografi lulus 100% |
| **6** | **Gaya Sitasi dalam Teks (*In-Text*)** | Subbab 3.6 (hlm. 19–20) | - 1 penulis: *Nama (Tahun)*<br>- 2 penulis: *Nama dan Nama (Tahun)*<br>- >2 penulis: *Nama et al. (Tahun)* (*et al.* miring) | Sebagian masih menggunakan tanda `&` atau `and` dari sintaks LaTeX/Markdown | **PERLU PENYELARASAN (ACTION)** | Standarisasi kata hubung **"dan"** dan miringkan ***et al.*** |
| **7** | **Format Daftar Pustaka** | Subbab 3.7 (hlm. 21–23) | - Urut abjad<br>- **DILARANG MENGGUNAKAN NOMOR URUT**<br>- Hanging indent 1.25 cm<br>- Format Buku: *Nama. Tahun. Judul. Kota: Penerbit.*<br>- Format Jurnal: *Nama. Tahun. “Judul”. Nama Jurnal Vol: Hal.* | Markdown & Word masih memuat **nomor urut (1. 2. 3...)** dan belum menggunakan tanda kutip pada judul artikel | **PERLU PENYELARASAN (ACTION)** | Hapus nomor urut; terapkan format kutip judul artikel UKRIDA 2023 |

---

## 3. Rincian Aturan Sitasi & Daftar Pustaka Pedoman FEB UKRIDA 2023

### A. Aturan Sitasi dalam Teks (Subbab 3.6)
1. **Satu Penulis:**
   - Di awal/tengah kalimat: `Colline (2024)`
   - Di akhir kalimat: `(Colline, 2024)`
   - Nama Tionghoa tidak dibalik: `Kwik (2010)`
2. **Dua Penulis:**
   - Wajib menggunakan kata hubung bahasa Indonesia **"dan"** (bukan `&` atau `and`):
     - Contoh: `Tan dan Adyantari (2024)` atau `(Tan dan Adyantari, 2024)`
     - Contoh: `Barber dan Odean (2008)` atau `(Barber dan Odean, 2008)`
3. **Lebih dari Dua Penulis:**
   - Ditulis nama keluarga penulis pertama diikuti singkatan ***et al.*** yang dicetak miring:
     - Contoh: `Gong et al. (2024)` atau `(Gong et al., 2024)`
     - Contoh: `Barasz et al. (2017)` atau `(Barasz et al., 2017)`
4. **Kutipan Tidak Langsung vs Langsung:**
   - Kutipan tidak langsung: dirangkai dalam kalimat tanpa tanda kutip.
   - Kutipan langsung $\le 3$ baris: diapit dua tanda kutip `“...”`.
   - Kutipan langsung $> 3$ baris: alinea terpisah, spasi 1, indentasi kiri dan kanan 5 ketukan (1.25 cm).

---

### B. Aturan Format Daftar Pustaka (Subbab 3.7)
1. **Larangan Nomor Urut:**
   - Daftar pustaka disusun menurut abjad nama pengarang **tanpa didahului nomor urut (1, 2, 3) atau garis strip (-)**.
2. **Indentasi Gantung (*Hanging Indent*):**
   - Baris pertama rata kiri, baris kedua dan seterusnya menjorok 1.25 cm (5 ketukan), spasi 1.5.
3. **Format Artikel Jurnal Ilmiah:**
   - `Nama Pengarang. Tahun. “Judul Artikel”. *Nama Jurnal* Volume(Nomor): Halaman.`
   - *Perhatikan:* Judul artikel diapit tanda kutip dua `“...”`, nama jurnal dicetak miring (*italic*), tahun tidak diapit tanda kurung.
   - Contoh UKRIDA:
     > Aretz, K. dan Bartram, S. 2010. “Corporate hedging and shareholder value”. *Journal of Financial Research* 33: 317 – 371.
4. **Format Buku Teks:**
   - `Nama Pengarang. Tahun. *Judul Buku Miring*. Edisi (jika ada). Kota Penerbit: Nama Penerbit.`
   - Contoh UKRIDA:
     > Morgan, Daniel G. 2006. *Microeconomic theory*. Singapore: Prentice Hall.
     > Ghozali, I. 2018. *Aplikasi Analisis Multivariate dengan Program IBM SPSS 25*. Edisi 9. Semarang: Badan Penerbit Universitas Diponegoro.

---

## 4. Desain Implementasi 3-Layer Architecture

### Layer 1: Directives (Panduan & Standar Baku)
- File: `directives/verify_ukrida_2023_guidelines.md`
- Menetapkan SOP verifikasi kepatuhan naskah terhadap Buku Pedoman 2023 (checklist 7 poin).

### Layer 2: Orchestration (Perencanaan & Tata Sinkronisasi)
- Memastikan pembaruan format dilakukan serempak di:
  1. `03_Draft_Per_Bab/DAFTAR_PUSTAKA_TENTATIF.md` (membersihkan penomoran angka, mengonversi ke format UKRIDA 2023).
  2. `01_Naskah_Utama/PROPOSAL_SKRIPSI_POKEMON_TCG.md` (sinkronisasi teks markdown).
  3. `execution/build_proposal_word.py` (memodifikasi fungsi `build_daftar_pustaka` agar secara deterministik mencetak format gantung tanpa angka).
  4. Naskah Word (`Proposal_Arthur_PokemonTCG.docx` & `Proposal_Arthur_NoBab3.docx`) dan naskah XeLaTeX (`references.bib` & PDF).

### Layer 3: Execution (Skrip Otomasi & Audit Deterministik)
- File: `execution/verify_ukrida_compliance.py`
  - Memeriksa ketiadaan nomor urut pada Daftar Pustaka Word/Markdown.
  - Memeriksa keberadaan minimal 5 jurnal SINTA / Internasional.
  - Memeriksa keberadaan sitasi dosen FEB UKRIDA.
  - Memeriksa kata hubung sitasi dua penulis ("dan").
- Menjalankan kembali `execution/build_proposal_word.py` untuk menghasilkan naskah Word yang 100% compliant.
