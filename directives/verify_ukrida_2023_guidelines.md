# Directive: Verifikasi Kepatuhan Pedoman Tugas Akhir FEB UKRIDA 2023

> [!SUMMARY] Tujuan & Solusi Directive Ini
> - **Untuk Apa:** Menjadi prosedur operasional standar (SOP) baku dalam memvalidasi kepatuhan format naskah proposal dan skripsi terhadap Buku Pedoman Penyusunan Tugas Akhir FEB UKRIDA 2023 (SK Dekan No. 350a/SK/UKKW/FEB/D/VI/2023).
> - **Masalah yang Diselesaikan:** Mencegah sanksi administratif atau penolakan sidang proposal akibat pelanggaran format pengetikan, defisit kuota jurnal SINTA/Internasional, format sitasi asing (`&` / `and`), atau penomoran angka pada daftar pustaka.
> - **Keputusan/Output:** Digunakan oleh agen Layer 2 dan skrip Layer 3 (`verify_ukrida_compliance.py`) sebagai kriteria lolos-audit (acceptance criteria).

---

## 1. Lingkup & Otoritas Baku

Setiap naskah Tugas Akhir (Proposal maupun Skripsi Lengkap) Program Studi S1 Manajemen Konsentrasi Manajemen Keuangan FEB UKRIDA wajib mematuhi 7 pilar kepatuhan berikut:

---

## 2. Tujuh Pilar Kepatuhan FEB UKRIDA 2023

### Pilar 1: Kuota Jurnal Terindeks SINTA / Internasional (Subbab 1.4.c)
- **Ketentuan:** Wajib mensitasi minimal 5 artikel jurnal terindeks SINTA dan/atau jurnal Internasional.
- **Standar Verifikasi:**
  - Jurnal nasional wajib terakreditasi SINTA (SINTA 1 s.d. SINTA 6) yang terdaftar di portal Kemdiktisaintek.
  - Jurnal internasional wajib terindeks Scopus, Web of Science, atau DOAJ bereputasi.
  - Skripsi mahasiswa **dilarang keras** dijadikan referensi (Subbab 1.5.b.1).

### Pilar 2: Sitasi Dosen FEB UKRIDA (Subbab 1.4.b)
- **Ketentuan:** Wajib mensitasi minimal 1 karya ilmiah dari dosen aktif FEB UKRIDA yang relevan dengan topik.
- **Implementasi:** Mengutip artikel Dr. Fredella Colline, S.E., M.M., CFP®, PFM, CHCP-A (2024), *"Biases in Indonesian Stock Investor Behavior"*, *Accounting and Finance Studies*, disitasi di Bab 1, Bab 2, dan Bab 3.

### Pilar 3: Ketebalan Naskah (Subbab 1.4.a)
- **Ketentuan:** Naskah Tugas Akhir (Bab 1–5) minimal 50 halaman.
- **Implementasi:** Naskah proposal (Bab 1–3) harus berbobot dan komprehensif ($\ge 35$ halaman untuk varian tanpa Bab 3; $\ge 50$ halaman untuk proposal lengkap).

### Pilar 4: Jumlah dan Kemutakhiran Pustaka (Subbab 1.5.b.1 & 3.7)
- **Ketentuan:** Minimal 20 acuan kepustakaan. Pustaka empiris maksimal 5 tahun terakhir (2021–2025). Teori konvensional/klasik diperbolehkan menggunakan sumber aslinya.

### Pilar 5: Tata Letak & Tipografi Dokumen (Bab 3 Subbab 3.1 & 3.2)
- **Ukuran Kertas:** ISO A4 (21,0 x 29,7 cm).
- **Margin:** Kiri 4 cm (1 cm jilid), Kanan 3 cm, Atas 3 cm, Bawah 3 cm.
- **Huruf & Spasi:** Times New Roman 12 pt, Justified, 1,5 spasi antar baris.
- **Warna Huruf:** Hitam pekat (*pure black* `#000000`) seragam.
- **Alinea Baru:** Indentasi 5 ketukan (1,25 cm), minimal terdiri dari 2 kalimat.
- **Penomoran Halaman:**
  - Bagian Awal: Romawi kecil (ii, iii, dst.) di tengah bawah kertas.
  - Bagian Isi & Akhir: Angka latin (1, 2, dst.) di sudut kanan bawah kertas dengan format *Accent Bar 4* bertuliskan **"Universitas Kristen Krida Wacana"** (TNR 10 pt Bold).

### Pilar 6: Kaidah Sitasi dalam Teks / In-Text (Subbab 3.6)
- **Format:** Body citation (*endnotes/in-text*), dilarang menggunakan catatan kaki (*footnotes*).
- **1 Penulis:** `Nama (Tahun)` atau `(Nama, Tahun)`.
- **2 Penulis:** Wajib menggunakan kata hubung bahasa Indonesia **"dan"** (Dilarang menggunakan `&` atau `and` dalam narasi kalimat).
  - Contoh: `Tan dan Adyantari (2024)` atau `(Tan dan Adyantari, 2024)`.
- **>2 Penulis:** Nama pertama diikuti singkatan ***et al.*** yang dicetak miring (*italic*).
  - Contoh: `Gong et al. (2024)` atau `(Gong et al., 2024)`.

### Pilar 7: Kaidah Format Daftar Pustaka (Subbab 3.7)
- **Larangan Nomor Urut:** Disusun menurut abjad nama pengarang **tanpa didahului nomor urut (1, 2, 3) atau garis strip (-)**.
- **Indentasi Gantung:** Baris kedua dan seterusnya masuk 1,25 cm (5 ketukan), spasi 1,5 antar baris.
- **Artikel Jurnal:** `Nama Pengarang. Tahun. “Judul Artikel”. *Nama Jurnal* Volume(Nomor): Halaman.` (Judul artikel diapit tanda kutip dua `“...”`, nama jurnal miring, tahun tanpa tanda kurung).
- **Buku:** `Nama Pengarang. Tahun. *Judul Buku Miring*. Edisi. Kota: Penerbit.` (Tahun tanpa tanda kurung).

---

## 3. Prosedur Eksekusi & Validasi Otomatis (Layer 3)

Skrip validasi pada `execution/verify_ukrida_compliance.py` wajib dijalankan sebelum naskah dinyatakan selesai dan siap cetak. Status akhir dokumen harus menghasilkan:
```
[PASS] Kuota SINTA / Internasional >= 5
[PASS] Sitasi Dosen FEB UKRIDA terverifikasi
[PASS] Tidak ada nomor urut pada Daftar Pustaka
[PASS] Sitasi dua penulis menggunakan 'dan'
[PASS] Margin dan tipografi UKRIDA 2023 memenuhi standar
```
