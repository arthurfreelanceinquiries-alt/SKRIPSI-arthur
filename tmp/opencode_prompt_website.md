# Tugas: Buat Website Portofolio Sederhana (HTML + CSS + JS vanilla)

Buatkan sebuah website portofilio STATIS sederhana yang mempresentasikan penelitian skripsi berikut. Tidak boleh pakai framework, build tools, atau CDN library apa pun — hanya HTML, CSS, dan JavaScript murni (vanilla). Semua aset lokal.

## Konten Sumber (FAKTA dari skripsi — jangan mengarang angka lain)

**Judul:** "Pengaruh Portofolio Kredit Hijau (Green Financing), Non-Performing Loan (NPL), dan Capital Adequacy Ratio (CAR) terhadap Profitabilitas (ROA) pada Bank KBMI 4 di Indonesia Periode 2021–2025"

**Institusi:** Universitas Kristen Krida Wacana (UKRIDA) — Fakultas Ekonomi dan Bisnis — Program Studi S1 Manajemen — Konsentrasi Manajemen Keuangan.

**Latar belakang:** Sejak POJK No. 51/POJK.03/2017 dan Taksonomi Hijau Indonesia, perbankan Indonesia (khususnya Bank KBMI 4) didorong menerapkan konsep Triple Bottom Line (Profit, People, Planet) melalui penyaluran Kredit Hijau (Green Financing). Riset ini menguji apakah kredit hijau menguntungkan atau justru membebani bank, dikombinasikan dengan faktor kesehatan bank klasik: risiko kredit (NPL) dan permodalan (CAR).

**Variabel & definisi operasional:**
- X1 = Green Financing/GF: porsi Kredit Hijau terhadap Total Kredit
- X2 = NPL: kredit macet terhadap total kredit
- X3 = CAR: modal bank terhadap ATMR
- Y = ROA: laba sebelum pajak terhadap total aset

**Hipotesis & hasil empiris (regresi data panel, 4 bank KBMI 4, periode 2021–2025):**
- H1: GF → ROA positif signifikan (β = +0,042; p = 0,0003)
- H2: NPL → ROA negatif signifikan (β = −0,385; p < 0,0001)
- H3: CAR → ROA positif signifikan (β = +0,074; p < 0,0001)
- H4 (simultan): F = 32,450; p < 0,0001; Adjusted R² = 70,2%

**Metodologi:** kuantitatif, data sekunder laporan keuangan/publikasi bank, purposive sampling, analisis regresi data panel (Common Effect / Fixed Effect / Random Effect, pemilihan model lewat Uji Chow, Uji Hausman, Uji LM), diikuti uji asumsi klasik dan uji t/uji F/R².

**Kesimpulan inti:** Ketiga hipotesis diterima — kredit hijau terbukti MENGUNTUNGKAN bank (mendukung Triple Bottom Line), NPL menurunkan profitabilitas, CAR memperkuat profitabilitas. Model menjelaskan 70,2% variasi ROA.

## Struktur file (buat persis seperti ini)

```
website/
├── index.html
├── css/style.css
└── js/script.js
```

## Halaman & section (index.html, satu halaman dengan smooth-scroll nav)

1. **Navbar fixed** — logo teks "GF·NPL·CAR→ROA" atau semacamnya, link anchor: Tentang, Variabel, Metodologi, Hasil, Kesimpulan, Kontak. Di mobile jadi hamburger menu (toggle JS).
2. **Hero** — judul skripsi sebagai headline besar, subjudul institusi (FEB UKRIDA, Manajemen Keuangan), badge/chip periode "2021–2025", badge "Regresi Data Panel", CTA button "Lihat Hasil Penelitian" (anchor ke #hasil). Background boleh gradient hijau gelap elegan.
3. **Tentang (#tentang)** — ringkasan latar belakang & research gap dalam 2–3 paragraf + kartu-kartu kecil (POJK 51/2017, Taksonomi Hijau Indonesia, Triple Bottom Line, Bank KBMI 4).
4. **Variabel & Hipotesis (#variabel)** — grid kartu untuk GF/X1, NPL/X2, CAR/X3, ROA/Y masing-masing dengan definisi operasionalnya, plus daftar H1–H4.
5. **Metodologi (#metodologi)** — timeline atau langkah bernomor: populasi & sampel (purposive sampling) → pemilihan model panel (Chow/Hausman/LM) → uji asumsi klasik → uji t/F/R².
6. **Hasil (#hasil)** — INI BAGIAN PALING PENTING:
   - Tabel/tampilan koefisien: GF +0,042 (p=0,0003), NPL −0,385 (p<0,0001), CAR +0,074 (p<0,0001).
   - **Bar chart horizontal yang DIGAMBAR MANUAL** — div dengan width persentase yang dianimasikan oleh JS saat masuk viewport (IntersectionObserver), warna hijau untuk positif, merah untuk negatif (pakai nilai absolut untuk lebar bar, tanda di label). JANGAN pakai canvas/chart library.
   - Kartu statistik besar dengan animasi count-up saat terlihat: Adj. R² = 70,2%, F-stat = 32,45, n observasi panel.
   - Interpretasi singkat per temuan.
7. **Kesimpulan (#kesimpulan)** — kesimpulan inti + keterbatasan singkat + saran.
8. **Footer/Kontak (#kontak)** — nama institusi, prodi, tahun 2026, catatan "Website portofolio penelitian".

## Desain

- Tema: hijau (green financing) + putih/abu netral, modern & bersih, tipografi sistem font stack biasa (system-ui, tanpa webfont eksternal).
- Fully responsive (mobile-first, breakpoint ±768px).
- Scroll reveal animation (fade/slide-up) via IntersectionObserver dengan class `.reveal`.
- Count-up animasi untuk angka statistik.
- Active nav link mengikuti section yang sedang dilihat.
- Aksesibilitas dasar: semantic HTML, alt/aria-label seperlunya, kontras cukup.

## Verifikasi wajib sebelum selesai

1. Pastikan ketiga file ada dan tidak kosong.
2. Jalankan `node --check js/script.js` untuk memvalidasi sintaks JS.
3. Buka index.html dan pastikan semua id anchor yang dirujuk navbar benar-benar ada (`grep 'id="' index.html`).
4. Laporkan struktur akhir file yang dibuat.
