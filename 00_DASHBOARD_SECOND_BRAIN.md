# 🧠 DASHBOARD SECOND BRAIN — SKRIPSI POKÉMON TCG
### *S1 Manajemen Keuangan — Fakultas Ekonomi dan Bisnis — Universitas Kristen Krida Wacana (UKRIDA)*

> [!SUMMARY] Tujuan & Solusi Catatan Ini
> - **Untuk Apa:** Kokpit utama (*Master Dashboard / Map of Content*) untuk mengelola seluruh ekosistem riset skripsi, catatan teori, data empiris, dan persiapan sidang di Obsidian.
> - **Masalah yang Diselesaikan:** Menghilangkan fragmentasi catatan; menghubungkan seluruh naskah LaTeX, draf markdown, jurnal referensi, dan panduan belajar ke dalam satu pusat navigasi interaktif.
> - **Keputusan/Output:** Digunakan oleh Antigravity dan pengguna pada setiap awal sesi kerja untuk sinkronisasi konteks instan bersama Graphify.

---

## 📌 1. Identitas & Parameter Kunci Riset

* **Topik Skripsi:**  
  *Pengaruh Hedonic Motivation ($X_1$), Desire for Completeness ($X_2$), dan Speculative Motive ($X_3$) terhadap Impulsive Buying ($Y$) Booster Pack Kartu Pokémon TCG dengan Self-Control ($Z$) sebagai Variabel Moderasi.*
* **Dosen Pembimbing:** [[07_Review_&_Audit/Revisi_Dosen/|Dr. Fredella Colline, S.E., M.M., CFP®, PFM, CHCP-A]]
* **Metodologi Analisis:** Kuantitatif Asosiatif, Survei Kros-Seksional, *Moderated Regression Analysis (MRA)* dengan *Mean-Centering*.
* **Status Naskah Terkini:**
  - Naskah Utama Lengkap: [[01_Naskah_Utama/Proposal_Arthur_PokemonTCG.pdf|Proposal_Arthur_PokemonTCG.pdf]] (64 halaman pasca-humanisasi R3 Bab II+III 18 Sep 2026 — melampaui standar K-02 UKRIDA 2023, 54 entri referensi; sitasi 245 hyperlink internal ke DP; paritas full-doc PASS, 0 link mati)
  - Varian Tanpa Bab 3: [[01_Naskah_Utama/Proposal_Arthur_NoBab3.pdf|Proposal_Arthur_NoBab3.pdf]] (46 halaman — diregenerasi 18 Sep 2026 dari TeX kanonis via pipeline non-destruktif agar gate parity 7/7; keputusan Opsi-1 17 Sep tetap berlaku bila user ingin hapus ulang)
  - Dokumen Word Hybrid (Native TOC Word/Docs): [[01_Naskah_Utama/Proposal_Arthur_PokemonTCG.docx|Proposal_Arthur_PokemonTCG.docx]] (OMML native, 54 entri daftar pustaka alfabetis bebas angka, 54 bookmark DP + 245 sitasi terhyperlink; tipografi full-doc PASS pure-black + dot leaders 14,0 cm; **Frontmatter modular 6 lembar formal dipisah mandiri ke [[01_Naskah_Utama/01_Lembar_Persetujuan_Proposal/|01_Lembar_Persetujuan_Proposal/]], naskah DOCX utama bersih mulai Cover → TOC → Bab 1**; Daftar Tabel & Gambar terpisah mandiri via `PageBreakBefore: True`)
