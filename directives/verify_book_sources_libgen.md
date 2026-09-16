# Directive: SOP Verifikasi Sumber Teori Buku & Penelusuran Unduhan LibGen
### *Standard Operating Procedure (SOP) Verifikasi Keabsahan Buku Teks Ilmiah & Anti-Ghost Citation*

> [!SUMMARY] Tujuan & Solusi Directive Ini
> - **Untuk Apa:** Menjadi Standard Operating Procedure (SOP) resmi untuk memverifikasi bahwa setiap kutipan teori dari buku teks dalam naskah skripsi Arthur Reezan memiliki sumber autentik yang dapat diakses dan diunduh berkas PDF-nya secara terbuka melalui Library Genesis (`https://libgen.li/`) atau repositori akademik resmi.
> - **Masalah yang Diselesaikan:** Mencegah terjadinya "sitasi hantu" (*ghost citations*) di mana teori buku dicantumkan tanpa memiliki dokumen fisik/digital aslinya, serta memastikan mahasiswa siap memperlihatkan buku asli saat diminta oleh Dosen Pembimbing atau Dewan Penguji sidang.
> - **Keputusan/Output:** Prosedur verifikasi pra-sidang mandatori untuk 12 buku referensi naskah. Berkas PDF buku disimpan di `06_Referensi_Jurnal_PDF/Buku_Referensi/`.

---

## 1. Prinsip Utama: *Zero-Unverified-Theory*

1. **Keberadaan Bukti Fisik/Digital (Tangible Evidence Requirement):**
   Setiap teori buku yang dirujuk dalam Bab 1 (latar belakang), Bab 2 (landasan teori & hipotesis), dan Bab 3 (metodologi) **WAJIB** memiliki salinan digital utuh (PDF/EPUB) atau minimal bab terkait (*book chapter*) yang tersimpan dalam repositori riset.
2. **Keterverifikasian Melalui Library Genesis:**
   Buku referensi internasional harus dapat ditelusuri di `https://libgen.li/index.php` (atau `https://libgen.li/`) dengan status cermin unduhan (*download mirror*) aktif tanpa paywall.
3. **Kebijakan Buku Metodologi Lokal:**
   Untuk buku teks metodologi berbahasa Indonesia (seperti Prof. Imam Ghozali dan Prof. Sugiyono), jika tidak tercatat pada repositori LibGen internasional, wajib diverifikasi melalui pindaian PDF digital resmi di repositori lokal `06_Referensi_Jurnal_PDF/Buku_Referensi/`.

---

## 2. Alur Penelusuran di Library Genesis (`libgen.li`)

```
[ Input Query: Judul / Penulis ] ──► Buka https://libgen.li/index.php
                 │
                 ▼
[ Evaluasi Hasil Pencarian ] ──────► Cocokkan: Judul, Penulis, Tahun, Edisi, Penerbit
                 │
                 ▼
[ Uji Tautan Cermin Unduhan ] ────► Periksa ketersediaan mirror (libgen.li / ipfs / cloudflare)
                 │
                 ▼
[ Status Keterunduhan ] ──────────► (A) Tersedia: Konfirmasi & simpan metadata/PDF
                                    (B) Tidak Tersedia: Jalankan Protokol Penggantian (Section 3)
```

### Langkah 1: Formulasi Query Penelusuran
- Gunakan judul buku inti dalam bahasa Inggris (tanpa kata sambung berlebih).
- Contoh:
  - `Mehrabian An Approach to Environmental Psychology`
  - `Belk Collecting in a Consumer Society`
  - `Keynes General Theory of Employment`
  - `Shiller Irrational Exuberance`
  - `Cohen Statistical Power Analysis`
  - `Aiken Multiple Regression Testing and Interpreting Interactions`
  - `Hayes Introduction to Mediation Moderation`
  - `Hair Multivariate Data Analysis`

### Langkah 2: Verifikasi Edisi & Penerbit
- Pastikan edisi yang ditemukan memuat bab atau konstruk teori yang disitasi.
- Jika tahun terbitan di LibGen berbeda (misalnya edisi ke-2 atau edisi revisi terbaru), mutakhirkan metadata sitasi pada `references.bib` agar pembaca dapat merujuk edisi yang presisi.

---

## 3. Protokol Penggantian Buku (*Book Substitution Protocol*)

Jika suatu buku teks yang direncanakan disitasi ternyata **TIDAK DITEMUKAN** di LibGen dan tidak memiliki pindaian digital resmi:
1. **Aturan Evaluasi Esensialitas:**
   - Apakah buku ini melandasi Grand Theory / Supporting Theory utama?
   - Jika **YA**, cari buku teks internasional seminal dengan topik setara yang 100% tersedia di LibGen.
2. **Tabel Padanan Rekomendasi Pengganti:**
   - Metodologi Regresi Moderasi Lokal $\rightarrow$ Andy Field (*Discovering Statistics Using IBM SPSS Statistics*) atau Aiken & West (1991).
   - Metodologi Bisnis Lokal $\rightarrow$ Uma Sekaran & Roger Bougie (*Research Methods for Business*, Wiley) atau Saunders, Lewis, & Thornhill (*Research Methods for Business Students*).
   - Perilaku Konsumen $\rightarrow$ Solomon (*Consumer Behavior: Buying, Having, and Being*, Pearson) atau Schiffman & Wisenblit (*Consumer Behavior*).
3. **Penyelarasan Naskah Multilayer:**
   Jika terjadi penggantian buku, seluruh sitasi di Bab 1, 2, 3 naskah LaTeX, Word DOCX, draf Markdown, BibTeX, dan pustaka Mendeley wajib disinkronkan serentak.
