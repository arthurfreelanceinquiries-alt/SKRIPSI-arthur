r"""
verify_word_outline.py
Deterministic verification tool to inspect the outline structure, heading styles,
OpenXML <w:outlineLvl> attributes, and typography in Proposal_Arthur_PokemonTCG.docx.
Ensures full compatibility with Microsoft Word Navigation Pane and Google Docs Document Tabs.
"""

import sys
from pathlib import Path
import docx
from docx import Document
from docx.oxml.ns import qn

def verify_document_outline(docx_path):
    print(f"[*] Inspecting Document Outline Structure: {docx_path}")
    doc = Document(str(docx_path))
    
    headings_found = []
    
    for idx, p in enumerate(doc.paragraphs):
        style_name = p.style.name if p.style else "None"
        pPr = p._p.find(qn('w:pPr'))
        outline_lvl = None
        if pPr is not None:
            outline_node = pPr.find(qn('w:outlineLvl'))
            if outline_node is not None:
                outline_lvl = outline_node.get(qn('w:val'))
        
        is_heading_style = "Heading" in style_name
        has_outline = outline_lvl is not None
        
        if is_heading_style or has_outline:
            text = p.text.strip()
            # Inspect first run font properties
            font_name = None
            font_size = None
            font_bold = None
            if p.runs:
                font_name = p.runs[0].font.name
                font_size = p.runs[0].font.size.pt if p.runs[0].font.size else None
                font_bold = p.runs[0].font.bold
            
            headings_found.append({
                "para_index": idx,
                "text": text[:60] + ("..." if len(text) > 60 else ""),
                "full_text": text,
                "style": style_name,
                "outline_level": outline_lvl,
                "font_name": font_name,
                "font_size": font_size,
                "font_bold": font_bold
            })
            
    print(f"\n[+] Total Outline Headings Detected: {len(headings_found)}")
    print("-" * 90)
    print(f"{'No':<4} | {'Lvl':<4} | {'Style':<12} | {'Font / Size / Bold':<25} | {'Heading Text'}")
    print("-" * 90)
    
    h1_count = 0
    h2_count = 0
    h3_count = 0
    
    for i, h in enumerate(headings_found, 1):
        lvl_str = str(h['outline_level']) if h['outline_level'] is not None else "N/A"
        font_info = f"{h['font_name']} {h['font_size']}pt {'B' if h['font_bold'] else '-'}"
        print(f"{i:<4} | {lvl_str:<4} | {h['style']:<12} | {font_info:<25} | {h['text']}")
        
        if h['outline_level'] == '0':
            h1_count += 1
        elif h['outline_level'] == '1':
            h2_count += 1
        elif h['outline_level'] == '2':
            h3_count += 1

    print("-" * 90)
    print(f"Summary: Level 0 (H1) = {h1_count}, Level 1 (H2) = {h2_count}, Level 2 (H3) = {h3_count}")

    # Critical checkpoints
    expected_frontmatter = [
        "PERNYATAAN KEASLIAN",
        "HALAMAN PERSETUJUAN",
        "HALAMAN PENGESAHAN",
        "KATA PENGANTAR",
        "ABSTRAK",
        "ABSTRACT",
        "DAFTAR ISI",
        "DAFTAR TABEL",
        "DAFTAR GAMBAR"
    ]
    
    missing_frontmatter = []
    for ef in expected_frontmatter:
        found = any(ef in h['full_text'].upper() for h in headings_found)
        if not found:
            missing_frontmatter.append(ef)
            
    expected_babs = ["BAB 1", "BAB 2", "BAB 3", "DAFTAR PUSTAKA"]
    missing_babs = []
    for eb in expected_babs:
        found = any(eb in h['full_text'].upper() for h in headings_found)
        if not found:
            missing_babs.append(eb)
            
    # Check compliance
    errors = []
    if missing_frontmatter:
        errors.append(f"Missing frontmatter headings in outline: {missing_frontmatter}")
    if missing_babs:
        errors.append(f"Missing chapter headings in outline: {missing_babs}")
    if h2_count < 10:
        errors.append(f"Suspiciously low Level 2 headings count: {h2_count}")
    if h3_count < 5:
        errors.append(f"Suspiciously low Level 3 headings count: {h3_count}")
        
    for h in headings_found:
        if h['outline_level'] is None:
            errors.append(f"Heading '{h['text']}' is missing XML <w:outlineLvl> attribute.")
        if h['font_name'] != "Times New Roman":
            errors.append(f"Heading '{h['text']}' has font {h['font_name']}, expected Times New Roman.")
        if h['font_size'] not in [12.0, None]:
            errors.append(f"Heading '{h['text']}' has size {h['font_size']}pt, expected 12pt.")
            
    if errors:
        print("\n[FAIL] Outline verification failed with errors:")
        for err in errors:
            print(f"  - {err}")
        return False
    else:
        print("\n[PASS] All heading styles, outline levels, and font parameters are 100% compliant!")
        return True

if __name__ == "__main__":
    target_path = Path(r"z:\SKRIPSII\SKRIPSI-arthur\01_Naskah_Utama\Proposal_Arthur_PokemonTCG.docx")
    if len(sys.argv) > 1:
        target_path = Path(sys.argv[1])
        
    if not target_path.exists():
        print(f"[ERROR] Target file does not exist: {target_path}")
        sys.exit(1)
        
    success = verify_document_outline(target_path)
    sys.exit(0 if success else 1)
