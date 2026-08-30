# Product Requirements Document (PRD): KBMI 4 Green Financing Thesis Remediation
**Framework: Spec-Driven Development (SDD) & Invariant Specification Contract**
*Versi: 2.0.0 | Tanggal: 30 Agustus 2026 | Target: Kelayakan Sidang Skripsi FEB UKRIDA (100% Bebas Revisi)*

---

## 1. Project Overview & Problem Statement

### 1.1 Background & Context
Naskah skripsi program studi Akuntansi/Manajemen FEB UKRIDA berjudul *"Analisis Pengaruh Green Financing, Non-Performing Loans (NPL), dan Capital Adequacy Ratio (CAR) terhadap Return on Assets (ROA) pada Bank KBMI 4 Periode 2021–2025"* mengalami kegagalan audit replikasi oleh PRISM AI.
Ditemukan kontradiksi fatal antara dataset lampiran, data publikasi resmi OJK/Bank, output ekonometrika, dan interpretasi teoritis.

### 1.2 Core Objective
Mentransformasi dan merekonstruksi seluruh ekosistem skripsi (dataset, skrip ekonometrika, naskah LaTeX, bibliografi BibTeX, dan pembahasan Bab 1 s.d. Bab 5) menjadi karya ilmiah yang **100% reproducible, bebas bias, mathematically sound, dan mematuhi regulasi perbankan Indonesia terkini**.

---

## 2. Invariant Contracts & Non-Goals

### 2.1 Invariant System Contracts (Unbreakable Rules)
1. **Single Source of Truth (SSOT):** Seluruh statistik, tabel Bab 4, lampiran Appendix 1, dan output EViews/R/Python harus diturunkan secara deterministik dari **satu berkas dataset master (`dataset_kbmi4_master.csv`)**. Tidak boleh ada angka yang diubah secara manual tanpa skrip generator.
2. **Provenance & Audit Trail:** Setiap titik observasi (80 baris: 4 bank $\times$ 20 kuartal) wajib memiliki metadata sumber primer: *Nama Dokumen Resmi*, *Tahun/Kuartal Laporan*, *Halaman Laporan*, *Basis Pelaporan (Bank-Only vs Konsolidasi)*, dan *Metode Anualisasi ROA*.
3. **Reproducibility Guarantee:** Eksekusi skrip replikasi wajib menghasilkan $R^2$, koefisien regresi, $t$-statistic, $F$-statistic, dan uji asumsi klasik yang identik dengan teks narasi di Bab 4.
4. **Epistemic Honesty:** Seluruh klaim kausalitas absolut ("membuktikan", "menyelesaikan perdebatan") dilarang keras. Klaim harus diformulasikan secara proporsional sebagai asosiasi empiris berbasis estimasi panel data.
5. **Typesetting & Notation Integrity:** Dokumen LaTeX wajib bebas dari karakter tanda tanya (`?`), menggunakan notasi standar tanpa ambiguitas ($n=NT$ untuk total sampel, $N$ untuk entitas bank, $T$ untuk periode kuartal, $K$ untuk jumlah variabel independen, $\kappa$ untuk kurtosis, $\alpha_i = \alpha + \mu_i$ untuk efek bank).

### 2.2 Non-Goals
- Tidak memperluas cakupan sampel ke bank KBMI 3/2/1 untuk menjaga konsistensi dengan proposal yang telah disetujui (tetap fokus pada 4 Bank KBMI 4: BBRI, BMRI, BBCA, BBNI).
- Tidak menggunakan model *Black-Box* Machine Learning yang tidak diakui dalam standar metodologi ekonometrika skripsi S1 FEB UKRIDA.
- Tidak merekayasa data agar seluruh hipotesis signifikan, melainkan melaporkan temuan empiris murni dengan pembahasan teoritis yang mendalam.

---

## 3. Scope of Remediation & Detailed Feature Requirements

