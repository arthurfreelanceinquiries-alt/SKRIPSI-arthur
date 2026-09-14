# 📑 Catatan Review Teknis Prism AI & Matriks Resolusi
### *Audit Komprehensif Naskah Proposal Skripsi Pokémon TCG (14 September 2026)*

> [!SUMMARY] Tujuan & Solusi Catatan Ini
> - **Untuk Apa:** Dokumentasi resmi catatan hasil audit otomatis dan mendalam (*technical and editorial review*) oleh Prism AI terhadap proposal skripsi Arthur, serta tindak lanjut perbaikannya.
> - **Masalah yang Diselesaikan:** Menyediakan audit trail lengkap yang membedakan antara perbaikan metodologis esensial (isolasi model moderasi, perbaikan sitasi hukum, penghilangan kontradiksi literatur) dengan peringatan palsu sistem (*false alarm*).
> - **Keputusan/Output:** Matriks resolusi 11 temuan teknis yang menjadi dasar pembaruan naskah LaTeX, draf per bab, dokumen Word, dan Source of Truth skripsi.

---

## 1. Ringkasan Eksekutif Hasil Review

Audit dilakukan pada naskah lengkap `Proposal_Arthur_PokemonTCG.tex` (1.227 baris kode). Reviewer menyimpulkan bahwa penelitian memiliki perumusan masalah tiga prediktor dan moderasi yang jelas serta kuesioner yang telah terpetakan, namun membutuhkan **revisi metodologis penting sebelum pengumpulan data lapangan**.

Evaluasi mencakup 11 temuan teknis berprioritas tinggi dan beberapa catatan editorial:

1. **Model Comparison Moderasi Tidak Terisolasi:** Model 1 memuat 3 prediktor ($X_1, X_2, X_3$) sedangkan Model 2 memuat 7 prediktor ($X_1, X_2, X_3, M$ dan 3 interaksi). Kenaikan $R^2$ tidak mengisolasi efek moderasi murni.
2. **Kekeliruan Terminologi Mean-Centering:** Pengurangan nilai rata-rata disebut "standarisasi" dan diklaim "menghilangkan multikolinearitas struktural secara matematis".
3. **Interpretasi Efek Moderasi Bersyarat:** Perlu kejelasan pengujian kemiringan kondisional (*conditional slopes / simple slopes*).
4. **Daya Uji Statistik & Ukuran Sampel:** Perhitungan sampel Green (1991) benar ($N \ge 111$), namun justifikasi daya uji Cohen 0,80 ($f^2=0,15$) perlu ditegaskan untuk model regresi utama.
5. **Penyimpangan Butir Kuesioner (Construct Drift):** Butir X1.4 (*Role Shopping*), X3.2 (*Likuiditas*), dan potensi tumpang tindih antara $Y$ dengan $M$.
6. **Agregasi Skor Komposit & Validitas:** Prosedur pembentukan skor (apakah rata-rata atau total) dan kriteria korelasi item-total perlu ditegaskan.
7. **Klaim Uji Asumsi Klasik OLS:** Klaim bahwa uji asumsi "menjamin BLUE" merupakan overstatement; perlu diluruskan secara proporsional.
8. **Kesalahan Fakta Hukum Usia 17 Tahun (Pasal 330 KUHPerdata):** Pasal 330 KUHPerdata menetapkan usia 21 tahun, bukan 17 tahun.
9. **Kontradiksi Sitasi Penelitian Terdahulu:** Sitasi `prasetio2021hedonic` disebut tidak signifikan di Bab 1, namun disebut positif signifikan di Bab 2.
10. **Klaim Data Pasar & Grading:** Angka pangsa pasar global dan premium grading 5–50x perlu disajikan sebagai data observasi empiris kartu langka tertentu.
11. **Rentang Waktu Pembelian:** Penegasan rentang waktu kriteria inklusi 6 bulan (maksimal 12 bulan terakhir).

---

## 2. Matriks Resolusi 11 Temuan Teknis

