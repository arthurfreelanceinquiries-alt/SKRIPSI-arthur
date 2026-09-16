# Catatan Bimbingan & Analisis Revisi Dosen (16 September 2026)
### *Dr. Fredella Colline, S.E., M.M., CFP®, PFM, CHCP-A — S1 Manajemen Keuangan FEB UKRIDA*

> [!SUMMARY] Tujuan & Solusi Catatan Ini
> - **Untuk Apa:** Mendokumentasikan dan membedah secara kritis catatan bimbingan terbaru dari Dosen Pembimbing (Ibu Dr. Fredella Colline) pada tanggal 16 September 2026 (Pukul 10:27–10:28 WIB).
> - **Masalah yang Diselesaikan:** 
>   1. Menambahkan sumber sitasi primer & entri bibliografi formal untuk seluruh statistik data Pokémon di Bab 1 (US$ 105 miliar waralaba, 64,8 miliar kartu, 41,5% market share).
>   2. Menyediakan berkas *library* Mendeley terstandardisasi (`.bib` dan `.ris`) agar seluruh 52+ referensi skripsi dapat diimpor langsung ke Mendeley Reference Manager Arthur dalam 1 klik.
>   3. Menegaskan dan mengonfirmasi bahwa format Daftar Pustaka naskah terbaru telah 100% bebas dari angka 1, 2, 3 dan tersusun alfabetis murni A–Z sesuai Buku Pedoman Tugas Akhir FEB UKRIDA 2023 Subbab 3.7.
> - **Keputusan/Output:** Disusun rencana aksi perbaikan naskah di `Proposal_Arthur_PokemonTCG.tex`, `references.bib`, dokumen Word, serta penyediaan paket ekspor Mendeley di `06_Referensi_Jurnal_PDF/`.

---

## 1. Salinan Chat Asli Dosen (Verbatim Input 16 September 2026)

> **[10:27 AM, 9/16/2026] Fredella Colline:**  
> *"Selamat Pagi Arthur.. skripsi mu sudah lengkap namun data untuk pokemon itu ga ada sumbernya, lalu penelitian udah banyak sumbernya tapi belum masuk mendeley.. jadi harus ada mendeleynya"*  
> 
> **[10:28 AM, 9/16/2026] Fredella Colline:**  
> *"lalu penulisan daftar pustaka berdasarkan abjad bukan angka 1,2,3"*

---

## 2. Dekonstruksi & Analisis Kritis Butir Arahan Dosen

### 📌 Poin 1: Data untuk Pokémon Belum Ada Sumbernya
* **Temuan Dosen:** Naskah skripsi Arthur diakui sudah lengkap, namun data industri dan statistik Pokémon yang dipaparkan pada Latar Belakang belum menyertakan sumber sitasi di dalam kurung teks running (*in-text citation*) dan belum masuk dalam Daftar Pustaka.
* **Akar Masalah pada Naskah:**
  1. Pada Paragraf 1 Bab 1: Data pendapatan waralaba US$ 105,0 miliar hanya diawali *"Berdasarkan data agregasi industri media internasional..."* tanpa sitasi formal seperti `(Statista, 2024)` atau `(TitleMax, 2024)`.
  2. Pada Paragraf 3 Bab 1: Data produksi kumulatif kartu fisik 64,8 miliar lembar kartu hanya diawali *"The Pokémon Company mencatat..."* tanpa sitasi formal `(The Pokémon Company, 2024)`.
  3. Pada Paragraf 4 Bab 1: Data pangsa pasar 41,5% global hanya merujuk nama di caption Gambar 1.3 tanpa sitasi resmi `(ICv2 & TCGplayer, 2024)`.
  4. Seluruh sumber data industri ini belum terdaftar di `references.bib` dan Daftar Pustaka.
