# Implementation Plan
## Pembuatan Halaman Persetujuan Proposal Tugas Akhir (Lampiran 2 Pedoman UKRIDA 2023)

---

### 1. Ringkasan Eksekutif
Rencana ini bertujuan untuk memproduksi lembar persetujuan proposal skripsi mahasiswa **Arthur Reezan (NIM: 312023002)** dengan format baku **Lampiran 2 Buku Pedoman Penyusunan Tugas Akhir UKRIDA 2023**. Dokumen dihasilkan dalam format **DOCX** dan **PDF**, dengan konfigurasi:
- **Dosen Pembimbing:** Dr. Fredella Colline, S.E., M.M., CFP®, PFM, CHCP-A
- **Dosen Pendamping:** Dikosongkan `( ...................................................... )`
- **Ketua Program Studi:** Dikosongkan `( ...................................................... )`

---

### 2. Struktur Folder & Berkas
Folder baru dibuat pada:
`d:/Perkuliahan/Skripsi/SKRIPSI-arthur/01_Naskah_Utama/01_Lembar_Persetujuan_Proposal/`

```
01_Naskah_Utama/
└── 01_Lembar_Persetujuan_Proposal/
    ├── PRD_Halaman_Persetujuan_Proposal.md                 <- Dokumen Persyaratan & Desain
    ├── IMPLEMENTATION_PLAN_Halaman_Persetujuan.md           <- Dokumen Rencana Teknis
    ├── Halaman_Persetujuan_Proposal_Arthur_Reezan.docx      <- Dokumen Word Siap Cetak & Edit
    └── Halaman_Persetujuan_Proposal_Arthur_Reezan.pdf       <- Dokumen PDF Resmi Siap Cetak
```

Skrip pembangun otomatis disimpan pada:
`d:/Perkuliahan/Skripsi/SKRIPSI-arthur/execution/build_lembar_persetujuan.py`

---

### 3. Tahapan Pelaksanaan Teknis

#### Tahap 1: Penyusunan Skrip Generator Python (`build_lembar_persetujuan.py`)
1. Menggunakan pustaka `python-docx` untuk membuat struktur dokumen Word dengan spesifikasi:
   - Ukuran kertas: ISO A4 (21,0 cm x 29,7 cm).
   - Margin: Top 3.0 cm, Bottom 3.0 cm, Left 4.0 cm, Right 3.0 cm.
   - Font global: Times New Roman 12 pt.
2. Membentuk tabel borderless untuk data diri mahasiswa:
   - Kolom 1 (Label): `Nama`, `N.I.M.`, `Alamat`, `No. Telp`, `Judul yang diajukan`.
   - Kolom 2 (Titik dua): `:`.
   - Kolom 3 (Isi):
     - `Arthur Reezan                                                         Pria/Wanita`
     - `312023002`
     - Garis titik-titik alamat
     - Garis titik-titik nomor telepon
     - Judul proposal skripsi lengkap
3. Membentuk tanggal `Jakarta, .............................. 2026` dengan perataan kanan proporsional.
4. Membentuk tabel 2 kolom borderless untuk pengesahan pembimbing:
   - Kiri: `Dosen Pembimbing` -> spasi tanda tangan -> `(Dr. Fredella Colline, S.E., M.M., CFP®, PFM, CHCP-A)`.
   - Kanan: `Dosen Pendamping` -> spasi tanda tangan -> `( ...................................................... )`.
5. Membentuk bagian mengetahui Kaprodi:
   - Rata tengah: `Mengetahui,` -> spasi tanda tangan -> `( ...................................................... )` -> `Ketua Program Studi`.
6. Menghitung spasi vertikal agar seluruh komponen pas tepat **1 halaman (single page fit)** tanpa overflow.

#### Tahap 2: Kompilasi DOCX dan Konversi PDF
1. Simpan berkas Word ke:
   `01_Naskah_Utama/01_Lembar_Persetujuan_Proposal/Halaman_Persetujuan_Proposal_Arthur_Reezan.docx`
2. Konversi berkas Word ke PDF menggunakan Microsoft Word Automation (Word COM via `win32com.client` atau PowerShell):
   - Menjamin 100% kesamaan visual dan tata letak antara DOCX dan PDF.
   - Disimpan ke:
     `01_Naskah_Utama/01_Lembar_Persetujuan_Proposal/Halaman_Persetujuan_Proposal_Arthur_Reezan.pdf`

#### Tahap 3: Verifikasi & Uji Mutu
1. **Verifikasi Jumlah Halaman:** Memastikan PDF hasil build tepat 1 halaman via PyMuPDF.
2. **Verifikasi Teks:** Memastikan seluruh data mahasiswa, pembimbing Colline, dan judul tampil lengkap.
3. **Penyediaan Image Pratinjau:** Mengekstrak gambar PNG dari halaman PDF untuk kemudahan peninjauan cepat oleh mahasiswa.

---

### 4. Rencana Pemeliharaan & Eksekusi Ulang
Bila suatu saat terdapat perubahan data (misal penambahan alamat resmi atau pengisian dosen pendamping / Kaprodi), cukup jalankan:
```bash
python execution/build_lembar_persetujuan.py
```
Seluruh berkas DOCX dan PDF akan diperbarui secara otomatis dan instan.
