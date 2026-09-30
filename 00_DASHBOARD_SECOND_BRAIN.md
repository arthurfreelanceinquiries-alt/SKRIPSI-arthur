# 🧠 DASHBOARD SECOND BRAIN — SKRIPSI POKÉMON TCG
### *S1 Manajemen Keuangan — Fakultas Ekonomi dan Bisnis — Universitas Kristen Krida Wacana (UKRIDA)*

> [!SUMMARY] Tujuan & Solusi Catatan Ini
> - **Untuk Apa:** Kokpit utama (*Master Dashboard / Map of Content*) untuk mengelola seluruh ekosistem riset skripsi, catatan teori, data empiris, dan persiapan sidang di Obsidian.
> - **Masalah yang Diselesaikan:** Menghilangkan fragmentasi catatan; menghubungkan seluruh naskah LaTeX, draf markdown, jurnal referensi, dan panduan belajar ke dalam satu pusat navigasi interaktif.
> - **Keputusan/Output:** Digunakan oleh Antigravity dan pengguna pada setiap awal sesi kerja untuk sinkronisasi konteks instan bersama Graphify.

---

## 📌 1. Identitas & Parameter Kunci Riset

* **Topik Skripsi:**  
  *Pengaruh Hedonic Motivation ($X_1$), Desire for Completeness ($X_2$), dan Speculative Motive ($X_3$) terhadap Impulsive Buying ($Y$) Booster Pack Kartu Pokémon TCG dengan Self-Control ($Z$) sebagai Variabel Moderasi (Studi pada Konsumen di Jakarta Barat).*
* **Dosen Pembimbing:** [[07_Review_&_Audit/Revisi_Dosen/|Dr. Fredella Colline, S.E., M.M., CFP®, PFM, CHCP-A]]
* **Metodologi Analisis:** Kuantitatif Asosiatif, Survei Kros-Seksional, *Moderated Regression Analysis (MRA)* dengan *Mean-Centering*.
* **Status Naskah Terkini (revisi Sylvia 23 Sep 2026 & Bimbingan 29 Sep 2026):**
  - Naskah Utama Lengkap: [[01_Naskah_Utama/Proposal_Arthur_PokemonTCG.pdf|Proposal_Arthur_PokemonTCG.pdf]] (51 halaman settled pasca revisi Sempro 29 Sep 2026; frontmatter Cover i + TOC ii–iii + LOT iv + LOF v [5 hal]; Bab 1–3 + DP arab 1–46 [46 hal]; Alpha 0,70; 54 entri referensi paritas 5-arah 100% PASS; gerbang extended 11/11 PASS mutlak (Gate G8 Paritas Italic 100.00%))
  - Varian Tanpa Bab 3: DIHAPUS 23 Sep 2026 atas arahan Sylvia — semua mengerucut ke file utama (skrip `build_proposal_nobab3_pdf.py`/`verify_nobab3_pdf.py` dan gerbang X2 ikut dihapus; paritas kini 5-arah)
  - Dokumen Word Hybrid (Native TOC Word/Docs): [[01_Naskah_Utama/Proposal_Arthur_PokemonTCG.docx|Proposal_Arthur_PokemonTCG.docx]] (54 entri daftar pustaka alfabetis bebas angka, 54 bookmark DP; judul BAB dua baris via shift+enter; rujukan gambar/persamaan/tabel bernomor eksplisit; 0 typo backslash; tipografi full-doc PASS pure-black + dot leaders 14,0 cm; **Frontmatter modular 6 lembar formal dipisah mandiri ke [[01_Naskah_Utama/01_Lembar_Persetujuan_Proposal/|01_Lembar_Persetujuan_Proposal/]], naskah DOCX utama bersih mulai Cover → TOC → Bab 1**; Daftar Tabel & Gambar terpisah mandiri via `PageBreakBefore: True`)
  - Paritas Tipografi Miring & Rerangka Bus Sentral (30 Sep 2026 / Sesi 38): Inviolable Rule [[.agents/rules/mandatory_cross_format_typography_and_italic_parity.md]] aktif; Gate G8 terpasang (249/249 ekspresi miring LaTeX 100% lolos di DOCX); Rerangka Gambar 2.1 disempurnakan ke Bus Sentral (Option 3); Keputusan D32 tercatat.
  - Agenda Sesi 39 Berikutnya: (1) Penyeragaman ukuran font hyperlink sitasi dalam sel tabel (Tabel 3.1: 'Colline, 2024' menjadi 9pt); (2) Tinjauan & restrukturisasi format penulisan hipotesis (H1–H6) di Bab 2.
  - Humanisasi Bahasa Skripsi (30 Sep 2026): Rule permanen [[.agents/rules/mandatory_humanized_academic_tone.md]] aktif; 40+ frasa bombastis/robotik dieliminasi dari Bab 1–3 (Kategori A); istilah metodologis baku dipertahankan (Kategori B); sinkronisasi Markdown & Word 100% selesai.
  - Revisi Terkini Dosen: [[07_Review_&_Audit/Revisi_Dosen/2026-09-29_Revisi_Fredella_Colline_Populasi_Jakarta_Barat_dan_Judul.md|Revisi Dosen Pembimbing (29 Sep 2026: Populasi Jakarta Barat, Penyesuaian Judul & 4 Pilar Justifikasi - D31)]] · [[07_Review_&_Audit/Revisi_Dosen/2026-09-24_Catatan_Revisi_Seminar_Proposal_Sempro.md|Catatan Revisi Sempro 24 Sep 2026]] (Butir 1 Rerangka Elips SELESAI; Butir 2 Rasio Pustaka SELESAI Fase 1 [61,6%]; Butir 3 Jembatan Narasi Bab 1 SELESAI; Butir 4 Eliminasi Grand Theory SELESAI per D30) · [[07_Review_&_Audit/Revisi_Dosen/2026-09-23_Revisi_Sylvia_Pascapangkas_Bab1.md|Catatan Sylvia 23 Sep 2026]]
