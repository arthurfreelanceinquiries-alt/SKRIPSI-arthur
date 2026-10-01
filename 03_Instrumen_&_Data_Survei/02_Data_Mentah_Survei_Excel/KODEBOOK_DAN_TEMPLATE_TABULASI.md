> [!SUMMARY] Tujuan & Solusi Catatan Ini
> - **Untuk Apa:** Kodebook tabulasi dan header CSV mentah pilot (N=30) serta final (N=111-150) siap salin-tempel.
> - **Masalah yang Diselesaikan:** Mencegah inkonsistensi nama kolom, kode skor, missing value, dan filter inklusi antar penabulator.
> - **Keputusan/Output:** Skema 40 kolom baku (S1-S4, P1-P5, Y1-M6, INCLUDE) plus template header CSV teks.

# KODEBOOK DAN TEMPLATE TABULASI — Pilot N=30 & Final N=111–150

> Acuan: Tabel 3.2 proposal (27 butir), kriteria inklusi Bab 3 (WNI; usia >=17; domisili/aktivitas Jakarta Barat; beli pack resmi >=1x dalam 6–12 bulan), Green (1991) N>=111 target 120–150 purposive sampling, pilot N=30 (r-tabel 0,361; Alpha>=0,70), Likert 5 poin. Format tabulasi berupa **teks/CSV dalam MD ini — bukan file biner**.

---

## 1. Aturan pengodean skor Likert

| Skor | Label | Keterangan |
|---|---|---|
| 5 | Sangat Setuju (SS) | Konstruk tertinggi |
| 4 | Setuju (S) | — |
| 3 | Netral (N) | — |
| 2 | Tidak Setuju (TS) | — |
| 1 | Sangat Tidak Setuju (STS) | Konstruk terendah |

- Seluruh 27 butir **searah positif (favorabel)** — tanpa reverse-scoring; skor mentah dipakai apa adanya.
- Nilai yang sah hanya bilangan bulat 1–5. Nilai lain (0, 6+, teks) = salah input dan wajib dikoreksi ke sumber Forms sebelum analisis.
- **Missing-value rule:** Google Forms diset wajib-isi sehingga idealnya nol missing. Bila terjadi sel kosong pada entri manual: biarkan **kosong** (jangan isi 0/9/mean); baris dengan butir kosong diestimasi dengan **listwise deletion** di SPSS; pilot test N=30 wajib **lengkap 100%** (30 baris x 27 butir terisi). Screening gagal (INCLUDE=0) dieksklusi sebelum uji apa pun — bukan missing.

## 2. Filter inklusi (4 kriteria → flag INCLUDE)

| Kolom | Kode | Lulus (=1) | Gagal (=0) |
|---|---|---|---|
| S1_WNI | 1=Ya WNI; 0=Tidak | WNI | Bukan WNI |
| S2_Usia17 | 1=Ya >=17 th; 0=Tidak | Usia >=17 | Usia <17 |
| S3_Jakbar | 1=Ya domisili/aktivitas Jakbar; 0=Tidak | Jakbar | Luar Jakbar |
| S4_Beli | 1=Ya beli 6 bln terakhir; 2=Ya beli 6–12 bln terakhir; 0=Tidak | 1 atau 2 | 0 |
| INCLUDE | 1=layak analisis; 0=eksklusi | S1>=1 & S2=1 & S3=1 & S4>=1 | selain itu |

> Rumus tabulasi: `INCLUDE = 1 JIKA (S1=1 DAN S2=1 DAN S3=1 DAN S4>=1), SELAIN ITU 0`. Hanya baris INCLUDE=1 yang masuk SPSS (pilot: 30 baris lulus; final: 111–150 baris lulus bersih di luar pilot).

## 3. Kamus kolom (urutan baku — jangan diubah)

