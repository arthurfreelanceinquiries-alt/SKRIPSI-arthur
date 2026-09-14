# Directive: Curate, Generate, and Integrate Empirical Market Graphics for Bab 1

## Goal
Curate verified empirical market data, generate publication-grade 300 DPI graphics matching the academic standards of FEB UKRIDA 2023 (Model B) and senior student benchmarks, and seamlessly integrate them into XeLaTeX (`Proposal_Arthur_PokemonTCG.tex`), Word DOCX (`build_proposal_word.py`), and Markdown proposals.

## Inputs
1. **PRD Specification:** `04_Riset_&_Metodologi/PRD_GRAFIK_EMPIRIS_BAB1.md`
2. **Primary Data Sources:**
   - The Pokémon Company Corporate Business Data (Cumulative card production 2019–2024: 28.8B -> 64.8B).
   - Statista & TitleMax All-Time Media Franchise Revenue Database (Pokémon #1 with >$105B).
   - ICv2 / TCGplayer Market Share Analysis.
3. **Target Documents:**
   - `01_Naskah_Utama/Proposal_Arthur_PokemonTCG.tex`
   - `01_Naskah_Utama/PROPOSAL_SKRIPSI_POKEMON_TCG.md`
   - `03_Draft_Per_Bab/BAB_I_PENDAHULUAN.md`
   - `execution/build_proposal_word.py`

## Tools & Execution Scripts (Layer 3)
- **Graphic Generator:** `execution/generate_bab1_figures.py`
  - Uses `matplotlib`, `seaborn`, `PIL`
  - Output files:
    - `01_Naskah_Utama/images/gambar1_1_media_franchise_ranking.png`
    - `01_Naskah_Utama/images/gambar1_2_pokemon_tcg_production_growth.png`
- **Word DOCX Builder:** `execution/build_proposal_word.py`
- **Typography & Layout Verifier:** `execution/verify_docx_typography.py`
- **LaTeX Compiler:** `xelatex` / `latexmk`

## Standards & Formatting Rules
1. **Resolution & Canvas:**
   - 300 DPI, clean vector-like rasterization, width 13.0–13.5 cm.
   - Font: Times New Roman exclusively.
2. **Academic Color Palette:**
   - Deep Academic Navy (`#1A365D`), Slate Grey (`#4A5568`), Warm Amber (`#D69E2E`), Muted Crimson (`#9B2C2C`).
3. **Caption & Numbering Placement:**
   - Below the graphic, centered: `Gambar 1.1: [Judul]`
   - Followed immediately by: `Sumber: [Lembaga] ([Tahun])`
4. **List of Figures (Daftar Gambar):**
   - Automatically included in `\listoffigures` (PDF) and Word frontmatter table with page numbers and dot leaders.
5. **Academic Narrative:**
   - Bab 1 text must explicitly cite and interpret `Gambar 1.1` and `Gambar 1.2`.
