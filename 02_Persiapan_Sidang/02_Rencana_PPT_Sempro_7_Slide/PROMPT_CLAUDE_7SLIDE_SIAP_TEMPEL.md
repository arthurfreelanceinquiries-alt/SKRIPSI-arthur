# 📋 PROMPT SIAP TEMPEL UNTUK CLAUDE — PLAN PEMBUATAN PPT 7 SLIDE

> Salin seluruh isi blok `text` di bawah dan tempel ke Claude. Dokumen ini sudah dikoreksi terhadap naskah (6 hipotesis, sampel 120–150, tanpa klaim paylater).

```text
Halo Claude! Anda adalah Senior Presentation Designer + Academic Coach untuk sidang skripsi S1 Manajemen Keuangan FEB UKRIDA. Buatkan saya deck Seminar Proposal TEPAT 7 SLIDE, format 16:9, tema FinTech Dark Mode (bg #0B0F19, kartu #1E293B border #334155, teks #F8FAFC, aksen cyan #06B6D4 / emerald #10B981 / amber #F59E0B). NO wall of text (maks 3 baris per kartu), istilah asing selalu italic, dan WAJIB speaker notes ±1-1,5 menit per slide.

DATA KUNCI (dilarang diubah):
- Judul: Pengaruh Hedonic Motivation (X1), Desire for Completeness (X2), dan Speculative Motive (X3) terhadap Impulsive Buying (Y) Booster Pack Kartu Pokémon TCG dengan Self-Control (M) sebagai Variabel Moderasi
- Peneliti: Arthur Reezan (NIM: 312023002). Pembimbing: Dr. Fredella Colline, S.E., M.M., CFP®, PFM, CHCP-A. FEB UKRIDA, Jakarta 2026.

ATURAN ANTI-HALUSINASI (pelanggaran = deck ditolak):
1. TEPAT 6 HIPOTESIS (H1-H3 positif; H4-H6 moderasi melemah). DILARANG membuat H7. DILARANG menggambar panah langsung M -> Y sebagai hipotesis.
2. Sampel: kolektor WNI populasi infinite, purposive, target N = 120-150 (+ pilot n = 30). DILARANG menulis "Jabodetabek saja" atau "N >= 150".
3. DILARANG mengklaim dana darurat/paylater — tidak ada di naskah. Gunakan "berpotensi mengorbankan alokasi keuangan pribadi".
4. Hanya sitasi yang ada di naskah: Behavioral Finance (Simon 1955; Kahneman & Tversky 1979; Shiller 2000; Thaler & Shefrin 1981), S-O-R (Mehrabian & Russell 1974), Gao (2014), Barasz et al. (2017), Tangney et al. (2004), Baumeister (2002), IBTS Verplanken & Herabadi (2001), Arnold & Reynolds (2003), Keynes (1936). DILARANG menambah sumber (mis. Shefrin 2000).
5. Ambang yang boleh tampil: Alpha >= 0,70; r-hitung > r-tabel; Tolerance > 0,10 & VIF < 10; KS & Glejser p > 0,05; uji-t/F p < 0,05.

ISI 7 SLIDE:
- S1 Pembuka: badge SEMINAR PROPOSAL SKRIPSI S1 MANAJEMEN KEUANGAN + judul + nama/NIM + pembimbing + footer FEB UKRIDA 2026. Notes: salam + perkenalan (~45 detik).
- S2 Fenomena (3 kartu): > 64,8 miliar kartu global (The Pokemon Company, 2024) | blind-pack Rp20-30 ribu isi acak, kartu SAR/PSA 10 jutaan rupiah | impulsive buying berulang tanpa anggaran. Notes: mainan -> komoditas investasi (~1,5 mnt).
- S3 Gap & novelty (2 kolom): kiri 3 gap (hedonis diperdebatkan di produk mahal; pseudo-set belum diuji di kartu Indonesia; FOMO kolektor vs investor hati-hati); kanan 3 novelty (3 anteseden sekaligus; M sebagai rem; pionir kartu berbahasa Indonesia). Notes: tekankan inkonsistensi (~1,5 mnt).
- S4 Teori & variabel: grand theory + 3 supporting; 5 kartu Y/X1/X2/X3/M beserta skala baku (IBTS; Arnold & Reynolds 5 dimensi adaptasi; Gao/Barasz; Keynes/Shiller; BSCS Tangney). Notes: sebut "sesuai konsentrasi Manajemen Keuangan" (~1,5 mnt).
- S5 Model & hipotesis: diagram jalur (3 panah + ke Y; 3 panah putus-putus M melemah) + daftar H1-H6. Notes: sebutkan M masuk Model 1 hanya sebagai kontrol baseline, bukan hipotesis (~1,5 mnt).
- S6 Metode (4 kuadran): desain cross-sectional Likert 5 | sampel seperti aturan-2 | uji kualitas+asumsi seperti aturan-5 | MRA mean-centering Model 1->2, uji-t/F, delta-R2 + F-change, simple slopes. Notes: purposive, N, validitas, mean-centering (~1,5 mnt).
- S7 Penutup: kontribusi teoretis (Behavioral Finance aset hobi) + praktis (edukasi kontrol diri generasi muda) + "Terima kasih — sesi tanya jawab dibuka" + identitas. Notes: santun, kembalikan ke Ketua Sidang (~30 detik).

OUTPUT: kode python-pptx siap jalan (16:9, editable, speaker notes tertanam) ATAU HTML slide tunggal. Setelah jadi, lakukan SELF-CHECK dan laporkan: (a) jumlah slide = 7, (b) jumlah hipotesis = 6, (c) tidak ada klaim paylater/dana darurat/Jabodetabek-only/H7/Shefrin-2000, (d) semua istilah asing italic.
```

---

## 📎 Lampiran untuk Claude (opsional, bila ia meminta detail)

- Alur cerita + naskah bicara lengkap: `ALUR_PRESENTASI_7_SLIDE_DETAIL.md` (file sebelah ini).
- Spesifikasi teknis + palet + template kode: `IMPLEMENTATION_PLAN_PPT_SEMPRO_7_SLIDE.md`.
- Spesifikasi dosen (sumber): `PRD_PPT_SEMPRO_7_SLIDE.md`.
