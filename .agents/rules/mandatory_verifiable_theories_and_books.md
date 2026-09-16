# Mandatory Rule: Kewajiban Sumber Terverifikasi untuk Seluruh Teori Buku & Artikel Ilmiah
### *Zero-Unverified-Theory & Open-Access Academic Source Policy*

> [!CRITICAL] PERATURAN MUTLAK KELAYAKAN SUMBER TEORI SKRIPSI
> Seluruh teori yang dicantumkan dalam Skripsi Arthur Reezan (baik yang bersumber dari buku teks, monograf, artikel jurnal, maupun prosiding) **WAJIB MEMILIKI SUMBER NYATA YANG DAPAT DIVERIFIKASI DAN DAPAT DIUNDUH (*FULLY DOWNLOADABLE*)**.
> **DILARANG KERAS** menyitasi buku atau literatur yang fiktif, tidak dapat dilacak, atau tidak memiliki berkas digital utuh (PDF/EPUB) di Library Genesis (`libgen.li`) atau repositori institusional resmi.

---

## 1. Lingkup & Standar Pembuktian Teori

1. **Teori dari Buku Teks (Monograf Ilmiah):**
   - Setiap sitasi buku (`@book` dalam bibliografi) wajib dapat dicek di Library Genesis (`https://libgen.li/`) dan memiliki tautan cermin unduhan aktif.
   - Mahasiswa wajib menyimpan salinan berkas digital buku (atau minimal bab yang disitasi) dalam arsip repositori `06_Referensi_Jurnal_PDF/Buku_Referensi/`.
   - Jika suatu buku **tidak ditemukan** di LibGen dan tidak memiliki pindaian digital resmi, buku tersebut **WAJIB DIHAPUS** atau **DIGANTI** dengan buku referensi setara yang 100% dapat diunduh.
2. **Teori dari Artikel Jurnal:**
   - Seluruh artikel jurnal wajib memiliki DOI (*Digital Object Identifier*) aktif dan berkas PDF naskah lengkap yang tersimpan di `06_Referensi_Jurnal_PDF/`.
   - Artikel harus terindeks dalam pangkalan data bereputasi (SINTA atau Scopus/Web of Science).
3. **Data Empiris & Industri:**
   - Mematuhi aturan mandatori bebas dinding login (`.agents/rules/no_login_wall_empirical_sources.md`).

---

## 2. Larangan Spesifik (Negative Constraints)

1. **Dilarang "Sitasi Buta" (*Blind/Ghost Citation*):**  
   Menyitasi definisi konstruk atau rumus matematika dari buku yang mahasiswa sendiri tidak memiliki berkas aslinya dilarang keras.
2. **Dilarang Menggunakan Buku Kadaluwarsa / Fiktif:**  
   Buku teks metodologi atau teori yang dirujuk harus merupakan edisi terbitan resmi dari penerbit bereputasi (seperti MIT Press, Routledge, Sage, Macmillan, Wiley, Cengage, Guilford Press, Undip, Alfabeta).
3. **Dilarang Inkonsistensi Edisi:**  
   Tahun dan edisi yang tertulis pada Daftar Pustaka harus sesuai dengan berkas PDF yang diverifikasi.

---

## 3. Penegakan Otomatis (Enforcement Mechanism)

Sebelum naskah diajukan ke Dosen Pembimbing atau pendaftaran Seminar Proposal:
1. Skrip pengujian otomatis `execution/verify_book_sources.py` akan memvalidasi ketersediaan dan status keterunduhan seluruh buku referensi.
2. Suite pengujian integritas `execution/verify_ukrida_compliance.py` akan memastikan bahwa tidak ada satu pun sitasi buku yang berstatus belum terverifikasi.
