# Mandatory Rule: Thesis Synchronization, Parity, & LaTeX-Grade Quality

> **STATUS: INVIOLABLE PERMANENT DIRECTIVE**
> Every assistant, agent, and subagent modifying the thesis MUST read, comply with, and verify against this rule.
> Canonical PRDs:
> - [[04_Riset_&_Metodologi/PRD_SINKRONISASI_DOCX_DAN_AUDIT_FILE.md]]
> - [[04_Riset_&_Metodologi/PRD_REVISI_DOCX_KUALITAS_LATEX.md]]
> - [[directives/generate_thesis_word_document.md]]

---

## 1. Core Principles (Zero Regressions)

Whenever any modification is made to the thesis (content, hypotheses, tables, figures, bibliography, or formatting), the following rules MUST be strictly enforced:

### A. Single Source of Truth & Zero Desync
1. **LaTeX Master**: `01_Naskah_Utama/Proposal_Arthur_NoBab3.tex` (compiled into `Proposal_Arthur_NoBab3.pdf`) is the definitive master (*Golden Reference*).
2. **Word Parity**: `Proposal_Arthur_NoBab3.docx` and `Proposal_Arthur_PokemonTCG.docx` must match the LaTeX master with 100% fidelity.
3. **Synchronous Update**: If LaTeX changes, `execution/build_proposal_word.py` and `01_Naskah_Utama/PROPOSAL_SKRIPSI_POKEMON_TCG.md` must be regenerated and validated immediately.

### B. Pure Black Color (#000000) & Zero Theme Colors
- No `w:themeColor`, `w:themeTint`, or `w:themeShade` in any style or run.
- All headings (`Heading 1`, `Heading 2`, `Heading 3`), frontmatter titles (`DAFTAR ISI`, `DAFTAR TABEL`, `DAFTAR GAMBAR`, `KATA PENGANTAR`, `ABSTRAK`), body paragraphs, table headers/cells, figure captions, and footers MUST have explicit `<w:color w:val="000000"/>` (`RGBColor(0, 0, 0)`).
- This prevents headings from turning blue in Google Docs, Word Online, or default desktop Word templates.

### C. Universal Table of Contents (TOC), LOT, & LOF Compatibility
1. **Zero Right Indent (`right_indent = 0`)**:
   - Never set `right_indent` on TOC, LOT, or LOF paragraphs (e.g. `right_indent = Cm(0.8)` is STRICTLY FORBIDDEN).
   - Printable text width is exactly 14.0 cm (A4 width 21.0 cm - left 4.0 cm - right 3.0 cm = 14.0 cm = 7938 dxa).
   - Setting a right indent contracts the paragraph boundary, causing Google Docs and web/mobile viewers to discard the 14.0 cm tab stop and drop all dot leaders.
2. **Tab Stop & Dot Leader Attributes**:
   - Must contain `<w:tab w:val="right" w:leader="dot" w:pos="7938"/>`.
3. **Dedicated XML Run Structure**:
   - Title run: `<w:r><w:t xml:space="preserve">{title}</w:t></w:r>`
   - Tab run: dedicated `<w:r><w:tab/></w:r>`
   - Page number run: dedicated `<w:r><w:t>{page}</w:t></w:r>`
4. **Wrap in Standard Word TOC SDT (`<w:sdt>`)**:
   - The TOC block must be wrapped in standard Structured Document Tag markup for native Google Docs and Word interoperability.

### D. Strict Dual-Mode Separation
1. **Review Variant (`Proposal_Arthur_NoBab3.docx` / `.pdf`)**:
   - CLI flag: `--no-chapter3` (`skip_chapter3=True`).
   - NO Bab 3 (Metode Penelitian).
   - NO formal sheets (Pernyataan Keaslian, Lembar Persetujuan, Lembar Pengesahan).
   - Frontmatter starts at `ii` (Kata Pengantar).
   - Bab 1 ends at page 10, Bab 2 ends at page 20, Daftar Pustaka at page 21.
2. **Full Variant (`Proposal_Arthur_PokemonTCG.docx` / `.pdf`)**:
   - Contains Bab 1, Bab 2, Bab 3, and Daftar Pustaka.
   - Contains formal academic sheets.

---

## 2. Mandatory Pre-Completion Audit

Before closing ANY task or response that modifies the skripsi, the assistant MUST execute:
```bash
python execution/verify_docx_typography.py
python execution/verify_pdf_docx_parity.py
```
Both scripts must return `[PASS]`. If any audit fails, the assistant must self-anneal and resolve the issue before finishing.
