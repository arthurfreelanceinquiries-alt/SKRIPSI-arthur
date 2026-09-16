# Directive: Prosedur Audit Ilmiah Proposal & Skripsi dengan `paper-audit`

> [!SUMMARY] Tujuan & Solusi Directive Ini
> - **Untuk Apa:** Menjadi Standard Operating Procedure (SOP) resmi untuk menjalankan audit ilmiah komprehensif (*scientific peer review*) menggunakan skill `paper-audit` pada naskah proposal dan skripsi Arthur.
> - **Masalah yang Diselesaikan:** Menghilangkan kebingungan kapan audit harus dijalankan, mencegah *false alarm* terhadap aturan institusional lokal FEB UKRIDA, serta membakukan format laporan temuan agar langsung dapat ditindaklanjuti.
> - **Keputusan/Output:** Ditetapkan sebagai prosedur **Tier-3 Gated Audit** (Pra-Bimbingan, Pra-Sidang, Pasca-Revisi Mayor, dan On-Demand). Laporan disimpan di `07_Review_&_Audit/Paper_Audits/`.

---

## 1. Otoritas & Kebijakan Aktivasi (Activation Triggers)

Skill `paper-audit` **TIDAK** dijalankan pada setiap perubahan baris kode/teks (*not per-edit*). Skill ini hanya dipicu pada tonggak pencapaian (*milestones*) tertentu:

1. **Trigger A (Pra-Bimbingan Dosen / Pre-Advisory):**
   - Sebelum Arthur mengirimkan draf naskah ke Dosen Pembimbing ([[Dr. Fredella Colline]]).
   - Fokus: Menemukan celah logika kausalitas, kelemahan justifikasi kriteria inklusi, dan inkonsistensi sitasi.
2. **Trigger B (Pra-Seminar Proposal / Pre-Defense):**
   - Sebelum naskah diserahkan ke bagian Tata Usaha FEB UKRIDA untuk pendaftaran seminar proposal.
   - Fokus: Simulasi pertanyaan kritis penguji, uji asumsi model MRA, dan kepatuhan absolut pedoman UKRIDA 2023.
3. **Trigger C (Pasca Perombakan Struktur / Major Rewrite):**
   - Setelah modifikasi besar pada variabel, instrumen kuesioner, atau rekonstruksi persamaan regresi.
4. **Trigger D (Verifikasi Resolusi Revisi):**
   - Menguji apakah butir-butir masukan bimbingan/review sebelumnya sudah tuntas diselesaikan atau masih menyisakan anomali.
5. **Trigger E (Instruksi Eksplisit User):**
   - Kapan pun Arthur meminta: *"Jalankan audit naskah dengan paper-audit"*.

---

## 2. Pengecualian & Penyelarasan Lokal (Context Anchors)

Saat mengevaluasi naskah, agen **WAJIB** memperhitungkan ketetapan metodologis yang telah terkunci di [[04_Riset_&_Metodologi/SOURCE_OF_TRUTH.md]] dan [[05_Pedoman_&_Referensi/Buku Pedoman Penyusunan Tugas Akhir 2023.md]]:

1. **Sitasi Dosen (K-04 UKRIDA):**
   - Sitasi terhadap Dr. Fredella Colline (2024) adalah pemenuhan kewajiban administratif universitas, bukan *citation bias*.
2. **Model Aditif Baseline MRA (D20):**
   - Spesifikasi Model 1 menyertakan pemoderasi $M^*$ bersama variabel independen ($X_1^*, X_2^*, X_3^*, M^*$) agar Model 2 MRA Penuh murni mengisolasi peningkatan daya penjelas 3 istilah interaksi moderasi ($\Delta R^2$). Ini adalah desain ekonometrika yang benar, bukan redundansi.
3. **Pemusatan Rata-Rata (*Mean-Centering*):**
   - Variabel prediktor interaksi menggunakan $X^* = X - \bar{X}$ untuk mereduksi multikolinearitas non-esensial. Ini bukan standarisasi z-score.
4. **Dasar Hukum Batas Usia 17 Tahun (D20):**
   - Menggunakan UU No. 24 Tahun 2013 tentang Administrasi Kependudukan (KTP) dan diskresi finansial mandiri, bukan KUHPerdata Pasal 330.
5. **Status Proposal (Belum Ada Data Lapangan):**
   - Sesuai `references/thesis.md`, jangan menuntut hasil uji regresi empiris aktual, angka output SPSS riil, atau temuan lapangan pada dokumen proposal. Proposal dinilai dari kelayakan rancangan (*planned design & feasibility*).

