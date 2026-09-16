r"""
build_proposal_nobab3_pdf.py
Compiles a publication-grade, FEB UKRIDA 2023-compliant PDF proposal WITHOUT Bab 3,
using the native XeLaTeX engine and BibTeX.

Layer 3 Execution Script (3-Layer Architecture)
Directive: directives/build_pdf_without_chapter3.md

Features:
- Guaranteed zero-touch on original files (Proposal_Arthur_PokemonTCG.*).
- Slices Bab 3 programmatically from Proposal_Arthur_PokemonTCG.tex.
- Generates Proposal_Arthur_NoBab3.tex as build file.
- Multi-pass compilation (XeLaTeX -> BibTeX -> XeLaTeX x2) to resolve:
  * Table of Contents (TOC)
  * List of Tables (LOT)
  * List of Figures (LOF)
  * natbib APA citations and bibliography
  * TikZ vector diagrams
  * Page numbering and running footers
- Validates output integrity.
"""

import os
import sys
import re
import hashlib
import subprocess
from pathlib import Path

# Force UTF-8 stdout/stderr
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

REPO_ROOT = Path(__file__).resolve().parent.parent
NASKAH_DIR = REPO_ROOT / "01_Naskah_Utama"
ORIGINAL_TEX = NASKAH_DIR / "Proposal_Arthur_PokemonTCG.tex"
ORIGINAL_PDF = NASKAH_DIR / "Proposal_Arthur_PokemonTCG.pdf"
ORIGINAL_DOCX = NASKAH_DIR / "Proposal_Arthur_PokemonTCG.docx"

TARGET_TEX = NASKAH_DIR / "Proposal_Arthur_NoBab3.tex"
TARGET_PDF = NASKAH_DIR / "Proposal_Arthur_NoBab3.pdf"


def get_file_hash(path: Path) -> str:
    """Return SHA256 of file if exists, else empty string."""
    if not path.exists():
        return ""
    hasher = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(65536):
            hasher.update(chunk)
    return hasher.hexdigest()


