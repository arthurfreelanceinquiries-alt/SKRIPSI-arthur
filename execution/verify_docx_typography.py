"""
verify_docx_typography.py
=========================
Layer 3 Verification Script: Audits Word documents (.docx) for publication-grade typography,
zero AI artifacts, proper dot leaders in TOC, and 12pt font sizes for abstracts.
"""

import sys
from pathlib import Path
from docx import Document
from docx.enum.text import WD_TAB_LEADER


def _style_tab_stops(doc, paragraph):
    """Fallback: baca tab-stop dari definisi style paragraf.

    Mengembalikan [(is_dot, pos_pt, src)] atau []. Word menghapus stop
    paragraf yg identik dgn style saat save (normalisasi), sehingga
    satu-satunya sumber kebenaran render adalah style (mis. TOC11:
    right-dot-7938). Hanya menerima dot di ~14.0cm; style lain diabaikan.
    """
    W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
    try:
        pPr = paragraph._p.find(f"{W}pPr")
        sid = None
        if pPr is not None:
            ps = pPr.find(f"{W}pStyle")
            if ps is not None:
                sid = ps.get(f"{W}val")
        if not sid:
            return []
        for st in doc.styles.element.iterfind(f"{W}style"):
            if st.get(f"{W}styleId") != sid:
                continue
            out = []
            for tb in st.iterfind(f".//{W}tabs/{W}tab"):
                leader = tb.get(f"{W}leader")
                pos = tb.get(f"{W}pos")
                if tb.get(f"{W}val") != 'right' or not pos:
                    continue
                try:
                    pt = int(pos) / 20.0
                except (TypeError, ValueError):
                    continue
                out.append((leader == 'dot', pt, f"style:{sid}"))
            return out
    except Exception:
        pass
    return []
from docx.shared import Pt


