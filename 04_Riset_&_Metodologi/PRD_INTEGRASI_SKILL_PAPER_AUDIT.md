# 📋 PRD: Integrasi & Tata Kelola Skill `paper-audit` pada Ekosistem Skripsi

> [!SUMMARY] Tujuan & Solusi Catatan Ini
> - **Untuk Apa:** Menetapkan arsitektur integrasi, peran, batasan, dan protokol aktivasi (*activation gating*) untuk skill baru `paper-audit` di dalam ekosistem skripsi Pokémon TCG Arthur.
> - **Masalah yang Diselesaikan:** Menjawab secara definitif apakah skill harus dijalankan pada setiap perubahan (mencegah *token exhaustion*, *latency lag*, dan *alert fatigue*), sekaligus menyelaraskan rubric evaluasi ilmiah internasional dengan standar lokal *Buku Pedoman Penyusunan Tugas Akhir FEB UKRIDA 2023*.
> - **Keputusan/Output:** Skill `paper-audit` **TIDAK** dijalankan pada setiap perubahan kecil (*per-edit*), melainkan ditetapkan sebagai **Tier-3 Milestone / Gated Audit** (Pra-Bimbingan, Pra-Sidang, Pasca-Revisi Besar, dan On-Demand).

---

## 1. Latar Belakang & Analisis Skill `paper-audit`

Skill `paper-audit` (`.agents/skills/paper-audit/`) adalah mesin audit ilmiah komprehensif (*scientific peer-review engine*) independen yang dirancang untuk menguji keabsahan klaim, metodologi, kalkulasi angka, sitasi, dan konsistensi naskah akademik (skripsi/proposal/jurnal).

### 1.1 Komponen & Kapabilitas Inti `paper-audit`
1. **Rubrik Evaluasi Akademik (`references/review-rubric.md`):**
   - Menelusuri rantai logika ilmiah: *Fenomena $\rightarrow$ Rumusan Masalah $\rightarrow$ Teori $\rightarrow$ Model Penelitian $\rightarrow$ Operasionalisasi $\rightarrow$ Metodologi Sampling & MRA $\rightarrow$ Kesimpulan*.
   - Menguji batasan kausalitas (*causal language check*), kelayakan estimand statistik, dan keabsahan klaim novelty.
2. **Profil Khusus Skripsi / Proposal (`references/thesis.md`):**
   - Menyesuaikan ekspektasi akademik dengan jenjang S1 (Undergraduate).
   - Membedakan temuan secara tegas:
     - **Necessary Correction:** Cacat fatal/inkonsistensi metodologis yang wajib diperbaiki.
     - **Feasible Strengthening:** Penguatan yang realistis dalam batas waktu & kapasitas S1.
     - **Future Work:** Saran pengembangan yang tidak wajib dieksekusi sekarang.
   - Tidak menuntut data empiris selesai jika naskah masih berstatus *Proposal*.
3. **Kontrak Bukti & Klasifikasi Temuan (`references/findings-and-evidence.md`):**
   - Severity: **Critical**, **Major**, **Minor**.
   - Classification: **Definite error**, **Unsupported claim**, **Likely issue**, **Needs verification**.
   - Mengharuskan bukti verbatim (*quote/equation/table number*), dampak akademik, dan solusi terkecil (*smallest adequate fix*).
4. **Orkestrasi Multi-Peran / Specialist (`references/orchestration.md`):**
   - Menjalankan analisis terspesialisasi (Methods/Statistics, Technical/Math, Claims/Citations) yang dilanjutkan dengan peran penantang (*challenger*) untuk mengeliminasi kritik keliru (*false alarms*), sebelum dihakimi (*adjudicated*) oleh root agent.
5. **Skrip Proofing Deterministik (`scripts/proofing_scan.py`):**
   - Skrip Python cepat untuk mendeteksi tanda baca ganda, kapitalisasi pustaka pemrograman, dan rasio $\arctan$ pada teks `.tex`, `.md`, `.bib`, dan `.pdf`.

---

## 2. Analisis Kritis: Apakah Harus Dinyalakan Setiap Ada Perubahan?

### ❌ Keputusan Definitif: **TIDAK PADA SETIAP PERUBAHAN (NOT PER-EDIT)**

