# 📑 PANDUAN STANDARISASI HEADING & DAFTAR ISI OTOMATIS DOCX

> [!SUMMARY] Tujuan & Solusi Dokumen Ini
> - **Untuk Apa:** Dokumentasi komprehensif standardisasi gaya Heading (`Heading 1`, `Heading 2`, `Heading 3`), proteksi judul tabel/gambar, dan arsitektur *Native Table of Contents* (`w:sdt`) pada berkas Microsoft Word (`.docx`) proposal skripsi.
> - **Masalah yang Diselesaikan:** Menghilangkan masalah titik-titik (*dot leaders*) yang hilang saat dibuka di Google Docs, mencegah judul tabel/gambar terseret ke dalam Daftar Isi, serta memastikan Daftar Isi dapat diperbarui secara otomatis dari Bab 1 hingga Daftar Pustaka baik di Microsoft Word maupun Google Docs.
> - **Keputusan/Output:** Diterapkan langsung pada generator [[execution/build_proposal_word.py]], diaudit dengan [[execution/verify_docx_typography.py]] dan [[execution/verify_word_outline.py]], serta menghasilkan berkas siap pakai [[01_Naskah_Utama/Proposal_Arthur_PokemonTCG.docx]] dan [[01_Naskah_Utama/Proposal_Arthur_NoBab3.docx]].

---

## 🔍 1. Latar Belakang & Akar Masalah (Root Cause)

Saat naskah proposal skripsi berformat Microsoft Word (`.docx`) diunggah atau dibuka di **Google Docs**, pengguna menemui kendala visual:
1. **Titik-titik (*Dot Leaders*) Hilang:** Jarak antara judul bab/sub-bab dengan nomor halaman pada Daftar Isi menjadi ruang kosong putih lebar tanpa titik-titik (`. . . . . . .`).
2. **Penyebab Teknis:** Generator dokumen Word sebelumnya menyusun Daftar Isi menggunakan paragraf teks biasa yang dipisahkan oleh karakter tab (`\t`) dan atribut XML `<w:tab w:leader="dot"/>`. Microsoft Word desktop mendukung atribut ini pada tab stop reguler, **namun mesin rendering Google Docs mengabaikan atribut `w:leader="dot"` pada paragraf biasa**.
3. **Persyaratan Google Docs:** Google Docs **hanya** menampilkan garis titik-titik jika elemen tersebut merupakan **komponen resmi Table of Contents (*Structured Document Tag* / `w:sdt` atau `w:fldSimple`)**.

---

## 🏗️ 2. Arsitektur Solusi & Hierarki Heading Baku

Untuk memastikan kompatibilitas 100% di Microsoft Word Desktop, Word Online, dan Google Docs, diterapkan arsitektur 3 pilar:

### A. Hierarki Heading FEB UKRIDA 2023
Seluruh judul bab, sub-bab, dan anak sub-bab dikonfigurasi menggunakan gaya bawaan Word (*Built-in Heading Styles*) dengan atribut `w:outlineLvl`:

| Level | Gaya Word | OpenXML Level | Format Tipografi | Elemen Naskah yang Dicakup |
|---|---|---|---|---|
| **Level 1** | `Heading 1` | `w:outlineLvl="0"` | 12 pt, Tebal, Kapital Penuh, Rata Tengah, Spasi 1.5, Pure Black (`#000000`) | `BAB 1 PENDAHULUAN`, `BAB 2 KAJIAN PUSTAKA...`, `BAB 3 METODE PENELITIAN`, `DAFTAR TABEL`, `DAFTAR GAMBAR`, `DAFTAR PUSTAKA` |
| **Level 2** | `Heading 2` | `w:outlineLvl="1"` | 12 pt, Tebal, Rata Kiri, Spasi 1.5, Pure Black (`#000000`), Sebelum 12 pt, Sesudah 6 pt | `1.1 Latar Belakang...`, `1.2 Perumusan Masalah...`, `2.1 Landasan Teori...`, `3.1 Jenis dan Sumber Data...`, dst. |
| **Level 3** | `Heading 3` | `w:outlineLvl="2"` | 12 pt, Tebal, Rata Kiri, Spasi 1.5, Pure Black (`#000000`), Sebelum 6 pt, Sesudah 3 pt | `1.4.1 Manfaat Teoritis`, `2.1.1 Grand Theory...`, `3.5.1 Justifikasi...`, dst. |

