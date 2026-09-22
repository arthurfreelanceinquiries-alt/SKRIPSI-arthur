# 📋 PRODUCT REQUIREMENTS DOCUMENT (PRD)
## Revisi Naskah DOCX: Eliminasi Font Biru, Penyempurnaan Dot Leaders Daftar Isi, & Penyelarasan Kualitas Tipografi LaTeX/PDF

> [!SUMMARY] Tujuan & Solusi Catatan Ini
> - **Untuk Apa:** PRD komprehensif untuk merevisi generator Microsoft Word (`execution/build_proposal_word.py`) agar naskah DOCX (`Proposal_Arthur_NoBab3.docx` dan `Proposal_Arthur_PokemonTCG.docx`) memiliki kualitas tipografi setara publikasi LaTeX/PDF.
> - **Masalah yang Diselesaikan:** 
>   1. Menghilangkan warna font biru pada semua judul bab (`Heading 1`), sub-bab (`Heading 2`, `Heading 3`), dan judul frontmatter (`DAFTAR GAMBAR`, `DAFTAR TABEL`, `DAFTAR ISI`).
>   2. Memperbaiki tampilan Daftar Isi, Daftar Tabel, dan Daftar Gambar agar garis titik-titik (*dot leaders*) muncul sempurna, rapi di batas margin kanan (14,0 cm), dan kompatibel baik di Microsoft Word Desktop maupun Google Docs / Word Online / WPS Office.
>   3. Memperbaiki nomor halaman pada footer agar nomor romawi/arab tidak hilang pada viewer non-desktop.
> - **Keputusan/Output:** Panduan spesifikasi teknis dan implementasi revisi generator DOCX.

---

## 1. Identifikasi Masalah & Akar Penyebab (Root Cause Analysis)

### A. Masalah 1: Font Berwarna Biru pada Judul (`Heading 1`, `Heading 2`, `Heading 3`)
* **Gejala:** Judul `DAFTAR GAMBAR`, `BAB 1 PENDAHULUAN`, dan `1.1 Latar Belakang Penelitian` berwarna biru saat dibuka oleh pengguna.
* **Akar Masalah Teknis:**
  1. Paragraf judul menggunakan `style='Heading 1'` dan `style='Heading 2'`. Di dalam template bawaan OpenXML / Word / Google Docs, gaya Heading dikaitkan dengan *theme accent color* (Accent 1 = Biru `#2E74B5` atau `#1155CC`).
  2. Fungsi `parse_markdown_runs()` yang mengisi teks judul hanya mengatur font (`Times New Roman`), ukuran (`12 pt`), dan tebal (`bold`), tetapi **tidak menyematkan warna teks eksplisit** (`run.font.color.rgb = RGBColor(0, 0, 0)`).
  3. Akibatnya, aplikasi pembaca dokumen (Google Docs, Word Online, WPS, dan Word Desktop dengan template default) mewarisi warna biru dari tema dokumen.
* **Solusi Mutlak:**
  - Sematkan warna eksplisit `<w:color w:val="000000"/>` (RGB `0, 0, 0`) langsung pada setiap *run* judul di tingkat XML (`run._r.get_or_add_rPr()`). Di OpenXML, format run langsung (*direct run formatting*) memiliki prioritas tertinggi dan **kebal dari override tema aplikasi apapun**.
  - Bersihkan seluruh atribut `w:themeColor`, `w:themeShade`, dan `w:themeTint` pada `styles.xml` untuk semua gaya `Heading 1`, `Heading 2`, `Heading 3`, `Title`, `Subtitle`, dan `Normal`.

---

### B. Masalah 2: Garis Titik-Titik Hilang pada Daftar Isi, Daftar Tabel, & Daftar Gambar
* **Gejala:** Entri daftar isi menampilkan judul yang langsung diikuti nomor halaman dengan spasi kosong atau tab polos (contoh: `BAB 1 PENDAHULUAN   1`), tanpa garis titik-titik (*dot leaders*).
* **Akar Masalah Teknis:**
  1. Paragraf TOC saat ini menggunakan gaya `Normal` dengan modifikasi ad-hoc `tab_stops.add_tab_stop()`. Aplikasi seperti Google Docs dan Word Online mengabaikan tab stop ad-hoc pada gaya `Normal` dan mengubah `\t` menjadi tab spasi kosong standar (0,5 inci).
  2. Gaya resmi TOC (`TOC 1`, `TOC 2`, `TOC 3`) belum terdaftar secara resmi di `styles.xml` dengan atribut `<w:tabs><w:tab w:val="right" w:leader="dot" w:pos="7938"/></w:tabs>`.
  3. Ketika judul bab/sub-bab panjang mengalami pemenggalan baris (*wrap*), baris kedua tidak memiliki *hanging indent* yang tepat, sehingga titik-titik memenuhi satu baris penuh sebelum nomor halaman.
