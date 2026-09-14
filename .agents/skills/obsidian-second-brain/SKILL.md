---
name: obsidian-second-brain
description: >
  Mengaktifkan protokol Obsidian Second Brain untuk riset skripsi dan personal knowledge management.
  Melakukan pembacaan status graphify dan dashboard pada awal sesi, menegakkan format catatan
  purpose-driven (> [!SUMMARY]), menghubungkan ide dengan bidirectional links [[...]],
  serta otomatis mencatat setiap keputusan penting, arahan bimbingan dosen, dan solusi ke dalam Obsidian.
  Aktifkan ketika user meminta "jalankan skill", "mulai sesi", "catat ke obsidian", atau saat mengelola
  vault Obsidian skripsi.
---

# Obsidian Second Brain Skill: Skripsi & PKM Architecture

Skill ini mengubah vault Obsidian pada repositori skripsi menjadi **Otak Kedua (*Second Brain*)** yang hidup, terstruktur, dan terintegrasi secara otomatis dengan Antigravity dan Graphify.

---

## 🚀 1. Protokol Awal Sesi (Session Start / Pre-Flight Hook)

Setiap kali pengguna memulai sesi baru atau meminta *"jalankan skill second brain"* / *"mulai sesi"*, agen **WAJIB** menjalankan urutan 3 langkah pre-flight berikut sebelum mengeksekusi pekerjaan:

### Langkah 1: Sinkronisasi Pengetahuan dengan Graphify
- Periksa keberadaan direktori `graphify-out/` di workspace.
- Baca `graphify-out/manifest.json` atau `graphify-out/GRAPH_REPORT.md` untuk memahami:
  - Struktur komunitas entitas terkini (God Nodes, cluster variabel $Y, X_1, X_2, X_3, Z$).
  - Dependensi antar file (skrip di `execution/`, panduan di `directives/`, dan naskah di `01_Naskah_Utama/`).
- Jika terdapat pertanyaan terkait arsitektur atau relasi antar file, jadikan data graphify sebagai rujukan utama.

### Langkah 2: Baca Kokpit Dashboard Second Brain
- Baca file `00_DASHBOARD_SECOND_BRAIN.md` di root workspace untuk memuat:
  - Status aktif skripsi (Bab 1, Bab 2, Bab 3, dan naskah varian).
  - Peta variabel penelitian dan skala pengukurannya.
  - Catatan revisi dosen terakhir yang belum tuntas.
  - Target fokus sesi yang sedang berjalan.

### Langkah 3: Konfirmasi Kesiapan ke Pengguna
- Sampaikan salam pembuka ringkas yang memuat:
  - Status pengetahuan sistem (Graphify terhubung, Dashboard terbaca).
  - Agenda/target yang siap dieksekusi pada sesi tersebut.

---

## 📝 2. Protokol Dokumentasi Catatan (In-Flight Rules)

Setiap kali membuat catatan baru atau memperbarui dokumen markdown di Obsidian, patuhi aturan baku berikut:

### A. Wajib Callout `> [!SUMMARY]` di Bagian Paling Atas
Setiap catatan kerja, PRD, kajian teori, atau catatan bimbingan **HARUS** memiliki ringkasan tujuan pada 2–4 baris pertama menggunakan Obsidian Callout:

```markdown
> [!SUMMARY] Tujuan & Solusi Catatan Ini
> - **Untuk Apa:** [Tujuan pembuatan dokumen / pekerjaan ini]
> - **Masalah yang Diselesaikan:** [Pertanyaan dosen / kendala metodologis / celah yang diatasi]
> - **Keputusan/Output:** [Keputusan akhir, rumus yang dipilih, atau file output terkait]
```

### B. Terapkan Bidirectional Linking (`[[...]]`)
Jangan biarkan sebuah konsep terisolasi. Selalu hubungkan dengan entitas terkait:
- Hubungkan variabel ke teorinya: `[[Desire for Completeness]]` $\rightarrow$ `[[Zeigarnik Effect]]` dan `[[Barasz et al. 2017]]`.
- Hubungkan pengujian ke skripnya: `[[MRA]]` $\rightarrow$ `[[execution/build_proposal_word.py]]`.
- Hubungkan revisi ke dosennya: `[[Dr. Fredella Colline]]`.

### C. Tiga Kategori Catatan (The 3 Note Types)
1. **Fleeting / Log Notes:** Catatan mentah obrolan bimbingan di `07_Review_&_Audit/Revisi_Dosen/`.
2. **Literature Notes:** Bedah 1 artikel jurnal atau 1 bab buku di `06_Referensi_Jurnal_PDF/`.
3. **Atomic Notes:** 1 konsep/variabel mandiri di `04_Riset_&_Metodologi/` atau subfolder terkait.

---

## 💾 3. Protokol Pencatatan Otomatis (Auto-Capture & Session End)

Setiap kali terjadi perkembangan penting selama sesi kerja (misalnya: revisi naskah disetujui, rumus baru ditentukan, jurnal baru dianalisis, atau keputusan metodologi diambil):

### Langkah Auto-Logging:
1. **Catat ke Log Sesi:** Buka `04_Riset_&_Metodologi/LOG_SESI_SECOND_BRAIN.md` dan tambahkan entri baru:
   ```markdown
   ### 📅 Sesi: [Tanggal & Waktu]
   - **Fokus Pekerjaan:** [Apa yang dikerjakan]
   - **Masalah yang Diselesaikan:** [Solusi apa yang dicapai]
   - **Keputusan / Insight:** [Keputusan penting yang diambil]
   - **File yang Diperbarui:** [[file-1]], [[file-2]]
   ```
2. **Update Dashboard:** Jika ada perubahan status penting, sinkronkan checklist pada `00_DASHBOARD_SECOND_BRAIN.md`.
3. **Peringatan Sinkronisasi Graphify:** Jika ada penambahan banyak file baru atau perubahan arsitektur besar, ingatkan atau jadwalkan pembaruan graphify.

---

## 🛠️ 4. Panduan Eksekusi Teknis (3-Layer Architecture)

- **Layer 1 (Directives):** Prosedur dan SOP skripsi berada di `directives/*.md`.
- **Layer 2 (Orchestration):** AI Agent mengatur alur kerja, membaca dashboard, dan mencatat ke Obsidian.
- **Layer 3 (Execution):** Skrip otomasi di `execution/*.py` bertugas mengompilasi PDF, memvalidasi referensi, dan mengekstrak data secara deterministik.