Menjalankan `paper-audit` pada setiap modifikasi kecil (misalnya koreksi typo kata, perubahan indentasi DOCX, perbaikan nomor tabel, atau penyesuaian CSS) adalah **tindakan kontra-produktif dan keliru secara arsitektur**.

### 2.1 Alasan Teknis & Metodologis

| Aspek | Jika Dijalankan Tiap Perubahan (Per-Edit) | Pendekatan Gated / Milestone (Direkomendasikan) |
|---|---|---|
| **Konsumsi Token & Biaya** | ❌ Sangat boros (membaca ulang 54 halaman PDF/LaTeX, memetakan claim ledger, multi-role review tiap ketukan edit). | ✅ Efisien, token difokuskan pada tahap krusial di mana keputusan besar telah terakumulasi. |
| **Latensi & Kecepatan Kerja** | ❌ Menimbulkan waktu tunggu 1–3 menit setiap kali agent ingin menyelesaikan tugas kecil. | ✅ Eksekusi cepat; tugas kecil selesai dalam hitungan detik. |
| **Spam / Polusi Vault** | ❌ Sesuai klausul `paper-audit`, setiap audit substantial membuat berkas `paper-reviews/review-YYYY-MM-DD-HHMMSS.md`. Vault akan dibanjiri ratusan berkas review usang. | ✅ Laporan tersimpan rapi, bermakna, dan memiliki tanggal tonggak sejarah riset yang jelas. |
| **Noise & Alert Fatigue** | ❌ Memunculkan kembali peringatan-peringatan yang sedang dalam proses pengerjaan bertahap. | ✅ Ulasan menyeluruh dilakukan saat draf sudah berada pada kondisi stabil (*freeze*). |
| **Kesesuaian Filosofi Skill** | ❌ Melanggar aturan `SKILL.md` baris 3 & 14: *"ordinary summarization and writing from scratch do not require this skill. A narrowly scoped request stays narrow."* | ✅ Selaras dengan tujuan asli perancangan `paper-audit`. |

---

## 3. Kebijakan Aktivasi Bertingkat (3-Tier Governance Matrix)

Untuk menjaga kualitas naskah setara standar publikasi tanpa memperlambat ritme penulisan, ekosistem skripsi Arthur membagi evaluasi ke dalam 3 Tingkatan:

```
┌────────────────────────────────────────────────────────────────────────┐
│ TIER 1: CONTINUOUS VERIFICATION (Setiap Perubahan / In-Flight)         │
│ - Eksekusi skrip deterministik Python Layer 3 (< 2 detik, 0 token)     │
│ - verify_docx_typography.py | verify_ukrida_compliance.py             │
│ - verify_pdf_docx_parity.py | verify_word_outline.py                   │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ TIER 2: HEURISTIC PROOFING (Pra-Kompilasi / Batch Edit)                │
│ - proofing_scan.py (Pemeriksaan tanda baca, inkonsistensi teks ringan)  │
│ - Pemeriksaan referensi hilang via BibTeX engine                       │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ TIER 3: GATED PAPER-AUDIT (Milestone Tertentu / Freeze Draft)          │
│ - Deep Scientific Audit (Claim-to-Evidence, Metodologi MRA, S-O-R)     │
│ - Multi-Agent / Specialist Orchestration & Challenger Pass             │
│ - Output Laporan Resmi: 07_Review_&_Audit/Paper_Audits/                │
└────────────────────────────────────────────────────────────────────────┘
```

### 3.1 Kapan Tier 3 (`paper-audit`) Wajib Dijalankan? (Trigger Events)
1. **Milestone 1: Pra-Bimbingan Dosen (Pre-Advisory Audit):**
   - Dijalankan sebelum Arthur mengirimkan draf ke Ibu [[07_Review_&_Audit/Revisi_Dosen/|Dr. Fredella Colline]].
   - Tujuan: Menemukan kelemahan metodologi, celah logika kausalitas, atau sitasi sebelum dikritik dosen.
2. **Milestone 2: Pra-Pendaftaran Seminar Proposal (Pre-Sempro / Pre-Defense):**
   - Dijalankan saat naskah proposal dinyatakan "final" untuk pendaftaran sidang.
   - Tujuan: Simulasi pengujian eksternal independen guna memastikan naskah kebal dari pertanyaan jebakan penguji.
