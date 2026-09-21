> [!SUMMARY] Tujuan & Solusi Catatan Ini
> - **Untuk Apa:** Framework universal brainstorming + pembuatan skripsi S1 berbasis Graph of Agents, dikompilasi dari seluruh PRD/directives/rules workspace ini.
> - **Masalah yang Diselesaikan:** PRD tersebar (16 PRD + 14 directives + 5 rules + 22 scripts) belum menjadi satu pipeline eksekusi dengan kontrol riset, reasoning hygiene, dan acceptance criteria yang observable.
> - **Keputusan/Output:** Satu research-control framework 6-stage pyramid + 11 agen + chained rules + skill registry, siap dipakai untuk topik apapun di universitas manapun (parameterisasi pedoman & variabel).

# UNIVERSAL SKRIPSI FRAMEWORK — Graph of Agents + Research-Control Pyramid

> **Sumber kanonik:** [[MASTER_GUIDE_SKRIPSI.md]] · [[04_Riset_&_Metodologi/SOURCE_OF_TRUTH.md]] · [[04_Riset_&_Metodologi/REUSABLE_THESIS_PLAYBOOK.md]] · [[05_Pedoman_&_Referensi/PRD_AI_Dosen_Pembimbing_Skripsi_v2.md]] · 16× `PRD_*.md` · 14× `directives/*.md` · 5× `.agents/rules/*.md` · 22× `execution/*.py`
> **Status:** v1.0 — 16 Sep 2026. Naskah aktif tidak diubah; zero-desync preserved.

---

## 0. Cara Pakai (30 detik)

1. **Isi 1 file parameter:** duplikat [[04_Riset_&_Metodologi/SOURCE_OF_TRUTH.md]] → ganti blok `JUDUL / X / Y / Z / POPULASI / N / METODE / PEDOMAN KAMPUS`. Framework sisanya tidak berubah.
2. **Jalankan agen berurutan** A0 → A11 sesuai graph §2. Setiap agen punya satu GOAL + DONE criteria observable. Dilarang lanjut jika DONE = FAIL.
3. **Setiap klaim empiris** wajib masuk Evidence Ledger (§1.3) dengan label `fact / observation / inference / assumption / unknown`.
4. **Sebelum bimbingan/sidang** wajib lewati gerbang A8 (parity) + A9 (paper-audit Tier-3). Tanpa keduanya = BUILD BROKEN.

### Parameterisasi universitas

| Parameter kampus | Default workspace ini | Ganti dengan |
|---|---|---|
| Pedoman format | Buku Pedoman TA FEB UKRIDA 2023 (A4, margin 4-3-3-3, TNR 12, spasi 1.5, `#000000`, pustaka tanpa nomor, hanging 1.25cm) | Pedoman kampusmu → update 1 file `verify_ukrida_compliance.py` + `PRD_AUDIT_DAN_PENYELARASAN*` |
| Syarat minimal | ≥50 hlm, ≥20 ref, ≥5 jurnal SINTA/Scopus ≤5 thn, sitasi dosen FEB | Ganti angka di A8 acceptance |
| Master naskah | LaTeX `Proposal_Arthur_NoBab3.pdf` = golden truth | `.tex` / `.docx` / `.md` apapun — tetapkan 1 golden truth, jangan dua |
| Variabel | Y=Impulsive Buying, X1=Hedonic, X2=Desire Completeness, X3=Speculative, M=Self-Control, MRA mean-centering | X/Y/Z apapun + metode apapun (regresi/SEM/kualitatif) — ganti hanya di A4–A6 |
| Tools sitasi | Mendeley RIS whitelist JOUR/BOOK/RPRT/CONF/THES/GEN | Zotero/Mendeley apapun — pertahankan aturan "no silent-drop" |

---

## 1. Core Architecture — Six-Stage Research Pyramid

Setiap agen MENJALANKAN keenam stage ini secara rekursif (fraktal), bukan sekali jalan:

```
Question → Canon → Evidence → Scope filter → Target filter → Audited conclusion
```

### 1.1 Establish Canon (otoritas sumber)

Hierarki diadopsi dari [[directives/empirical_source_verification.md]] + [[.agents/rules/mandatory_verifiable_theories_and_books.md]] + [[.agents/rules/no_login_wall_empirical_sources.md]]:

- **T1 Primer korporat/negara:** laporan perusahaan, statistik resmi, regulasi, dataset mentah. Contoh: `corporate.pokemon.co.jp/en/aboutus/figures/`.
- **T2 Riset terakreditasi:** jurnal SINTA/Scopus/WoS/DOAJ, Statista chart bernomor, buku penerbit bereputasi (Sage, Wiley, Routledge, Undip, Alfabeta).
- **T3 Sertifikasi/populasi terbuka:** PSA pop report, PriceCharting (open, no-login), repositori OA (DASH, Garuda, OneSearch).
- **T4 BANNED:** blog spekulatif, forum, estimasi sintetis, judul whitepaper karangan, URL direktori (`/news/`, `/articles/markets`), link login-wall/OTP/paywall/Cloudflare-403.

**Chained rule C-CANON-1:** tidak ada klaim kuantitatif tanpa T1–T3 + deep-link kanonis + HTTP 200 terverifikasi (`verify_live_urls.py`). Meragukan → hapus ("atau tidak sama sekali"), jangan ganti dengan sumber lebih lemah.

### 1.2 Define Interpretation Rules SEBELUM kumpul bukti

Diambil dari [[04_Riset_&_Metodologi/REUSABLE_THESIS_PLAYBOOK.md]] + [[05_Pedoman_&_Referensi/PRD_AI_Dosen_Pembimbing_Skripsi_v2.md]] Fase 1–3:

