> [!SUMMARY] Tujuan & Solusi Catatan Ini
> - **Untuk Apa:** PRD remediasi skor kemiripan AI 70% pada `[[05_Pedoman_&_Referensi/hasil-cek-ai-Proposal_Arthur_PokemonTCG (1).pdf]]` menjadi ambang praktik kampus ≤20% memakai skill `humanizer-id` yang terintegrasi framework universal.
> - **Masalah yang Diselesaikan:** Naskah 65 hlm pasca-humanisasi Fase 1–4 masih terdeteksi 70% (probabilitas AI, bukan % teks); perlu rencana terarah tanpa janji lolos detektor, tanpa merusak paritas 54 ref / 245 tautan / ledger D26.
> - **Keputusan/Output:** Rencana 5 fase (Audit → Tulis-ulang → Porting+Paritas → Uji mandiri) + registrasi skill di [[04_Riset_&_Metodologi/PRD_UNIVERSAL_SKRIPSI_FRAMEWORK_GRAPH_OF_AGENTS.md]] (C-HUM-1); eksekusi menunggu persetujuan user per bab.

# PRD Remediasi AI 70% → Ambang Praktik ≤20% (Humanizer-ID × Universal Framework)

> **Otoritas:** [[04_Riset_&_Metodologi/PRD_UNIVERSAL_SKRIPSI_FRAMEWORK_GRAPH_OF_AGENTS.md]] (A0–A11, F1–F11) · [[directives/universal_thesis_graph_of_agents.md]] · [[04_Riset_&_Metodologi/PRD_HUMANISASI_KEASLIAN_TULISAN_AI_20_PERSEN.md]] (PRD induk, Fase 1–4 selesai 18 Sep 2026) · Skill `humanizer-id` (`C:\Users\arthu\.agents\skills\humanizer-id\humanizer-id`) · [[00_DASHBOARD_SECOND_BRAIN.md]] · [[04_Riset_&_Metodologi/SOURCE_OF_TRUTH.md]] (D01–D26)
> **Status:** v1.0 — 18 Sep 2026. Naskah aktif tidak diubah oleh PRD ini (read-only sampai Fase 2 disetujui).

---

## 1. Bukti Masuk (Evidence, A3)

- **Sumber:** [[05_Pedoman_&_Referensi/hasil-cek-ai-Proposal_Arthur_PokemonTCG (1).pdf]] — header `AI Report — Version 2026-06-10-multilingual — We are moderately confident this text is AI Generated — AI Probability 70% — Plagiarism scan was not run`.
- **Interpretasi jujur (wajib):** 70% adalah **probabilitas dokumen diklasifikasikan sebagai AI-generated**, bukan "70% teks adalah AI". Detektor probabilistik, tidak stabil antar-versi, tidak membuktikan kepengarangan. Tidak ada klaim "bagian X = AI".
- **Baseline naskah:** [[01_Naskah_Utama/Proposal_Arthur_PokemonTCG.pdf]] 65 hlm + [[01_Naskah_Utama/Proposal_Arthur_PokemonTCG.docx]] (54 bookmark DP + 245 tautan sitasi-klik) + [[01_Naskah_Utama/PROPOSAL_SKRIPSI_POKEMON_TCG.md]] 984 baris; paritas 54 ref; ledger [[04_Riset_&_Metodologi/EVIDENCE_LEDGER_HALAMAN.md]] PASS; audit Tier-3 [[07_Review_&_Audit/Paper_Audits/review-2026-09-18-213000.md]] 0 terbuka.
- **Scan humanizer-id 18 Sep 2026 (pasca-humanisasi, `audit_text.py scan`):**
  - BAB I (`[[03_Draft_Per_Bab/BAB_I_PENDAHULUAN.md]]`): 19 temuan — H07 struktural dominan (caption/bold sah) + H06 em-dash sah (5) + H10 `komprehensif` (1).
  - BAB II (`[[03_Draft_Per_Bab/BAB_II_TINJAUAN_PUSTAKA.md]]`): 30 temuan — H07 struktural (29: S-O-R, Tabel 2.1, Landasan/Kajian/Keterkaitan per-H) + H06 (1).
  - BAB III (`[[03_Draft_Per_Bab/BAB_III_METODE_PENELITIAN.md]]`): 30 temuan — H07 struktural (28: Tabel 3.1/3.2/3.3, Gambar 3.1, MRA) + H06 (2) + H10 `Komprehensif` (1).
  - **Kesimpulan:** `scan` tidak menjelaskan skor 70% (ia hanya menandai pemicu leksikal). Target remediasi adalah **prosa**: ritme seragam, pembuka generik Latar Belakang, ringkasan berderet Tabel 1.1/2.1, abstraksi menumpuk — sesuai prioritas §5 PRD induk.