* **Kickoff AI Sesi:** 🌐 [[PROMPT_KICKOFF.html|Buka Aplikasi Web Kickoff 1-Klik]] | 📋 [[00_PROMPT_MULAI_SESI_TINGGAL_COPY_PASTE.md|Versi Dokumen Markdown]]
* **Status Mendeley Live:** 54 entri RIS/Bib (53 ber-websites; `sugiyono2019` buku cetak tanpa link — wajar); cloud Mendeley menunggu `--prune` (hapus ghost Tan & Prasetio) + `--push` (tambah Azizah) oleh user pasca-`--auth` (token sesi lama hilang); RIS siap impor [[06_Referensi_Jurnal_PDF/Mendeley_Library_Arthur_PokemonTCG.ris|Berkas RIS (54 Ref)]]
* **Framework Universal (pakai-ulang):** [[04_Riset_&_Metodologi/PRD_UNIVERSAL_SKRIPSI_FRAMEWORK_GRAPH_OF_AGENTS.md|Graph of Agents A0–A11]] · SOP [[directives/universal_thesis_graph_of_agents.md|F1–F11]] · Orchestrator `py execution/run_thesis_graph.py --gate parity` (8/8 PASS; extended 11/11 PASS) · Template [[04_Riset_&_Metodologi/TEMPLATE_SOURCE_OF_TRUTH_UNIVERSAL.md|SoT Baru]] · Konektor `execution/mendeley_connector.py`
* **Status Graphify Knowledge Graph:** 🌐 [[graphify-out/graph.html|Peta Pengetahuan Interaktif]] (2.416 Nodes, 2.558 Edges, 223 Komunitas — refresh 30 Sep 2026: tokenizer AST paritas italic 100%, Gate G8, rerangka Bus Sentral)


---

## 🗺️ 2. Map of Content (MOC) Peta Navigasi Vault

```
                             [ 00_DASHBOARD_SECOND_BRAIN ]
                                          │
       ┌──────────────────┬───────────────┴───────────────┬──────────────────┐
       ▼                  ▼                               ▼                  ▼
[ 01_Naskah_Utama ] [ 02_Persiapan_Sidang ] [ 04_Riset_&_Metodologi ] [ 06_Referensi_Jurnal ]
  - Naskah TeX/PDF    - Master Study Guide     - Source of Truth         - 10 Jurnal Empiris
  - Format Word       - Bank Soal Sulit        - PRD & Log Sesi          - Katalog Metadata
  - Asset Vektor      - Presentasi Web         - Matriks Literatur       - Paper Barasz (2017)
```

