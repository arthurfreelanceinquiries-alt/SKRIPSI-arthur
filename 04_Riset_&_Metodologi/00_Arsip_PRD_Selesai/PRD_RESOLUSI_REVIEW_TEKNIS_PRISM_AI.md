# PRD: Resolusi Review Teknis & Editorial Prism AI (Proposal Skripsi Pokémon TCG)

> [!SUMMARY] Tujuan & Solusi Dokumen Ini
> - **Untuk Apa:** Menjadi dokumen arsitektur dan spesifikasi kebutuhan (*Product Requirements Document*) untuk merespons dan menyelesaikan 11 temuan teknis serta audit editorial dari Prism AI tertanggal 14 September 2026 pada naskah proposal skripsi Arthur.
> - **Masalah yang Diselesaikan:** Menyelamatkan validitas metodologi penelitian dari kekeliruan fatal isolasi efek moderasi ($\Delta R^2$), mispersepsi terminologi *mean-centering*, kesalahan sitasi hukum kedewasaan (Pasal 330 KUHPerdata), kontradiksi internal sitasi empiris, serta ketidaksesuaian butir kuesioner sebelum kuesioner disebarkan ke lapangan.
> - **Keputusan/Output:** Panduan eksekusi teknis untuk pembaruan master XeLaTeX, naskah DOCX hybrid OMML, draf per bab, serta pencatatan keputusan baru D20 ke dalam [[04_Riset_&_Metodologi/SOURCE_OF_TRUTH.md]].

---

## 1. Konteks & Latar Belakang

Pada 14 September 2026, naskah proposal skripsi [[01_Naskah_Utama/Proposal_Arthur_PokemonTCG.tex]] diaudit menggunakan engine pemindaian **Prism AI**. Evaluasi ini menghasilkan laporan mendalam setara standar telaah sejawat (*peer review*) jurnal ilmiah internasional bereputasi tinggi.

Meskipun Prism AI mengonfirmasi bahwa arah hubungan tiga prediktor dan moderasi yang diajukan memiliki relevansi yang jelas dan kuesioner telah terstruktur, laporan tersebut mengidentifikasi beberapa cacat metodologis dan editorial yang **krusial untuk diperbaiki sebelum pengumpulan data**:

1. **Kegagalan Isolasi Uji Moderasi (Model Comparison):** Model 1 tidak menyertakan efek utama pemoderasi ($M$), sehingga perubahan koefisien determinasi ($\Delta R^2$) mencampuradukkan efek langsung $M$ dengan interaksi moderasi.
2. **Kekeliruan Konseptual Mean-Centering:** Pengurangan rata-rata diklaim sebagai "standarisasi" dan "menghilangkan multikolinearitas struktural secara matematis".
3. **Kesalahan Fakta Hukum Usia 17 Tahun:** Menghubungkan kedewasaan hukum usia 17 tahun dengan Pasal 330 KUHPerdata (yang sebenarnya mengatur usia 21 tahun).
4. **Kontradiksi Sitasi Empiris:** Celah penelitian di Bab 1 mengutip riset yang sama sebagai "tidak signifikan", namun di Bab 2 dikutip sebagai "positif signifikan".
5. **Penyimpangan Isi Butir Kuesioner (Construct Drift):** Beberapa butir pernyataan kuesioner bergeser dari konstruk aslinya (misalnya $X_1$ *Role Shopping* dan $X_3$ *Likuiditas*).
6. **Salah Ketik Causal Role:** Istilah "dimediasi" tertulis pada hipotesis moderasi H5.

Di sisi lain, laporan Prism AI juga memuat beberapa **kesalahpahaman sistem (*false alarm*)**, khususnya klaim hilangnya berkas gambar dan daftar pustaka `references.bib` yang sebenarnya 100% lengkap dan tersedia di repositori lokal.

---

## 2. Matriks Keputusan: Revisi vs Non-Revisi

Setiap temuan telah ditelaah dengan mempertimbangkan kaidah metodologi ilmiah murni serta proporsionalitas kurikulum **S1 Manajemen Keuangan FEB UKRIDA**:

