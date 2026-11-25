> [!SUMMARY] Tujuan & Solusi Catatan Ini
> - **Untuk Apa:** Kodebook tabulasi pilot (N=30) dan final (minimal 111 responden), dengan pemisahan versi instrumen.
> - **Masalah yang Diselesaikan:** Mencegah pencampuran kode legacy, label form live, nilai hilang, dan urutan kolom ekspor yang berbeda dari urutan butir di form.
> - **Keputusan/Output:** Dataset analisis 40 kolom untuk form versi D45 (38 pertanyaan + RespID + INCLUDE), dipetakan dari 39 kolom Google Sheets yang terverifikasi 24 November 2026.

# KODEBOOK DAN TEMPLATE TABULASI — Pilot N=30 & Final Minimal 111

> Acuan: Tabel 3.2 proposal (27 butir), keputusan D41 dan D45, serta risalah 17 November 2026 tentang validasi kuesioner.

## 0. Versi instrumen dan batas bukti

Tiga hal yang harus dibedakan: **draf legacy**, **form live yang diperiksa**, dan **spesifikasi target**. Hanya yang kedua punya bukti terpasang.

| Versi | Bukti | Pertanyaan | Kolom Sheets |
|---|---|---|---|
| LEGACY (sebelum D45) | Tidak diverifikasi ulang pada sesi ini | P3 kode 8 memuat Tanjung Duren; P5 empat opsi dengan marketplace terakhir | Tidak dipakai |
| LIVE-20261124 | `forms.get` revisionId **0000002c**, spreadsheets.values.get pada lembar `Form Responses 1` | 38 pertanyaan; S3 redaksi inklusif; P5 lima opsi dengan marketplace pertama | **39** (Timestamp + 38 jawaban) |
| Target D45 | Terpasang pada form live per 24 November 2026 | Sama dengan LIVE | Sama dengan LIVE |

Bukti LIVE: form publik HTTP 200 (50 item, 13 section, 27 butir Likert), `isAcceptingResponses=true`, `emailCollectionType=DO_NOT_COLLECT`, dan lembar respons berisi **hanya baris header** (nol respons saat diperiksa). Patch P3a menaikkan revisionId `0000002b` → `0000002c`, menambah satu `itemId` (`105e79fe`), tanpa mengubah item, routing, pengaturan, atau status publikasi lain.

**Peringatan urutan kolom:** Google Sheets menambahkan pertanyaan baru di **ujung kanan** lembar, bukan pada posisi section-nya di form. P3a yang tampil setelah P3 di form justru berada di **kolom 39**, sesudah M6. Dataset analisis karena itu memakai urutan baku di bawah, bukan urutan mentah lembar, dan setiap impor wajib memetakan ulang nama kolom.

Angka kolom di bawah adalah **urutan dataset analisis**. Simpan ekspor mentah apa adanya, beserta revisionId form dan tanggal ekspor, di samping peta label pertanyaan. Jangan menggabungkan kode numerik lintas versi tanpa menelusuri label asalnya.

---

## 1. Aturan pengodean skor Likert

| Skor | Label | Keterangan |
|---|---|---|
| 5 | Sangat Setuju (SS) | Konstruk tertinggi |
| 4 | Setuju (S) | — |
| 3 | Netral (N) | — |
| 2 | Tidak Setuju (TS) | — |
| 1 | Sangat Tidak Setuju (STS) | Konstruk terendah |

- Seluruh 27 butir **searah positif (favorabel)**; tanpa reverse-scoring, skor mentah dipakai apa adanya.
- Nilai sah hanya bilangan bulat 1–5. Nilai 0, 6 atau lebih, dan teks adalah kesalahan input dan harus dikoreksi ke sumber Forms sebelum analisis.
- **Aturan nilai hilang:** seluruh butir Likert diset wajib-isi sehingga seharusnya nol hilang. Bila terjadi sel kosong pada entri manual, biarkan **kosong** — jangan isi 0, 9, atau rata-rata. Baris dengan butir kosong ditangani dengan *listwise deletion* di SPSS. Pilot N=30 wajib lengkap (30 baris × 27 butir terisi). Respons gagal screening (INCLUDE=0) dieksklusi sebelum uji apa pun dan **bukan** nilai hilang; simpan di berkas terpisah.

## 2. Filter inklusi (4 kriteria → flag INCLUDE)