### 📁 A. Naskah & Dokumen Induk
* **Naskah Utama LaTeX:** [[01_Naskah_Utama/Proposal_Arthur_PokemonTCG.tex]] (satu-satunya master; varian NoBab3 dihapus 23 Sep 2026)
* **Draft Markdown Terpisah:**
  - Bab I Pendahuluan: [[03_Draft_Per_Bab/BAB_I_PENDAHULUAN.md]]
  - Bab II Tinjauan Pustaka: [[03_Draft_Per_Bab/BAB_II_TINJAUAN_PUSTAKA.md]]
  - Bab III Metode Penelitian: [[03_Draft_Per_Bab/BAB_III_METODE_PENELITIAN.md]]
  - Daftar Pustaka: [[03_Draft_Per_Bab/DAFTAR_PUSTAKA_TENTATIF.md]]

### 📁 B. Persiapan Sidang & Bimbingan
* **Master Study Guide v4.0 (Tri-Format MD, PDF, HTML):** [[02_Persiapan_Sidang/PANDUAN_BELAJAR_PROPOSAL.md]] | [[02_Persiapan_Sidang/PANDUAN_BELAJAR_PROPOSAL.pdf|PDF Panduan Belajar]] | [[02_Persiapan_Sidang/PANDUAN_BELAJAR_PROPOSAL.html|HTML Panduan Belajar]] *(Edisi Terlengkap: 34 Q&A + Q20B anti-cecaran + §17 bedah Bab 3 + §18 anatomi rumus + §19 anatomi Bab 1–2 + §21 suplemen kritis + §22 ENSIKLOPEDIA 54 SITASI LENGKAP: audit berkas fisik, konfirmasi bebas error 2 lembar, peran dalam skripsi & tameng sidang 1 kalimat)*
* **Alur Presentasi 7 Slide (naskah bicara + durasi):** [[02_Persiapan_Sidang/02_Rencana_PPT_Sempro_7_Slide/ALUR_PRESENTASI_7_SLIDE_DETAIL.md]] | **Prompt siap-tempel Claude:** [[02_Persiapan_Sidang/02_Rencana_PPT_Sempro_7_Slide/PROMPT_CLAUDE_7SLIDE_SIAP_TEMPEL.md]] *(spesifikasi terkoreksi: 6H, N 120–150, tanpa klaim paylater)*
* **Blueprint PPT Sempro Ringkas 7 Slide:** [[07_Review_&_Audit/Revisi_Dosen/2026-09-22_Arahan_Dosen_Struktur_PPT_Sempro_7_Slide.md|Cetak Biru 7 Slide & Talking Points (Arahan Ci Colline 22 Sep 2026)]]
* **Paket Handoff AI Lain (PRD & Plan PPT 7 Slide):** [[02_Persiapan_Sidang/02_Rencana_PPT_Sempro_7_Slide/README.md|Folder 02_Rencana_PPT_Sempro_7_Slide/]] · [[02_Persiapan_Sidang/02_Rencana_PPT_Sempro_7_Slide/PRD_PPT_SEMPRO_7_SLIDE.md|PRD]] · [[02_Persiapan_Sidang/02_Rencana_PPT_Sempro_7_Slide/IMPLEMENTATION_PLAN_PPT_SEMPRO_7_SLIDE.md|Implementation Plan]] · [[02_Persiapan_Sidang/02_Rencana_PPT_Sempro_7_Slide/PROMPT_UNTUK_AI_LAIN.md|Prompt Siap Copy-Paste]]
* **Slide Deck Seminar Proposal (PPTX):** [[02_Persiapan_Sidang/ppt_seminar_proposal/Proposal_Arthur_Sempro_PokemonTCG.pptx]] *(15 slide FinTech Dark Mode, 5,17 MB, editable)* | [[02_Persiapan_Sidang/ppt_seminar_proposal/slides/|Folder Slide HTML]]
* **Simulasi Sidang & Soal Sulit:** [[02_Persiapan_Sidang/01_Bank_Soal_&_Flashcard/03_PERTANYAAN_SIDANG_SULIT.md]] *(Termasuk SULIT 11: Cara menjawab asal usul referensi)*
* **Flashcard & Kamus Istilah:** [[02_Persiapan_Sidang/01_Bank_Soal_&_Flashcard/02_FLASHCARD_ISTILAH.md]]
* **Aplikasi Presentasi Interaktif:** [[02_Persiapan_Sidang/presentasi_interaktif/index.html]]

