# 🧠 PANDUAN PENGGUNAAN OBSIDIAN SECOND BRAIN SKRIPSI
### *Integrasi Antigravity IDE + Graphify + Obsidian Vault*

> [!SUMMARY] Tujuan & Solusi Catatan Ini
> - **Untuk Apa:** Panduan operasional bagi Arthur untuk memicu skill `obsidian-second-brain` di Antigravity, memanfaatkan integrasi Graphify, dan mengelola vault riset skripsi.
> - **Masalah yang Diselesaikan:** Memberikan petunjuk jelas bagaimana mahasiswa berinteraksi dengan AI asisten di awal sesi, saat bekerja, dan saat mengakhiri sesi bimbingan/analisis.
> - **Keputusan/Output:** Protokol 3 langkah: Mulai Sesi $\rightarrow$ Eksekusi Terhubung $\rightarrow$ Auto-Logging.

---

## ⚡ 1. Cara Memulai Sesi dengan Antigravity

Cukup ketik salah satu perintah berikut di chat Antigravity saat Anda membuka IDE:
* *"Mulai sesi"*
* *"Jalankan skill second brain"*
* *"Yuk lanjut skripsi"*

### Apa yang Otomatis Dilakukan Antigravity?
1. **Membaca Graphify:** Membaca `graphify-out/manifest.json` dan `graphify-out/GRAPH_REPORT.md` untuk memahami seluruh entitas skripsi, dependensi script `execution/`, dan variabel $Y, X_1, X_2, X_3, Z$.
2. **Membaca Dashboard Second Brain:** Membaca `[[00_DASHBOARD_SECOND_BRAIN.md]]` untuk mengetahui status naskah terbaru, catatan pembimbing, dan target kerja hari ini.
3. **Melaporkan Kesiapan:** Menyapa Anda dengan ringkasan status riset dan langsung siap mengeksekusi tugas.

---

## ✍️ 2. Cara Kerja Pencatatan Otomatis Selama Sesi

Setiap kali Anda meminta Antigravity membuat dokumen, merumuskan hipotesis, menganalisis jurnal, atau merevisi bab:

1. **Format Wajib Purpose-Driven:**
   Setiap catatan markdown baru otomatis diawali dengan blok ringkasan:
   ```markdown
   > [!SUMMARY] Tujuan & Solusi Catatan Ini
   > - **Untuk Apa:** ...
   > - **Masalah yang Diselesaikan:** ...
   > - **Keputusan/Output:** ...
   ```
2. **Penautan Otomatis (`[[...]]`):**
   Setiap nama variabel, nama teori, nama jurnal, atau nama dosen otomatis dihubungkan menggunakan tanda kurung siku ganda sehingga Graph View Obsidian Anda selalu terhubung.
3. **Auto-Logging ke Buku Harian Riset:**
   Setiap terobosan penting atau arahan bimbingan otomatis dicatat ke:
   `[[04_Riset_&_Metodologi/LOG_SESI_SECOND_BRAIN.md]]`.

---

## 🧭 3. Pusat Kendali (Map of Content)

Buka file **`[[00_DASHBOARD_SECOND_BRAIN.md]]`** di Obsidian sebagai "beranda" utama Anda. Dari sana, Anda dapat melompat ke:
- Naskah LaTeX & PDF: `[[01_Naskah_Utama/Proposal_Arthur_PokemonTCG.pdf]]`
- Varian Tanpa Bab 3: `[[01_Naskah_Utama/Proposal_Arthur_NoBab3.pdf]]`
- Panduan Belajar Sidang: `[[02_Persiapan_Sidang/PANDUAN_BELAJAR_PROPOSAL.md]]`
- Bank Soal Sulit Penguji: `[[02_Persiapan_Sidang/01_Bank_Soal_&_Flashcard/03_PERTANYAAN_SIDANG_SULIT.md]]`
- Katalog 10 Jurnal Empiris: `[[06_Referensi_Jurnal_PDF/KATALOG_REFERENSI_JURNAL.md]]`
- Log Sesi Riset: `[[04_Riset_&_Metodologi/LOG_SESI_SECOND_BRAIN.md]]`

---
*Kini Obsidian dan Antigravity Anda telah resmi bersinergi sebagai Otak Kedua yang cerdas dan otomatis!* 🚀