| # | Nama kolom | Isi / kode | Wajib |
|---|---|---|---|
| 1 | RespID | P001..P030 (pilot); R001..R150 (final) | Ya |
| 2–5 | S1_WNI, S2_Usia17, S3_Jakbar, S4_Beli | sesuai tabel filter §2 | Ya |
| 6–10 | P1_JK, P2_Usia, P3_Kec, P4_Frek, P5_Kanal | 0=tidak menjawab; P1:1=L,2=P; P2:1=17–20,2=21–25,3=26–30,4=>30; P3:1=Cengkareng,2=Grogol Petamburan,3=Kalideres,4=Kebon Jeruk,5=Kembangan,6=Palmerah,7=Taman Sari,8=Tanjung Duren/Lainnya-Jakbar; P4:1=1x,2=2–3x,3=4–6x,4=>6x; P5:1=LGS,2=Ritel modern,3=COD komunitas,4=Marketplace | P4 disarankan terisi |
| 11–16 | Y1, Y2, Y3, Y4, Y5, Y6 | 1–5 (Impulsive Buying) | Ya |
| 17–21 | X1_1, X1_2, X1_3, X1_4, X1_5 | 1–5 (Hedonic Motivation) | Ya |
| 22–26 | X2_1, X2_2, X2_3, X2_4, X2_5 | 1–5 (Desire for Completeness) | Ya |
| 27–31 | X3_1, X3_2, X3_3, X3_4, X3_5 | 1–5 (Speculative Motive) | Ya |
| 32–37 | M1, M2, M3, M4, M5, M6 | 1–5 (Self-Control) | Ya |
| 38 | INCLUDE | 1/0 sesuai §2 | Ya |

Skor komposit (Y_mean, X1_mean, X2_mean, X3_mean, M_mean) **tidak** ditabulasi manual — dihitung di SPSS via sintaks (`MEAN(...)`), lalu di-centering (X1c, X2c, X3c, Mc) dan interaksi (X1Mc, X2Mc, X3Mc).

## 4. Template header CSV — PILOT (N=30 lengkap, INCLUDE=1 semua)

Salin blok di bawah sebagai baris pertama file CSV pilot (`data_pilot_N30.csv`). Isi 30 baris data; contoh 1 baris ilustratif disertakan (hapus sebelum analisis bila hanya butuh header).

```csv
RespID,S1_WNI,S2_Usia17,S3_Jakbar,S4_Beli,P1_JK,P2_Usia,P3_Kec,P4_Frek,P5_Kanal,Y1,Y2,Y3,Y4,Y5,Y6,X1_1,X1_2,X1_3,X1_4,X1_5,X2_1,X2_2,X2_3,X2_4,X2_5,X3_1,X3_2,X3_3,X3_4,X3_5,M1,M2,M3,M4,M5,M6,INCLUDE
P001,1,1,1,1,1,2,8,2,1,4,3,4,5,3,4,5,4,3,4,5,4,5,4,5,4,3,4,4,3,4,4,4,3,4,4,3,1
```

Kontrol kualitas pilot: 30 baris; tiap baris 27 butir 1–5 terisi; S1–S4 lulus; uji validitas Pearson r-hitung > r-tabel 0,361 (df=28, alfa 5% dua sisi) + corrected item-total >=0,30 pendukung; reliabilitas per konstruk Cronbach Alpha >=0,70; butir gagal → revisi redaksi lalu ulangi sebar hingga 30 lulus valid-reliabel sebelum lanjut final.

## 5. Template header CSV — FINAL (N=111–150 bersih, di luar pilot)

Header **identik** dengan pilot (agar sintaks SPSS jalan tanpa edit); bedanya RespID R001… dan jumlah baris 111–150 baris INCLUDE=1. Baris INCLUDE=0 disimpan di file terpisah (`log_eksklusi.csv`) dan tidak ikut analisis.

```csv
RespID,S1_WNI,S2_Usia17,S3_Jakbar,S4_Beli,P1_JK,P2_Usia,P3_Kec,P4_Frek,P5_Kanal,Y1,Y2,Y3,Y4,Y5,Y6,X1_1,X1_2,X1_3,X1_4,X1_5,X2_1,X2_2,X2_3,X2_4,X2_5,X3_1,X3_2,X3_3,X3_4,X3_5,M1,M2,M3,M4,M5,M6,INCLUDE
R001,1,1,1,2,2,1,5,1,2,4,4,3,4,3,5,4,5,4,3,4,5,4,4,5,5,4,3,4,4,3,3,4,4,3,4,4,1
```

Kontrol kualitas final: N bersih 111–150 (memenuhi Green 1991: 50+8k=106 dan 104+k=111 untuk k=7; target 120–150, power Cohen >=0,80 efek sedang); sampling purposive; pastikan tidak ada RespID pilot yang masuk ulang (pilot dan final saling lepas); impor ke SPSS lalu jalankan `03_Output_SPSS_MRA/SINTAKS_MRA_2TAHAP.sps`.
