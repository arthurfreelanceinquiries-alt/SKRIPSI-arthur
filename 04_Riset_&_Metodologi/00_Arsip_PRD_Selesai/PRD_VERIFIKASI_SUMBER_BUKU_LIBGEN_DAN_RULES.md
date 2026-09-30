# PRD: Penjaminan Ketersediaan Sumber Teori Buku & Verifikasi Mandatori LibGen
### *Protokol Zero-Unverified-Theory, Aturan Akses Terbuka Buku Referensi, dan Verifikasi Peramban Nyata*

> [!SUMMARY] Metadata PRD & Tujuan Dokumen
> - **Inisiator:** Arthur Reezan (Peneliti) & AI Pair-Programmer (Antigravity)
> - **Konteks Masalah:** Setiap teori dari buku dan artikel ilmiah wajib memiliki sumber autentik yang dapat diakses (tautan langsung, DOI, atau PDF buku lengkap yang dapat diunduh). Dosen pembimbing dan penguji tidak boleh menemukan satu pun sitasi buku yang tidak memiliki berkas fisik/digitalnya.
> - **Solusi Arsitektural:** Menetapkan aturan permanen (Rule), Standard Operating Procedure (Directive), dan mekanisme verifikasi peramban interaktif (*Browser Subagent*) di basis data Library Genesis (`https://libgen.li/` / `https://libgen.li/index.php`) untuk memeriksa dan mengunduh seluruh 12 buku referensi naskah skripsi.
> - **Kebijakan Penggantian (*Replacement Policy*):** Jika suatu buku tidak ditemukan di LibGen atau repositori akademik terbuka lainnya, buku tersebut wajib diganti dengan buku teori/artikel jurnal seminal yang memiliki ketersediaan berkas PDF 100%, atau dihapus jika tidak esensial bagi kerangka hipotesis.

---

## 1. Latar Belakang & Analisis Kebutuhan

Dalam penulisan skripsi akademik jenjang Sarjana (S1) FEB UKRIDA, kredibilitas landasan teori sangat ditentukan oleh ketertelusuran (*traceability*) sumber primer:
1. **Risiko "Ghost Citation" (Sitasi Hantu):** Sering kali mahasiswa menyitasi buku teks klasik atau metodologi hanya berdasarkan kutipan sekunder (*"dikutip dalam..."*). Penguji kritis sering meminta mahasiswa memperlihatkan berkas asli buku atau bab terkait saat sidang.
2. **Kewajiban Bukti Fisik/Digital:** Mahasiswa wajib memiliki berkas PDF utuh dari setiap buku yang disitasi di Bab 1, 2, dan 3 agar mampu mempertanggungjawabkan definisi konstruk, skala indikator, dan rumus ekonometrika.
3. **Standarisasi Repositori LibGen:** Platform Library Genesis (`libgen.li`) merupakan standar de facto global untuk penelusuran buku teks ilmiah dan monograf akademik.

---

## 2. Inventarisasi 11 Buku Referensi Naskah Skripsi

Berdasarkan audit ketat terhadap seluruh naskah skripsi dan master `01_Naskah_Utama/references.bib`, terdapat tepat 11 entri buku (`@book`) yang aktif disitasi dan melandasi teori serta metodologi skripsi (*catatan: entri orphan `mowen1990consumer` yang tidak disitasi dan tidak terlacak di LibGen telah dihapus sesuai aturan pengguna*):

