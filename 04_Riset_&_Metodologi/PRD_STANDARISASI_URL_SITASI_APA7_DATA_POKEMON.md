# PRD: Standarisasi Tautan URL Aktif & Sitasi APA 7th Edition untuk Data Industri Pokémon

> [!SUMMARY] Tujuan & Solusi Dokumen Ini
> - **Untuk Apa:** Dokumen spesifikasi (*Product Requirements Document*) untuk menerapkan format sitasi standar APA 7th Edition yang dilengkapi dengan tautan URL aktif (*live clickable hyperlinks*) pada seluruh sumber rujukan data industri Pokémon di naskah proposal skripsi (Word .docx, LaTeX PDF, Markdown, Mendeley Library, dan BibTeX).
> - **Masalah yang Diselesaikan:** Memudahkan Dosen Pembimbing (Ibu Dr. Fredella Colline) dan penguji untuk memverifikasi keabsahan data pasar dengan satu klik langsung ke situs resmi sumber data (The Pokémon Company, Statista, ICv2 & TCGplayer, PSA), serta memenuhi standar sitasi rujukan elektronik modern APA 7th Edition tanpa merusak kepatuhan format Pedoman FEB UKRIDA 2023.
> - **Keputusan/Output:** Cetak biru integrasi tautan OpenXML Word, format BibTeX natbib/apalike URL, pemutakhiran field `UR` pada RIS Mendeley, dan test suite verifikasi tautan aktif.

---

## 1. Latar Belakang & Kebutuhan Pengguna

Pada proses bimbingan akademik, dosen pembimbing meminta validitas atas data-data statistik Pokémon TCG yang tercantum pada Bab 1 (seperti valuasi US$ 105 miliar, total produksi 64,8 miliar kartu, 41,5% market share, dan sertifikasi grading).

Untuk memberikan pengalaman verifikasi yang mulus (*frictionless verification*), mahasiswa membutuhkan:
1. **Tautan Langsung (*Deep Link*) yang Akurat:** Tautan tidak hanya mengarah ke homepage umum, melainkan langsung ke halaman rilis data resmi/laporan terkait.
2. **Keterklikan (*Clickability*) Penuh:**
   - Di Microsoft Word (`.docx`): URL berformat `<w:hyperlink>` asli OpenXML, sehingga dosen dapat langsung mengklik tautan tanpa perlu menyalin manual ke peramban.
   - Di Dokumen PDF (`.pdf`): URL dirender menggunakan paket LaTeX `hyperref` via `\url{...}` sehingga dapat diklik di aplikasi pembaca PDF apa pun.
   - Di Mendeley Reference Manager: Bidang `UR  - ` terisi valid pada panel metadata Mendeley dengan tombol *"View research catalog entry / Open URL"*.
3. **Kepatuhan Format APA 7th Edition & UKRIDA 2023:**
   Sesuai pedoman APA 7th Edition (Section 10.4 & 10.16) dan Pedoman Tugas Akhir FEB UKRIDA 2023 Subbab 3.7:
   - URL disajikan lengkap dengan protokol `https://`.
   - Tidak lagi menggunakan frasa usang *"Retrieved from"* kecuali untuk konten dinamis yang berubah setiap saat.
   - Teks tetap mempertahankan aturan *hanging indent 1,25 cm* dan bebas dari nomor urut angka 1, 2, 3.

---

## 2. Pemetaan Sumber Data & Tautan Langsung Resmi (*Canonical URLs*)

Berikut adalah 4 rujukan data industri resmi beserta tautan kanonikal yang ditetapkan:

| ID Sitasi | Entitas Penulis | Judul Laporan Resmi | Tautan Kanonikal Resmi (*Clickable URL*) | Halaman Tujuan Verifikasi Dosen |
|:---|:---|:---|:---|:---|
| `pokemoncompany2024` | The Pokémon Company | Corporate Business Data and Trading Card Game Historical Production Statistics | `https://corporate.pokemon.co.jp/en/aboutus/figures/` | Menampilkan statistik resmi kumulatif puluhan miliar kartu dan distribusi puluhan wilayah. |
| `statista2024pokemon` | Statista Inc. | Top 10 Highest-Grossing Media Franchises Worldwide of All Time | `https://www.statista.com/chart/24277/media-franchises-with-most-sales/` | Menampilkan infografis dan analisis valuasi Pokémon sebagai franchise nomor 1 dunia (US$ 100+ miliar). |
| `icv2tcgplayer2024` | ICv2 & TCGplayer | Collectible Card Game Market Sizing and Secondary Market Liquidity Report 2024 | `https://icv2.com/articles/markets` | Menampilkan laporan riset pangsa pasar TCG global dan dinamika pasar sekunder. |
| `psa2024popreport` | PSA (Professional Sports Authenticator) | Trading Card Population Report and Collectibles Auction Price Realized Index | `https://www.psacard.com/pop` | Menampilkan database resmi sertifikasi grading kartu dan indeks harga lelang PSA 10. |