* **Solusi Mutlak:**
  - Daftarkan gaya resmi `TOC 1` (tingkat BAB/Frontmatter), `TOC 2` (tingkat sub-bab), dan `TOC 3` (tingkat anak sub-bab) di `styles.xml` dengan font `Times New Roman`, warna `000000`, dan tab stop kanan di posisi margin teks `14.0 cm` (7938 dxa) dengan `w:leader="dot"`.
  - Terapkan gaya paragraf tersebut pada setiap item daftar isi, daftar tabel, dan daftar gambar.
  - Atur *hanging indent* dan *right indent* agar judul yang panjang terpotong rapi sebelum kolom nomor halaman dan tidak menimpa garis titik-titik.

---

### C. Masalah 3: Nomor Halaman Footer Kosong pada Viewer Tertentu
* **Gejala:** Footer hanya menampilkan teks `Universitas Kristen Krida Wacana |` tanpa angka halaman di sebelahnya pada aplikasi seperti Google Docs.
* **Akar Masalah Teknis:**
  - Penomoran halaman menggunakan kode bidang dinamis `<w:fldSimple w:instr="PAGE"/>` tanpa elemen teks *fallback/cached run* (`<w:r><w:t>...</w:t></w:r>`). Viewer yang tidak mengevaluasi field Word dinamis akan menampilkan field tersebut sebagai ruang kosong.
* **Solusi Mutlak:**
  - Sisipkan *cached run* di dalam elemen `w:fldSimple` dan atur warna font hitam pekat (`000000`), ukuran 10 pt Times New Roman tebal, sehingga nomor halaman tetap tampil sempurna di semua aplikasi.

---

### D. Masalah 4: Kebocoran Sintaks Mentah LaTeX Tabel 1.1 pada Paragraf DOCX
* **Gejala:** Di Bab 1, tabel matriks kesenjangan empiris (Tabel 1.1) tercetak sebagai blok kode mentah TeX (`\begingroup`, `\small`, `\begin{longtable}`, `\toprule`, `&`, `\\`, `\end{longtable}`) sebagai paragraf isi biasa, bukan tabel Word.
* **Akar Masalah Teknis:**
  1. Pipeline sinkronisasi `execution/sync_markdown_from_tex.py` memiliki regex konversi untuk Tabel 2.1, 3.1, dan 3.2, tetapi tidak memiliki konverter untuk `\begin{longtable}` Tabel 1.1.
  2. Parser baris di `execution/build_proposal_word.py` hanya menangkap blok `\begin{table}` (Tabel 3.3) dan tabel Markdown pipes (`|...|`), namun tidak memiliki *interceptor* untuk lingkungan `\begin{longtable}` maupun `\begingroup`, sehingga baris mentah dilewatkan ke `add_body_paragraph()`.
  3. Inline math expressions seperti `$X_3 \rightarrow Y$`, `$\rightarrow$`, `\emph{The Why*}`, dan `n.s.\` tidak dinormalisasi secara tuntas oleh `clean_academic_text()`.
* **Solusi Mutlak:**
  - Tambahkan fungsi *builder* tabel khusus `build_tabel_research_gap(doc)` yang memproduksi 8 baris × 5 kolom tabel Word APA 7 murni (*open format*, tanpa garis vertikal, header abu-abu tipis `#F2F2F2`, garis horizontal hitam pekat `#000000`).
  - Pasang *interceptor* di parser `build_proposal_word.py` yang mendeteksi `\begin{longtable}` atau tanda Markdown `Tabel 1.1` dan memanggil `build_tabel_research_gap(doc)` secara atomik.
  - Sempurnakan `clean_academic_text()` dengan pembersihan tuntas: konversi panah `\rightarrow` → `→`, normalisasi angka koma `0{,}092` → `0,092`, dan eliminasi seluruh token perintah TeX liar.
  - Tambahkan audit fatal pada `execution/verify_docx_typography.py` untuk menggagalkan *build* jika ditemukan token `\begin{`, `\toprule`, `\rightarrow`, atau token TeX lainnya di paragraf naskah Word.

---

### E. Masalah 5: Border Grid Liar dan Asimetri Spasi Tanda Tangan pada Lembar Formal
* **Gejala:** 
  1. Pada lembar *Pernyataan Keaslian* (hal. ii) dan *Halaman Persetujuan* (hal. iii), tabel identitas mahasiswa memiliki garis tepi (*grid borders*) yang terlihat jelas dan titik dua (`:`) terletak terlalu jauh di tengah halaman akibat pembagian kolom default yang sama rata (33%-33%-33%).
  2. Blok tanda tangan pada *Halaman Persetujuan* memiliki kotak border terlihat dan posisi vertikal nama Kaprodi (Rita Amelinda) naik ~1,5 cm lebih tinggi daripada Dosen Pembimbing (Dr. Fredella Colline).