## 2. Batas Jujur Mengikat (dari skill humanizer-id, A0)

1. **Tanpa janji lolos detektor / skor keaslian.** Target ≤20% adalah ambang risiko praktik kampus, bukan hasil yang dijamin penyuntingan.
2. **Tanpa curang:** dilarang salah-ketik buatan, tata-bahasa rusak, pengalaman rekaan, kutipan palsu, penghapusan pernyataan AI yang diwajibkan.
3. **Naskah tidak dikirim ke layanan humanizer/detektor eksternal.** Verifikasi lokal (`scan` + `compare` + baca manual).
4. **Makna dibekukan:** angka/satuan, sitasi, DOI/URL, persamaan MRA, label/ref, caption — nol diff tak-disengaja (kontrak fidelity PRD induk §4 + glosarium §6).
5. Pedoman kampus: [[05_Pedoman_&_Referensi/Buku Pedoman Penyusunan Tugas Akhir 2023.md]] mewajibkan Turnitin plagiarisme ≤30%, **tanpa pasal AI** — ambang AI diperlakukan sebagai ketentuan praktik/pembimbing.

## 3. Diagnosis Terarah (A4 + A9, bukan daftar kata terlarang)

Prioritas baca manual memakai taksonomi H01–H20 skill:

1. H13 ritme seragam + H12 daftar dipaksakan — variasi panjang kalimat mengikuti beban informasi (kandidat utama penanda detektor).
2. H04 pembuka pengisi Latar Belakang — mulai dari masalah/fenomena kasir minimarket yang tersedia.
3. H14 penjelasan berulang Y/X1/X2/X3/Z lintas Bab I–III — padatkan via rujukan silang tanpa hapus definisi operasional.
4. H10 abstraksi (`komprehensif` L66 Bab I, L294 Bab III) — ganti verba + objek konkret dari bahan.
5. H11 penghubung otomatis (`oleh karena itu/sehingga`) — pertahankan hanya kausal yang didukung.
6. Ringkasan berderet Tabel 1.1 (7 subjek) + Tabel 2.1 (10 studi) — variasikan pembuka/penutup tiap baris, tegaskan `Verified vs Proposed`, pertahankan dukungan sitasi per-kalimat (Lienardy-H4 genuine; Apidana/Artadita-H3 gagal-moderasi; 6A/7A tak-langsung eksplisit).

## 4. Rencana 5 Fase (terpetakan ke Universal F1–F11)

