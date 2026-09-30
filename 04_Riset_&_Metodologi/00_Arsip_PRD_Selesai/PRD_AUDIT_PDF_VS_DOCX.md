# Product Requirements Document (PRD): Audit Komparasi Dokumen PDF vs DOCX

## 1. Problem Statement
Mahasiswa menyusun naskah proposal skripsi dalam dua format keluaran utama:
1. **PDF** yang dikompilasi menggunakan engine LaTeX dari `Proposal_Arthur_PokemonTCG.tex`.
2. **DOCX** yang digenerasi secara deterministik via Python OpenXML dari `build_proposal_word.py`.

Terdapat kebutuhan verifikasi kritis: memastikan bahwa kedua format tersebut menyampaikan substansi akademik yang sama persis 1:1, tanpa ada paragraf yang hilang, rumusan masalah yang timpang, perbedaan nama pembimbing, ataupun inkonsistensi tabel empiris.

## 2. Tujuan & Sasaran
- **Objektif Utama**: Menghasilkan audit perbandingan terotomatisasi yang memeriksa seluruh bab (Frontmatter, Bab 1, Bab 2, Bab 3, Daftar Pustaka).
- **Target Kualitas**: Memastikan 100% konsistensi variabel, hipotesis ($H_1$–$H_6$), data sampel ($N=150$), 10 artikel jurnal empiris, dan pedoman UKRIDA 2023.
- **Keluaran**: Laporan audit komparatif mendalam di `04_Riset_&_Metodologi/LAPORAN_KOMPARASI_PDF_VS_DOCX.md`.

## 3. Acceptance Criteria (Kriteria Keberhasilan)
| Komponen | Spesifikasi / Syarat Lulus | Bobot |
| :--- | :--- | :---: |
| **Identitas & Pembimbing** | Dr. Fredella Colline tercantum di kedua dokumen | Wajib (100%) |
| **Rumusan Masalah** | Tepat 6 butir rumusan masalah di PDF dan DOCX | Wajib (100%) |
| **Tujuan Penelitian** | Tepat 6 butir tujuan penelitian di PDF dan DOCX | Wajib (100%) |
| **Kajian Variabel** | Konsisten 5 variabel ($Y, X_1, X_2, X_3, M$) | Wajib (100%) |
| **Tabel 2.1 Empiris** | 10 jurnal empiris (2021–2025) tercantum lengkap di kedua tabel | Wajib (100%) |
| **Hipotesis ($H_1$–$H_6$)** | 6 hipotesis searah dan terdefinisi persis | Wajib (100%) |
| **Metode & Sampel** | Kriteria inklusi & ukuran sampel $N=150$ identik | Wajib (100%) |
| **Tabel Operasionalisasi** | Tabel 3.1 & 3.2 memuat seluruh dimensi & skala Likert | Wajib (100%) |
| **Daftar Pustaka** | Jumlah referensi seimbang dan tidak ada sitasi hilang | Wajib (100%) |

## 4. Rencana Tindak Lanjut
Jika hasil audit mendeteksi diskrepansi:
- Laporkan rincian selisih (*diff log*) secara transparan.
- Perbarui skrip generator `build_proposal_word.py` (Layer 3) dan jalankan ulang untuk mencapai keselarasan 100%.