### 📁 C. Riset, Metodologi, & Riwayat Sesi (Living Core)
* **Framework Universal (Arsitektur Utama):** [[04_Riset_&_Metodologi/PRD_UNIVERSAL_SKRIPSI_FRAMEWORK_GRAPH_OF_AGENTS.md]] *(SOP Graph of Agents A0–A11)*
* **Source of Truth (Parameter Kanonis):** [[04_Riset_&_Metodologi/SOURCE_OF_TRUTH.md]] *(Ketetapan definitif D01–D30+)*
* **Matriks 54 Referensi Q1/SSCI:** [[04_Riset_&_Metodologi/LITERATURE_MATRIX.md]] *(Matriks pustaka terverifikasi)*
* **Catatan Log Sesi Otomatis:** [[04_Riset_&_Metodologi/LOG_SESI_SECOND_BRAIN.md]] *(Catatan progres dan keputusan tiap sesi)*
* **Ledger Bukti Halaman (D26):** [[04_Riset_&_Metodologi/EVIDENCE_LEDGER_HALAMAN.md]] *(15 klaim → halaman PDF; SOP [[directives/evidence_page_ledger.md]]; uji `verify_evidence_ledger.py`)*
* **Ground Truth Data Empiris Terverifikasi:** [[04_Riset_&_Metodologi/VERIFIED_EMPIRICAL_DATA.md]] *(Catatan audit fisik Statista, Pokémon Company, PriceCharting)*
* **SOP Audit Ilmiah Naskah:** [[directives/run_paper_audit.md]] *(SOP pelaksanaan audit pra-bimbingan & pra-sidang)*
* **Laporan Audit Ilmiah Formal:** [[07_Review_&_Audit/Paper_Audits/]] *(terbaru: [[07_Review_&_Audit/Paper_Audits/review-2026-09-29-011500.md|audit pasca-sempro 29 Sep 2026]] — F026–F031 resolved, 0 temuan terbuka)*
* 📦 **Katalog Arsip PRD Sprint (Completed):** [[04_Riset_&_Metodologi/00_Arsip_PRD_Selesai/README.md|Folder 00_Arsip_PRD_Selesai/]] *(Koleksi 20 PRD & rencana implementasi tugas masa lalu yang telah 100% selesai dan lulus uji 10 gerbang)*
* **Riwayat Revisi & Audit:** [[07_Review_&_Audit/Revisi_Dosen/2026-09-29_Revisi_Fredella_Colline_Populasi_Jakarta_Barat_dan_Judul.md|Revisi Dosen (29 Sep 2026: Populasi Jakarta Barat & Judul D31)]] | [[07_Review_&_Audit/Revisi_Dosen/2026-09-24_Catatan_Revisi_Seminar_Proposal_Sempro.md|Catatan Revisi Sempro 24 Sep 2026]] | [[07_Review_&_Audit/Revisi_Dosen/2026-09-22_Arahan_Dosen_Struktur_PPT_Sempro_7_Slide.md|Revisi Dosen (22 Sep 2026: Tips & Trik PPT Sempro Ringkas 7 Slide)]] | [[07_Review_&_Audit/Revisi_Dosen/2026-09-16_Revisi_Dosen_Sumber_Pokemon_Mendeley_Daftar_Pustaka.md|Revisi Dosen (16 Sep 2026: Sumber Pokemon, Mendeley, DP A-Z)]] | [[07_Review_&_Audit/Revisi_Dosen/2026-09-14_Review_Teknis_Prism_AI_dan_Matriks_Resolusi.md]] | [[07_Review_&_Audit/Revisi_Dosen/2026-09-09_Revisi_Dosen_dan_Opsi_Moderasi.md]]



### 📁 D. Referensi & Jurnal Ilmiah
* **Paket Library Mendeley (Universal RIS):** [[06_Referensi_Jurnal_PDF/Mendeley_Library_Arthur_PokemonTCG.ris|Berkas RIS Siap Impor (54 Ref)]] | [[06_Referensi_Jurnal_PDF/Mendeley_Library_Arthur_PokemonTCG.bib|Berkas BibTeX (54 Ref)]]
* **Panduan 1-Menit Impor Mendeley:** [[06_Referensi_Jurnal_PDF/PANDUAN_IMPORT_MENDELEY_1_MENIT.md]] *(Panduan tangkapan layar 55 referensi untuk dosen)*
* **Katalog Lengkap:** [[06_Referensi_Jurnal_PDF/KATALOG_REFERENSI_JURNAL.md]]
* **10 Jurnal Empiris Mutakhir (2021–2026):** [[06_Referensi_Jurnal_PDF/01_Empiris_Utama_2021-2025/]]
* **Paper Seminal Kelengkapan:** [[06_Referensi_Jurnal_PDF/02_Jurnal_Teori_&_Metodologi/2017_Barasz_et_al_Pseudo_Set_Framing.pdf]]

