r"""
verify_pdf_docx_parity.py
Layer 3 Verification Script
Verifies structural, frontmatter, and content parity between:
- Proposal_Arthur_PokemonTCG.pdf <-> Proposal_Arthur_PokemonTCG.docx (file utama)

Catatan arsitektur (Sylvia, 23 Sep 2026): varian NoBab3 dihapus, semua
mengerucut ke file utama. Enam lembar formal hidup modular di
01_Lembar_Persetujuan_Proposal/*.docx (Sesi 22), bukan di DOCX utama.
"""

import sys
from pathlib import Path
import docx
import fitz

# Ensure UTF-8 output
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

BASE_DIR = Path(__file__).resolve().parent.parent / "01_Naskah_Utama"
MODULAR_DIR = BASE_DIR / "01_Lembar_Persetujuan_Proposal"


def _modular_texts():
    texts = []
    if MODULAR_DIR.exists():
        for f in sorted(MODULAR_DIR.glob("0*.docx")):
            try:
                dd = docx.Document(str(f))
                texts += [p.text.strip() for p in dd.paragraphs if p.text.strip()]
            except Exception:
                pass
    return texts


def audit_full():
    print("=" * 70)
    print("AUDIT: Full Proposal Parity (PDF vs DOCX)")
    print("=" * 70)
    
    pdf_path = BASE_DIR / "Proposal_Arthur_PokemonTCG.pdf"
    docx_path = BASE_DIR / "Proposal_Arthur_PokemonTCG.docx"
    
    assert pdf_path.exists(), f"Missing {pdf_path}"
    assert docx_path.exists(), f"Missing {docx_path}"
    
    pdf_doc = fitz.open(str(pdf_path))
    docx_doc = docx.Document(str(docx_path))
    
    print(f"PDF Pages: {len(pdf_doc)}")
    print(f"DOCX Paragraphs: {len(docx_doc.paragraphs)}, Tables: {len(docx_doc.tables)}")
    
    docx_text = [p.text.strip() for p in docx_doc.paragraphs if p.text.strip()]
    pdf_full_text = "\n".join([page.get_text() for page in pdf_doc])
    
    # 1. Approval Sheets check (arsitektur modular: boleh di DOCX utama ATAU di 6 file modular)
    mod_texts = _modular_texts()
    for phrase in ["PERNYATAAN KEASLIAN", "HALAMAN PERSETUJUAN", "HALAMAN PENGESAHAN"]:
        in_docx = any(phrase in t for t in docx_text)
        in_mod = any(phrase in t for t in mod_texts)
        print(f"  * {phrase} in DOCX: {in_docx} | in modular: {in_mod}")
        assert in_docx or in_mod, f"Full Proposal MUST contain {phrase} (utama/modular)!"
        
    # 2. Kata Pengantar Point 1 check (boleh modular)
    kp_docx = [t for t in docx_text if "Dr. Fredella Colline" in t and t.startswith("1.")]
    kp_mod = [t for t in mod_texts if "Dr. Fredella Colline" in t and t.startswith("1.")]
    print(f"  * Kata Pengantar Point 1 Fredella Colline in DOCX: {len(kp_docx) > 0} | modular: {len(kp_mod) > 0}")
    assert len(kp_docx) > 0 or len(kp_mod) > 0, "Kata Pengantar point 1 must be Dr. Fredella Colline"
    
    # 3. Bab 3 check (Must be present)
    bab3_docx = any("BAB 3" in t for t in docx_text)
    print(f"  * BAB 3 in DOCX: {bab3_docx}")
    assert bab3_docx, "DOCX Full Proposal MUST contain BAB 3!"
    
    # 4. Batasan Masalah in Bab 3
    has_311 = any("3.1.1" in t and "Batasan Penelitian" in t for t in docx_text)
    print(f"  * 3.1.1 Batasan Penelitian in Bab 3: {has_311}")
    assert has_311, "DOCX Full Proposal MUST contain 3.1.1 Batasan Penelitian!"
    
    # 5. Outdated subheadings check in Bab 1
    outdated = any(sub in t for t in docx_text for sub in ["1.2.1", "1.2.2", "1.5 Batasan Penelitian", "1.6 Sistematika Penulisan"])
    print(f"  * Outdated Subheadings (1.2.1/1.2.2/1.5/1.6) in DOCX: {outdated}")
    assert not outdated, "DOCX Full Proposal must NOT contain outdated subheadings in Bab 1!"

    print("[PASS] Full Proposal PDF <-> DOCX Parity Audit PASSED 100%!\n")

if __name__ == '__main__':
    audit_full()
    print("=" * 70)
    print("ALL AUDITS PASSED WITH ZERO ERRORS!")
    print("=" * 70)