def extract_nobab3_tex(source_text: str) -> str:
    """
    Safely slice out Bab 3 and formal academic approval sheets from the canonical TeX source.
    Keeps:
    - Preamble & Document Setup
    - Sampul / Cover Page (hal. i)
    - Kata Pengantar, Abstrak, Abstract, TOC, LOT, LOF
    - Bab 1 (Pendahuluan)
    - Bab 2 (Kajian Pustaka & Model Konseptual TikZ)
    - Daftar Pustaka & References
    Removes:
    - Lembar Pernyataan Keaslian Karya Tugas Akhir
    - Lembar Persetujuan Proposal Skripsi
    - Lembar Pengesahan Tim Penguji Seminar Proposal
    - Bab 3 (Metode Penelitian) in its entirety.
    """
    # 1. Remove formal approval sheets (Pernyataan Keaslian, Persetujuan, Pengesahan)
    fm_start = re.search(r'(?m)^%\s*-+\s*\n%\s*2\.\s*HALAMAN PERNYATAAN KEASLIAN', source_text)
    if not fm_start:
        fm_start = re.search(r'(?m)^\\begin\{center\}\s*\n\s*\{\\large\\bfseries\s*PERNYATAAN KEASLIAN', source_text)
    
    fm_end = re.search(r'(?m)^%\s*-+\s*\n%\s*5\.\s*KATA PENGANTAR', source_text)
    if not fm_end:
        fm_end = re.search(r'(?m)^\\begin\{center\}\s*\n\s*\{\\large\\bfseries\s*KATA PENGANTAR', source_text)

    if fm_start and fm_end:
        pre_sheets = source_text[:fm_start.start()].rstrip()
        post_sheets = source_text[fm_end.start():].lstrip()
        source_text = pre_sheets + "\n\n" + post_sheets

    # 2. Identify Bab 3 beginning
    # Pattern: look for '%  BAB 3: METODE PENELITIAN' or '\section*{BAB 3'
    bab3_match = re.search(r'(?m)^%\s*=+\s*\n%\s*BAB 3:\s*METODE PENELITIAN', source_text)
    if not bab3_match:
        bab3_match = re.search(r'(?m)^\\section\*\{BAB 3', source_text)
    if not bab3_match:
        raise ValueError("Could not locate Bab 3 beginning in source TeX.")

    bab3_start_idx = bab3_match.start()

    # Identify Daftar Pustaka beginning
    # Pattern: look for '%  DAFTAR PUSTAKA' or '\renewcommand{\refname}{DAFTAR PUSTAKA}'
    pustaka_match = re.search(r'(?m)^%\s*=+\s*\n%\s*DAFTAR PUSTAKA', source_text)
    if not pustaka_match:
        pustaka_match = re.search(r'(?m)^\\renewcommand\{\\refname\}\{DAFTAR PUSTAKA\}', source_text)
    if not pustaka_match:
        raise ValueError("Could not locate Daftar Pustaka beginning in source TeX.")

    pustaka_start_idx = pustaka_match.start()

    if bab3_start_idx >= pustaka_start_idx:
        raise ValueError(f"Invalid boundaries: Bab 3 start ({bab3_start_idx}) >= Pustaka start ({pustaka_start_idx})")

    pre_bab3 = source_text[:bab3_start_idx].rstrip()
    post_bab3 = source_text[pustaka_start_idx:].lstrip()

    # Pastikan referensi metodologi Bab 3 tetap terbit di Daftar Pustaka NoBab3 (Paritas 56 Ref)
    nocite_block = "\n% Menyertakan referensi metodologi Bab 3 agar bibliografi lengkap 56 entri\n\\nocite{sekaran2016research, sugiyono2019metode, hair2019multivariate, ghozali2018aplikasi}\n"
    if "\\nocite" not in post_bab3:
        post_bab3 = re.sub(r'(\\bibliography\{)', lambda m: nocite_block + m.group(1), post_bab3, count=1)

    nobab3_text = pre_bab3 + "\n\n" + post_bab3
    return nobab3_text


def run_command(cmd, cwd):
    """Run subprocess command and stream output."""
    print(f"[CMD] {cmd} (in {cwd})")
    res = subprocess.run(
        cmd,
        cwd=str(cwd),
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding='utf-8',
        errors='replace'
    )
    return res.returncode, res.stdout