> [!IMPORTANT] Perlakuan Khusus Judul Halaman "DAFTAR ISI"
> Judul halaman **DAFTAR ISI** diformat menggunakan paragraf teks biasa (`Normal`), tebal, rata tengah, 12 pt, **tanpa `Heading 1` dan tanpa `w:outlineLvl`**. Hal ini mencegah terjadinya error rekursif di mana kata "DAFTAR ISI" muncul di dalam halaman Daftar Isi itu sendiri.

### B. Injeksi Komponen Resmi Native Table of Contents (`w:sdt`)
1. Pada proses kompilasi melalui [[execution/build_proposal_word.py]], setelah naskah utama selesai disusun, script menjalankan otomatisasi Word COM (`inject_native_word_toc`).
2. Script menghapus teks statis Daftar Isi dan menyisipkan komponen resmi `doc.TablesOfContents.Add`.
3. Komponen ini secara otomatis:
   - Menghitung nomor halaman riil setiap bab dan sub-bab berdasarkan tata letak Word.
   - Membuat *hyperlink bookmark* internal (`_Toc...`).
   - Menghasilkan tab stop bertitik (*dot leader*) resmi yang dikenali oleh Google Docs sebagai widget interaktif.
4. Saat dibuka di Google Docs, widget ini dapat diperbarui sewaktu-waktu dengan 1-klik (*Update table of contents*).

### C. Proteksi Judul Tabel dan Judul Gambar
- Judul tabel (`Tabel 2.1`, `Tabel 3.1`, `Tabel 3.2`, `Tabel 3.3`) dan judul gambar (`Gambar 1.1`, `1.2`, `1.3`, `2.1`, `3.1`) diformat secara eksplisit menggunakan gaya `Normal` tanpa indentasi paragraf (`first_line_indent = 0`) dan `keep_with_next = True`.
- **Jaminan:** Judul tabel dan gambar **tidak akan pernah** terseret masuk ke dalam Daftar Isi utama (*Table of Contents*).

---

## 🧪 3. Verifikasi Determinasi Kualitas

Kedua varian naskah Word diverifikasi melalui dua script deterministik:

1. **Audit Tipografi & Garis Titik-Titik:**
   ```powershell
   python execution/verify_docx_typography.py
   ```
   - Memastikan tidak ada artefak AI, tidak ada bintang markdown mentah, font 100% pure black `#000000`, dan tab stop bertitik pada margin kanan 14.0 cm.
   - **Hasil:** `[PASS] ALL WORD DOCUMENTS PASSED PUBLICATION-GRADE VERIFICATION!`

2. **Audit Struktur Outline Navigasi:**
   ```powershell
   python execution/verify_word_outline.py 01_Naskah_Utama/Proposal_Arthur_PokemonTCG.docx
   ```
   - Memastikan 56 entri heading terdeteksi sempurna: Level 0 (H1) = 12, Level 1 (H2) = 16, Level 2 (H3) = 28.
   - **Hasil:** `[PASS] All heading styles, outline levels, and font parameters are 100% compliant!`

---

## 📁 4. Tautan Naskah & Sumber Daya Terkait

- [[01_Naskah_Utama/Proposal_Arthur_PokemonTCG.docx|Proposal_Arthur_PokemonTCG.docx]] (Naskah Lengkap Bab 1–3 + Pengesahan)
- [[01_Naskah_Utama/Proposal_Arthur_NoBab3.docx|Proposal_Arthur_NoBab3.docx]] (Naskah Varian Review Tanpa Bab 3)
- [[execution/build_proposal_word.py|build_proposal_word.py]] (Generator Naskah Word Hybrid)
- [[04_Riset_&_Metodologi/LOG_SESI_SECOND_BRAIN.md|LOG_SESI_SECOND_BRAIN.md]] (Catatan Log Sesi Obsidian)
- [[00_DASHBOARD_SECOND_BRAIN.md|00_DASHBOARD_SECOND_BRAIN.md]] (Dashboard Vault Utama)
