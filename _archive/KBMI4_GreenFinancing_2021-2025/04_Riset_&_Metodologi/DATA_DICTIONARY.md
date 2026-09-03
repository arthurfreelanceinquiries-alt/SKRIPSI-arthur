# Data Dictionary & Audit Dataset Skripsi

> **Topik:** Pengaruh Portofolio Kredit Hijau (*Green Financing*), *Non-Performing Loan* (NPL), dan *Capital Adequacy Ratio* (CAR) terhadap Profitabilitas (*Return on Assets* / ROA) pada Bank KBMI 4 di Indonesia Periode 2021–2025.  
> **Status:** 100% Data Sekunder Publik Terverifikasi.  
> **Unit Observasi:** Bank Umum Kategori KBMI 4 di Bursa Efek Indonesia per periode kuartalan (Triwulan 1 s.d. 4) tahun 2021–2025.

---

## 1. Identifikasi Objek & Kerangka Sampel (Purposive Sampling)

Objek penelitian adalah seluruh bank yang masuk dalam Kelompok Bank Berdasarkan Modal Inti (KBMI) 4 (modal inti di atas Rp70 Triliun) sesuai POJK No. 12/POJK.03/2021:

| No | Kode Emiten | Nama Entitas Perbankan | Status Kepemilikan | Ketersediaan *Sustainability Report* | Ketersediaan *Annual Report* 2021–2025 |
|---|---|---|---|---|---|
| 1 | **BBRI** | PT Bank Rakyat Indonesia (Persero) Tbk | BUMN | Tersedia Lengkap (2021–2025) | Tersedia Lengkap (Audited) |
| 2 | **BMRI** | PT Bank Mandiri (Persero) Tbk | BUMN | Tersedia Lengkap (2021–2025) | Tersedia Lengkap (Audited) |
| 3 | **BBCA** | PT Bank Central Asia Tbk | Swasta Nasional | Tersedia Lengkap (2021–2025) | Tersedia Lengkap (Audited) |
| 4 | **BBNI** | PT Bank Negara Indonesia (Persero) Tbk | BUMN | Tersedia Lengkap (2021–2025) | Tersedia Lengkap (Audited) |

---

## 2. Definisi Operasional Variabel & Formula Matematis

| Kode Variabel | Nama Variabel | Konsep Teoritis | Definisi Operasional & Rumus Matematis | Satuan / Skala | Letak pada Laporan Keuangan / Keberlanjutan | Tanda Dugaan Hipotesis |
|---|---|---|---|---|---|---|
| **$Y$** | **Return on Assets (ROA)** | Profitabilitas Bank | Rasio untuk mengukur kemampuan manajemen bank dalam menghasilkan laba sebelum pajak dari total aset yang dikelola.<br>$$\text{ROA} = \frac{\text{Laba Sebelum Pajak}}{\text{Total Aset Rata-rata}} \times 100\%$$ | Persen (%) / Rasio | Laporan Laba Rugi Komprehensif & Rasio Kinerja Keuangan (*Financial Highlights*) | - (Dependen) |
| **$X_1$** | **Green Financing (GF)** | Portofolio Kredit Hijau / Berkelanjutan | Proporsi pembiayaan untuk Kegiatan Usaha Berwawasan Lingkungan (KUBL) dan sektor berkelanjutan terhadap total kredit.<br>$$\text{GF} = \frac{\text{Penyaluran Kredit Berkelanjutan/Hijau}}{\text{Total Portofolio Kredit yang Disalurkan}} \times 100\%$$ | Persen (%) / Rasio | *Sustainability Report* (Laporan Keberlanjutan Tahunan) & Keterbukaan Informasi POJK 51/2017 | **Positif (+)** |
| **$X_2$** | **Non-Performing Loan (NPL Gross)** | Risiko Kredit | Rasio kredit bermasalah (kolektibilitas Kurang Lancar, Diragukan, Macet) terhadap total kredit yang diberikan bank.<br>$$\text{NPL} = \frac{\text{Total Kredit Bermasalah}}{\text{Total Kredit yang Disalurkan}} \times 100\%$$ | Persen (%) / Rasio | Catatan atas Laporan Keuangan (CALK) - Bagian Kredit & Rasio Keuangan (*Annual Report*) | **Negatif (-)** |
| **$X_3$** | **Capital Adequacy Ratio (CAR)** | Kecukupan Modal | Rasio kecukupan modal bank untuk menutup risiko kerugian dari aktiva tertimbang menurut risiko.<br>$$\text{CAR} = \frac{\text{Total Modal Inti + Pelengkap}}{\text{Aktiva Tertimbang Menurut Risiko (ATMR)}} \times 100\%$$ | Persen (%) / Rasio | Laporan Posisi Keuangan, CALK Modal, & Tabel Rasio Keuangan Resmi | **Positif (+)** |

---

## 3. Struktur Dataset Panel (Panel Data Design)

Penelitian menggunakan struktur data panel (*pooled time-series & cross-section*):
- **Dimensi Silang (*Cross-Section*, $N$):** 4 Bank (BBRI, BMRI, BBCA, BBNI).
- **Dimensi Waktu (*Time-Series*, $T$):** 20 Periode Kuartalan (Triwulan I 2021 s.d. Triwulan IV 2025) atau 5 Periode Tahunan.
- **Total Observasi ($N \times T$):**
  - Pada format kuartalan: $4 \times 20 = \mathbf{80 \text{ Observasi}}$ *(Sangat aman dan direkomendasikan untuk uji data panel EViews/SPSS)*.
  - Pada format tahunan: $4 \times 5 = \mathbf{20 \text{ Observasi}}$.

---

## 4. Protokol Ekstraksi & Integritas Data

1. **Sumber Unduhan Resmi:**
   - Website Bursa Efek Indonesia: `https://www.idx.co.id/id/perusahaan-tercatat/laporan-keuangan-dan-tahunan/`
   - Portal Resmi Emiten:
     - Bank Mandiri: `ir.bankmandiri.co.id`
     - Bank BRI: `ir.bri.co.id`
     - Bank BCA: `bca.co.id/id/tentang-bca/Hubungan-Investor`
     - Bank BNI: `bni.co.id/id-id/perusahaan/hubunganinvestor`
2. **Penanganan Data Missing / Tidak Lengkap:**
   - Seluruh 4 bank KBMI 4 wajib mempublikasikan Laporan Keberlanjutan tahunan dan Laporan Keuangan Kuartalan ke OJK sesuai POJK 51/2017. Tidak ada isu *missing data* struktural.
   - Angka *Green Financing* tahunan pada data kuartalan dialokasikan sesuai laporan triwulanan manajemen atau menggunakan interpolasi linier tertimbang realisasi kuartalan.
3. **Uji Outlier (Data Ekstrem):**
   - Menggunakan *Z-Score* standardisasi ($\pm 3.0$) dan *Boxplot Winsorizing* jika ditemukan lonjakan data akibat perubahan klasifikasi PSAK/regulasi perbankan.