def audit_docx(docx_path: Path) -> bool:
    print(f"\n=======================================================")
    print(f"AUDITING: {docx_path.name}")
    print(f"=======================================================")

    if not docx_path.exists():
        print(f"[FAIL] File not found: {docx_path}")
        return False

    doc = Document(str(docx_path))
    issues = []

    # 1. Audit paragraphs for stray *, $, and raw LaTeX commands
    total_paragraphs = len(doc.paragraphs)
    print(f"[*] Inspecting {total_paragraphs} paragraphs...")

    in_abstrak_section = False
    in_abstract_section = False

    for p_idx, p in enumerate(doc.paragraphs):
        p_text = p.text

        # Track abstract sections
        if "ABSTRAK" in p_text and p_text.isupper():
            in_abstrak_section = True
            in_abstract_section = False
        elif "ABSTRACT" in p_text and p_text.isupper():
            in_abstract_section = True
            in_abstrak_section = False
        elif p_text.startswith("DAFTAR ISI") or p_text.startswith("BAB 1"):
            in_abstrak_section = False
            in_abstract_section = False

        # Check font sizes in Abstrak and Abstract
        if in_abstrak_section or in_abstract_section:
            for r_idx, r in enumerate(p.runs):
                if r.font.size and r.font.size < Pt(11.5):
                    # Flag font size < 12pt (allowing slight float tolerances)
                    issues.append(
                        f"Abstract font size too small ({r.font.size.pt} pt) at P{p_idx} R{r_idx}: '{r.text[:30]}...'"
                    )

        # Check for stray asterisks in runs
        for r_idx, r in enumerate(p.runs):
            # Check for literal asterisks
            if "*" in r.text:
                # We allow standalone bullet points if any, but in text runs, stray asterisks represent unparsed markdown
                issues.append(f"Stray asterisk '*' in run text at P{p_idx} R{r_idx}: {repr(r.text)}")

            # Check for dollar signs (allowing legitimate US$ currency)
            text_without_currency = r.text.replace("US$", "").replace("USD", "")
            if "$" in text_without_currency:
                issues.append(f"Stray dollar '$' in run text at P{p_idx} R{r_idx}: {repr(r.text)}")

            # Check for raw LaTeX syntax
            for raw_cmd in [r"\cite", r"\ref", r"\emph", r"\beta", r"\alpha", r"\Delta", r"\cdot"]:
                if raw_cmd in r.text:
                    issues.append(f"Raw LaTeX command '{raw_cmd}' at P{p_idx} R{r_idx}: {repr(r.text)}")

    # 2. Audit Table Cells
    total_tables = len(doc.tables)
    print(f"[*] Inspecting {total_tables} tables...")
    for t_idx, tbl in enumerate(doc.tables):
        for r_idx, row in enumerate(tbl.rows):
            for c_idx, cell in enumerate(row.cells):
                for p in cell.paragraphs:
                    for r in p.runs:
                        if "*" in r.text:
                            issues.append(f"Stray asterisk '*' in Table {t_idx} Row {r_idx} Col {c_idx}: {repr(r.text)}")
                        if "$" in r.text:
                            issues.append(f"Stray dollar '$' in Table {t_idx} Row {r_idx} Col {c_idx}: {repr(r.text)}")
                        for raw_cmd in [r"\cite", r"\ref", r"\emph"]:
                            if raw_cmd in r.text:
                                issues.append(f"Raw LaTeX command '{raw_cmd}' in Table {t_idx} Row {r_idx} Col {c_idx}: {repr(r.text)}")

    # 3. Audit Table of Contents tab leaders & positions
    print(f"[*] Inspecting Table of Contents for dot leaders & 14.0cm tab stops...")
    toc_paragraphs_checked = 0
    in_toc = False
    for p in doc.paragraphs:
        txt = p.text.strip()
        if txt in ["DAFTAR ISI", "DAFTAR TABEL", "DAFTAR GAMBAR"]:
            in_toc = True
            continue
        if in_toc:
            # The actual body Chapter 1 heading has no tab '\t' and is BAB 1 PENDAHULUAN
            if txt == "BAB 1 PENDAHULUAN" and "\t" not in p.text:
                in_toc = False
                break
            if "\t" in p.text:
                toc_paragraphs_checked += 1
                # Check right indent: MUST be 0 to prevent Google Docs / Word Online tab stop discard
                r_ind = p.paragraph_format.right_indent
                if r_ind is not None and r_ind.pt > 1:
                    issues.append(f"TOC paragraph has non-zero right_indent ({r_ind.pt} pt): {repr(p.text)}")

                # Check tab stop leader (direct pPr stops, else style-inherited:
                # Word menormalisasi stop paragraf yg identik dgn style)
                stops = [(ts.leader == WD_TAB_LEADER.DOTS, ts.position.pt, 'direct')
                         for ts in p.paragraph_format.tab_stops]
                if not stops:
                    stops = _style_tab_stops(doc, p)
                if not stops:
                    issues.append(f"TOC paragraph missing tab stop: {repr(p.text)}")
                else:
                    dot_stops = [s for s in stops if s[0]]
                    if not dot_stops:
                        issues.append(f"TOC tab stop does not have DOTS leader: {repr(p.text)}")
                    else:
                        # Check position: 14.0 cm is approx 396.85 pt (tolerance 15 pt)
                        if abs(dot_stops[0][1] - 396.85) > 15:
                            issues.append(f"TOC tab stop pos not at 14.0cm (found {dot_stops[0][1]:.1f} pt via {dot_stops[0][2]}): {repr(p.text)}")


    print(f"[*] Checked {toc_paragraphs_checked} TOC/LOT/LOF entry paragraphs for dot leaders and 0 right_indent.")

    # 3b. Audit Frontmatter Mandatory Standalone Pages (DAFTAR TABEL & DAFTAR GAMBAR)
    # UKRIDA FEB 2023: Subbab 2.1 hlm 9-10 menetapkan Daftar Isi, Daftar Tabel, dan Daftar Gambar
    # masing-masing wajib berdiri sendiri pada halaman baru terpisah dengan angka romawi kecil.
    print(f"[*] Inspecting frontmatter headings for mandatory standalone page breaks...")
    W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
    for required_heading in ["DAFTAR TABEL", "DAFTAR GAMBAR"]:
        found_heading = False
        for p_idx, p in enumerate(doc.paragraphs):
            raw_text = p.text.strip()
            # Abaikan entri TOC (yang memiliki karakter tab '\t' diikuti nomor halaman)
            if "\t" in raw_text:
                continue

            # Cek jika heading terkontaminasi/ter-merge dengan paragraf non-tab lain
            if required_heading in raw_text and raw_text != required_heading:
                issues.append(
                    f"Frontmatter '{required_heading}' is merged/contaminated into paragraph at P{p_idx}: {repr(raw_text[:60])}"
                )
            elif raw_text == required_heading:
                found_heading = True
                pPr = p._p.find(f"{W}pPr")
                has_pbb = False
                if pPr is not None and pPr.find(f"{W}pageBreakBefore") is not None:
                    has_pbb = True
                elif p.paragraph_format.page_break_before:
                    has_pbb = True
                
                if not has_pbb:
                    issues.append(
                        f"Frontmatter '{required_heading}' at P{p_idx} missing mandatory page_break_before (<w:pageBreakBefore/>)"
                    )
        if not found_heading:
            issues.append(f"Frontmatter heading '{required_heading}' not found as standalone paragraph in document!")

    # 4. Audit Run Font Color (Pure Black #000000, zero blue/themeColor)
    print(f"[*] Inspecting all runs across document for pure black (#000000) color...")
    non_black_runs = 0
    for p_idx, p in enumerate(doc.paragraphs):
        for r_idx, r in enumerate(p.runs):
            rPr = r._element.find("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}rPr")
            if rPr is not None:
                color_elem = rPr.find("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}color")
                if color_elem is not None:
                    val = color_elem.get("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val")
                    theme_color = color_elem.get("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}themeColor")
                    if val != "000000" and val != "auto":
                        issues.append(f"Non-black run color val='{val}' at P{p_idx} R{r_idx}: {repr(r.text[:30])}")
                        non_black_runs += 1
                    if theme_color is not None:
                        issues.append(f"Stray themeColor='{theme_color}' at P{p_idx} R{r_idx}: {repr(r.text[:30])}")
                        non_black_runs += 1

    # Check table runs as well
    for t_idx, tbl in enumerate(doc.tables):
        for r_idx, row in enumerate(tbl.rows):
            for c_idx, cell in enumerate(row.cells):
                for p in cell.paragraphs:
                    for r in p.runs:
                        rPr = r._element.find("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}rPr")
                        if rPr is not None:
                            color_elem = rPr.find("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}color")
                            if color_elem is not None:
                                val = color_elem.get("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val")
                                theme_color = color_elem.get("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}themeColor")
                                if val != "000000" and val != "auto":
                                    issues.append(f"Non-black run color val='{val}' in T{t_idx} R{r_idx} C{c_idx}: {repr(r.text[:30])}")
                                    non_black_runs += 1
                                if theme_color is not None:
                                    issues.append(f"Stray themeColor='{theme_color}' in T{t_idx} R{r_idx} C{c_idx}: {repr(r.text[:30])}")
                                    non_black_runs += 1

    # Results
    if issues:
        print(f"\n[FAIL] Found {len(issues)} typography issues in {docx_path.name}:")
        for iss in issues[:20]:
            print(f"  - {iss}")
        if len(issues) > 20:
            print(f"  ... and {len(issues) - 20} more issues.")
        return False
    else:
        print(f"\n[PASS] {docx_path.name} is 100% CLEAN of AI artifacts, stray asterisks, math symbols, has 100% PURE BLACK font, and has valid 12pt abstracts and dot leaders!")
        return True


def main():
    base_dir = Path(__file__).resolve().parent.parent / "01_Naskah_Utama"
    doc_no_bab3 = base_dir / "Proposal_Arthur_NoBab3.docx"
    doc_full = base_dir / "Proposal_Arthur_PokemonTCG.docx"

    success1 = audit_docx(doc_no_bab3)
    success2 = audit_docx(doc_full)

    if success1 and success2:
        print("\n=======================================================")
        print("ALL WORD DOCUMENTS PASSED PUBLICATION-GRADE VERIFICATION!")
        print("=======================================================")
        sys.exit(0)
    else:
        print("\n[ERROR] One or more documents failed verification.")
        sys.exit(1)


if __name__ == "__main__":
    main()