```
                                [ Audit Prism AI: 11 Temuan ]
                                              │
               ┌──────────────────────────────┼──────────────────────────────┐
               ▼                              ▼                              ▼
      [ 1. Kategori Wajib ]        [ 2. Penyempurnaan ]            [ 3. Non-Revisi ]
   - Model 1 Aditif Baseline    - Butir Kuesioner (Tabel 3.2)   - Asset Gambar (Lengkap)
   - Mean-Centering Terminology - Simple Slopes (H4-H6)         - references.bib (Lengkap)
   - Hapus KUHPerdata 330       - Spesifikasi Skor Komposit     - Cluster-robust (Overkill)
   - Atasi Kontradiksi Sitasi   - Bahasa Uji Asumsi Klasik      - Formal IRB Medis (N/A)
   - Koreksi Typo "dimediasi"   - Usable Sample 120-150
```

### A. Tindakan Wajib (Mandatory Fixes)
1. **Model Aditif Baseline (Hierarchical MRA):**
   - **Model 1 (Baseline Efek Utama):**
     $$Y = \alpha + \beta_1 X_1^* + \beta_2 X_2^* + \beta_3 X_3^* + \beta_4 M^* + e$$
   - **Model 2 (Model MRA Penuh):**
     $$Y = \alpha + \beta_1 X_1^* + \beta_2 X_2^* + \beta_3 X_3^* + \beta_4 M^* + \beta_5 (X_1^* \cdot M^*) + \beta_6 (X_2^* \cdot M^*) + \beta_7 (X_3^* \cdot M^*) + e$$
   - Nilai $\Delta R^2 = R^2_{\text{Model 2}} - R^2_{\text{Model 1}}$ murni menguji kontribusi penjelas dari 3 istilah interaksi ($X_1^*M^*, X_2^*M^*, X_3^*M^*$), diuji melalui statistik $F_{\text{change}}$ dengan derajat kebebasan $(3, N-8)$.
2. **Koreksi Terminologi Mean-Centering:**
   - Mengganti istilah "standarisasi skor rata-rata" dengan "pemusatan rata-rata (*mean-centering*)".
   - Menjelaskan bahwa *mean-centering* mereduksi multikolinearitas non-esensial antara variabel prediktor dengan produk interaksinya tanpa mengubah nilai prediksi ($R^2$) maupun koefisien interaksi.
3. **Koreksi Dasar Hukum Usia 17 Tahun:**
   - Menghapus referensi Pasal 330 KUHPerdata.
   - Menegakkan justifikasi pada: (a) Undang-Undang No. 24 Tahun 2013 tentang Administrasi Kependudukan (kepemilikan KTP sebagai bukti identitas dan kedewasaan administratif sipil); (b) Diskresi keuangan mandiri (kemandirian mengelola uang saku atau penghasilan pribadi); (c) Kapasitas memberikan persetujuan riset (*informed consent*) secara sadar dan sukarela.
4. **Rekonsiliasi Sitasi `prasetio2021hedonic`:**
   - Mempertahankan [[06_Referensi_Jurnal_PDF/KATALOG_REFERENSI_JURNAL.md|Prasetio dkk. (2021)]] pada kelompok penelitian yang membuktikan pengaruh positif signifikan motivasi hedonis di Bab 2.
   - Mengganti sitasi gap tidak signifikan di Bab 1 dengan studi yang tepat, yaitu Zheng et al. (2019) dan Tirtayasa et al. (2020).
5. **Koreksi Tipografi & Editorial:**
   - Bab 2 baris 781: Mengubah kata "dimediasi" menjadi "dimoderasi".
   - Bab 1 baris 526: Mengubah "lebih dari 125%" menjadi "sebesar 125%" ($(64,8 - 28,8)/28,8 = 1,25$).
   - Legenda Gambar 2.1: Mengubah `; Garis` menjadi `; garis`.
   - Gambar 3.1: Mengubah label ambang batas menjadi `Cronbach's Alpha >= 0,60`.

### B. Penyempurnaan Konstruk & Butir Kuesioner (Tabel 3.2)
1. **$X_1$ (*Hedonic Motivation*):**
   - Menyelaraskan butir X1.4 yang berlabel dimensi *Role Shopping* sesuai teori Arnold & Reynolds (2003): berbelanja untuk kepentingan berbagi atau kesenangan bersama orang lain. Butir disesuaikan menjadi: *"Saya menikmati berbelanja kartu Pokémon untuk dihadiahkan atau dimainkan bersama teman dan keluarga sehobi."*