Wajib dibekukan sebelum evidence collection: scope, objek, subjek, RQ, eksklusi, batas populasi/versi/tanggal, completion criteria. Ini mencegah "search sampai ketemu yang mendukung jawaban favorit".

Template beku (simpan di Source of Truth D01–D26):

```text
UNIT: [siapa/apa diteliti] | POPULASI: [WNI ≥17th, beli ≥1x/6bln ...]
PERIODE: [2021–2025 / FY19–24] | ESTIMAND: [β / ΔR² / odds ...]
EKSKLUSI: [apa yang TIDAK diklaim] | SELESAI-JIKA: [N≥..., 6 hipotesis teruji ...]
```

### 1.3 Collect & Record — Evidence Ledger

Setiap fakta masuk ledger (format diambil dari [[04_Riset_&_Metodologi/VERIFIED_EMPIRICAL_DATA.md]]):

| Kolom | Isi |
|---|---|
| `claim` | kalimat klaim di naskah |
| `class` | `fact` (T1) / `observation` (data primer sendiri) / `inference` (hasil olah) / `assumption` (asumsi eksplisit) / `unknown` (belum tahu) |
| `source` | deep-link kanonis + tanggal akses |
| `check` | `verify_live_urls` / screenshot / PDF hash |
| `falsifier` | bukti apa yang akan MENGGUGURKAN klaim ini (wajib diisi — falsifikasi aktif) |

**Chained rule C-EVID-1:** setiap `inference` wajib punya ≥1 `falsifier`. Klaim tanpa falsifier = `assumption`, dilarang masuk Bab 1 sebagai fakta.

### 1.4 Scope Filter (generalisasi?)

Tanya: apakah bukti menggeneralisasi ke domain/populasi luas? Hasil 1 benchmark / 1 perusahaan / 1 sampel ≠ klaim universal. Contoh PRD: surge produksi Pokémon 28.8→64.8M tidak otomatis = "seluruh pasar TCG naik 125%".

### 1.5 Target/Object Filter (cocok dengan objek?)

Tanya: apakah environment/populasi/sampel/versi/workload SAMA dengan yang diteliti? Kontradiksi diselesaikan atau diawetkan eksplisit, tidak disembunyikan. Contoh: data global Statista vs populasi kolektor Indonesia → tulis batasnya di Bab 3, jangan klaim representatif nasional jika purposive.

### 1.6 Formalize + Audit

Review bukti → ekspos ketidakpastian + alternatif → definisikan acceptance criteria → simpulan terbatas (bounded conclusion) atau handoff ke agen berikutnya. Tidak ada "skipped check = pass".

---

## 2. Graph of Agents (11 agen)

```
                    ┌───────── A0 GOAL-KEEPER (Karpathy) ─────────┐
                    │  think→simple→surgical→goal-driven          │
                    └──────┬──────────────────────────────┬──────┘
                           ▼                              ▼
              A1 QUESTION-FRAMER ──→ A2 CANON-ARCHITECT ──→ A3 EVIDENCE-COLLECTOR
               (Bab1 gap)            (hierarki T1-T4)        (PDF+data+ledger)
                    │                       │                       │
                    ▼                       ▼                       ▼
              A4 CONSTRUCT-THEORIST ──→ A5 METHOD-DESIGNER ──→ A6 STATS-AUDITOR
               (Bab2, Tabel2.1)        (Bab3, sampling)        (MRA/validitas)
                    │                       │                       │
                    └───────────┬───────────┴───────────┬───────────┘
                                ▼                       ▼
                    A7 MANUSCRIPT-BUILDER ──→ A8 PARITY-ENFORCER
                     (LaTeX→DOCX/PDF)          (7 verifier gates)
                                │                       │
                                ▼                       ▼
                    A9 PAPER-AUDIT-CHALLENGER   A10 DEFENSE-COACH
                     (Tier-3 gated)              (sidang)
                                └───────────┬───────────┘
                                            ▼
                                  A11 BRAIN-LOGGER
                           (Obsidian+Graphify+dashboard)
```

**Aturan graph:**

- Jalur utama berurutan; A0 mengawasi semua; A11 mencatat semua.
- Loop resmi: A9 → kembali ke agen yang ditunjuk temuan (mis. F-stat → A5/A6; sitasi → A2/A3). A8 FAIL → kembali ke A7. Tidak ada loop silang liar.
- Paralelisasi aman: A2+A3 (kanon + kumpul) boleh paralel setelah A1 DONE; A7 varian Full/NoBab3 boleh paralel; sisanya sekuensial.

### A0 — GOAL-KEEPER (Karpathy hygiene layer)

- **Goal:** setiap output menelusur balik ke tujuan riset; tidak ada kompleksitas tak perlu.
- **Berasal dari:** prinsip `karpathy-guidelines` (user-supplied) + [[.agents/rules/3_layer_architecture.md]] Layer-2 orkestrasi.
- **Chained rules:**
  - `K1 Think-before-acting:` tulis asumsi material + alternatif interpretasi SEBELUM eksekusi.
  - `K2 Simplicity-first:` tolak cluster-robust/IRB/SEM jika OLS/SPSS cukup (preseden: PRD Prism menolak over-engineering S1).
  - `K3 Surgical-changes:` ubah minimal; dual-mode Full/NoBab3 tidak boleh saling merusak.
  - `K4 Goal-driven:` setiap simpulan punya acceptance criteria observable; bedakan *verified* vs *proposed*; skipped check ≠ pass.
- **Tools:** semua `verify_*.py` sebagai oracle.
- **DONE:** tiap agen output mencantumkan `Goal-link: [RQ/H ke-...]` + `Verified: [...]` + `Proposed (belum verif): [...]`.