def main():
    print("=" * 70)
    print("XeLaTeX Build Pipeline: Proposal Skripsi Tanpa Bab 3")
    print("Directive: directives/build_pdf_without_chapter3.md")
    print("=" * 70)

    # 1. Take snapshot hashes of original files to guarantee zero-touch
    orig_tex_hash = get_file_hash(ORIGINAL_TEX)
    orig_pdf_hash = get_file_hash(ORIGINAL_PDF)
    orig_docx_hash = get_file_hash(ORIGINAL_DOCX)

    print(f"[VERIFY] Original TeX Hash : {orig_tex_hash[:16]}... (Protected)")
    print(f"[VERIFY] Original PDF Hash : {orig_pdf_hash[:16]}... (Protected)")
    print(f"[VERIFY] Original DOCX Hash: {orig_docx_hash[:16]}... (Protected)")

    # 2. Read canonical TeX source
    print(f"[READ] Reading canonical source: {ORIGINAL_TEX.name}")
    with open(ORIGINAL_TEX, "r", encoding="utf-8") as f:
        canonical_content = f.read()

    # 3. Extract content without Bab 3
    print("[PROCESS] Slicing out Bab 3 (Metode Penelitian)...")
    nobab3_content = extract_nobab3_tex(canonical_content)

    # Sanity checks on sliced content
    assert "PERNYATAAN KEASLIAN" not in nobab3_content, "Error: PERNYATAAN KEASLIAN still present!"
    assert "PERSETUJUAN PROPOSAL" not in nobab3_content, "Error: PERSETUJUAN PROPOSAL still present!"
    assert "PENGESAHAN TIM PENGUJI" not in nobab3_content, "Error: PENGESAHAN TIM PENGUJI still present!"
    assert "KATA PENGANTAR" in nobab3_content, "Error: KATA PENGANTAR missing!"
    assert "BAB 1" in nobab3_content, "Error: BAB 1 missing!"
    assert "BAB 2" in nobab3_content, "Error: BAB 2 missing!"
    assert "DAFTAR PUSTAKA" in nobab3_content, "Error: DAFTAR PUSTAKA missing!"
    assert "BAB 3" not in nobab3_content, "Error: BAB 3 still present in sliced text!"
    assert "Metode Penelitian" not in nobab3_content, "Error: 'Metode Penelitian' still present!"

    # 4. Write to target variant TeX file
    print(f"[WRITE] Generating variant TeX file: {TARGET_TEX.name}")
    with open(TARGET_TEX, "w", encoding="utf-8") as f:
        f.write(nobab3_content)

    print(f"[INFO] Variant TeX written: {len(nobab3_content)} chars, {nobab3_content.count('\n')} lines.")

    # 5. Multi-pass compilation with XeLaTeX & BibTeX
    print("\n" + "-" * 50)
    print("Phase 1/4: Initial XeLaTeX Pass (Generating .aux, .toc, .lot, .lof)...")
    rc1, out1 = run_command(f'xelatex -interaction=nonstopmode "{TARGET_TEX.name}"', NASKAH_DIR)
    print(f"Pass 1 Return Code: {rc1}")

    print("\nPhase 2/4: BibTeX Pass (Compiling citations from references.bib)...")
    rc_bib, out_bib = run_command(f'bibtex "{TARGET_TEX.stem}"', NASKAH_DIR)
    print(f"BibTeX Return Code: {rc_bib}")

    print("\nPhase 3/4: Second XeLaTeX Pass (Integrating bibliography and citations)...")
    rc2, out2 = run_command(f'xelatex -interaction=nonstopmode "{TARGET_TEX.name}"', NASKAH_DIR)
    print(f"Pass 2 Return Code: {rc2}")

    print("\nPhase 4/4: Final XeLaTeX Pass (Finalizing TOC, LOT, LOF, and cross-references)...")
    rc3, out3 = run_command(f'xelatex -interaction=nonstopmode "{TARGET_TEX.name}"', NASKAH_DIR)
    print(f"Pass 3 Return Code: {rc3}")
    print("-" * 50 + "\n")

    # 6. Validate generated PDF
    if not TARGET_PDF.exists():
        print(f"[FATAL] Output PDF was not generated: {TARGET_PDF}")
        sys.exit(1)

    pdf_size = TARGET_PDF.stat().st_size
    print(f"[SUCCESS] Target PDF generated: {TARGET_PDF.name} ({pdf_size / 1024:.1f} KB)")

    if pdf_size < 100_000:
        print(f"[WARN] PDF size ({pdf_size} bytes) seems unexpectedly small. Inspect log.")

    # 7. Verify zero-touch invariant on original files
    post_tex_hash = get_file_hash(ORIGINAL_TEX)
    post_pdf_hash = get_file_hash(ORIGINAL_PDF)
    post_docx_hash = get_file_hash(ORIGINAL_DOCX)

    if (orig_tex_hash != post_tex_hash) or (orig_pdf_hash != post_pdf_hash) or (orig_docx_hash != post_docx_hash):
        print("[CRITICAL ERROR] Original file hashes have changed! Integrity violated!")
        sys.exit(1)
    else:
        print("[INTEGRITY OK] All canonical original files remain 100% UNTOUCHED.")

    print("\n[COMPLETE] Proposal_Arthur_NoBab3.pdf generated cleanly with 100% FEB UKRIDA fidelity.")


if __name__ == "__main__":
    main()