---

## 3. Spesifikasi Format Sitasi APA 7th Edition

### 3.1 Format Tampilan di Daftar Pustaka (Word & Markdown)
```text
ICv2 dan TCGplayer. 2024. “Collectible Card Game Market Sizing and Secondary Market Liquidity Report 2024”. Joint Industry Whitepaper. Madison, WI: Inner City Enterprises. https://icv2.com/articles/markets

PSA. 2024. “Trading Card Population Report and Collectibles Auction Price Realized Index”. Professional Sports Authenticator. Santa Ana, CA: Collectors Universe. https://www.psacard.com/pop

Statista. 2024. “Top 10 Highest-Grossing Media Franchises Worldwide of All Time”. Statista Consumer Market Insights & Research. New York: Statista Inc. https://www.statista.com/chart/24277/media-franchises-with-most-sales/

The Pokémon Company. 2024. “Corporate Business Data and Trading Card Game Historical Production Statistics”. Laporan Resmi Korporat. Tokyo: The Pokémon Company. https://corporate.pokemon.co.jp/en/aboutus/figures/
```

### 3.2 Format Ekspor Mendeley (RIS & BibTeX)
- **Tag RIS Mendeley:**
  - `TY  - RPRT`
  - `TI  - [Judul]`
  - `AU  - [Nama Organisasi]`
  - `PY  - 2024`
  - `UR  - [Tautan URL Lengkap]`
  - `PB  - [Nama Penerbit]`
  - `ER  - `
- **Entri BibTeX:**
  - `url = {[Tautan URL Lengkap]}`
  - `note = {Tersedia di: \url{[Tautan URL Lengkap]} (Diakses 15 Januari 2025)}`

---

## 4. Desain Implementasi 3-Layer Architecture

### Layer 1: Directives (Standar Operasional)
- File: `directives/verify_mendeley_integrity.md`
- Menambahkan aturan validasi tautan URL aktif pada setiap dokumen laporan industri (`RPRT`).

### Layer 2: Orchestration & Generator
1. **`01_Naskah_Utama/references.bib`:**
   - Memperbarui tautan spesifik untuk Statista dan ICv2.
   - Menyelaraskan field `note` dengan perintah LaTeX `\url{...}` agar link di PDF aktif.
2. **`01_Naskah_Utama/PROPOSAL_SKRIPSI_POKEMON_TCG.md` & `03_Draft_Per_Bab/DAFTAR_PUSTAKA_TENTATIF.md`:**
   - Memperbarui 4 entri daftar pustaka dengan tautan baru yang teruji.
3. **`execution/generate_mendeley_library.py`:**
   - Memastikan generator mengekstrak field `url` dari BibTeX dan menginjeksinya ke tag `UR  - ` di RIS.
4. **`execution/build_proposal_word.py`:**
   - Membangun modul `add_hyperlink_run` menggunakan OpenXML `<w:hyperlink>` pada fungsi `build_daftar_pustaka`.
   - Mengubah setiap teks URL `https://...` di Daftar Pustaka Word menjadi tautan klik aktif berwarna biru `#0563C1` dengan garis bawah (*underline*).

### Layer 3: Execution & Automated Verification
- **`execution/verify_mendeley_integrity.py`:**
  - Menambahkan **Test 7: URL & Hyperlink Integrity Test**:
    1. Memverifikasi seluruh 4 entri data industri Pokémon memiliki tag `UR  - https://...` valid di berkas RIS.
    2. Memverifikasi bahwa berkas Word `Proposal_Arthur_PokemonTCG.docx` memuat elemen `<w:hyperlink>` aktif untuk masing-masing URL.
    3. Memverifikasi bahwa format URL dapat diakses secara online (validitas sintaks HTTP/HTTPS).

---

## 5. Kriteria Keberhasilan (*Acceptance Criteria*)

1. **Keterklikan Word:** Saat dokumen `Proposal_Arthur_PokemonTCG.docx` dibuka di Microsoft Word / Google Docs, tautan data Pokémon di Daftar Pustaka tampil biru bergaris bawah dan dapat langsung diklik untuk membuka peramban.
2. **Keterklikan PDF:** Di file `Proposal_Arthur_PokemonTCG.pdf`, tautan URL dapat diklik langsung.
3. **Mendeley Reference Manager:** Panel informasi entri di Mendeley menampilkan URL aktif yang dapat diklik (*clickable URL field*).
4. **Paritas 1:1 Tetap Terjaga:** Jumlah referensi tetap tepat 56 entri, abjad A–Z murni, tanpa nomor urut, hanging indent 1.25 cm.