### A1 — QUESTION-FRAMER (Bab 1: fenomena → masalah → tujuan)

- **Goal:** judul terkunci HANYA setelah Fase 1–3 lulus (anti "langsung kasih judul").
- **PRD/directives:** [[04_Riset_&_Metodologi/PRD_PENELITIAN.md]] · `REUSABLE_THESIS_PLAYBOOK` Fase 1–4 · `PRD_AI_Dosen_Pembimbing_Skripsi_v2` gerbang F1–F4 · [[04_Riset_&_Metodologi/PRD_GRAFIK_EMPIRIS_BAB1.md]] · [[directives/curate_bab1_market_graphics.md]].
- **Inputs:** fenomena lapangan spesifik+aktual+primer; data makro ekosistem.
- **Outputs:** 6 rumusan masalah + 6 tujuan + manfaat (teoretis/praktis) + Gambar 1.1/1.2/1.3 + narasi pengait ekonomi.
- **Steps:** (1) bekukan interpretation rules §1.2; (2) pilih 2–3 grafik empiris T1–T3 (PNG 300 DPI, TNR only, palet navy/crimson/amber/slate, caption `Gambar 1.x` + `Sumber:`); (3) tulis gap 4-jalur + novelty; (4) kunci ke Source of Truth.
- **Tools:** `generate_bab1_figures.py`, `VERIFIED_EMPIRICAL_DATA.md`.
- **DONE:** fenomena terbukti primer; unit/populasi/periode/estimand jelas; grafik terdaftar di Daftar Gambar; narasi mensitasi tiap gambar.
- **Anti-pattern:** tautologi masalah; ecological fallacy (agregat nasional → perilaku individu); grafik tanpa sumber T1–T3.

### A2 — CANON-ARCHITECT (hierarki otoritas)

- **Goal:** tetapkan kanon sumber sebelum kumpul bukti.
- **PRD/directives:** `empirical_source_verification.md` · `verify_book_sources_libgen.md` · rules `mandatory_verifiable_theories_and_books` + `no_login_wall_empirical_sources` · [[04_Riset_&_Metodologi/PRD_VERIFIKASI_SUMBER_BUKU_LIBGEN_DAN_RULES.md]] · [[04_Riset_&_Metodologi/PRD_DOWNLOAD_BUKU_REFERENSI_LIBGEN.md]].
- **Outputs:** daftar kanon T1–T3 + blacklist T4 + substitusi sah (mis. PriceCharting ganti ICv2; Field/Aiken&West ganti buku moderasi hilang).
- **Steps:** (1) query LibGen per `@book` (judul inti EN + ISBN); (2) uji no-login-wall (incognito/curl HTTP 200); (3) sinkronkan edisi `references.bib` jika beda; (4) buku lokal → scan resmi Perpusnas.
- **Tools:** `verify_book_sources.py`, `download_libgen_books.py`, `verify_live_urls.py`.
- **DONE:** 100% teori punya PDF Bab 1–3 + mirror aktif; 0 ghost citation; `NOT_FOUND=0`.

### A3 — EVIDENCE-COLLECTOR (akuisisi + ledger)

- **Goal:** kumpulkan bukti + catat di ledger §1.3, cari bukti yang bisa MENGGUGURKAN penjelasan unggulan.
- **PRD/directives:** `download_journal_references.md` · [[04_Riset_&_Metodologi/PRD_ELIMINASI_SUMBER_PALSU_DAN_VERIFIKASI_DATA_PRIMER_BAB1.md]] · [[04_Riset_&_Metodologi/PRD_SUBSTITUSI_GAMBAR_1_3_DATA_LEGIT_BAB1.md]] · [[04_Riset_&_Metodologi/PRD_STANDARISASI_URL_SITASI_APA7_DATA_POKEMON.md]].
- **Outputs:** 10 jurnal empiris ≤5 thn di `01_Empiris_Utama_2021-2025/` + buku di `03_Buku_Referensi_PDF/` + `KATALOG_REFERENSI_JURNAL.md` + `VERIFIED_EMPIRICAL_DATA.md` + ledger.
- **Steps:** (1) unduh PDF (tolak <20KB / `<!DOCTYPE html>` / WAF → mirror institusi); (2) penamaan `[Tahun]_[Penulis]_[Keyword].pdf`; (3) audit 100% angka Bab 1 (kasus ICv2 41.5% fiktif → eliminasi total, 56→55 ref); (4) URL APA7 §10.4/10.16: full `https://`, tanpa `Retrieved from`, RIS `UR`, Bib `url+\note`, Word hyperlink OpenXML biru `#0563C1` underline.
- **Tools:** `verify_pdf_headers.py`, `generate_journal_catalog.py`, `verify_live_urls.py`, `generate_bab1_figures.py`.
- **DONE:** semua PDF `%PDF` + ≥300KB; katalog memuat penulis/tahun/judul/jurnal/vol/DOI/indeksasi/peran variabel; ledger tiap klaim punya falsifier.

### A4 — CONSTRUCT-THEORIST (Bab 2: teori → operasionalisasi)