* **Akar Masalah Teknis:**
  1. Pembuatan tabel `tbl_id` dan `tbl_per` di `build_formal_approval_sheets()` tidak menerapkan `tblBorders w:val="none"`, sehingga OpenXML merender border bawaan tabel default. Lebar kolom juga tidak ditentukan secara eksplisit, menyebabkan Word membagi lebar 14,0 cm secara merata menjadi ~4,67 cm per kolom.
  2. Blok tanda tangan `tbl_apv` dibangun sebagai tabel 1-baris dengan memasukkan karakter baris baru manual (`\n\n\n\n\n` vs `\n\n\n\n`). Perbedaan panjang teks judul jabatan ("Dosen Pembimbing Skripsi," [2 baris] vs "Ketua Program Studi S1 Manajemen," [1 baris]) menyebabkan tinggi dasar teks tanda tangan menjadi asimetris (*misaligned baseline*).
* **Solusi Mutlak:**
  - Terapkan helper `remove_table_borders(table)` yang menyematkan elemen `<w:tblBorders>` dengan `<w:top w:val="none"/>`, `<w:left w:val="none"/>`, `<w:bottom w:val="none"/>`, `<w:right w:val="none"/>`, `<w:insideH w:val="none"/>`, `<w:insideV w:val="none"/>` ke seluruh tabel frontmatter.
  - Kunci lebar kolom identitas dengan `set_col_widths_fixed(table, [Cm(3.8), Cm(0.4), Cm(9.8)])` dan hilangkan batas kiri tabel agar titik dua rapat rapi di posisi 3,8 cm.
  - Ubah arsitektur tabel tanda tangan `tbl_apv` menjadi tabel 3-baris × 2-kolom:
    - Baris 0: Judul Jabatan ("Menyetujui,\nDosen Pembimbing Skripsi," dan "Mengetahui,\nKetua Program Studi S1 Manajemen,")
    - Baris 1: Ruang Tanda Tangan Kosong (tinggi tetap minimal 55 pt)
    - Baris 2: Nama Lengkap dan NIDN Penandatangan.
    - Struktur 3-baris ini menjamin 100% simetri garis dasar (*horizontal baseline alignment*) terlepas dari variasi pembungkusan teks judul jabatan.

---

## 2. Rencana Eksekusi & Tahapan Perubahan

1. **Refaktorisasi Style Engine di `execution/build_proposal_word.py`:**
   - Inisialisasi gaya `TOC 1`, `TOC 2`, `TOC 3`, `Heading 1`, `Heading 2`, `Heading 3`, `Normal` dengan warna murni `#000000` (tanpa themeColor).
2. **Penyempurnaan Fungsi Pembuat Teks & Judul:**
   - Tambahkan pewarnaan eksplisit `RGBColor(0, 0, 0)` pada `parse_markdown_runs()`, `add_heading_1()`, `add_heading_2()`, `add_heading_3()`, `add_frontmatter_heading()`.
3. **Penyempurnaan Generator Daftar Isi (TOC, LOT, LOF):**
   - Terapkan `TOC 1`, `TOC 2`, `TOC 3` dengan tab stop dot leader kanan `14.0 cm` dan perataan hanging indent.
4. **Pencegahan Border Liar & Perapihan Identitas / Tanda Tangan Formal:**
   - Implementasikan `remove_table_borders()` dan `set_col_widths_fixed()` pada seluruh tabel frontmatter.
   - Restrukturisasi `tbl_apv` menjadi 3-baris (Jabatan, Spasi Tanda Tangan 55pt, Nama/NIDN).
5. **Konstruksi Tabel 1.1 Matriks Kesenjangan APA 7:**
   - Bangun `build_tabel_research_gap()` dan pasang pencegat parser untuk `\begin{longtable}`.
6. **Kompilasi & Pembuatan Dokumen DOCX:**
   - Bangun ulang `01_Naskah_Utama/Proposal_Arthur_NoBab3.docx`.
   - Bangun ulang `01_Naskah_Utama/Proposal_Arthur_PokemonTCG.docx`.
7. **Verifikasi Kualitas:**
   - Audit otomatis dengan `execution/verify_docx_typography.py` (0 error fatal LaTeX, 0 border bocor di frontmatter, 100% font hitam, dot leaders valid).
   - Ekspor via Word COM ke PDF dan inspeksi setiap blok teks untuk memastikan warna `#000000` dan keberadaan garis titik-titik.
   - Uji paritas dengan master LaTeX/PDF menggunakan `execution/run_thesis_graph.py --gate parity`.