| Kolom | Kode | Lulus (=1) | Gagal (=0) |
|---|---|---|---|
| S1_WNI | 1=Ya WNI; 0=Tidak | Warga Negara Indonesia | Bukan WNI |
| S2_Usia17 | 1=Ya ≥17 tahun; 0=Tidak | Usia ≥17 | Usia <17 |
| S3_Jakbar | 1=Ya (minimal salah satu keterkaitan: tinggal/kost, kuliah/kerja, atau berbelanja/bermain di LGS Jakarta Barat); 0=Tidak | Terkait Jakarta Barat | Tidak terkait |
| S4_Beli | 1=Beli dalam ≤6 bulan terakhir; 2=Beli >6–≤12 bulan terakhir; 0=≥12 bulan lalu atau belum pernah | 1 atau 2 | 0 |
| INCLUDE | 1=layak analisis; 0=eksklusi | S1=1 **dan** S2=1 **dan** S3=1 **dan** S4≥1 | Selain itu |

> Rumus: `INCLUDE = 1 JIKA (S1=1 DAN S2=1 DAN S3=1 DAN S4>=1), SELAIN ITU 0`. Hanya baris INCLUDE=1 masuk SPSS (pilot 30 baris; final 111–150 baris lulus, di luar pilot).

Eligibility tetap **12 bulan**. Profil P4 tetap berjendela **6 bulan** dan menyediakan kategori `0 kali`, sehingga responden yang lulus S4 kategori 2 tetap terwakili di profil demografi.

- **C0** (persetujuan) tidak boleh bernilai "Tidak" pada dataset analisis. Jika ada respons dengan C0=Tidak, itu penolakan, bukan data penelitian: pisahkan dan jangan analisis.
- **P3a** bersifat opsional dan **tidak** dipakai sebagai filter inklusi; hanya untuk deskripsi bentuk keterkaitan wilayah.

## 3. Kamus kolom (urutan baku dataset — jangan diubah)

| # | Nama kolom | Isi / kode | Wajib |
|---|---|---|---|
| 1 | RespID | P001..P030 (pilot); R001..R150 (final) | Ya |
| 2 | C0_Consent | 1=Ya setuju; 0=Tidak setuju (eksklusi, tidak dianalisis) | Ya |
| 3–6 | S1_WNI, S2_Usia17, S3_Jakbar, S4_Beli | sesuai §2 | Ya |
| 7 | P1_JK | 0=tidak menjawab; 1=Laki-laki; 2=Perempuan | Tidak |
| 8 | P2_Usia | 0=tidak menjawab; 1=17–20; 2=21–25; 3=26–30; 4=>30 tahun | Tidak |
| 9 | P3_Kec | 0=tidak menjawab; 1=Cengkareng; 2=Grogol Petamburan; 3=Kalideres; 4=Kebon Jeruk; 5=Kembangan; 6=Palmerah; 7=Taman Sari; **8=Tambora** | Tidak |
| 10 | P4_Frek | 0=tidak menjawab; **5=0 kali**; 1=1 kali; 2=2–3 kali; 3=4–6 kali; 4=lebih dari 6 kali | Ya |
| 11 | P5_Kanal | 0=tidak menjawab; 1=Marketplace daring/E-commerce; 2=LGS resmi; 3=Minimarket/toko buku; 4=Transaksi langsung/COD komunitas; 5=Lainnya | Tidak |
| 12 | P3a_Keterkaitan | 0=tidak menjawab; 1=Domisili/kost; 2=Tempat kuliah; 3=Tempat bekerja; 4=Lokasi bermain/belanja (LGS/mall); 5=Beberapa sekaligus (komuter) | Tidak |
| 13–18 | Y1…Y6 | 1–5 (Impulsive Buying) | Ya |
| 19–23 | X1_1…X1_5 | 1–5 (Hedonic Motivation) | Ya |
| 24–28 | X2_1…X2_5 | 1–5 (Desire for Completeness) | Ya |
| 29–33 | X3_1…X3_5 | 1–5 (Speculative Motive) | Ya |
| 34–39 | M1…M6 | 1–5 (Self-Control) | Ya |
| 40 | INCLUDE | 1/0 sesuai §2 | Ya |

**Catatan versi kode:**

- **P3:** kode `8` pada kodebook legacy berarti "Tanjung Duren/Lainnya-Jakbar". Sejak D45, kode `8` berarti **Tambora**, mengikuti delapan kecamatan resmi Jakarta Barat. Jangan menggabungkan berkas lintas versi tanpa menelusuri label. Tanjung Duren adalah bagian Grogol Petamburan, bukan kecamatan terpisah.
- **P4:** kode `0` khusus berarti **tidak menjawab**. Nol pembelian nyata diberi kode `5`. Jangan menyatukan keduanya.
- **P5:** urutan opsi berubah pada D45 (marketplace dari terakhir ke pertama). Penomoran di atas mengikuti urutan baru; ekspor versi lama memakai penomoran berbeda.