- **Goal:** tiap konstruk punya lineage teori → istilah baku EN → padanan ID → indikator terukur.
- **PRD/directives:** `review_desire_for_completeness.md` · `PRD_RESOLUSI_REVIEW_TEKNIS_PRISM_AI` (rekonsiliasi sitasi, Tabel 3.2) · Teori: Rook 1987, Babin 1994, Gao 2014, Barasz 2017, Zeigarnik 1927, Shiller 2000, Keynes 1936, Baumeister 2002, Tangney 2004.
- **Outputs:** Bab 2 (§2.1–2.9) + Tabel 2.1 (10 jurnal) + hipotesis H1–H6 + Gambar rerangka 2.1.
- **Steps:** (1) text-mining seminal (`analyze_completeness_construct.py`: `complet*`, `set completion`, `kelengkapan`); (2) susun matriks literatur (query/log/matriks/sintesis, korpus terbatas); (3) operasionalisasi Likert 1–5: X1 5 item (Arnold&Reynolds), X2 4–5 item (Gao/Barasz), X3 4–5 item (Shiller; tulis `Apresiasi Modal`, bukan `Cuan`), M 5–6 item BSCS umum (hindari antonim Y), Y 6–9 item IBTS; (4) siapkan draf argumen lisan defensif per istilah (untuk sidang).
- **DONE:** tiap indikator menelusur ke teori + jurnal Tabel 2.1; tidak ada konstruk tanpa skala baku.

### A5 — METHOD-DESIGNER (Bab 3: desain → sampling → model)

- **Goal:** desain layak S1, etis, ter-frozen sebelum olah data.
- **PRD/directives:** `PRD_PENELITIAN` (metode) + `PRD_RESOLUSI_REVIEW_TEKNIS_PRISM_AI` (Model 1/2, mean-centering, UU 24/2013, N).
- **Outputs:** Bab 3 (§3.1–3.5): batasan, desain cross-sectional Google Forms, populasi/purposive (WNI ≥17th, beli ≥1x/6–12 bln), N≥111 ideal 120–150 (Green `50+8k=106`, `104+k=111`, Cohen power .80), instrumen Tabel 3.1/3.2, model MRA, Gambar 3.1 alur, uji validitas (Pearson, Cronbach α≥0.60).
- **Frozen model (wajib verbatim, ganti simbol sesuai topikmu):**
  - Model 1 Baseline Aditif: `Y = α + β1X1* + β2X2* + β3X3* + β4M* + e`
  - Model 2 Penuh: `Y = α + β1X1* + β2X2* + β3X3* + β4M* + β5(X1*·M*) + β6(X2*·M*) + β7(X3*·M*) + e` (`*` = mean-centered; ΔR² murni interaksi; F-change df(3,N-8))
  - Tulis `mean-centering`, bukan `standarisasi`/`z-score`.
- **Etika:** UU 24/2013 (bukan KUHPerdata 330) + informed consent + PII minimal; purposive ≠ representatif (tulis batasnya).
- **DONE:** estimand + freeze model + flow/missing/diagnostik/sensitivitas direncanakan; XeLaTeX kompilasi bersih.

### A6 — STATS-AUDITOR (pengukuran + analisis)

- **Goal:** bedakan signifikansi / efek / makna; asosiasi observasional ≠ kausal.
- **Aturan:** jangan p-value tanpa effect size; jangan α untuk single-item; jangan kontrol tanpa teori; jangan klaim signifikan jika n.s.; data sintetis hanya dry-run berlabel terpisah (dilarang rekayasa responden/statistik/DOI).
- **Outputs:** hasil Pearson/α/asumsi klasik/regresi+MRA + simple slopes (Hayes 2018) + Tabel 3.3.
- **DONE:** ΔR² + F-change dilaporkan; non-esensial mean-centering tidak mengubah R²/interaksi (cek Prism).

### A7 — MANUSCRIPT-BUILDER (LaTeX → DOCX/PDF, dual-mode)

- **Goal:** 1 golden truth → semua format sinkron 100%.
- **PRD/directives:** [[04_Riset_&_Metodologi/PRD_HYBRID_PANDOC_SCRIPT_GENERATOR.md]] · [[04_Riset_&_Metodologi/PRD_SINKRONISASI_DOCX_DAN_AUDIT_FILE.md]] · [[04_Riset_&_Metodologi/PRD_REVISI_DOCX_KUALITAS_LATEX.md]] · [[04_Riset_&_Metodologi/PRD_DOCX_HEADING_OUTLINE_TABS.md]] · `generate_thesis_word_document.md` · `build_pdf/docx_without_chapter3.md` · `audit_pdf_vs_docx_fidelity.md` · `PANDUAN_STANDARISASI_HEADING_DAN_DAFTAR_ISI_DOCX.md`.
- **Arsitektur Hybrid:** Pandoc = parser rumus (`$$`, `equation` → `<m:oMathPara>` Cambria Math, 6 rumus kanonis N + Model 1/2); `build_proposal_word.py` = governor layout.
- **Spesifikasi baku (jangan diubah tanpa update verifier):**
  - A4 margin 4-3-3-3 (area 14.0cm); TNR 12pt; spasi 1.5; justify; indent 1.25cm; pure black `#000000` eksplisit di semua run (bersihkan `themeColor/Tint/Shade`).
  - Sectioning: sampul unnumbered + romawi ii–x + arab 1+; footer `UKRIDA | hal`.
  - Heading: H1 `outlineLvl 0` (frontmatter + BAB + Pustaka + Lampiran, ALL CAPS center page-break); H2 lvl1 (1.1–1.7…); H3 lvl2; abstrak ID regular 1.0 vs abstract EN italic.
  - TOC universal: tab-stop kanan `14.0cm = 7938 dxa`, `w:leader="dot"`, `right_indent = 0`, struktur 3-run (title/tab/page) + `<w:sdt>` native (klik + update 1-klik di Word/Docs).
  - **Pemisahan Halaman Frontmatter Mutlak (Pedoman FEB UKRIDA 2023 Subbab 2.1 hlm 9–10):** `DAFTAR ISI`, `DAFTAR TABEL`, dan `DAFTAR GAMBAR` adalah 3 entitas struktural independen yang masing-masing WAJIB berdiri sendiri pada halaman baru terpisah (dengan penomoran romawi kecil). Heading `DAFTAR TABEL` dan `DAFTAR GAMBAR` wajib menyematkan `<w:pageBreakBefore/>` (`p.paragraph_format.page_break_before = True`) dan diproteksi dengan buffer paragraf pada injeksi TOC Word COM Interop guna mencegah paragraph merging. Dilarang keras menggabungkan daftar tabel/gambar ke dalam daftar isi utama (seperti kecacatan pada naskah kakak tingkat).
  - Tabel APA7 (atas 1pt, header 0.75pt, bawah 1pt, tanpa vertikal); rumus OMML native; caption tabel atas / gambar bawah + `Sumber:`; zero AI artifacts (tidak ada `*`/`$`/`\cite` bocor; `X₁,X₂,X₃,Y,M,R²,ΔR²,p<0,05,α,n` dirender benar).
  - Dual-mode: `--no-chapter3` (tanpa Bab 3 + tanpa 3 lembar formal, frontmatter mulai ii) vs full.