2. **$X_3$ (*Speculative Motive*):**
   - Mengeliminasi istilah percakapan non-formal *"Ekspektasi Cuan"* dan menggantinya dengan istilah baku akademik *"Ekspektasi Keuntungan Finansial / Apresiasi Modal"*.
   - Mengoreksi butir X3.2 (*Likuiditas*) agar mengukur persepsi kemudahan dan kecepatan pencairan kembali kartu menjadi uang tunai: *"Saya yakin kartu Pokémon langka memiliki likuiditas tinggi sehingga mudah dan cepat dijual kembali menjadi uang tunai di pasar sekunder."*
   - Mengoreksi butir X3.5 (*Grading Value*) agar menegaskan grading sebagai sertifikasi kondisi fisik mikroskopis dan keaslian kartu.
3. **$Y$ (*Impulsive Buying*) & $M$ (*Self-Control*):**
   - Menjaga butir-butir $M$ agar merefleksikan kapasitas regulasi diri umum (*general volisional capacity* skala BSCS Tangney, 2004) dan ketaatan anggaran, guna menghindari kesan bahwa $M$ hanyalah antonim kalimat langsung dari butir belanja mendadak di etalase kasir ($Y$).

### C. Alasan Pengecualian Temuan (Non-Revisi)
1. **Aset Gambar dan Daftar Pustaka:** Prism AI mengira file-file ini hilang karena lingkungan pengujian yang tidak mengikutsertakan folder `images/` dan file `references.bib`. Berkas-berkas tersebut sudah terverifikasi lengkap di repositori lokal dan tidak memerlukan tindakan apa pun.
2. **Klaim Ketiadaan `gao2014completing`:** Entri bibtex untuk paper seminal Gao, Huang, & Simonson (2014) di *Journal of Marketing Research* sudah tersimpan rapi di baris 417 `references.bib`.
3. **Cluster-Aware Analysis / Robust Standard Errors:** Tidak diterapkan karena analisis skripsi FEB UKRIDA berpedoman pada OLS SPSS standar (D05). Isu dependensi kluster komunitas cukup didiskusikan sebagai keterbatasan metodologis.

---

## 3. Spesifikasi Perubahan Berkas

| Berkas Sasaran | Jenis Perubahan | Deskripsi Singkat |
|---|---|---|
| `01_Naskah_Utama/Proposal_Arthur_PokemonTCG.tex` | MODIFY | Update Abstrak (Indo & Eng), Bab 1, Bab 2, Bab 3 (Model aditif, KUHPerdata, Tabel 3.2, OLS). |
| `01_Naskah_Utama/Proposal_Arthur_NoBab3.tex` | MODIFY | Update Abstrak, Bab 1, dan Bab 2 agar sinkron 100% (*zero desync*). |
| `execution/build_proposal_word.py` | MODIFY | Update persamaan OMML matematika Model 1 & 2 di Bab 3, teks narasi, dan tabel kuesioner. |
| `03_Draft_Per_Bab/BAB_I_PENDAHULUAN.md` | MODIFY | Sinkronisasi Bab 1 (market claims, persentase 125%, sitasi gap). |
| `03_Draft_Per_Bab/BAB_II_TINJAUAN_PUSTAKA.md` | MODIFY | Sinkronisasi Bab 2 (koreksi typo "dimediasi", legenda Gambar 2.1). |
| `03_Draft_Per_Bab/BAB_III_METODE_PENELITIAN.md` | MODIFY | Sinkronisasi Bab 3 (Model 1 aditif baseline, KUHPerdata, butir Tabel 3.2). |
| `04_Riset_&_Metodologi/SOURCE_OF_TRUTH.md` | MODIFY | Penambahan klausul keputusan terkunci D20. |
| `04_Riset_&_Metodologi/LOG_SESI_SECOND_BRAIN.md` | MODIFY | Pencatatan log sesi kerja dan pemecahan review. |

---

## 4. Protokol Verifikasi Mutu

Pekerjaan dinyatakan selesai jika seluruh kriteria berikut terpenuhi:
1. `xelatex` berhasil mengompilasi kedua naskah tanpa peringatan kesalahan, menghasilkan `Proposal_Arthur_PokemonTCG.pdf` (50 halaman) dan `Proposal_Arthur_NoBab3.pdf` (33 halaman).
2. Skrip `execution/build_proposal_word.py` menghasilkan dokumen Word ber-OMML native yang lulus audit `execution/verify_docx_typography.py` (100% Pure Black `#000000` & dot leaders valid).
3. Skrip `execution/verify_pdf_docx_parity.py` mengonfirmasi *zero desync* antara dokumen Word dan master PDF.
4. Seluruh keputusan dan catatan tersimpan rapi di Obsidian Second Brain.