3. **Milestone 3: Pasca Perombakan Struktur / Hipotesis Mayor:**
   - Dijalankan jika terjadi penambahan/pengubahan variabel, rekonstruksi rumus MRA, atau perubahan instrumen kuesioner.
4. **Milestone 4: Verifikasi Pasca-Revisi (Revision Resolution Audit):**
   - Menggunakan mode komparasi `paper-audit` untuk memastikan catatan bimbingan dosen atau review sebelumnya telah teratasi 100% tanpa menyisakan regresi.
5. **Milestone 5: On-Demand:**
   - Dijalankan saat pengguna memberikan instruksi eksplisit: *"Jalankan audit naskah proposal dengan paper-audit"*.

---

## 4. Penyelarasan dengan Pedoman FEB UKRIDA 2023

`paper-audit` memiliki standar umum internasional. Agar hasil audit tidak menghasilkan *false positive* terhadap tradisi lokal kampus, integrasi wajib mengunci parameter lokal:

1. **Pedoman Formal:** Wajib merujuk pada [[05_Pedoman_&_Referensi/Buku Pedoman Penyusunan Tugas Akhir 2023.md|Buku Pedoman Penyusunan Tugas Akhir FEB UKRIDA 2023]].
2. **Aturan Sitasi Dosen (K-04):** Wajib memperhitungkan sitasi karya dosen pembimbing ([[Dr. Fredella Colline]]) sebagai pemenuhan syarat kelulusan formal, bukan sebagai *citation bias*.
3. **Model Ekonometrika MRA (D20):** Evaluasi harus memahami bahwa Model 1 sengaja dirancang sebagai Model Aditif Baseline ($X_1, X_2, X_3, M$) dan Model 2 sebagai Model Interaksi Moderasi Penuh dengan teknik *mean-centering* ($X^* = X - \bar{X}$).
4. **Format Dokumen:** Standar naskah fisik UKRIDA 2023 mensyaratkan margin 4-4-3-3 cm, Daftar Pustaka format APA tanpa nomor urut urutan angka, dan tata letak tabel APA 7th edition (tanpa garis vertikal).

---

## 5. Arsitektur 3-Layer untuk Integrasi `paper-audit`

Sesuai aturan baku sistem:
* **Layer 1 (Directives):**
  - Membuat berkas petunjuk resmi: `directives/run_paper_audit.md`.
  - Mendefinisikan kapan audit dipanggil, berkas mana yang menjadi input utama (`Proposal_Arthur_PokemonTCG.pdf` / `.tex`), di mana laporan disimpan, dan bagaimana memilah temuan UKRIDA vs standar umum.
* **Layer 2 (Orchestration):**
  - AI Agent mengelola pemanggilan peran spesialis, memicu *challenger pass*, dan menyintesis temuan ke dalam format laporan terstruktur.
  - Memutakhirkan [[00_DASHBOARD_SECOND_BRAIN.md]] dan [[04_Riset_&_Metodologi/LOG_SESI_SECOND_BRAIN.md]].
* **Layer 3 (Execution):**
  - Menggunakan skrip deterministik `scripts/proofing_scan.py` untuk pemeriksaan awal.
  - Skrip pendukung verifikasi deterministik yang sudah ada di `execution/` tetap bertindak sebagai benteng pertahanan kualitas harian.
* **Lokasi Penyimpanan Laporan:**
  - Mengikuti struktur folder repositori, laporan audit akan disimpan di:
    `07_Review_&_Audit/Paper_Audits/review-YYYY-MM-DD-HHMMSS.md`
    (dengan tautan bidirectional langsung di Dashboard).

---

## 6. Kriteria Keberhasilan (Success Metrics)

1. **Zero False Friction:** Tidak ada keterlambatan kerja pada pengeditan harian/rutin; alur penulisan tetap tangkas (*agile*).
2. **Defensible Thesis:** Sebelum bimbingan atau seminar, naskah telah melewati audit Tier 3 dengan temuan *Critical* = 0 dan temuan *Major* terselesaikan atau memiliki justifikasi tertulis.
3. **Paritas & Ketertelusuran:** Setiap laporan audit memiliki daftar ID temuan (`F001`, `F002`, dst.) yang dapat dilacak status penyelesaiannya pada log sesi berikutnya.