| No | Citation Key | Penulis & Tahun | Judul Buku | Penerbit | Fungsi dalam Naskah Skripsi |
|:---:|:---|:---|:---|:---|:---|
| 1 | `mehrabian1974approach` | Mehrabian & Russell (1974) | *An Approach to Environmental Psychology* | MIT Press | Supporting Theory: Stimulus-Organism-Response (S-O-R) untuk $X_1 \rightarrow Y$ |
| 2 | `belk1995collecting` | Belk (1995) | *Collecting in a Consumer Society* | Routledge | Supporting Theory: Psikologi Kolektor & Konsumsi Koleksi |
| 3 | `keynes1936general` | Keynes (1936) | *The General Theory of Employment, Interest and Money* | Macmillan | Landasan Motif Spekulasi Finansial ($X_3$) |
| 4 | `shiller2000irrational` | Shiller (2000) | *Irrational Exuberance* | Princeton University Press | Grand Theory: Behavioral Finance & Euforia Spekulasi Pasar |
| 5 | `ghozali2018aplikasi` | Ghozali (2018) | *Aplikasi Analisis Multivariate dengan Program IBM SPSS 25* | Badan Penerbit Undip | Panduan Baku Uji SPSS & Asumsi Klasik OLS lokal Indonesia |
| 6 | `cohen1988statistical` | Cohen (1988) | *Statistical Power Analysis for the Behavioral Sciences* | Lawrence Erlbaum | Penentuan Ukuran Sampel Berdasarkan *Statistical Power* ($N=120-150$) |
| 7 | `aiken1991multiple` | Aiken & West (1991) | *Multiple Regression: Testing and Interpreting Interactions* | Sage Publications | Landasan Utama Prosedur *Mean-Centering* & Interaksi MRA ($X \cdot M$) |
| 8 | `hayes2018introduction` | Hayes (2018) | *Introduction to Mediation, Moderation, and Conditional Process Analysis* | The Guilford Press | Ekonometrika MRA Lanjutan & Analisis Kemiringan Bersyarat (*Simple Slopes*) |
| 9 | `sekaran2016research` | Sekaran & Bougie (2016) | *Research Methods for Business: A Skill-Building Approach* | John Wiley & Sons | Metodologi Kuantitatif Bisnis & Standar Uji Reliabilitas Cronbach's Alpha |
| 10 | `sugiyono2019metode` | Sugiyono (2019) | *Metode Penelitian Kuantitatif, Kualitatif, dan R&D* | Alfabeta | Landasan Sampling Purposive & Skala Pengukuran Lokal Indonesia |
| 11 | `hair2019multivariate` | Hair et al. (2019) | *Multivariate Data Analysis* | Cengage Learning | Justifikasi Komparatif MRA vs SEM & Uji Kualitas Data Multivariat |

---

## 3. Penerapan Arsitektur 3-Layer (3-Layer Architecture)

### Layer 1: Directives (Standard Operating Procedures)
- Berkas: `directives/verify_book_sources_libgen.md`
- Menetapkan SOP penelusuran buku di LibGen:
  1. Protokol query penelusuran (Judul Buku / Nama Penulis / ISBN).
  2. Verifikasi cermin unduhan (*mirrors download verification*).
  3. Prosedur penyimpanan berkas PDF buku ke folder lokal `06_Referensi_Jurnal_PDF/Buku_Referensi/`.
  4. Protokol substitusi buku jika edisi tertentu tidak dapat ditemukan secara terbuka.

### Layer 2: Orchestration & Rules
- Berkas Rule: `.agents/rules/mandatory_verifiable_theories_and_books.md`
  - Mewajibkan setiap sitasi buku memiliki tautan atau berkas PDF yang dapat diunduh.
  - Melarang penggunaan buku fiktif, tanpa berkas, atau tidak terverifikasi.
- Dokumen Rujukan: `04_Riset_&_Metodologi/SOURCE_OF_TRUTH.md` (Mengunci Keputusan **D23**).
- Penyelarasan Multi-Media: Jika terjadi penggantian atau eliminasi buku, sinkronkan 6 lapisan dokumen: TeX, Word DOCX, Markdown, references.bib, RIS Mendeley, dan BibTeX Mendeley.

### Layer 3: Execution & Automation
- **Browser Subagent Live Demonstration:**
  - Menjalankan `browser_subagent` untuk membuka `https://libgen.li/` di peramban baru, mencari judul buku, dan mendokumentasikan bukti ketersediaan unduhan dalam rekaman video WebP interaktif.
- **Skrip Verifikasi Otomatis:**
  - `execution/verify_book_sources.py`: Memeriksa keberadaan berkas fisik PDF di `06_Referensi_Jurnal_PDF/Buku_Referensi/` dan menguji validitas metadata DOI/ISBN/URL.
  - Integrasi ke dalam `execution/verify_ukrida_compliance.py`.

---

## 4. Kriteria Keberhasilan (*Success Criteria*)

1. **Aturan Permanen Aktif:** Terbitnya `.agents/rules/mandatory_verifiable_theories_and_books.md`.
2. **SOP Terbit:** Terbitnya `directives/verify_book_sources_libgen.md`.
3. **100% Verifikasi LibGen:** Seluruh 12 buku referensi (atau pengganti yang sah) terverifikasi ada dan dapat diunduh di LibGen.
4. **Bukti Visual Browser:** Aktivitas penelusuran LibGen terekam secara visual melalui subagent browser.
5. **Paritas Penuh:** Jika ada buku yang diganti/dieliminasi, seluruh 6 lapisan naskah (PDF, Word, TeX, MD, Bib, RIS) tetap mempertahankan paritas 1:1 tanpa celah inkonsistensi.