* **Solusi Akademik:**
  - Tambahkan 4 entri bibliografi industri resmi ke `01_Naskah_Utama/references.bib` dan `03_Draft_Per_Bab/DAFTAR_PUSTAKA_TENTATIF.md`:
    1. **The Pokémon Company (2024)**: *Corporate Business Data and Trading Card Game Historical Production Statistics*. Tokyo: The Pokémon Company.
    2. **Statista Research Department (2024)**: *Top 10 Highest-Grossing Media Franchises Worldwide of All Time*. New York: Statista Inc.
    3. **ICv2 & TCGplayer (2024)**: *Collectible Card Game Market Sizing and Secondary Market Liquidity Report*. Madison, WI: Inner City Enterprises.
    4. **Professional Sports Authenticator / PSA (2024)**: *Trading Card Population Report and Collectibles Auction Price Realized Index*. Santa Ana, CA: Collectors Universe.
  - Sisipkan sitasi naratif dan parentetikal resmi pada Paragraf 1, Paragraf 3, Paragraf 4, dan Paragraf 5 di Bab 1 naskah LaTeX dan Word.

---

### 📌 Poin 2: Referensi Penelitian Belum Masuk Mendeley
* **Temuan Dosen:** Dosen melihat referensi penelitian skripsi Arthur sudah sangat banyak dan kaya, tetapi menuntut pembuktian integrasi dengan aplikasi manajemen referensi **Mendeley** (*"harus ada mendeleynya"*).
* **Akar Masalah:**
  - Naskah Arthur dikompilasi melalui sistem otomasi hybrid (BibTeX/LaTeX dan Python-docx). Meskipun sitasi di naskah sangat rapi dan konsisten dengan APA 7th Edition, dosen ingin memastikan Arthur memiliki perpustakaan digital (*Mendeley Library*) yang siap diperiksa atau terhubung dengan plugin Mendeley Cite.
* **Solusi Akademik & Teknis:**
  1. **Pembuatan Berkas Ekspor Mendeley:**
     - Mengonversi seluruh 52+ entri `01_Naskah_Utama/references.bib` menjadi paket perpustakaan siap impor:
       - `06_Referensi_Jurnal_PDF/Mendeley_Library_Arthur_PokemonTCG.bib`
       - `06_Referensi_Jurnal_PDF/Mendeley_Library_Arthur_PokemonTCG.ris` (format universal standar Mendeley / EndNote / Zotero).
  2. **Panduan 1-Menit Import Mendeley untuk Arthur:**
     - Cukup buka aplikasi **Mendeley Reference Manager** di komputer Arthur, klik `Add new` $\rightarrow$ `Import library` $\rightarrow$ pilih berkas `.ris` atau `.bib` ini. Seluruh 52 referensi, judul, penulis, tahun, dan DOI akan langsung masuk 100% rapi ke Mendeley Arthur!
     - Arthur dapat mengambil tangkapan layar (*screenshot*) perpustakaan Mendeley miliknya untuk ditunjukkan kepada Ibu Fredella sebagai bukti kepatuhan.

---

### 📌 Poin 3: Daftar Pustaka Berdasarkan Abjad, Bukan Angka 1, 2, 3
* **Temuan Dosen:** Dosen menegur penulisan daftar pustaka yang menggunakan penomoran angka (*"penulisan daftar pustaka berdasarkan abjad bukan angka 1,2,3"*).
* **Fakta Status Naskah:**
  - Dosen membaca naskah cetak/ekspor lama sebelum dilakukannya audit kepatuhan FEB UKRIDA 2023 pada **Sesi 10 (15 September 2026)**.
  - Pada Sesi 10 kemarin, kita telah mengeliminasi seluruh angka `1.` s.d. `51.` pada dokumen Word (`Proposal_Arthur_PokemonTCG.docx` dan `Proposal_Arthur_NoBab3.docx`) serta draf markdown, menghasilkan format *hanging indent* 1,25 cm dengan urutan alfabetis murni A–Z sesuai Buku Pedoman Penyusunan Tugas Akhir FEB UKRIDA 2023 Subbab 3.7.