---

## 🔬 3. Matriks Teori & Variabel Penelitian

| Simbol | Variabel Penelitian | Landasan Teori Utama | Skala Baku / Indikator | Jurnal Rujukan Mutakhir |
|---|---|---|---|---|
| **$Y$** | *Impulsive Buying* | Teori Impulsif Rook (1987) | Skala IBTS (Verplanken & Herabadi, 2001) | Dewi et al. (2026), Gong et al. (2024) |
| **$X_1$** | *Hedonic Motivation* | *Hedonic Value* Babin et al. (1994) | 6 dimensi sumber, 5 diadaptasi (tanpa *Value Shopping*; Bab 2 §2.2.1) | Pranggabayu (2022), Apidana (2022) |
| **$X_2$** | *Desire for Completeness* | *Completing the Set* Gao (2014) & Zeigarnik (1927) | *Pseudo-Set Framing* (Barasz et al., 2017) | Dewi et al. (2026) |
| **$X_3$** | *Speculative Motive* | *Behavioral Finance* Shiller (2000) & Keynes (1936) | Arbitrase Grading PSA 10 & Secondary Market | Aryadi & Lingga (2024), Colline (2024) |
| **$Z$** | *Self-Control* (Moderator) | *Self-Regulation Theory* Baumeister (2002) | *Brief Self-Control Scale* / BSCS (Tangney, 2004) | Artadita & Firmialy (2024), Lienardy (2024) |

---

## 🌐 4. Integrasi Jaringan Pengetahuan (Graphify)

* Laporan Graf Pengetahuan: [[graphify-out/GRAPH_REPORT.md]]
* Peta Graf Interaktif: `graphify-out/graph.html`
* Manifest Entitas: `graphify-out/manifest.json`
* Saat membuka sesi baru, Antigravity memverifikasi integritas arsitektur melalui Graphify sebelum memulai eksekusi.

---

## ⚖️ 5. Pedoman Mutlak Sinkronisasi Naskah & Tipografi LaTeX (Zero Desync)

Setiap perubahan pada naskah, bab, tabel, gambar, atau skrip generator **wajib** mematuhi pedoman baku:
* 📜 **PRD Sinkronisasi & Audit File:** [[04_Riset_&_Metodologi/00_Arsip_PRD_Selesai/PRD_SINKRONISASI_DOCX_DAN_AUDIT_FILE.md]]
* 📜 **PRD Kualitas Tipografi DOCX:** [[04_Riset_&_Metodologi/00_Arsip_PRD_Selesai/PRD_REVISI_DOCX_KUALITAS_LATEX.md]]
* 📜 **Aturan Permanen Workspace:** [[.agents/rules/mandatory_thesis_sync_and_quality.md]]
* 📜 **SOP Generator Word:** [[directives/generate_thesis_word_document.md]]

**Prinsip yang Tidak Boleh Dilanggar:**
1. **Source of Truth:** Master utama adalah LaTeX (`Proposal_Arthur_PokemonTCG.pdf`). Dokumen Word (`Proposal_Arthur_PokemonTCG.docx`) wajib 100% selaras (*zero desync*).
2. **Pure Black (#000000):** Dilarang keras menggunakan *theme accent colors*. Semua judul, tabel, dan nomor halaman wajib warna hitam pekat `#000000`.
3. **Kompatibilitas Penuh Daftar Isi di Google Docs & Word:** Tab stop kanan wajib `14.0 cm` (7938 dxa) dengan `w:leader="dot"` dan **tanpa `right_indent`** agar titik-titik dan nomor halaman tidak hilang atau rusak saat dibuka di Google Docs / Word Online.
4. **Verifikasi Wajib Sebelum Selesai:** Wajib menjalankan `python execution/verify_docx_typography.py` dan `python execution/verify_pdf_docx_parity.py`.

---
*Dashboard ini dimutakhirkan secara otomatis oleh Antigravity Obsidian Second Brain Protocol.* 🚀