- **Tools:** `build_proposal_word.py` (+pandoc), `build_proposal_nobab3_pdf.py` (xelatex→bibtex→xelatex×2), `sync_markdown_from_tex.py`, `compare_pdf_docx_fidelity.py`.
- **DONE:** 2 DOCX + 2 PDF ter-build; §A8 PASS.

### A8 — PARITY-ENFORCER (7 gerbang verifikasi — tidak bisa dinego)

Jalankan berurutan; 1 FAIL = BUILD BROKEN, dilarang ke pembimbing. (Dipetakan dari [[.agents/rules/mandatory_thesis_sync_and_quality.md]] + `PRD_AUDIT_DAN_PENYELARASAN_PEDOMAN_FEB_UKRIDA_2023` + `PRD_SISTEM_INTEGRITAS_DAN_VERIFIKASI_MENDELEY`.)

| # | Gate | Script | Kriteria PASS |
|---|---|---|---|
| G1 | Mendeley 6-way parity | `verify_mendeley_integrity.py` (T1–T7) | `TeX=MD=Word=RIS=Bib=Mendeley=N`; whitelist `JOUR/BOOK/RPRT/CONF/THES/GEN` (larang `ELEC/WEB/MISC` — silent-drop); metadata TY/TI/AU/PY/PB-JO/ID/UR lengkap; UTF-8 bersih; `UR` + hyperlink OpenXML aktif |
| G2 | Live URL | `verify_live_urls.py` | 0 pola blacklist; key+URL kanonis ada di bib; HTTP 200/301/302/403 = live |
| G3 | UKRIDA compliance | `verify_ukrida_compliance.py` | ≥5 jurnal SINTA/Scopus; sitasi dosen; DP ≥20 tanpa nomor, hanging 1.25cm; `dan` (bukan `&`); `et al.` miring; margin 4-3-3-3 |
| G4 | Tipografi DOCX | `verify_docx_typography.py` | 0 artefak; TOC tab 14.0cm + `right_indent=0`; semua run `#000000` tanpa themeColor; pemisahan halaman mandiri (`pageBreakBefore`) `DAFTAR TABEL` & `DAFTAR GAMBAR` terisolasi 100% dari TOC |
| G5 | Paritas PDF↔DOCX | `verify_pdf_docx_parity.py` | NoBab3 steril (tanpa Bab 3/lembar formal usang); Full lengkap; butir-1 = pembimbing |
| G6 | Outline | `verify_word_outline.py` | H1/H2/H3 + `outlineLvl` + TNR12 (ref: 12/16/28) |
| G7 | Buku | `verify_book_sources.py` | 12 buku verified, `NOT_FOUND=0` |

Tambahan: `verify_format_and_typos.py` (typo `dimoderasi`, `sebesar 125%`, legenda `; garis`), `verify_nobab3_pdf.py` (A4, 13 checkpoint, Times embedded), `verify_word_layout.py`, `verify_pdf_headers.py`.

### A9 — PAPER-AUDIT-CHALLENGER (Tier-3 gated review)

- **Goal:** defensible sebelum bimbingan/sempro — Critical=0.
- **PRD/directives:** [[04_Riset_&_Metodologi/PRD_INTEGRASI_SKILL_PAPER_AUDIT.md]] · [[directives/run_paper_audit.md]] · [[04_Riset_&_Metodologi/PRD_RESOLUSI_REVIEW_TEKNIS_PRISM_AI.md]].
- **Kebijakan Tier (anti-boros token):**
  - T1 Continuous (<2s, 0 token): G4+G3+G5+G6 tiap edit.
  - T2 Heuristic pra-kompilasi: `proofing_scan.py` + BibTeX.
  - T3 Gated paper-audit: hanya pada (A) Pra-Bimbingan, (B) Pra-Sempro, (C) Major Rewrite, (D) Verifikasi Resolusi, (E) On-demand eksplisit.
- **SOP T3:** pre-scan → claims-to-evidence mapping (fenomena→gap→hipotesis→indikator→MRA) → multi-role (Methods/Stats, Technical/Math, Claims/Literature) → challenger pass (Necessary Correction / Feasible Strengthening / Future Work; drop over-engineering S1) → terbitkan `07_Review_&_Audit/Paper_Audits/review-YYYY-MM-DD-HHMMSS.md` (ID F001+, severity, bukti, lokasi, dampak, rekomendasi tabel).
- **Context anchors (anti-false-alarm):** sitasi dosen = kewajiban bukan bias; Model 1 sertakan M* = desain benar; mean-centering ≠ z-score; usia 17 = UU 24/2013; proposal dinilai dari kelayakan desain, bukan output SPSS empiris.
- **DONE:** Critical=0; Major selesai/terjustifikasi; traceability ID.