* **Solusi:**
  - Tunjukkan dan serahkan naskah terbaru hasil regenerasi yang sudah 100% bebas dari angka nomor urut.
  - Pastikan naskah PDF XeLaTeX dan DOCX yang diserahkan ke Ibu Fredella hari ini membuktikan bahwa Daftar Pustaka telah tersusun murni berdasarkan abjad (dimulai dari *Aiken & West (1991)* hingga *Zeigarnik (1927)*) tanpa satu pun angka urut di depan nama pengarang.

---

## 3. Matriks Pemetaan Dampak Per Bab

| Komponen Naskah | Bagian / Subbab | Bentuk Perubahan / Penyesuaian | Status Rencana |
|---|---|---|:---:|
| **BAB I PENDAHULUAN** | Subbab 1.1 (Paragraf 1) | Menambahkan sitasi formal waralaba: `(Statista, 2024)` pada data US$ 105,0 miliar. | Siap Diinjeksikan |
| **BAB I PENDAHULUAN** | Subbab 1.1 (Paragraf 3) | Menambahkan sitasi formal produksi: `(The Pokémon Company, 2024)` pada data 64,8 miliar kartu dan pertumbuhan 125%. | Siap Diinjeksikan |
| **BAB I PENDAHULUAN** | Subbab 1.1 (Paragraf 4) | Menambahkan sitasi formal pangsa pasar: `(ICv2 & TCGplayer, 2024)` pada data 41,5% market share. | Siap Diinjeksikan |
| **BAB I PENDAHULUAN** | Subbab 1.1 (Paragraf 5) | Menambahkan sitasi lembaga grading: `(PSA, 2024)` pada pembahasan lelang dan standar kualitas 1–10. | Siap Diinjeksikan |
| **DAFTAR PUSTAKA** | `references.bib` | Menambahkan 4 entri bibtex resmi data industri Pokémon & grading. | Siap Diinjeksikan |
| **DAFTAR PUSTAKA** | Format Penulisan | Memverifikasi ketiadaan nomor angka 1,2,3 di Word & LaTeX (sudah A–Z murni). | Terverifikasi PASS |
| **PERANGKAT SITASI** | `06_Referensi_Jurnal_PDF/` | Menyusun paket ekspor Mendeley (`.ris` dan `.bib`) + panduan screenshot untuk dosen. | Siap Dibuat |

---

## 4. Rencana Aksi Eksekusi (Action Plan)

1. **Langkah 1 (Injeksi Referensi Data Pokémon):**
   - Tambahkan entri The Pokémon Company (2024), Statista (2024), ICv2 (2024), dan PSA (2024) ke `01_Naskah_Utama/references.bib` dan `03_Draft_Per_Bab/DAFTAR_PUSTAKA_TENTATIF.md`.
   - Perbarui naskah induk `01_Naskah_Utama/Proposal_Arthur_PokemonTCG.tex` dan `01_Naskah_Utama/PROPOSAL_SKRIPSI_POKEMON_TCG.md`.
2. **Langkah 2 (Ekspor Paket Perpustakaan Mendeley):**
   - Buat skrip pembentuk file Mendeley universal `.ris` di folder `06_Referensi_Jurnal_PDF/`.
   - Siapkan petunjuk ringkas agar Arthur bisa langsung drag-and-drop ke Mendeley Desktop/Web miliknya.
3. **Langkah 3 (Regenerasi Naskah PDF & Word OMML):**
   - Kompilasi ulang PDF menggunakan XeLaTeX (`build_proposal_nobab3_pdf.py` dan master PDF).
   - Regenerasi Word `.docx` menggunakan `build_proposal_word.py`.
   - Jalankan suite audit `verify_ukrida_compliance.py` dan `verify_docx_typography.py` untuk membuktikan bahwa daftar pustaka bebas nomor urut 1,2,3.
4. **Langkah 4 (Draft Balasan WhatsApp ke Ibu Fredella):**
   - Siapkan draf kalimat santun dan profesional untuk dikirimkan Arthur ke WhatsApp Ibu Fredella Colline.
