# Mandatory Rule: Zero Raw LaTeX Leakage & Native APA 7 Tables in Word (.docx)

> **STATUS: INVIOLABLE PERMANENT DIRECTIVE**
> Every assistant, agent, and subagent modifying the thesis MUST read, comply with, and verify against this rule.
> Canonical PRDs:
> - [[04_Riset_&_Metodologi/PRD_REVISI_DOCX_KUALITAS_LATEX.md]]
> - [[04_Riset_&_Metodologi/PRD_SINKRONISASI_DOCX_DAN_AUDIT_FILE.md]]
> - [[directives/generate_thesis_word_document.md]]

---

## 1. Core Principle: Zero Raw LaTeX Tokens in Word Documents

Under NO circumstances may raw LaTeX syntax, environments, table markup, math delimiters, or escaping backslashes be rendered as literal body paragraphs or table cell text in Microsoft Word (`.docx`) documents.

### A. Prohibited Syntax in DOCX Body & Tables
The following tokens must NEVER appear in paragraph text or table cells of `.docx`:
- **LaTeX Environments**: `\begin{...}`, `\end{...}`, `\begingroup`, `\endgroup`, `\begin{longtable}`, `\begin{table}`, `\begin{figure}`, `\begin{flushleft}`.
- **Booktabs & Table Tokens**: `\toprule`, `\midrule`, `\bottomrule`, `\multicolumn`, `\addlinespace`, `\endhead`, `\endfoot`, `\endlastfoot`, raw row separators `\\`, raw column separators `&`.
- **Formatting Commands**: `\small`, `\footnotesize`, `\centering`, `\raggedright`, `\emph{...}`, `\textbf{...}`, `\caption{...}`, `\label{...}`.
- **Math Commands & Arrows**: `\rightarrow`, `\leftarrow`, `\Rightarrow`, `\ge`, `\le`, `\cdot`, `\alpha`, `\beta`, `\Delta`, `\partial`, `\epsilon`.
- **Escaped Characters & Math Delimiters**: Raw `$` math enclosures, `\#`, `\%`, `\&`, `\_`, `0{,}092`, `n.s.\ `.

### B. Standard Replacement Mapping
Every generator script (`execution/build_proposal_word.py` and `execution/sync_markdown_from_tex.py`) must convert TeX syntax to clean unicode typography before inserting runs:
| Raw LaTeX Syntax | Required Word Typography |
| :--- | :--- |
| `\rightarrow`, `$\rightarrow$` | `→` |
| `\leftarrow`, `$\leftarrow$` | `←` |
| `\ge`, `$\ge$` | `≥` |
| `\le`, `$\le$` | `≤` |
| `\cdot`, `$\cdot$` | `·` |
| `0{,}092`, `0{,}60` | `0,092`, `0,60` |
| `n.s.\ ` | `n.s. ` |
| `\beta_1` | `β₁` |
| `$X_1$`, `$X_2$`, `$X_3$`, `$M$`, `$Y$` | `*X*₁`, `*X*₂`, `*X*₃`, `*M*`, `*Y*` |
| `(\emph{The Why*):}` | `(*The Why*):` |

---

## 2. Table Construction Standard: Native APA 7th Edition

All tables in the thesis (Tabel 1.1, Tabel 2.1, Tabel 3.1, Tabel 3.2, Tabel 3.3) must be built as **native Microsoft Word tables** via `python-docx` (`doc.add_table()`), adhering strictly to APA 7th Edition open format:
1. **Borders**:
   - Top horizontal border: 1.0 pt solid black (`#000000`).
   - Header bottom border: 0.75 pt solid black (`#000000`).
   - Table bottom border: 1.0 pt solid black (`#000000`).
   - **Zero Vertical Borders**: Strictly forbidden inside or outside the table.
2. **Typography & Width**:
   - Header: Times New Roman 10 pt Bold, Centered, pure black (`#000000`), shading `#F2F2F2`.
   - Cell Content: Times New Roman 9.5 pt–10 pt Regular, Justified/Left, pure black (`#000000`), line spacing 1.0, space after 2 pt.
   - Total table width must match printable text width (14.0 cm). Column widths must be set explicitly per cell.
3. **Repeat Header Across Pages**:
   - Header row must contain `<w:tblHeader/>` to repeat automatically if the table spans multiple pages.
   - `<w:cantSplit/>` must be set on all rows to prevent awkward line breaks across page boundaries.

---

## 3. Formal Academic Frontmatter Standards

Formal approval and statement sheets on `Proposal_Arthur_PokemonTCG.docx` must meet publication-grade layout standards:
1. **Identity Tables (`tbl_id`, `tbl_per`)**:
   - Must be 100% borderless (`remove_table_borders(table)`).
   - Fixed column widths: `[Cm(3.8), Cm(0.4), Cm(9.8)]` (total 14.0 cm).
   - Left table margin set to 0 to align flush with the left text margin (4.0 cm page margin).
   - Colons (`:`) must sit snugly at 3.8 cm, never floating in the center of the page.
2. **Signature Approval Block (`tbl_apv`)**:
   - Must be 100% borderless.
   - Widths: `[Cm(7.0), Cm(7.0)]`.
   - **Mandatory 3-Row Architecture**:
     - Row 0 (Titles): "Menyetujui,\nDosen Pembimbing Skripsi," (Col 0) and "Mengetahui,\nKetua Program Studi S1 Manajemen," (Col 1).
     - Row 1 (Signature space): Empty row with exact height 55 pt (`<w:trHeight w:val="1100" w:hRule="exact"/>`).
     - Row 2 (Signatory details): Full Name (bold, underlined) and NIDN.
   - **Never use a 1-row table with manual `\n` newlines** for signatures, as differing title wraps will break horizontal baseline symmetry.

---

## 4. Mandatory Pre-Flight Verification Gate

Before completing any task, delivering any `.docx` file, or notifying the user:
```bash
python execution/verify_docx_typography.py
```
**Verification Requirements**:
- `Proposal_Arthur_NoBab3.docx`: 0 fatal LaTeX errors, 0 stray asterisks, 0 theme colors, valid dot leaders.
- `Proposal_Arthur_PokemonTCG.docx`: 0 fatal LaTeX errors, 0 frontmatter border leaks, 0 stray asterisks, 0 theme colors, valid dot leaders.
- Exit code must be `0` (`ALL WORD DOCUMENTS PASSED PUBLICATION-GRADE VERIFICATION!`).