### A10 — DEFENSE-COACH (persiapan sidang)

- **Goal:** mahasiswa bisa mempertahankan tiap angka, istilah, dan rumus secara lisan.
- **Directives:** `generate_interactive_study_presentation.md` · `update_study_guide_and_pdf.md` · bank soal/flashcard (termasuk "SULIT 11: asal-usul referensi" — jawab: snowballing/Perpusnas).
- **Outputs:** `PANDUAN_BELAJAR_PROPOSAL.md/.pdf` (<5MB, A4 2.5cm) + `presentasi_interaktif/{index.html,style.css,app.js}` + `PRESENTASI_PANDUAN_BELAJAR.html` (12 slide, 27 flashcard, 16 soal defense, 16 kuis, simulator + visualisator MRA).
- **Tools:** `build_interactive_presentation.py`, `build_study_guide_pdf.py`.
- **DONE:** panduan sinkron dengan SoT terbaru (diff RQ/tujuan/hipotesis/audit); diuji Chrome/Edge/Safari/Firefox.

### A11 — BRAIN-LOGGER (memori persisten)

- **Goal:** nol amnesia antar sesi.
- **Rules:** [[.agents/rules/obsidian_second_brain.md]] + 3-layer architecture.
- **Pre-flight tiap sesi:** baca `graphify-out/manifest.json` / `GRAPH_REPORT.md` + [[00_DASHBOARD_SECOND_BRAIN.md]] → nyatakan kesiapan kontekstual.
- **In-flight:** tiap MD/PRD diawali callout `[!SUMMARY]` + `[[wikilinks]]` dua arah.
- **Post:** append `LOG_SESI_SECOND_BRAIN.md` (timestamp + keputusan + file tersentuh) + update dashboard tiap milestone.

---

## 3. Thesis Pipeline 7-tahap (dimensi vertikal)

Berjalan di atas pyramid §1; tiap tahap dimiliki satu agen:

| Tahap | Pemilik | Bab | Output kunci |
|---|---|---|---|
| 1. Research Methodology | A1+A5 | Bab 1 + Bab 3 awal | SoT beku, estimand, N, etik |
| 2. Literature / Deep Research | A3 | Bab 2 bahan | 10 jurnal + katalog + ledger |
| 3. Construct & Theory Analysis | A4 | Bab 2 | lineage, Tabel 2.1, H1–H6 |
| 4. Methodological Design | A5 | Bab 3 | purposive, instrumen, Model 1/2 frozen |
| 5. Statistical / Measurement Analysis | A6 | Bab 3–4 | validitas, MRA, ΔR² |
| 6. Evidence Review | A9 | Lintas-bab | audit T3 + matriks resolusi 11 temuan |
| 7. Cross-chapter Audit | A8 | Full | 7 gerbang PASS + komparasi PDF↔DOCX |

---

## 4. Chained Rules Registry (aturan berantai — tidak boleh dilompat)