- **Fase R0 — Bekukan scope (A0/A1, 0,5 sesi).** Scope: prosa Bab I–III + abstrak; urutan III→II→I. Out-of-scope: `references.bib`, sitasi, angka, persamaan, caption, ledger. *Gerbang:* user setuju scope + kedalaman seimbang.
- **Fase R1 — Audit terarah per bab, mode audit saja (A9, 3 sesi).** `scan` → baca ±5 baris → tulis `.tmp/humanize/AUDIT_R1_B{III,II,I}.md` (lokasi|ID|potongan|dampak|tindakan|batas bukti). Bedakan makna/bukti vs gaya. *Gerbang:* AUDIT disetujui user; ambiguitas jadi pertanyaan, bukan tebakan.
- **Fase R2 — Tulis-ulang seimbang di salinan (A4/A5, 3 sesi).** Salin ke `B.humanized-R1.md`; sunting salinan saja; jaga kontrak fidelity + glosarium + EYD V; `compare` 0 diff angka/sitasi/ref/kode. *Gerbang per bab:* user terima/tolak per bagian (tanpa auto-porting); user wajib bisa mempertahankan tiap kalimat di sidang (Lampiran 4 Orisinalitas).
- **Fase R3 — Porting + paritas workspace (A7/A8, 1–2 sesi).** Porting prosa disetujui ke master TeX → `xelatex+bibtex` → `sync_markdown_from_tex.py` → `build_proposal_word.py` → verifier (`verify_docx_typography`, `verify_pdf_docx_parity`, `verify_intext_citations`, `verify_italic_typography`, `verify_mendeley_integrity`, `verify_evidence_ledger`) semua PASS (toleransi: FAIL NoBab3 sesuai Opsi-1). *Gerbang:* `run_thesis_graph.py --gate parity` konsep 7/7 (di luar pengecualian NoBab3).
- **Fase R4 — Serah terima + uji mandiri (A10/A11, 0,5 sesi).** Tabel sebelum/sesudah substantif + klaim ditahan + update [[04_Riset_&_Metodologi/LOG_SESI_SECOND_BRAIN.md]] + dashboard. Pengujian ≤20% **mandiri oleh user di sistem resmi kampus** terhadap dokumen final. Bila masih >ambang: kirim **bagian yang ditandai sistem + konteksnya** untuk perbaikan terarah (bukan parafrasa buta).

## 5. Implementation Plan Konkret (Layer 3)

```powershell
# R1 audit (dari root repo):
py "C:\Users\arthu\.agents\skills\humanizer-id\humanizer-id\scripts\audit_text.py" scan "03_Draft_Per_Bab\BAB_III_METODE_PENELITIAN.md"
py "C:\Users\arthu\.agents\skills\humanizer-id\humanizer-id\scripts\audit_text.py" scan "03_Draft_Per_Bab\BAB_II_TINJAUAN_PUSTAKA.md"
py "C:\Users\arthu\.agents\skills\humanizer-id\humanizer-id\scripts\audit_text.py" scan "03_Draft_Per_Bab\BAB_I_PENDAHULUAN.md"
# R2 compare (setelah salinan disunting):
py "C:\Users\arthu\.agents\skills\humanizer-id\humanizer-id\scripts\audit_text.py" compare "03_Draft_Per_Bab\BAB_III_METODE_PENELITIAN.md" ".tmp\humanize\BAB_III_METODE_PENELITIAN.humanized-R1.md"
# R3 porting + paritas:
py execution/sync_markdown_from_tex.py
py execution/build_proposal_word.py
py execution/verify_docx_typography.py
py execution/verify_pdf_docx_parity.py
py execution/verify_evidence_ledger.py
py execution/run_thesis_graph.py --gate parity
```

## 6. Acceptance Criteria (observable, A0 hygiene)

- [ ] 100% temuan R1 berstatus ditangani/ditahan-beralasan (nol menggantung).
- [ ] `compare` per bab: 0 diff tak-disengaja angka/sitasi/ref/URL/DOI/LaTeX.
- [ ] Seluruh verifier R3 PASS (dengan toleransi NoBab3 yang dinyatakan).
- [ ] Baca-akhir user: "lebih mudah dimengerti, makna dan suara utuh".
- [ ] Uji mandiri kampus oleh user tercatat (tanggal + sistem + skor + bagian ditandai bila ada).

## 7. Integrasi ke PRD Universal (surgical, aditif)

- **Skill baru:** `skill-humanize-id` (audit `scan`/`compare`, kedalaman seimbang, kontrak fidelity) → dipakai A4/A9, digate di F9/R3. Didaftarkan di §5 PRD Universal.
- **Chained rule baru C-HUM-1:** setiap suntingan prosa wajib `compare` 0-diff angka/sitasi/ref + baca-akhir user sebelum porting; skipped-check ≠ pass; tanpa janji detektor. Ditegakkan A0→A4→A7→A8.
- **Arsitektur 3-Layer:** Layer 1 directive = PRD ini + PRD induk; Layer 2 orchestration = agen A0/A4/A7–A11 bab-per-bab; Layer 3 execution = `audit_text.py` + `sync/build/verify_*.py` + `run_thesis_graph.py`.