```
+==================================================================================================+
|                                SPEC-DRIVEN REMEDIATION MODULES                                    |
+==================================================================================================+
|  [MODULE 1: DATA]        [MODULE 2: ECONOMETRICS]     [MODULE 3: THEORY & REGULATION]             |
|  - Rekonstruksi 80 Baris  - Dynamic Panel / FEM-DK    - Update POJK 18/2023 & Taksonomi Hijau     |
|  - Validasi Laporan Resmi - Uji CSD & Driscoll-Kraay  - PSAK 71 / IFRS 9 Staging True Logic       |
|  - Green Finance Formula  - Wald Test df Koreksi      - Re-grounding 40+ Jurnal (BibTeX)          |
|                                         │                                                        |
|                                         ▼                                                        |
|  [MODULE 4: PROSE & LATEX]                            [MODULE 5: POLICY & DEFENSE]                |
|  - Encoding Fix (? -> UTF-8/LaTeX)                    - Kalibrasi Rekomendasi Bab 5               |
|  - Rekonstruksi Bab 1 s.d. Bab 5                      - Sinkronisasi PPT & Lembar Ujian Sidang    |
|  - Kompilasi Bebas Warning pdflatex                   - Defense Dossier untuk Penguji             |
+==================================================================================================+
```

### Module 1: Data Engineering & Dataset Master Reconstruction
- **REQ-1.1:** Ekstraksi ulang 80 baris data dari Laporan Keuangan Publikasi Triwulanan (Q1 2021 s.d. Q4 2025) resmi dari Investor Relations BBRI, BMRI, BBCA, dan BBNI.
- **REQ-1.2:** Standarisasi basis pelaporan:
  - **ROA:** Menggunakan rasio kinerja tahunan (*annualized year-to-date*) sesuai publikasi resmi OJK / BI.
  - **NPL:** Menggunakan *NPL Gross* (posisi akhir periode).
  - **CAR:** Menggunakan rasio kecukupan modal *Total CAR* posisi akhir periode.
  - **Green Financing:** Menetapkan formula kuantitatif rasio:
    $$\text{Green Financing Ratio}_{i,t} = \frac{\text{Portofolio Pembiayaan Hijau / KUBL}_{i,t}}{\text{Total Kredit yang Diberikan}_{i,t}} \times 100\%$$
    Mendokumentasikan dengan transparan apakah data kuartalan berasal dari *Quarterly Financial Report / Investor Presentation* atau interpolasi linear teruji.
- **REQ-1.3:** Pembuatan berkas `dataset_kbmi4_master.csv` dan kamus data `DATA_DICTIONARY_V2.md` lengkap dengan tautan halaman laporan keuangan.

### Module 2: Rigorous Econometric Pipeline
- **REQ-2.1:** Pemilihan model formal melalui uji Chow ($F$-statistic), uji Hausman ($\chi^2$), dan uji Lagrange Multiplier (LM Breusch-Pagan).
- **REQ-2.2:** Penanganan komprehensif isu diagnostik panel:
  - Uji *Cross-Sectional Dependence* (Pesaran CD test / Frees test).
  - Uji Heteroskedastisitas Panel (Modified Wald test for groupwise heteroskedasticity).
  - Uji Autokorelasi Serial Panel (Wooldridge test for serial correlation in panel data).
  - Jika terdapat autokorelasi/heteroskedastisitas/CSD, terapkan **Driscoll-Kraay Standard Errors** atau **Panel Corrected Standard Errors (PCSE)** pada Fixed Effects Model (FEM) agar inferensi $t$-statistic dan $p$-value valid.
- **REQ-2.3:** Koreksi derajat kebebasan (*degrees of freedom*) pada perhitungan *Adjusted* $R^2$ ($df = NT - N - K$) dan uji Wald $F$-test khusus untuk parameter lereng ($\beta_1, \beta_2, \beta_3 = 0$).
- **REQ-2.4:** Ekstraksi skrip ekonometrika otomatis (`run_econometrics.py` / `eviews_script.prg`) yang menghasilkan log dan tabel yang dapat diverifikasi secara instan.