| ID | Rule | Ditegakkan di | Jika dilanggar |
|---|---|---|---|
| C-Q1 | Judul terkunci HANYA setelah Fase 1–3 lulus | A1 | tolak sopan "langsung kasih judul" |
| C-CANON-1 | Klaim kuantitatif wajib T1–T3 + deep-link + HTTP 200 | A2→A3→A8-G2 | hapus grafik/klaim |
| C-BOOK-1 | Tiap `@book` wajib PDF LibGen + mirror aktif | A2→A8-G7 | ganti setara / hapus jika non-esensial |
| C-LEDGER-1 | Tiap inference wajib falsifier; tanpa falsifier = assumption | A3→A9 | turunkan kelas klaim |
| C-LINK-1 | Tiap DOI/URL sitasi wajib lolos `verify_all_citation_links.py` (0 DEAD). Klasifikasi: ALIVE (2xx/3xx) / WALLED (401/403/405/429/468 = terdaftar & me-resolve, anti-bot) / DEAD (404/timeout = perbaiki atau GANTI sumber). DOI mati → cari ground truth (Crossref + PDF primer + web), bukan nebak suffix. Kasus preseden 16 Sep 2026: Gao (judul+jurnal+vol+DOI fiktif → tulis ulang ke JM 2014), Sultan (judul+jurnal fiktif → Marketing Letters 2012), Tirtayasa (entri campuran → ganti IJBE 2020 + selaraskan klaim gap), Dewi/Long (satu digit salah → betulkan). Klaim teks yang menempel pada sumber yang diganti WAJIB diselaraskan (gap Temuan A/B, matriks, label konsep). | A2→A3→A8 | BUILD BROKEN sampai 0 DEAD |
| C-SCOPE-1 | 1 sampel ≠ klaim universal; tulis batas generalisasi | A3→A4→A9 | revisi Bab 1/3 |
| C-OBJ-1 | Purposive ≠ representatif; kontradiksi diawetkan eksplisit | A5→A9 | revisi Bab 3 + simpulan bounded |
| C-MODEL-1 | Freeze Model 1 (aditif+M*) + Model 2 (penuh mean-centered) | A5→A6→A7 | A9 Critical |
| C-CITE-1 | `dan` untuk 2 penulis; `et al.` miring; pustaka A-Z tanpa nomor, hanging 1.25cm | A7→A8-G3 | A8 FAIL |
| C-PARITY-1 | LaTeX golden → Word/MD sinkron 100%; pure black; TOC 14.0cm/`7938`/`right_indent=0`/`<w:tab/>` | A7→A8-G4/G5/G6 | BUILD BROKEN |
| C-MEND-1 | Whitelist RIS; `TeX=MD=Word=RIS=Bib=Mendeley`; selisih 1 = BROKEN | A7→A8-G1 | regenerate + re-import Mendeley |
| C-MEND-2 | Tiga-arah terkunci: kunci sitasi (`\cite`) = kunci BibTeX = `ID` RIS = judul dokumen cloud (cocok string). Cloud WAJIB cermin RIS: `--push` (idempoten) + `--prune` (hapus basi) + `--sync-links` (PATCH websites/identifiers); verifikasi baca-balik (55 dokumen, N ber-websites). Token kedaluwarsa → `--refresh`, bukan `--auth` ulang. Peta highlight (`directives/highlight_mendeley_citations.md`) wajib sinkron dgn metadata Bib (judul/jurnal/hlm/DOI ground truth; tanpa PDF = tulis statusnya, jangan karang hlm). | A7→A8 | cloud tak cermin = BROKEN |
| C-CITE-2 | Sitasi tubuh BUKAN teks mati di DOCX: tiap `(Penulis, Tahun)` / `Penulis (Tahun)` di DOCX adalah hyperlink internal (tetap hitam, tanpa garis bawah) ke visible bookmark entri DP (`Ref_<kunci>` tanpa awalan underscore `_Ref_` dari urutan `.bbl`; panjang `<40` char, mulai huruf). Dilarang: kunci mentah (`(key2020)`), titik ganda (`et al..`), aksen mentah (`Pok{\'e}mon`). Pola pencocokan dari `.aux` natbib (termasuk segmen multi-sitasi dan penulis tunggal); inwarian teruji: teks paragraf tak berubah (snapshot+restore), 0 yatim (anchor tanpa bookmark = FAIL). | A7→A8-G4/G5 | rebuild + perbaiki pola |
| C-CITE-3 | Sitasi tubuh BUKAN teks mati di Google Docs: Saat DOCX di-upload dan di-convert ke Google Docs di Drive, konverter Google kerap membuang hyperlink internal Word. Wajib jalankan `relinkCitationsToDP()` dari `execution/fix_gdocs_citation_links.gs` via Google Docs Apps Script untuk membuat bookmark native Docs (`#bookmark=<id>`) pada tiap entri DP dan menautkan sitasi tubuh (navigasi klik biasa tanpa Ctrl). Audit via `verifyCitationLinks()` wajib menunjukkan 0 tak ber-link. | A7→A8-G4/G5 | jalankan Apps Script di Docs |
| C-LOT-1 | Angka Daftar Isi/Tabel/Gambar Word = angka cetak PDF golden truth (bukan tebakan). Entri LOT/LOF: style TOC + SATU tab kanan-7938-dot (style-level; stop paragraf ganda/konflik dilarang), hyperlink internal ke bookmark caption tubuh (tetap hitam, tanpa garis bawah), tanpa bocoran sintaks LaTeX (`\caption{...}` longtable wajib dirender). Caption tubuh yang hilang = entri tak terhubung = FAIL. | A7→A8-G4/G5 | rebuild + perbaiki generator |
| C-AUDIT-1 | T3 hanya pada 5 trigger; temuan ber-ID F001+ | A9 | tolak audit per-edit (boros) |
| C-KAR-1 | Tiap output: asumsi + alternatif + goal-link + verified-vs-proposed | A0→semua | kembalikan ke agen |
| C-HUM-1 | Remediasi humanisasi (`humanizer-id`, seimbang): tiap suntingan prosa wajib `audit_text.py scan/compare` 0-diff angka/sitasi/ref/kode + baca-akhir user sebelum porting; tanpa janji lolos detektor; detail [[04_Riset_&_Metodologi/PRD_REMEDIASI_AI_70_PERSEN_HUMANIZER.md]] | A0→A4→A7→A8 | kembalikan ke agen, dilarang porting |
| C-LOG-1 | Tiap sesi: pre-flight Graphify+dashboard; post: log + dashboard | A11 | sesi dianggap tidak terjadi |

---

## 5. Skill Registry (dari `execution/*.py` / `*.gs` — pakai sebelum tulis skrip baru)

| Skill | Script | Dipakai oleh |
|---|---|---|
| `skill-build-word` (hybrid Pandoc OMML, dual-mode) | `build_proposal_word.py` | A7 |
| `skill-build-pdf-nobab3` (xelatex×3, hash-check) | `build_proposal_nobab3_pdf.py` | A7 |
| `skill-sync-md` (TeX→MD, Tabel 2.1/3.1/3.2) | `sync_markdown_from_tex.py` | A7 |
| `skill-gdocs-citation-linker` (Native Google Docs Apps Script relink, bookmark `#bookmark=<id>`, idempoten) | `fix_gdocs_citation_links.gs` | A7, A8 |
| `skill-fig-bab1` (300/400 DPI, palet UKRIDA) | `generate_bab1_figures.py` | A1, A3 |
| `skill-journal-catalog` | `generate_journal_catalog.py` | A3 |
| `skill-mendeley-gen` (55 ref, whitelist, UTF-8) | `generate_mendeley_library.py` | A7, A8 |
| `skill-verify-mendeley` (7 tes) | `verify_mendeley_integrity.py` | A8-G1 |
| `skill-verify-url` (blacklist + live) | `verify_live_urls.py` | A8-G2 |
| `skill-verify-all-links` (DOI/URL 0-DEAD + saran Crossref) | `verify_all_citation_links.py` | A3, A8 (C-LINK-1) |
| `skill-resolve-urls` (Crossref + live-check DOI) | `resolve_mendeley_urls.py` | A3 |
| `skill-mendeley-push` (OAuth + push + sync-links + prune) | `mendeley_connector.py` | A8 |
| `skill-verify-ukrida` (7 pilar) | `verify_ukrida_compliance.py` | A8-G3 |
| `skill-verify-typo` (pure-black, TOC 14cm) | `verify_docx_typography.py` | A8-G4 |
| `skill-verify-parity` (NoBab3 vs Full) | `verify_pdf_docx_parity.py` | A8-G5 |
| `skill-verify-outline` (H1/H2/H3 lvl) | `verify_word_outline.py` | A8-G6 |
| `skill-verify-books` (LibGen) | `verify_book_sources.py` + `download_libgen_books.py` | A8-G7 |
| `skill-verify-headers` (`%PDF` massal) | `verify_pdf_headers.py` | A3 |
| `skill-fidelity-compare` (PDF↔DOCX statistik) | `compare_pdf_docx_fidelity.py` | A7, A8 |
| `skill-proofing-scan` (T2 heuristic) | `paper-audit/scripts/proofing_scan.py` | A9 |
| `skill-construct-mine` (keyword seminal) | `analyze_completeness_construct.py` | A4 |
| `skill-study-suite` (web interaktif) | `build_interactive_presentation.py` + `build_study_guide_pdf.py` | A10 |
| `skill-format-forensic` (margin/font/typo) | `verify_format_and_typos.py` + `verify_word_layout.py` + `verify_nobab3_pdf.py` | A8 |
| `skill-humanize-id` (audit `scan`/`compare`, seimbang, fidelity; C-HUM-1) | `humanizer-id/scripts/audit_text.py` | A4, A9 |