---

## 3. Alur Kerja Eksekusi 5 Langkah (The 5-Step Audit Workflow)

```
[ Step 1: Pre-Scan Heuristik ] ──► python scripts/proofing_scan.py
              │
              ▼
[ Step 2: Pemetaan Bukti ] ─────► Petakan Fenomena -> Gap -> Hipotesis -> Indikator -> MRA
              │
              ▼
[ Step 3: Multi-Role Review ] ──► (A) Methods/Stats  (B) Technical/Math  (C) Claims/Literature
              │
              ▼
[ Step 4: Challenger Pass ] ────► Uji validitas temuan; eliminasi false alarms
              │
              ▼
[ Step 5: Laporan & Log ] ──────► Buat 07_Review_&_Audit/Paper_Audits/review-YYYY-MM-DD-HHMMSS.md
```

### Langkah 1: Pre-Scan Cepat (Layer 3)
Jalankan skrip proofing heuristik terhadap berkas naskah markdown atau PDF:
```powershell
python ".agents/skills/paper-audit/scripts/proofing_scan.py" "01_Naskah_Utama/PROPOSAL_SKRIPSI_POKEMON_TCG.md"
```

### Langkah 2: Pemetaan Klaim ke Bukti (*Claims-to-Evidence Mapping*)
Periksa keselarasan antara:
- Fenomena lonjakan pasar TCG $\rightarrow$ Rumusan Masalah (3 butir) $\rightarrow$ Tujuan Penelitian (3 butir).
- Teori Utama (*Behavioral Finance*, S-O-R, *Zeigarnik Effect*, *Self-Regulation*) $\rightarrow$ Definisi Operasional $\rightarrow$ Butir Tabel 3.2.

### Langkah 3: Audit Spesialis (Multi-Perspective Check)
- **Perspektif 1 (Metodologi & Sampling):** Kriteria inklusi, penentuan ukuran sampel Cohen/Green (120–150 responden), komparasi *purposive sampling*, dan prosedur kuesioner.
- **Perspektif 2 (Ekonometrika & Notasi Matematika):** Persamaan MRA Model 1 & 2, notasi *mean-centering*, rumus uji F, dan pengujian asumsi klasik.
- **Perspektif 3 (Literatur & Sitasi):** 10 jurnal empiris utama (2021–2025), konsistensi gap, format APA 7th tanpa nomor urut, serta kepatuhan 7 pilar UKRIDA 2023.

### Langkah 4: Pengujian Penantang (*Challenger Pass*)
Buka kembali kutipan asli naskah untuk setiap temuan:
- Apakah konteks di bab lain sudah menjawab kritik tersebut?
- Apakah temuan ini merupakan *Necessary Correction*, *Feasible Strengthening*, atau sekadar saran *Future Work*?
- Jika kritik terbukti keliru atau merupakan *over-engineering* jenjang S1, turunkan atau hapus temuan.

### Langkah 5: Penerbitan Laporan & Auto-Logging
1. Tuliskan laporan audit ke berkas baru:
   `07_Review_&_Audit/Paper_Audits/review-YYYY-MM-DD-HHMMSS.md`
2. Gunakan format tabel temuan resmi:
   | ID | Tingkat (*Severity*) | Klasifikasi | Lokasi | Temuan & Bukti | Dampak | Rekomendasi Perbaikan |
3. Catat ringkasan hasil audit ke [[04_Riset_&_Metodologi/LOG_SESI_SECOND_BRAIN.md]] dan perbarui [[00_DASHBOARD_SECOND_BRAIN.md]].

---

## 4. Format Keluaran Temuan (Finding Contract)

Setiap temuan yang dimasukkan ke dalam laporan akhir wajib memiliki struktur:
* **ID:** Format `F001`, `F002`, dst.
* **Tingkat Keparahan (*Severity*):**
  - **Critical:** Cacat fatal yang membatalkan validitas riset (misal: variabel di model tidak ada di kuesioner, persamaan matematika salah total).
  - **Major:** Inkonsistensi metodologi, kontradiksi sitasi gap, atau pelanggaran syarat kelulusan UKRIDA.
  - **Minor:** Perbaikan editorial, istilah yang kurang presisi, atau perapian tabel/diagram.
* **Klasifikasi Bukti:**
  - `Definite error` (kesalahan nyata terbukti).
  - `Unsupported claim` (klaim tidak didukung bukti/teori memadai).
  - `Likely issue` (berpotensi bermasalah di mata penguji).
  - `Needs verification` (membutuhkan konfirmasi dari dosen pembimbing).