### Module 3: Theoretical & Regulatory Realignment
- **REQ-3.1:** Perbaikan regulasi keberlanjutan:
  - Merujuk pada **POJK No. 51/POJK.03/2017** dengan batasan yang tepat ("verifikasi independen bersifat sukarela/jika ada").
  - Memperbarui dasar hukum *Green Bond* dari POJK 60/2017 ke **POJK No. 18 Tahun 2023** tentang Penerbitan dan Persyaratan Efek Bersifat Utang dan Sukuk Berlandaskan Keberlanjutan.
  - Menyajikan klasifikasi Kategori Usaha Berwawasan Lingkungan (KUBL) 12 kategori sesuai Taksonomi Keuangan Berkelanjutan Indonesia (TKBI) Versi Terkini.
- **REQ-3.2:** Penjelasan akurat PSAK 71 / IFRS 9:
  - Menjelaskan klasifikasi 3 Staging (*Stage 1: 12-month ECL, Stage 2: Lifetime ECL with SICR, Stage 3: Lifetime ECL Credit-Impaired*).
  - Menegaskan bahwa CKPN dihitung berdasarkan *Probability-Weighted Discounted Cash Shortfall*, bukan asumsi pukul rata 100% provisi.
- **REQ-3.3:** Rekonstruksi Bibliografi:
  - Membangun `references.bib` yang valid dengan metadata DOI dan publikasi terverifikasi.
  - Mengoreksi seluruh mismatch sitasi (Cui et al. 2018, Chiaramonte et al. 2020, Yin et al. 2021).
  - Mengganti sitasi teks mentah dengan perintah `\cite{...}` atau `\citep{...}`.

### Module 4: Naskah LaTeX & Typesetting Perfection
- **REQ-4.1:** Perbaikan encoding global: menghilangkan seluruh simbol `?` dan menggantikannya dengan format LaTeX yang benar.
- **REQ-4.2:** Penulisan ulang Bab 1 s.d. Bab 5 dalam format LaTeX (`skripsi_ukrida.tex`):
  - Mengganti klaim kausal berlebihan dengan bahasa ilmiah presisi.
  - Memperbaiki analisis elastisitas dan sensitivitas parsial tanpa mencampuradukkan *percentage points* dan elastisitas persentase murni.
  - Menghapus judul ganda dan typo (*"batas batas toleransi"*, *"antarbang"*).
  - Mengisi seluruh metadata front matter (NIM, Pembimbing, Penguji, Biodata).
- **REQ-4.3:** Kompilasi bersih menghasilkan `skripsi_ukrida.pdf` bebas error, layout tabel *booktabs* rapi, dan konsisten dengan panduan FEB UKRIDA 2022.

---

## 4. Definition of Done (Acceptance Criteria)

| ID | Kriteria Penerimaan (DoD) | Metode Verifikasi | Status |
| :---: | :--- | :--- | :---: |
| **AC-1** | 100% Angka Bab 4 identik dengan output ekonometrika dari `dataset_kbmi4_master.csv`. | Script automated diff & cross-table check | Target: PASS |
| **AC-2** | Seluruh 80 titik data terverifikasi terhadap Laporan Keuangan Publikasi Bank (BBRI, BMRI, BBCA, BBNI). | Provenance table audit | Target: PASS |
| **AC-3** | Estimasi regresi menggunakan robust standard errors (Driscoll-Kraay/PCSE) jika terdeteksi CSD/autokorelasi. | Log ekonometrika eksekusi | Target: PASS |
| **AC-4** | *Adjusted* $R^2$ dan Uji $F$ menggunakan rumus derajat kebebasan yang benar ($df = NT - N - K$). | Audit matematis naskah | Target: PASS |
| **AC-5** | Tidak ada karakter `?` pada simbol matematika, tabel, dan teks naskah. | Linter regex check pada `.tex` | Target: PASS |
| **AC-6** | Seluruh sitasi terhubung ke `references.bib` dan metadata DOI terverifikasi. | BibTeX compilation audit | Target: PASS |
| **AC-7** | Naskah `skripsi_ukrida.pdf` terkompilasi sempurna tanpa overfull/underfull fatal. | Log pdflatex / latexmk | Target: PASS |