**Self-anneal loop (wajib):** error → perbaiki skrip → uji ulang → update directive terkait. Jangan manipulasi manual jika bisa diskrip. Jangan buat skrip baru jika skill sudah ada.

---

## 6. Goal-Driven Execution Checklist (dibaca A0 tiap handoff)

- [ ] GOAL-link tertulis (RQ/H ke-...)?
- [ ] Asumsi material + alternatif interpretasi tertulis?
- [ ] Acceptance criteria observable (angka, bukan "rapi")?
- [ ] Verified vs Proposed dipisah?
- [ ] Falsifier diisi (untuk inference)?
- [ ] Tidak ada skipped-check yang diklaim pass?
- [ ] Kesederhanaan dipilih (tolak metode overkill)?
- [ ] Perubahan surgical (file lain tidak ikut rusak — cek `git status`/hash)?

---

## 7. Contoh Instansiasi (Pokémon TCG — bukti framework jalan)

- Q: Pengaruh X1/X2/X3 → Y dengan M=Self-Control (kolektor Indonesia).
- Canon: Statista chart 24277 (US$100M #1) + Pokémon Co figures (64.8M, 93 wilayah) + PriceCharting Shining Fates (disparitas Raw vs PSA10 2.0–26.0x).
- Evidence difalsifikasi: ICv2 41.5% → terbukti fiktif → dieliminasi (55 ref, zero-hallucination).
- Scope: data global ≠ klaim nasional; purposive 120–150 ≠ sensus.
- Target: booster pack fisik Rp20–30rb vs SAR Rp500rb–3jt; grading PSA/BGS/CGC.
- Audit: Prism 11 temuan → Model 1/2 frozen + mean-centering + UU 24/2013; paper-audit EXEMPLARY (0 Critical); 7/7 verifier PASS; PDF 55/37 hlm.

---

## 8. File Map (jejak ke PRD asal — tiap klaim di atas terlacak)

- Pyramid + Canon + Ledger → `empirical_source_verification.md`, `PRD_ELIMINASI_SUMBER_PALSU*`, `VERIFIED_EMPIRICAL_DATA.md`, `PRD_STANDARISASI_URL*`, `PRD_SUBSTITUSI_GAMBAR_1_3*`.
- Interpretation rules + Fase → `REUSABLE_THESIS_PLAYBOOK.md`, `PRD_AI_Dosen_Pembimbing_Skripsi_v2.md`, `PRD_PENELITIAN.md`, `SOURCE_OF_TRUTH.md`, `MASTER_GUIDE_SKRIPSI.md`.
- Construct → `review_desire_for_completeness.md`, `analyze_completeness_construct.py`, Tabel 2.1.
- Method/Stats → `PRD_RESOLUSI_REVIEW_TEKNIS_PRISM_AI.md` (Model 1/2, N, mean-centering, Tabel 3.2).
- Manuscript → `PRD_HYBRID_PANDOC*`, `PRD_SINKRONISASI*`, `PRD_REVISI_DOCX*`, `PRD_DOCX_HEADING*`, `PANDUAN_STANDARISASI_HEADING*`, `generate_thesis_word_document.md`, `build_*_without_chapter3.md`, `audit_pdf_vs_docx_fidelity.md`, `PRD_AUDIT_PDF_VS_DOCX.md`.
- Parity → `mandatory_thesis_sync_and_quality.md`, `PRD_SISTEM_INTEGRITAS_MENDELEY*`, `verify_mendeley_integrity.md`, `verify_ukrida_2023_guidelines.md`, `PRD_AUDIT_DAN_PENYELARASAN_PEDOMAN*`.
- Audit → `PRD_INTEGRASI_SKILL_PAPER_AUDIT.md`, `run_paper_audit.md`.
- Defense → `generate_interactive_study_presentation.md`, `update_study_guide_and_pdf.md`.
- Memory → `obsidian_second_brain.md`, `00_DASHBOARD_SECOND_BRAIN.md`, `LOG_SESI_SECOND_BRAIN.md`, `3_layer_architecture.md`.
- Books → `PRD_VERIFIKASI_SUMBER_BUKU*`, `PRD_DOWNLOAD_BUKU*`, `verify_book_sources_libgen.md`, `mandatory_verifiable_theories_and_books.md`, `no_login_wall_empirical_sources.md`.