Skor komposit (Y_mean, X1_mean, X2_mean, X3_mean, M_mean) **tidak** ditabulasi manual — dihitung di SPSS via `MEAN(...)`, lalu di-*centering* (X1c, X2c, X3c, Mc) dan dihitung interaksinya (X1Mc, X2Mc, X3Mc).

## 4. Template header CSV — PILOT (N=30 lengkap, INCLUDE=1 semua)

Salin blok berikut sebagai baris pertama berkas CSV pilot (`data_pilot_N30.csv`). Isi 30 baris data; satu baris ilustratif disertakan dan harus dihapus sebelum analisis.

```csv
RespID,C0_Consent,S1_WNI,S2_Usia17,S3_Jakbar,S4_Beli,P1_JK,P2_Usia,P3_Kec,P4_Frek,P5_Kanal,P3a_Keterkaitan,Y1,Y2,Y3,Y4,Y5,Y6,X1_1,X1_2,X1_3,X1_4,X1_5,X2_1,X2_2,X2_3,X2_4,X2_5,X3_1,X3_2,X3_3,X3_4,X3_5,M1,M2,M3,M4,M5,M6,INCLUDE
P001,1,1,1,1,1,1,2,2,2,1,2,4,3,4,5,3,4,5,4,3,4,5,4,5,4,5,4,3,4,4,3,4,4,4,3,4,4,3,1
```

Kontrol kualitas pilot: 30 baris; tiap baris 27 butir Likert 1–5 terisi; S1–S4 lulus; C0=1; uji validitas Pearson r-hitung > r-tabel 0,361 (df=28, alfa 5% dua sisi) dengan *corrected item-total* ≥0,30 sebagai pendukung; reliabilitas per konstruk Cronbach Alpha ≥0,70. Butir yang gagal direvisi redaksinya, lalu penyebaran diulang sampai 30 baris lulus valid dan reliabel sebelum lanjut ke final.

## 5. Template header CSV — FINAL (N=111–150 bersih, di luar pilot)

Header **identik** dengan pilot agar sintaks SPSS berjalan tanpa penyuntingan; bedanya RespID R001… dan jumlah baris 111–150 dengan INCLUDE=1. Baris INCLUDE=0 disimpan terpisah (`log_eksklusi.csv`) dan tidak ikut analisis.

```csv
RespID,C0_Consent,S1_WNI,S2_Usia17,S3_Jakbar,S4_Beli,P1_JK,P2_Usia,P3_Kec,P4_Frek,P5_Kanal,P3a_Keterkaitan,Y1,Y2,Y3,Y4,Y5,Y6,X1_1,X1_2,X1_3,X1_4,X1_5,X2_1,X2_2,X2_3,X2_4,X2_5,X3_1,X3_2,X3_3,X3_4,X3_5,M1,M2,M3,M4,M5,M6,INCLUDE
R001,1,1,1,1,2,2,1,5,1,2,4,4,4,3,5,4,5,5,4,3,4,4,4,5,3,4,4,5,3,4,4,3,4,5,3,4,4,3,1
```

Kontrol kualitas final: N bersih 111–150 (memenuhi Green 1991: `N ≥ 50 + 8k` = 106 dan `N ≥ 104 + k` = 111 untuk k=7); sampling purposive; pastikan tidak ada RespID pilot yang masuk ulang; impor ke SPSS lalu jalankan `03_Output_SPSS_MRA/SINTAKS_MRA_2TAHAP.sps`.

## 6. Prosedur ekspor dan verifikasi ulang

1. Ekspor dari lembar `Form Responses 1` sebagai CSV, lalu simpan dengan nama yang memuat tanggal dan revisionId form.
2. Petakan kolom mentah ke nama baku §3 berdasarkan **teks pertanyaan**, bukan posisi. P3a akan berada di ujung kanan lembar.
3. Verifikasi: jumlah kolom hasil pemetaan = 40; jumlah butir Likert = 27; semua nilai Likert ∈ {1,…,5}; tidak ada C0=0 pada berkas analisis.
4. Simpan berkas mentah, berkas terpetakan, dan log eksklusi beserta catatan revisionId.
5. Bila form diubah lagi setelah ekspor, ekspor ulang dan perbarui kodebook ini; jangan mencampur berkas dari dua revisionId berbeda.