| No | Temuan Prism AI | Klasifikasi | Tindakan Resolusi | Status |
|:---:|---|:---:|---|:---:|
| **1** | Model 1 vs 2 tidak mengisolasi interaksi | **Wajib Direvisi** | Ubah Model 1 menjadi model aditif 4 prediktor ($X_1, X_2, X_3, M$), Model 2 model interaksi penuh 7 prediktor. Uji blok interaksi menggunakan $\Delta R^2$ dan $F_{\text{change}}$ $(3, N-8)$. | **Siap Eksekusi** |
| **2** | Standarisasi vs mean-centering | **Wajib Direvisi** | Perbaiki istilah menjadi *mean-centering* (pemusatan rata-rata); jelaskan fungsinya mereduksi multikolinearitas non-esensial dan mempermudah interpretasi koefisien pada nilai rata-rata pemoderasi. | **Siap Eksekusi** |
| **3** | Interpretasi kemiringan kondisional (H4–H6) | **Disempurnakan** | Tambahkan formula kemiringan kondisional $\frac{\partial Y}{\partial X_i^*} = \beta_i + \beta_{\text{int}} M^*$ dan penjelasan *simple slopes* pada tingkat kontrol diri tinggi (+1 SD). | **Siap Eksekusi** |
| **4** | Daya uji & sampel teranalisis | **Disempurnakan** | Perjelas bahwa 120–150 responden adalah sampel bersih yang dapat dianalisis (*usable sample*) terpisah dari 30 responden uji coba (*pilot test*). | **Siap Eksekusi** |
| **5** | Penyelarasan butir kuesioner (Tabel 3.2) | **Wajib Direvisi** | Sesuaikan X1.4 (*Role Shopping*), hapus istilah non-formal "Cuan" ganti "Keuntungan Finansial / Apresiasi Modal", perbaiki X3.2 (kemudahan likuiditas riil), perjelas butir $M$ (kapasitas volisional umum). | **Siap Eksekusi** |
| **6** | Spesifikasi pembentukan skor komposit | **Disempurnakan** | Nyatakan secara eksplisit bahwa skor variabel dihitung dari rata-rata (*mean*) butir valid, skala Likert 1–5 positif, dan validitas butir diuji via *corrected item-total correlation*. | **Siap Eksekusi** |
| **7** | Bahasa uji asumsi klasik OLS | **Disempurnakan** | Ubah klaim "menjamin BLUE" menjadi pemenuhan prasyarat estimasi OLS agar parameter tidak bias dan pengujian hipotesis valid. | **Siap Eksekusi** |
| **8** | Kesalahan sitasi Pasal 330 KUHPerdata | **Wajib Direvisi** | Hapus rujukan Pasal 330 KUHPerdata. Dasarkan justifikasi usia 17 tahun pada UU No. 24/2013 (KTP/Adminduk), diskresi keuangan mandiri, dan kesukarelaan *informed consent*. | **Siap Eksekusi** |
| **9** | Kontradiksi sitasi `prasetio2021hedonic` | **Wajib Direvisi** | Hapus Prasetio dari kelompok tidak signifikan di Bab 1 (ganti Zheng et al., 2019 / Tirtayasa et al., 2020); pertahankan di kelompok pengaruh positif Bab 2. | **Siap Eksekusi** |
| **10** | Klaim pasar & premium grading | **Disempurnakan** | Nyatakan premium grading 5–50x dan data pasar sebagai bukti observasional empiris pada kartu-kartu langka tertentu (*specific collectible cards*). | **Siap Eksekusi** |
| **11** | Kriteria waktu pembelian | **Disempurnakan** | Tegaskan rentang waktu: *"dalam 6 bulan terakhir (maksimal 12 bulan terakhir)"*. | **Siap Eksekusi** |

---

## 3. Klarifikasi Temuan yang Dikecualikan (Non-Revisi)

1. **Aset Gambar dan `references.bib`:**
   - Reviewer mengira berkas-berkas ini tidak ada karena lingkungan evaluasi sandbox yang hanya membaca potongan teks `.tex`.
   - Di repositori kerja Arthur, seluruh 4 berkas gambar di folder `01_Naskah_Utama/images/` dan `01_Naskah_Utama/references.bib` (berisi 50 referensi) lengkap, valid, dan berhasil dikompilasi.
2. **Klaim Ketiadaan Entri `gao2014completing`:**
   - Entri paper seminal Gao, Huang, & Simonson (2014) di *Journal of Marketing Research* telah tercatat lengkap pada baris 417 `references.bib`.
3. **Tuntutan Ekonometrika Lanjutan (Cluster-Robust & IRB Medis):**
   - Di luar ruang lingkup skripsi S1 Manajemen FEB UKRIDA yang menggunakan SPSS OLS (D05).