* **Kickoff AI Sesi:** 🌐 [Buka Aplikasi Web Kickoff 1-Klik](file:///z:/SKRIPSII/SKRIPSI%20ARTHUR/SKRIPSI-arthur-main/SKRIPSI-arthur-main/PROMPT_KICKOFF.html) | 📋 [[00_PROMPT_MULAI_SESI_TINGGAL_COPY_PASTE.md|Versi Dokumen Markdown]]
* **Status Mendeley Live:** 54 entri RIS/Bib (53 ber-websites; `sugiyono2019` buku cetak tanpa link — wajar); cloud Mendeley menunggu `--prune` (hapus ghost Tan & Prasetio) + `--push` (tambah Azizah) oleh user pasca-`--auth` (token sesi lama hilang); RIS siap impor [[06_Referensi_Jurnal_PDF/Mendeley_Library_Arthur_PokemonTCG.ris|Berkas RIS (54 Ref)]]
* **Framework Universal (pakai-ulang):** [[04_Riset_&_Metodologi/PRD_UNIVERSAL_SKRIPSI_FRAMEWORK_GRAPH_OF_AGENTS.md|Graph of Agents A0–A11]] · SOP [[directives/universal_thesis_graph_of_agents.md|F1–F11]] · Orchestrator `py execution/run_thesis_graph.py --gate parity` (7/7 PASS) · Template [[04_Riset_&_Metodologi/TEMPLATE_SOURCE_OF_TRUTH_UNIVERSAL.md|SoT Baru]] · Konektor `execution/mendeley_connector.py`
* **Status Graphify Knowledge Graph:** 🌐 [[graphify-out/graph.html|Peta Pengetahuan Interaktif]] (1.918 Nodes, 2.103 Edges, 188 Komunitas — refresh 22 Sep 2026: modular frontmatter DOCX, AST skrip ekstraksi lembar formal)


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
* **Naskah Utama LaTeX:** [[01_Naskah_Utama/Proposal_Arthur_PokemonTCG.tex]]
* **Naskah Varian Tanpa Bab 3:** [[01_Naskah_Utama/Proposal_Arthur_NoBab3.tex]]
* **Draft Markdown Terpisah:**
  - Bab I Pendahuluan: [[03_Draft_Per_Bab/BAB_I_PENDAHULUAN.md]]
  - Bab II Tinjauan Pustaka: [[03_Draft_Per_Bab/BAB_II_TINJAUAN_PUSTAKA.md]]
  - Bab III Metode Penelitian: [[03_Draft_Per_Bab/BAB_III_METODE_PENELITIAN.md]]
  - Daftar Pustaka: [[03_Draft_Per_Bab/DAFTAR_PUSTAKA_TENTATIF.md]]

### 📁 B. Persiapan Sidang & Bimbingan
* **Master Study Guide:** [[02_Persiapan_Sidang/PANDUAN_BELAJAR_PROPOSAL.md]] | [[02_Persiapan_Sidang/PANDUAN_BELAJAR_PROPOSAL.pdf|PDF Panduan Belajar]]
* **Blueprint PPT Sempro Ringkas 7 Slide:** [[07_Review_&_Audit/Revisi_Dosen/2026-09-22_Arahan_Dosen_Struktur_PPT_Sempro_7_Slide.md|Cetak Biru 7 Slide & Talking Points (Arahan Ci Colline 22 Sep 2026)]]
* **Slide Deck Seminar Proposal (PPTX):** [[02_Persiapan_Sidang/ppt_seminar_proposal/Proposal_Arthur_Sempro_PokemonTCG.pptx]] *(15 slide FinTech Dark Mode, 5,17 MB, editable)* | [[02_Persiapan_Sidang/ppt_seminar_proposal/slides/|Folder Slide HTML]]
* **Simulasi Sidang & Soal Sulit:** [[02_Persiapan_Sidang/01_Bank_Soal_&_Flashcard/03_PERTANYAAN_SIDANG_SULIT.md]] *(Termasuk SULIT 11: Cara menjawab asal usul referensi)*
* **Flashcard & Kamus Istilah:** [[02_Persiapan_Sidang/01_Bank_Soal_&_Flashcard/02_FLASHCARD_ISTILAH.md]]
* **Aplikasi Presentasi Interaktif:** [[02_Persiapan_Sidang/presentasi_interaktif/index.html]]

### 📁 C. Riset, Metodologi, & Riwayat Sesi
* **Source of Truth:** [[04_Riset_&_Metodologi/SOURCE_OF_TRUTH.md]] *(Dokumen rujukan mutlak parameter skripsi)*
* **Ledger Bukti Halaman (D26):** [[04_Riset_&_Metodologi/EVIDENCE_LEDGER_HALAMAN.md]] *(15 klaim → halaman PDF; SOP [[directives/evidence_page_ledger.md]]; uji `verify_evidence_ledger.py`)*
* **Catatan Log Sesi Otomatis:** [[04_Riset_&_Metodologi/LOG_SESI_SECOND_BRAIN.md]] *(Catatan progres dan keputusan tiap sesi)*
* **Panduan Standarisasi Heading & TOC:** [[04_Riset_&_Metodologi/PANDUAN_STANDARISASI_HEADING_DAN_DAFTAR_ISI_DOCX.md]] *(Kompatibilitas titik-titik Google Docs & Word)*
* **PRD Resolusi Review Teknis Prism AI:** [[04_Riset_&_Metodologi/PRD_RESOLUSI_REVIEW_TEKNIS_PRISM_AI.md]] *(Resolusi 11 temuan audit metodologi)*
* **PRD Arsitektur Hybrid Word:** [[04_Riset_&_Metodologi/PRD_HYBRID_PANDOC_SCRIPT_GENERATOR.md]]
* **PRD Kualitas Tipografi DOCX:** [[04_Riset_&_Metodologi/PRD_REVISI_DOCX_KUALITAS_LATEX.md]]
* **Grafik & Visual Empiris Bab 1:** [[04_Riset_&_Metodologi/PRD_GRAFIK_EMPIRIS_BAB1.md]]
* **PRD Integrasi Skill Paper-Audit:** [[04_Riset_&_Metodologi/PRD_INTEGRASI_SKILL_PAPER_AUDIT.md]] *(Kebijakan aktivasi bertingkat Tier-3 Gated Audit)*
* **SOP Audit Ilmiah Naskah:** [[directives/run_paper_audit.md]] *(SOP pelaksanaan audit pra-bimbingan & pra-sidang)*
* **Laporan Audit Ilmiah Formal:** [[07_Review_&_Audit/Paper_Audits/]] *(terbaru: [[07_Review_&_Audit/Paper_Audits/review-2026-09-18-213000.md|audit pasca-humanisasi 18 Sep 2026]] — F001–F019 resolved, F020–F025, 0 temuan terbuka)*
* **PRD Integritas & Paritas Mendeley:** [[04_Riset_&_Metodologi/PRD_SISTEM_INTEGRITAS_DAN_VERIFIKASI_MENDELEY.md]] *(Sistem pencegahan Silent Drop & Paritas 54 Referensi)*
* **PRD Eliminasi Sumber Fiktif & Verifikasi Data Primer:** [[04_Riset_&_Metodologi/PRD_ELIMINASI_SUMBER_PALSU_DAN_VERIFIKASI_DATA_PRIMER_BAB1.md]] *(Zero-Hallucination Protocol & Audit Faktual)*
* **Ground Truth Data Empiris Terverifikasi:** [[04_Riset_&_Metodologi/VERIFIED_EMPIRICAL_DATA.md]] *(Catatan audit fisik Statista, Pokémon Company, PSA)*
* **Directive Verifikasi Sumber Empiris:** [[directives/empirical_source_verification.md]] *(Aturan mutlak no-synthetic citations)*
* **PRD Tautan URL Aktif APA 7 Data Pokémon:** [[04_Riset_&_Metodologi/PRD_STANDARISASI_URL_SITASI_APA7_DATA_POKEMON.md]] *(Standarisasi Hyperlink OpenXML Word & Deep Link)*
* **SOP Validasi Integritas Mendeley:** [[directives/verify_mendeley_integrity.md]] *(Whitelist tag RIS & SOP verifikasi pra-terbang)*
* **Suite Uji Otomatis Integritas Mendeley:** [[execution/verify_mendeley_integrity.py]] *(Test suite 6-arah bebas dependensi)*
* **Suite Uji Otomatis URL Empiris:** [[execution/verify_live_urls.py]] *(Pemeriksa link hidup & deteksi direktori fiktif)*
* **Riwayat Revisi & Audit:** [[07_Review_&_Audit/Revisi_Dosen/2026-09-22_Arahan_Dosen_Struktur_PPT_Sempro_7_Slide.md|Revisi Dosen (22 Sep 2026: Tips & Trik PPT Sempro Ringkas 7 Slide)]] | [[07_Review_&_Audit/Revisi_Dosen/2026-09-16_Revisi_Dosen_Sumber_Pokemon_Mendeley_Daftar_Pustaka.md|Revisi Dosen (16 Sep 2026: Sumber Pokemon, Mendeley, DP A-Z)]] | [[07_Review_&_Audit/Revisi_Dosen/2026-09-14_Review_Teknis_Prism_AI_dan_Matriks_Resolusi.md]] | [[07_Review_&_Audit/Revisi_Dosen/2026-09-09_Revisi_Dosen_dan_Opsi_Moderasi.md]]



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
| **$X_1$** | *Hedonic Motivation* | *Hedonic Value* Babin et al. (1994) | 6 Dimensi Belanja (Arnold & Reynolds, 2003) | Pranggabayu (2022), Apidana (2022) |
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
* 📜 **PRD Sinkronisasi & Audit File:** [[04_Riset_&_Metodologi/PRD_SINKRONISASI_DOCX_DAN_AUDIT_FILE.md]]
* 📜 **PRD Kualitas Tipografi DOCX:** [[04_Riset_&_Metodologi/PRD_REVISI_DOCX_KUALITAS_LATEX.md]]
* 📜 **Aturan Permanen Workspace:** [[.agents/rules/mandatory_thesis_sync_and_quality.md]]
* 📜 **SOP Generator Word:** [[directives/generate_thesis_word_document.md]]

**Prinsip yang Tidak Boleh Dilanggar:**
1. **Source of Truth:** Master utama adalah LaTeX (`Proposal_Arthur_NoBab3.pdf`). Dokumen Word (`Proposal_Arthur_NoBab3.docx`) wajib 100% selaras (*zero desync*).
2. **Pure Black (#000000):** Dilarang keras menggunakan *theme accent colors*. Semua judul, tabel, dan nomor halaman wajib warna hitam pekat `#000000`.
3. **Kompatibilitas Penuh Daftar Isi di Google Docs & Word:** Tab stop kanan wajib `14.0 cm` (7938 dxa) dengan `w:leader="dot"` dan **tanpa `right_indent`** agar titik-titik dan nomor halaman tidak hilang atau rusak saat dibuka di Google Docs / Word Online.
4. **Verifikasi Wajib Sebelum Selesai:** Wajib menjalankan `python execution/verify_docx_typography.py` dan `python execution/verify_pdf_docx_parity.py`.

---
*Dashboard ini dimutakhirkan secara otomatis oleh Antigravity Obsidian Second Brain Protocol.* 🚀
