r"""
build_proposal_word.py
Generates a publication-grade, FEB UKRIDA 2023-compliant Microsoft Word (.docx)
thesis proposal directly from canonical TeX and Markdown sources.

Standards:
- Paper: ISO A4 (21.0 x 29.7 cm)
- Margins: Left 4.0 cm, Right 3.0 cm, Top 3.0 cm, Bottom 3.0 cm
- Font: Times New Roman 12 pt, 1.5 Line Spacing, Justified, 1.25 cm First-Line Indent
- Frontmatter: Roman numerals (i, ii, iii...), Academic Forms
- Main Text: Arabic numerals (1, 2, 3...)
- Tables: Strict APA 7th Edition open format (top/bottom 1pt, header 0.75pt, no vertical lines)
- Figures: Centered 300 DPI vector-rendered graphics
- Equations: Native Microsoft Word OMML equations
"""

import os
import re
import sys
import subprocess
import tempfile
import shutil
import copy
from pathlib import Path
import docx
from docx import Document
from docx.shared import Pt, Cm, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING, WD_TAB_ALIGNMENT, WD_TAB_LEADER
from docx.enum.section import WD_SECTION, WD_SECTION_START
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

# Ensure UTF-8 output
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

# ============================================================================
# HYBRID PANDOC OMML ENGINE SETUP
# ============================================================================

def get_pandoc_path():
    """Locate pandoc executable on Windows."""
    p = shutil.which('pandoc')
    if p and os.path.exists(p):
        return p
    candidates = [
        r"C:\Users\arthu\AppData\Local\Pandoc\pandoc.exe",
        r"C:\Program Files\Pandoc\pandoc.exe",
        os.path.expandvars(r"%LOCALAPPDATA%\Pandoc\pandoc.exe"),
        os.path.expandvars(r"%ProgramFiles%\Pandoc\pandoc.exe"),
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    return None

PANDOC_EXE = get_pandoc_path()
HAS_OMML = PANDOC_EXE is not None
if HAS_OMML:
    print(f"[INFO] Hybrid Pandoc OMML engine active: {PANDOC_EXE}")
else:
    print("[WARN] Pandoc not found. Equations will use fallback format.")


def latex_to_omml_pandoc(formula_latex: str):
    """Converts a LaTeX formula into a native Word OMML (<m:oMathPara> or <m:oMath>) element via Pandoc."""
    if not PANDOC_EXE:
        return None

    clean_tex = formula_latex.strip().strip('$').strip()
    latex_input = f"\\begin{{equation*}}\n{clean_tex}\n\\end{{equation*}}"

    with tempfile.NamedTemporaryFile(suffix='.docx', delete=False) as tmp:
        tmp_path = tmp.name

    try:
        res = subprocess.run(
            [PANDOC_EXE, '-f', 'latex', '-t', 'docx', '-o', tmp_path],
            input=latex_input,
            text=True,
            encoding='utf-8',
            capture_output=True
        )
        if res.returncode == 0 and os.path.exists(tmp_path):
            temp_doc = docx.Document(tmp_path)
            for p in temp_doc.paragraphs:
                for c in p._p:
                    if 'oMathPara' in c.tag or 'oMath' in c.tag:
                        return copy.deepcopy(c)
        return None
    except Exception as e:
        print(f"[WARN] Error converting equation via Pandoc: {e}")
        return None
    finally:
        if os.path.exists(tmp_path):
            try:
                os.remove(tmp_path)
            except Exception:
                pass


# ============================================================================
# XML & STYLING HELPERS
# ============================================================================

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """Set inner cell padding in twips (1 pt = 20 twips)."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)


def set_cell_shading(cell, color_hex="F2F2F2"):
    """Set background color of a cell."""
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    tcPr.append(shd)


def remove_table_borders(table):
    """Remove all borders from a table (for borderless identity & signature blocks)."""
    tblPr = table._tbl.tblPr
    borders = parse_xml(f'''
        <w:tblBorders {nsdecls("w")}>
            <w:top w:val="none"/>
            <w:left w:val="none"/>
            <w:bottom w:val="none"/>
            <w:right w:val="none"/>
            <w:insideH w:val="none"/>
            <w:insideV w:val="none"/>
        </w:tblBorders>
    ''')
    for existing in tblPr.findall(qn('w:tblBorders')):
        tblPr.remove(existing)
    tblPr.append(borders)


def set_col_widths_fixed(table, col_widths):
    """Set explicit fixed column widths at both table grid and cell levels."""
    tblPr = table._tbl.tblPr
    for ex in tblPr.findall(qn('w:tblLayout')):
        tblPr.remove(ex)
    tblLayout = parse_xml(f'<w:tblLayout {nsdecls("w")} w:type="fixed"/>')
    tblPr.append(tblLayout)

    tblGrid = table._tbl.find(qn('w:tblGrid'))
    if tblGrid is None:
        tblGrid = OxmlElement('w:tblGrid')
        table._tbl.insert(list(table._tbl).index(tblPr) + 1, tblGrid)
    else:
        tblGrid.clear()

    for w in col_widths:
        gridCol = OxmlElement('w:gridCol')
        w_dxa = int(w.twips if hasattr(w, 'twips') else (w * 567 if isinstance(w, (int, float)) else w))
        gridCol.set(qn('w:w'), str(w_dxa))
        tblGrid.append(gridCol)

    for row in table.rows:
        for c_idx, cell in enumerate(row.cells):
            if c_idx < len(col_widths):
                cell.width = col_widths[c_idx]
                tcPr = cell._tc.get_or_add_tcPr()
                for tcW in tcPr.findall(qn('w:tcW')):
                    tcPr.remove(tcW)
                w_dxa = int(col_widths[c_idx].twips if hasattr(col_widths[c_idx], 'twips') else (col_widths[c_idx] * 567 if isinstance(col_widths[c_idx], (int, float)) else col_widths[c_idx]))
                new_tcW = parse_xml(f'<w:tcW {nsdecls("w")} w:w="{w_dxa}" w:type="dxa"/>')
                tcPr.append(new_tcW)


def apply_apa7_table_borders(table):
    """Apply strict APA 7th Edition open table borders (no vertical lines, 3 horizontal rules)."""
    tblPr = table._tbl.tblPr
    borders = parse_xml(f'''
        <w:tblBorders {nsdecls("w")}>
            <w:top w:val="single" w:sz="8" w:space="0" w:color="000000"/>
            <w:left w:val="none"/>
            <w:bottom w:val="single" w:sz="8" w:space="0" w:color="000000"/>
            <w:right w:val="none"/>
            <w:insideH w:val="none"/>
            <w:insideV w:val="none"/>
        </w:tblBorders>
    ''')
    for existing in tblPr.findall(qn('w:tblBorders')):
        tblPr.remove(existing)
    tblPr.append(borders)

    # Apply bottom border to header row (row 0)
    if len(table.rows) > 0:
        for cell in table.rows[0].cells:
            tcPr = cell._tc.get_or_add_tcPr()
            tcBorders = parse_xml(f'''
                <w:tcBorders {nsdecls("w")}>
                    <w:bottom w:val="single" w:sz="6" w:space="0" w:color="000000"/>
                </w:tcBorders>
            ''')
            for existing in tcPr.findall(qn('w:tcBorders')):
                tcPr.remove(existing)
            tcPr.append(tcBorders)

    # Ensure rows do not split across pages and header repeats
    for i, row in enumerate(table.rows):
        trPr = row._tr.get_or_add_trPr()
        trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
        if i == 0:
            trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))


def add_page_number_to_footer(section, is_roman=False, start_num=None):
    """Configure footer with UKRIDA Accent Bar 4 and dynamic page number.
    Ensures seamless Times New Roman 10pt Bold Black typography in both
    Microsoft Word Desktop and Google Docs Web.
    """
    footer = section.footer
    p = footer.paragraphs[0]
    try:
        p.style = 'Footer'
    except Exception:
        pass
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.0

    run_text = p.add_run("Universitas Kristen Krida Wacana | ")
    run_text.font.name = "Times New Roman"
    run_text.font.size = Pt(10)
    run_text.font.bold = True
    run_text.font.color.rgb = RGBColor(0, 0, 0)

    # Fallback initial value for Google Docs Web and previewers
    if is_roman:
        def int_to_roman(n):
            val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
            syb = ["m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"]
            res = ""
            for i in range(len(val)):
                while n >= val[i]:
                    res += syb[i]
                    n -= val[i]
            return res
        fallback_val = int_to_roman(start_num) if start_num is not None else "ii"
    else:
        fallback_val = str(start_num if start_num is not None else 1)

    # Insert Word Page Number field with explicit Run Properties (Times New Roman 10pt Bold Black)
    # w:val="20" means 20 half-points = 10 pt.
    fld_xml = (
        f'<w:fldSimple {nsdecls("w")} w:instr="PAGE">'
        f'<w:r>'
        f'<w:rPr>'
        f'<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>'
        f'<w:b/>'
        f'<w:bCs/>'
        f'<w:sz w:val="20"/>'
        f'<w:szCs w:val="20"/>'
        f'<w:color w:val="000000"/>'
        f'</w:rPr>'
        f'<w:t>{fallback_val}</w:t>'
        f'</w:r>'
        f'</w:fldSimple>'
    )
    fld = parse_xml(fld_xml)
    p._p.append(fld)

    # Configure section page numbering restart and format
    sectPr = section._sectPr
    pgNumType = sectPr.find(qn('w:pgNumType'))
    if pgNumType is None:
        pgNumType = OxmlElement('w:pgNumType')
        sectPr.append(pgNumType)

    if is_roman:
        pgNumType.set(qn('w:fmt'), 'lowerRoman')
    else:
        pgNumType.set(qn('w:fmt'), 'decimal')

    if start_num is not None:
        pgNumType.set(qn('w:start'), str(start_num))


def add_equation_paragraph(doc, formula_latex, align=WD_ALIGN_PARAGRAPH.CENTER):
    """Insert a native OMML equation or clean fallback formula."""
    p = doc.add_paragraph()
    p.alignment = align
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.line_spacing = 1.5

    if HAS_OMML:
        elem = latex_to_omml_pandoc(formula_latex)
        if elem is not None:
            p._p.append(elem)
            return p

    # Fallback clean text
    clean_math = formula_latex.replace(r'\alpha', 'α').replace(r'\beta', 'β').replace(r'\cdot', ' · ')
    clean_math = re.sub(r'[_^{}]', '', clean_math)
    run = p.add_run(clean_math)
    run.font.name = "Cambria Math"
    run.font.size = Pt(11)
    run.font.italic = True
    return p


def clean_academic_text(text: str) -> str:
    """Cleans raw LaTeX citations, math expressions, and artifact syntax into publication-grade text."""
    if not text:
        return text

    # 0. Normalisasi aksen LaTeX ke Unicode (mencegah bocoran mentah)
    text = text.replace(r"{\'e}", 'é').replace(r"\'e", 'é')
    text = text.replace(r'{\"u}', 'ü').replace(r'\"u', 'ü')
    text = text.replace(r'{\"o}', 'ö').replace(r'\"o', 'ö')
    text = text.replace(r'{\`e}', 'è').replace(r'\`e', 'è')

    # 1. LaTeX Citations
    text = re.sub(r'\\citealp\{babin1994work\}', 'Babin *et al.*, 1994', text)
    text = re.sub(r'\\citealp\{arnold2003hedonic\}', 'Arnold dan Reynolds, 2003', text)
    text = re.sub(r'\\citealp\{gueltekin2012influence\}', 'Gültekin dan Özer, 2012', text)
    text = re.sub(r'\\citep\{aiken1991multiple,\s*ghozali2018aplikasi\}', '(Aiken dan West, 1991; Ghozali, 2018)', text)
    text = re.sub(r'\\citet\{green1991subjects\}', 'Green (1991)', text)
    text = re.sub(r'\\citet\{cohen1988statistical\}', 'Cohen (1988)', text)
    text = re.sub(r'\\citealp\{([^}]+)\}', r'\1', text)
    text = re.sub(r'\\citep\{([^}]+)\}', r'(\1)', text)
    text = re.sub(r'\\citet\{([^}]+)\}', r'\1', text)
    text = re.sub(r'\\emph\{([^}]+)\}', r'*\1*', text)

    # Standarisasi sitasi dua penulis bahasa Indonesia (menggunakan 'dan', bukan '&' atau 'and')
    text = re.sub(r'\b([A-Z][a-z]+)\s+&\s+([A-Z][a-z]+)\b', r'\1 dan \2', text)
    text = re.sub(r'\b([A-Z][a-z]+)\s+and\s+([A-Z][a-z]+)\b', r'\1 dan \2', text)
    text = re.sub(r'\bet al\.?', r'*et al.*', text)
    text = text.replace('**et al.**', '*et al.*').replace('**et al.*', '*et al.*').replace('***et al.***', '*et al.*')

    # 2. Multi-variable & Complex math expressions
    text = text.replace(r'$X_1^*, X_2^*, X_3^*, M^*, X_1^* \cdot M^*, X_2^* \cdot M^*, X_3^* \cdot M*$', '*X*₁*, *X*₂*, *X*₃*, *M*\\*, *X*₁* · *M*\\*, *X*₂* · *M*\\*, *X*₃* · *M*\\*')
    text = text.replace(r'$X_1^* \cdot M^*, X_2^* \cdot M^*, X_3^* \cdot M*$', '*X*₁* · *M*\\*, *X*₂* · *M*\\*, *X*₃* · *M*\\*')
    text = text.replace(r'$X_1^*, X_2^*, X_3^*, M^*$', '*X*₁*, *X*₂*, *X*₃*, *M*\\*')
    text = text.replace(r'$X_1^*, X_2^*, X_3^*$', '*X*₁*, *X*₂*, *X*₃*')
    text = text.replace(r'$X_1, X_2, X_3, M, X_1 \cdot M, X_2 \cdot M, X_3 \cdot M$', '*X*₁, *X*₂, *X*₃, *M*, *X*₁ · *M*, *X*₂ · *M*, *X*₃ · *M*')
    text = text.replace(r'$X_1 \cdot M, X_2 \cdot M, X_3 \cdot M$', '*X*₁ · *M*, *X*₂ · *M*, *X*₃ · *M*')
    text = text.replace(r'$X_1, X_2, X_3$', '*X*₁, *X*₂, *X*₃')
    text = text.replace(r'$Y, X_1, X_2, X_3, M$', '*Y*, *X*₁, *X*₂, *X*₃, *M*')

    # Regression formulas
    text = text.replace(r'$Y = \alpha + \beta_1 X_1^* + \beta_2 X_2^* + \beta_3 X_3^* + \beta_4 M^* + \beta_5 (X_1^* \cdot M^*) + \beta_6 (X_2^* \cdot M^*) + \beta_7 (X_3^* \cdot M^*) + e$',
                        '*Y* = α + β₁*X*₁* + β₂*X*₂* + β₃*X*₃* + β₄*M*\\* + β₅(*X*₁* · *M*\\*) + β₆(*X*₂* · *M*\\*) + β₇(*X*₃* · *M*\\*) + *e*')
    text = text.replace(r'$Y = \alpha + \beta_1 X_1^* + \beta_2 X_2^* + \beta_3 X_3^* + \beta_4 M^* + e$',
                        '*Y* = α + β₁*X*₁* + β₂*X*₂* + β₃*X*₃* + β₄*M*\\* + *e*')
    text = text.replace(r'$Y = \alpha + \beta_1 X_1 + \beta_2 X_2 + \beta_3 X_3 + \beta_4 M + \beta_5 (X_1 \cdot M) + \beta_6 (X_2 \cdot M) + \beta_7 (X_3 \cdot M) + e$',
                        '*Y* = α + β₁*X*₁ + β₂*X*₂ + β₃*X*₃ + β₄*M* + β₅(*X*₁ · *M*) + β₆(*X*₂ · *M*) + β₇(*X*₃ · *M*) + *e*')
    text = text.replace(r'$Y = \alpha + \beta_1 X_1 + \beta_2 X_2 + \beta_3 X_3 + e$',
                        '*Y* = α + β₁*X*₁ + β₂*X*₂ + β₃*X*₃ + *e*')

    # Centering formula & simple slopes
    text = text.replace(r'$X_i^* = X_i - \bar{X}_i; M^* = M - \bar{M}$', r'*X*ᵢ* = *X*ᵢ − *X̄*ᵢ; *M*\* = *M* − *M̄*')
    text = text.replace(r'$\frac{\partial Y}{\partial X_1^*} = \beta_1 + \beta_5 M^*$', '∂Y/∂X₁* = β₁ + β₅M*')
    text = text.replace(r'$\frac{\partial Y}{\partial X_2^*} = \beta_2 + \beta_6 M^*$', '∂Y/∂X₂* = β₂ + β₆M*')
    text = text.replace(r'$\frac{\partial Y}{\partial X_3^*} = \beta_3 + \beta_7 M^*$', '∂Y/∂X₃* = β₃ + β₇M*')
    text = text.replace(r'$\frac{\partial Y}{\partial X_i^*} = \beta_i + \beta_{\text{int}} M^*$', '∂Y/∂Xᵢ* = βᵢ + β_int M*')
    text = text.replace(r'$\beta_5 < 0$', 'β₅ < 0')
    text = text.replace(r'$\beta_6 < 0$', 'β₆ < 0')
    text = text.replace(r'$\beta_7 < 0$', 'β₇ < 0')
    text = text.replace(r'$-1\,\text{SD}$', '−1 SD')
    text = text.replace(r'$0\,\text{SD}$', '0 SD')
    text = text.replace(r'$+1\,\text{SD}$', '+1 SD')
    text = text.replace(r'$M^* = 0$', '*M*\\* = 0')
    text = text.replace(r'$F_{\text{change}}$', '*F*_{change}')

    # Sample size (Green & Cohen)
    text = text.replace(r'$N \ge 104 + 7 = 111\text{ responden}$', '*N* ≥ 104 + 7 = 111 responden')
    text = text.replace(r'$N \ge 104 + k$', '*N* ≥ 104 + *k*')
    text = text.replace(r'$N \ge 50 + 8(7) = 50 + 56 = 106\text{ responden}$', '*N* ≥ 50 + 8(7) = 50 + 56 = 106 responden')
    text = text.replace(r'$N \ge 50 + 8k$', '*N* ≥ 50 + 8*k*')
    text = text.replace(r'$N > 200$', '*N* > 200')
    text = text.replace(r'$r_{\text{hitung}} > r_{\text{tabel}}$', '*r*_{hitung} > *r*_{tabel}')
    text = text.replace(r'$F_{\text{hitung}} > F_{\text{tabel}}$', '*F*_{hitung} > *F*_{tabel}')
    text = text.replace(r'$t_{\text{hitung}} > t_{\text{tabel}}$', '*t*_{hitung} > *t*_{tabel}')

    # Interaction & Single variables
    text = text.replace(r'$X_1^* \cdot M^*$', '*X*₁* · *M*\\*')
    text = text.replace(r'$X_2^* \cdot M^*$', '*X*₂* · *M*\\*')
    text = text.replace(r'$X_3^* \cdot M^*$', '*X*₃* · *M*\\*')
    text = text.replace(r'$X_1^* \cdot M^*, X_2^* \cdot M^*, X_3^* \cdot M^*$', '*X*₁* · *M*\\*, *X*₂* · *M*\\*, *X*₃* · *M*\\*')
    text = text.replace(r'$X_1 \cdot M$', '*X*₁ · *M*')
    text = text.replace(r'$X_2 \cdot M$', '*X*₂ · *M*')
    text = text.replace(r'$X_3 \cdot M$', '*X*₃ · *M*')
    text = text.replace(r'$X_1 \\cdot M$', '*X*₁ · *M*')
    text = text.replace(r'$X_2 \\cdot M$', '*X*₂ · *M*')
    text = text.replace(r'$X_3 \\cdot M$', '*X*₃ · *M*')

    text = text.replace('($X_1^*$)', '(*X*₁*)')
    text = text.replace('($X_2^*$)', '(*X*₂*)')
    text = text.replace('($X_3^*$)', '(*X*₃*)')
    text = text.replace('($M^*$)', '(*M*\\*)')
    text = text.replace('$X_1^*, X_2^*, X_3^*, M^*$', '*X*₁*, *X*₂*, *X*₃*, *M*\\*')
    text = text.replace('$X_1^*, X_2^*, X_3^*$', '*X*₁*, *X*₂*, *X*₃*')
    text = text.replace('$X_1^*', '*X*₁*')
    text = text.replace('$X_2^*', '*X*₂*')
    text = text.replace('$X_3^*', '*X*₃*')
    text = text.replace('$M^*$', '*M*\\*')
    text = text.replace('$X_i^*$', '*X*ᵢ*')

    text = text.replace('($X_1$)', '(*X*₁)')
    text = text.replace('($X_2$)', '(*X*₂)')
    text = text.replace('($X_3$)', '(*X*₃)')
    text = text.replace('$X_1$', '*X*₁')
    text = text.replace('$X_2$', '*X*₂')
    text = text.replace('$X_3$', '*X*₃')
    text = text.replace('$Y$', '*Y*')
    text = text.replace('$M$', '*M*')
    text = text.replace('$Z$', '*Z*')
    text = text.replace('$e$', '*e*')
    text = text.replace('$X_i$', '*X*ᵢ')
    text = text.replace(r'$\bar{X}_i$', '*X̄*ᵢ')
    text = text.replace(r'$\bar{M}$', '*M̄*')

    # Statistical coefficients & metrics
    text = text.replace('$R^2$', '*R*²')
    text = text.replace(r'$\Delta R^2$', 'Δ*R*²')
    text = text.replace(r'$f^2 = 0,15$', '*f*² = 0,15')
    text = text.replace(r'$k = 7$', '*k* = 7')
    text = text.replace('$p < 0,05$', '*p* < 0,05')
    text = text.replace('$p > 0,05$', '*p* > 0,05')
    text = text.replace('$p < 0.05$', '*p* < 0,05')
    text = text.replace(r'$\alpha = 0,05$', 'α = 0,05')
    text = text.replace(r'$\alpha = 0.05$', 'α = 0,05')
    text = text.replace(r'$\alpha \ge 0,60$', 'α ≥ 0,60')
    text = text.replace(r'$\alpha >= 0,60$', 'α ≥ 0,60')
    text = text.replace(r'$\ge 0,60$', '≥ 0,60')
    text = text.replace(r'$\ge 17$', '≥ 17')
    text = text.replace(r'$\alpha$', 'α')
    text = text.replace(r'$\beta_1 \dots \beta_7$', 'β₁ ... β₇')
    text = text.replace(r'$\bullet$', '•')
    text = text.replace(r'$< 10$', '< 10')
    text = text.replace(r'$> 0,10$', '> 0,10')
    text = text.replace(r'$150$', '150')
    text = text.replace(r'$n = 30$', '*n* = 30')
    text = text.replace(r'$n=30$', '*n* = 30')
    text = text.replace(r'$n=120$', '*n* = 120')
    text = text.replace(r'$n=120--150$', '*n* = 120–150')
    text = text.replace(r'$n=120-150$', '*n* = 120–150')
    text = text.replace(r'$n = 120--150$', '*n* = 120–150')
    text = text.replace(r'$n = 120-150$', '*n* = 120–150')

    # Comprehensive LaTeX Greek and math command replacement
    text = text.replace(r'$\rightarrow$', '→').replace(r'\rightarrow', '→')
    text = text.replace(r'$\leftarrow$', '←').replace(r'\leftarrow', '←')
    text = text.replace(r'$\Rightarrow$', '⇒').replace(r'\Rightarrow', '⇒')
    text = text.replace(r'$\ge$', '≥').replace(r'\ge', '≥')
    text = text.replace(r'$\le$', '≤').replace(r'\le', '≤')
    text = text.replace(r'0{,}092', '0,092').replace(r'0{,}60', '0,60').replace(r'-0{,}3473', '-0,3473')
    text = re.sub(r'\{([0-9]+)\}', r'\1', text)
    text = text.replace(r'n.s.\ ', 'n.s. ').replace(r'n.s.\)', 'n.s.)').replace(r'n.s.\,', 'n.s.,')
    text = text.replace(r'(\emph{The Why*):}', '(*The Why*):')
    text = text.replace(r'(\emph{The Why*}):', '(*The Why*):')
    text = text.replace(r'\emph{The Why*}', '*The Why*')

    text = re.sub(r'\\beta_\{?([0-9]+)\}?', lambda m: 'β' + ''.join(chr(0x2080 + int(d)) for d in m.group(1)), text)
    text = text.replace(r'\beta_{\text{int}}', 'β_int')
    text = text.replace(r'\beta_{int}', 'β_int')
    text = text.replace(r'\beta', 'β')
    text = text.replace(r'\alpha', 'α')
    text = text.replace(r'\Delta', 'Δ')
    text = text.replace(r'\cdot', '·')
    text = text.replace(r'\partial', '∂')
    text = text.replace(r'\epsilon', 'ε')
    text = re.sub(r'\\text\{([^}]+)\}', r'\1', text)
    text = text.replace(r'R^2_{Model 2}', 'R²_Model 2')
    text = text.replace(r'R^2_{Model 1}', 'R²_Model 1')
    text = text.replace(r'R^2', 'R²')

    # Unescape LaTeX escaped symbols and spaces (e.g. US\$ -> US$, US\ -> US )
    text = text.replace(r'US\$', 'US$')
    text = text.replace(r'US\\$', 'US$')
    text = re.sub(r'\\([,%#&_])', r'\1', text)
    text = re.sub(r'\\(?=\s)', '', text)
    text = text.replace('~', ' ')

    # Remove any remaining stray math dollar signs while preserving currency notation
    text = text.replace('US$', '___USD_TOKEN___')
    text = text.replace('$', '')
    text = text.replace('___USD_TOKEN___', 'US$')
    return text


def add_body_paragraph(doc, text, bold_prefix=None, indent=True):
    """Add standard academic body paragraph."""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    if indent:
        p.paragraph_format.first_line_indent = Cm(1.25)
    else:
        p.paragraph_format.first_line_indent = Cm(0)

    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = "Times New Roman"
        r_pre.font.size = Pt(12)
        r_pre.font.bold = True

    clean_text = clean_academic_text(text)
    parse_markdown_runs(p, clean_text)
    return p


def make_run_pure_black(run, font_name="Times New Roman", font_size=Pt(12), bold=None, italic=None):
    """Guarantees pure black #000000 run formatting at both python-docx and raw OpenXML levels."""
    if font_name is not None:
        run.font.name = font_name
    if font_size is not None:
        run.font.size = font_size
    if bold is not None:
        run.font.bold = bold
    if italic is not None:
        run.font.italic = italic
    run.font.color.rgb = RGBColor(0, 0, 0)

    rPr = run._r.get_or_add_rPr()
    for c in rPr.findall(qn('w:color')):
        rPr.remove(c)
    color_elm = parse_xml(f'<w:color {nsdecls("w")} w:val="000000"/>')
    rPr.append(color_elm)

    if font_name is not None and font_name != "Cambria Math":
        for rf in rPr.findall(qn('w:rFonts')):
            rPr.remove(rf)
        rFonts = parse_xml(f'<w:rFonts {nsdecls("w")} w:ascii="{font_name}" w:hAnsi="{font_name}" w:cs="{font_name}"/>')
        rPr.append(rFonts)
    return run


def parse_markdown_runs(paragraph, text, base_size=Pt(12), base_bold=False):
    """Parse inline bold (***text***, **text**, *text*) into proper Word runs with guaranteed pure black color."""
    if not text:
        return
    pattern = re.compile(r'(\*\*\*.*?\*\*\*|\*\*.*?\*\*|\*.*?\*)')
    tokens = pattern.split(text)
    for token in tokens:
        if not token:
            continue
        if token.startswith('***') and token.endswith('***') and len(token) >= 6:
            content = token[3:-3].replace('*', '')
            run = paragraph.add_run(content)
            make_run_pure_black(run, "Times New Roman", base_size, bold=True, italic=True)
        elif token.startswith('**') and token.endswith('**') and len(token) >= 4:
            content = token[2:-2]
            sub_tokens = re.split(r'(\*.*?\*)', content)
            for st in sub_tokens:
                if not st:
                    continue
                if st.startswith('*') and st.endswith('*') and len(st) >= 2:
                    run = paragraph.add_run(st[1:-1].replace('*', ''))
                    make_run_pure_black(run, "Times New Roman", base_size, bold=True, italic=True)
                else:
                    clean_st = st.replace('*', '')
                    if clean_st:
                        run = paragraph.add_run(clean_st)
                        make_run_pure_black(run, "Times New Roman", base_size, bold=True, italic=False)
        elif token.startswith('*') and token.endswith('*') and len(token) >= 2:
            content = token[1:-1]
            sub_tokens = re.split(r'(\*\*.*?\*\*)', content)
            for st in sub_tokens:
                if not st:
                    continue
                if st.startswith('**') and st.endswith('**') and len(st) >= 4:
                    run = paragraph.add_run(st[2:-2].replace('*', ''))
                    make_run_pure_black(run, "Times New Roman", base_size, bold=True, italic=True)
                else:
                    clean_st = st.replace('*', '')
                    if clean_st:
                        run = paragraph.add_run(clean_st)
                        make_run_pure_black(run, "Times New Roman", base_size, bold=True if base_bold else False, italic=True)
        else:
            clean_plain = token.replace('*', '')
            if clean_plain:
                run = paragraph.add_run(clean_plain)
                make_run_pure_black(run, "Times New Roman", base_size, bold=True if base_bold else False, italic=False)


def set_paragraph_outline_level(paragraph, level):
    """Sets outline level on a paragraph for Word Navigation Pane & Google Docs Document Tabs."""
    pPr = paragraph._p.get_or_add_pPr()
    existing = pPr.find(qn('w:outlineLvl'))
    if existing is not None:
        existing.set(qn('w:val'), str(level))
    else:
        outline_elm = OxmlElement('w:outlineLvl')
        outline_elm.set(qn('w:val'), str(level))
        pPr.append(outline_elm)


def add_heading_1(doc, title, page_break=True):
    """BAB Heading: Centered, Bold, 12pt, ALL CAPS, Heading 1 style + outlineLvl 0."""
    if page_break:
        doc.add_page_break()
    p = doc.add_paragraph(style='Heading 1')
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(12)
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.first_line_indent = Cm(0)
    p.paragraph_format.keep_with_next = True
    set_paragraph_outline_level(p, 0)

    clean_title = clean_academic_text(title.upper())
    parse_markdown_runs(p, clean_title, base_size=Pt(12), base_bold=True)
    return p


def add_heading_2(doc, title):
    """Sub-bab Heading: Left, Bold, 12pt, Heading 2 style + outlineLvl 1."""
    p = doc.add_paragraph(style='Heading 2')
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.first_line_indent = Cm(0)
    p.paragraph_format.keep_with_next = True
    set_paragraph_outline_level(p, 1)

    clean_title = clean_academic_text(title)
    parse_markdown_runs(p, clean_title, base_size=Pt(12), base_bold=True)
    return p


def add_heading_3(doc, title):
    """Anak Sub-bab Heading: Left, Bold, 12pt, Heading 3 style + outlineLvl 2."""
    p = doc.add_paragraph(style='Heading 3')
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.first_line_indent = Cm(0)
    p.paragraph_format.keep_with_next = True
    set_paragraph_outline_level(p, 2)

    clean_title = clean_academic_text(title)
    parse_markdown_runs(p, clean_title, base_size=Pt(12), base_bold=True)
    return p


def add_frontmatter_heading(doc, title, page_break=False):
    """Frontmatter Heading: Centered, Bold, 12pt, ALL CAPS, Heading 1 style + outlineLvl 0."""
    p = doc.add_paragraph(style='Heading 1')
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(18)
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.first_line_indent = Cm(0)
    p.paragraph_format.keep_with_next = True
    if page_break:
        p.paragraph_format.page_break_before = True
    set_paragraph_outline_level(p, 0)

    clean_title = clean_academic_text(title.upper())
    parse_markdown_runs(p, clean_title, base_size=Pt(12), base_bold=True)
    return p


def add_daftar_isi_heading(doc, page_break=True):
    """Frontmatter Heading for DAFTAR ISI: Centered, Bold, 12pt, Pure Black, NO Heading 1 / outline level to prevent recursive inclusion in TOC."""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(18)
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.first_line_indent = Cm(0)
    p.paragraph_format.keep_with_next = True
    if page_break:
        p.paragraph_format.page_break_before = True
    r = p.add_run("DAFTAR ISI")
    make_run_pure_black(r, "Times New Roman", Pt(12), bold=True)
    return p



# ============================================================================
# MAIN BUILDER ENGINE
# ============================================================================


def _setup_doc_base_styles(doc):
    """Configure FEB UKRIDA 2023 base styles (Normal, Footer, Heading 1-3).
    Extracted as standalone function so it can be imported by extract_frontmatter_pages.py.
    """
    import docx
    try:
        style_normal = doc.styles['Normal']
        style_normal.font.name = 'Times New Roman'
        style_normal.font.size = Pt(12)
        style_normal.font.color.rgb = RGBColor(0, 0, 0)
    except Exception as e:
        print(f"[WARN] Could not customize Normal style: {e}")

    try:
        style_footer = doc.styles['Footer']
        style_footer.font.name = 'Times New Roman'
        style_footer.font.size = Pt(10)
        style_footer.font.bold = True
        style_footer.font.color.rgb = RGBColor(0, 0, 0)
        style_footer.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    except Exception as e:
        print(f"[WARN] Could not customize Footer style: {e}")

    for level, style_name in [(1, 'Heading 1'), (2, 'Heading 2'), (3, 'Heading 3')]:
        try:
            h_style = doc.styles[style_name]
            h_style.font.name = 'Times New Roman'
            h_style.font.size = Pt(12)
            h_style.font.bold = True
            h_style.font.color.rgb = RGBColor(0, 0, 0)
            h_style.paragraph_format.line_spacing = 1.5
            h_style.paragraph_format.keep_with_next = True
            h_style.paragraph_format.first_line_indent = Cm(0)
            if level == 1:
                h_style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
                h_style.paragraph_format.space_before = Pt(0)
                h_style.paragraph_format.space_after = Pt(12)
            elif level == 2:
                h_style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
                h_style.paragraph_format.space_before = Pt(12)
                h_style.paragraph_format.space_after = Pt(6)
            elif level == 3:
                h_style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
                h_style.paragraph_format.space_before = Pt(6)
                h_style.paragraph_format.space_after = Pt(3)

            rPr = h_style.element.get_or_add_rPr()
            for c in rPr.findall(qn('w:color')):
                rPr.remove(c)
            rPr.append(parse_xml(f'<w:color {nsdecls("w")} w:val="000000"/>'))
            for rf in rPr.findall(qn('w:rFonts')):
                rPr.remove(rf)
            rPr.append(parse_xml(f'<w:rFonts {nsdecls("w")} w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>'))
        except Exception as e:
            print(f"[WARN] Could not customize style {style_name}: {e}")


def build_formal_approval_sheets(doc, id_data):
    """Generates the 3 formal academic sheets required for full thesis proposals with borderless tables and perfect alignment."""
    # 1. Pernyataan Keaslian (hal. ii)
    add_frontmatter_heading(doc, "PERNYATAAN KEASLIAN KARYA TUGAS AKHIR", page_break=False)

    add_body_paragraph(doc, "Saya mahasiswa Universitas Kristen Krida Wacana:", indent=False)

    # Identity Table (Border-free, snug colon, fixed widths matching 14.0cm text width)
    tbl_id = doc.add_table(rows=4, cols=3)
    tbl_id.alignment = WD_TABLE_ALIGNMENT.CENTER
    col_id_widths = [Cm(3.8), Cm(0.4), Cm(9.8)]
    set_col_widths_fixed(tbl_id, col_id_widths)
    remove_table_borders(tbl_id)

    for row_idx, (col1, col2, col3) in enumerate(id_data):
        row = tbl_id.rows[row_idx]
        for c_idx, val in enumerate([col1, col2, col3]):
            cell = row.cells[c_idx]
            set_cell_margins(cell, top=20, bottom=20, left=0 if c_idx == 0 else 40, right=40)
            p_cell = cell.paragraphs[0]
            p_cell.paragraph_format.space_before = Pt(0)
            p_cell.paragraph_format.space_after = Pt(0)
            p_cell.paragraph_format.line_spacing = 1.15
            p_cell.paragraph_format.first_line_indent = Cm(0)
            p_cell.alignment = WD_ALIGN_PARAGRAPH.CENTER if c_idx == 1 else WD_ALIGN_PARAGRAPH.LEFT
            rc = p_cell.add_run(val)
            make_run_pure_black(rc, "Times New Roman", Pt(12), bold=(c_idx == 2))

    add_body_paragraph(doc, "Dengan ini menyatakan dengan sesungguhnya bahwa Proposal Skripsi yang berjudul:", indent=False)

    p_j = doc.add_paragraph()
    p_j.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_j.paragraph_format.space_before = Pt(6)
    p_j.paragraph_format.space_after = Pt(6)
    p_j.paragraph_format.line_spacing = 1.15
    p_j.paragraph_format.first_line_indent = Cm(0)
    rj = p_j.add_run("“PENGARUH HEDONIC MOTIVATION, DESIRE FOR COMPLETENESS, DAN SPECULATIVE MOTIVE TERHADAP IMPULSIVE BUYING BOOSTER PACK KARTU POKÉMON TCG DENGAN SELF-CONTROL SEBAGAI VARIABEL MODERASI”")
    make_run_pure_black(rj, "Times New Roman", Pt(11), bold=True)

    add_body_paragraph(doc, "adalah:", indent=False)

    points = [
        "Benar-benar hasil karya saya sendiri, bukan merupakan jiplakan, plagiarisme, fabrikasi, atau tiruan dari karya tulis ilmiah orang lain yang pernah diajukan untuk memperoleh gelar akademik di perguruan tinggi manapun.",
        "Seluruh kutipan, data, dan rujukan ilmiah yang digunakan dalam naskah ini telah dicantumkan sumbernya secara jelas dan lengkap sesuai dengan kaidah penulisan ilmiah yang berlaku di Universitas Kristen Krida Wacana.",
        "Apabila di kemudian hari terbukti bahwa pernyataan ini tidak benar atau ditemukan indikasi plagiarisme, saya bersedia menerima sanksi akademik yang berlaku sesuai dengan peraturan perundang-undangan dan ketentuan di lingkungan Universitas Kristen Krida Wacana."
    ]
    for idx, pt_text in enumerate(points):
        p_pt = doc.add_paragraph()
        p_pt.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p_pt.paragraph_format.left_indent = Cm(1.25)
        p_pt.paragraph_format.first_line_indent = Cm(-0.63)
        p_pt.paragraph_format.space_before = Pt(0)
        p_pt.paragraph_format.space_after = Pt(4)
        p_pt.paragraph_format.line_spacing = 1.15
        r_idx = p_pt.add_run(f"{idx+1}.  ")
        make_run_pure_black(r_idx, "Times New Roman", Pt(12), bold=True)
        r_txt = p_pt.add_run(pt_text)
        make_run_pure_black(r_txt, "Times New Roman", Pt(12))

    # Signature Block Pernyataan Keaslian (Border-free, fixed 7.0cm width)
    tbl_sig = doc.add_table(rows=1, cols=2)
    tbl_sig.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_col_widths_fixed(tbl_sig, [Cm(7.0), Cm(7.0)])
    remove_table_borders(tbl_sig)
    c_left = tbl_sig.rows[0].cells[0]
    c_right = tbl_sig.rows[0].cells[1]

    p_l = c_left.paragraphs[0]
    p_l.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_l.paragraph_format.space_before = Pt(24)
    p_l.paragraph_format.first_line_indent = Cm(0)
    rl = p_l.add_run("\n\n[ Materai Rp10.000 ]\n\n")
    make_run_pure_black(rl, "Times New Roman", Pt(10), italic=True)

    p_r = c_right.paragraphs[0]
    p_r.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_r.paragraph_format.space_before = Pt(12)
    p_r.paragraph_format.line_spacing = 1.15
    p_r.paragraph_format.first_line_indent = Cm(0)
    r_hdr = p_r.add_run("Jakarta, 12 September 2026\nYang membuat pernyataan,\n\n\n\n\n")
    make_run_pure_black(r_hdr, "Times New Roman", Pt(12))
    r_nm = p_r.add_run("Arthur Reezan\n")
    make_run_pure_black(r_nm, "Times New Roman", Pt(12), bold=True)
    r_nim = p_r.add_run("NIM: 312023002")
    make_run_pure_black(r_nim, "Times New Roman", Pt(12))

    # 2. Halaman Persetujuan Proposal Skripsi (hal. iii)
    add_frontmatter_heading(doc, "HALAMAN PERSETUJUAN PROPOSAL SKRIPSI", page_break=True)

    add_body_paragraph(doc, "Proposal Skripsi ini diajukan oleh:", indent=False)

    tbl_per = doc.add_table(rows=4, cols=3)
    tbl_per.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_col_widths_fixed(tbl_per, col_id_widths)
    remove_table_borders(tbl_per)

    for row_idx, (col1, col2, col3) in enumerate(id_data):
        row = tbl_per.rows[row_idx]
        for c_idx, val in enumerate([col1, col2, col3]):
            cell = row.cells[c_idx]
            set_cell_margins(cell, top=20, bottom=20, left=0 if c_idx == 0 else 40, right=40)
            p_cell = cell.paragraphs[0]
            p_cell.paragraph_format.space_before = Pt(0)
            p_cell.paragraph_format.space_after = Pt(0)
            p_cell.paragraph_format.line_spacing = 1.15
            p_cell.paragraph_format.first_line_indent = Cm(0)
            p_cell.alignment = WD_ALIGN_PARAGRAPH.CENTER if c_idx == 1 else WD_ALIGN_PARAGRAPH.LEFT
            rc = p_cell.add_run(val)
            make_run_pure_black(rc, "Times New Roman", Pt(12), bold=(c_idx == 2))

    p_j2 = doc.add_paragraph()
    p_j2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_j2.paragraph_format.space_before = Pt(12)
    p_j2.paragraph_format.space_after = Pt(12)
    p_j2.paragraph_format.line_spacing = 1.15
    p_j2.paragraph_format.first_line_indent = Cm(0)
    rj2 = p_j2.add_run("“PENGARUH HEDONIC MOTIVATION, DESIRE FOR COMPLETENESS, DAN SPECULATIVE MOTIVE TERHADAP IMPULSIVE BUYING BOOSTER PACK KARTU POKÉMON TCG DENGAN SELF-CONTROL SEBAGAI VARIABEL MODERASI”")
    make_run_pure_black(rj2, "Times New Roman", Pt(11), bold=True)

    add_body_paragraph(doc, "Telah disetujui untuk diajukan dalam Seminar Proposal Skripsi Program Studi S1 Manajemen Fakultas Ekonomi dan Bisnis Universitas Kristen Krida Wacana.", indent=False)

    # 3-Row Layout for Approval Signatures: Guaranteed Horizontal Baseline Parity & Border-Free
    tbl_apv = doc.add_table(rows=3, cols=2)
    tbl_apv.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_col_widths_fixed(tbl_apv, [Cm(7.0), Cm(7.0)])
    remove_table_borders(tbl_apv)

    # Row 0: Titles
    ca0_left = tbl_apv.rows[0].cells[0]
    set_cell_margins(ca0_left, top=0, bottom=0, left=20, right=20)
    p0_l = ca0_left.paragraphs[0]
    p0_l.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p0_l.paragraph_format.space_before = Pt(12)
    p0_l.paragraph_format.space_after = Pt(0)
    p0_l.paragraph_format.line_spacing = 1.15
    p0_l.paragraph_format.first_line_indent = Cm(0)
    r0_l = p0_l.add_run("Menyetujui,\nDosen Pembimbing")
    make_run_pure_black(r0_l, "Times New Roman", Pt(12))

    ca0_right = tbl_apv.rows[0].cells[1]
    set_cell_margins(ca0_right, top=0, bottom=0, left=20, right=20)
    p0_r = ca0_right.paragraphs[0]
    p0_r.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p0_r.paragraph_format.space_before = Pt(12)
    p0_r.paragraph_format.space_after = Pt(0)
    p0_r.paragraph_format.line_spacing = 1.15
    p0_r.paragraph_format.first_line_indent = Cm(0)
    r0_r = p0_r.add_run("Mengetahui,\nKetua Program Studi S1 Manajemen")
    make_run_pure_black(r0_r, "Times New Roman", Pt(12))

    # Row 1: Signature Space (fixed height ~55pt)
    ca1_left = tbl_apv.rows[1].cells[0]
    set_cell_margins(ca1_left, top=0, bottom=0, left=20, right=20)
    p1_l = ca1_left.paragraphs[0]
    p1_l.paragraph_format.space_before = Pt(55)
    p1_l.paragraph_format.space_after = Pt(0)
    p1_l.paragraph_format.line_spacing = 1.0

    ca1_right = tbl_apv.rows[1].cells[1]
    set_cell_margins(ca1_right, top=0, bottom=0, left=20, right=20)
    p1_r = ca1_right.paragraphs[0]
    p1_r.paragraph_format.space_before = Pt(55)
    p1_r.paragraph_format.space_after = Pt(0)
    p1_r.paragraph_format.line_spacing = 1.0

    # Row 2: Names & NIDN (Locked at exact same horizontal baseline)
    ca2_left = tbl_apv.rows[2].cells[0]
    set_cell_margins(ca2_left, top=0, bottom=0, left=20, right=20)
    p2_l = ca2_left.paragraphs[0]
    p2_l.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p2_l.paragraph_format.space_before = Pt(0)
    p2_l.paragraph_format.space_after = Pt(0)
    p2_l.paragraph_format.line_spacing = 1.15
    p2_l.paragraph_format.first_line_indent = Cm(0)
    r2_l_name = p2_l.add_run("Dr. Fredella Colline, S.E., M.M., CFP®, PFM, CHCP-A\n")
    make_run_pure_black(r2_l_name, "Times New Roman", Pt(12), bold=True)
    r2_l_nidn = p2_l.add_run("NIDN: [NIDN_DOSEN]")
    make_run_pure_black(r2_l_nidn, "Times New Roman", Pt(12))

    ca2_right = tbl_apv.rows[2].cells[1]
    set_cell_margins(ca2_right, top=0, bottom=0, left=20, right=20)
    p2_r = ca2_right.paragraphs[0]
    p2_r.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p2_r.paragraph_format.space_before = Pt(0)
    p2_r.paragraph_format.space_after = Pt(0)
    p2_r.paragraph_format.line_spacing = 1.15
    p2_r.paragraph_format.first_line_indent = Cm(0)
    r2_r_name = p2_r.add_run("Rita Amelinda, S.E., M.M.\n")
    make_run_pure_black(r2_r_name, "Times New Roman", Pt(12), bold=True)
    r2_r_nidn = p2_r.add_run("NIDN: [NIDN_KAPRODI]")
    make_run_pure_black(r2_r_nidn, "Times New Roman", Pt(12))

    # 3. Halaman Pengesahan Tim Penguji (hal. iv)
    add_frontmatter_heading(doc, "HALAMAN PENGESAHAN TIM PENGUJI SEMINAR PROPOSAL", page_break=True)

    add_body_paragraph(doc, "Proposal Skripsi yang berjudul:", indent=False)
    p_j3 = doc.add_paragraph()
    p_j3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_j3.paragraph_format.space_before = Pt(6)
    p_j3.paragraph_format.space_after = Pt(6)
    p_j3.paragraph_format.line_spacing = 1.15
    p_j3.paragraph_format.first_line_indent = Cm(0)
    rj3 = p_j3.add_run("“PENGARUH HEDONIC MOTIVATION, DESIRE FOR COMPLETENESS, DAN SPECULATIVE MOTIVE TERHADAP IMPULSIVE BUYING BOOSTER PACK KARTU POKÉMON TCG DENGAN SELF-CONTROL SEBAGAI VARIABEL MODERASI”")
    make_run_pure_black(rj3, "Times New Roman", Pt(11), bold=True)

    add_body_paragraph(doc, "Telah dipertahankan di hadapan Tim Penguji Seminar Proposal Skripsi Program Studi S1 Manajemen Fakultas Ekonomi dan Bisnis Universitas Kristen Krida Wacana pada tanggal yang ditetapkan dan dinyatakan telah memenuhi syarat kelayakan.", indent=False)

    tbl_penguji = doc.add_table(rows=2, cols=2)
    tbl_penguji.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_col_widths_fixed(tbl_penguji, [Cm(7.0), Cm(7.0)])
    remove_table_borders(tbl_penguji)

    c_p1 = tbl_penguji.rows[0].cells[0]
    c_p2 = tbl_penguji.rows[0].cells[1]
    c_p3 = tbl_penguji.rows[1].cells[0]
    c_p4 = tbl_penguji.rows[1].cells[1]

    p_p1 = c_p1.paragraphs[0]
    p_p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_p1.paragraph_format.line_spacing = 1.15
    p_p1.paragraph_format.first_line_indent = Cm(0)
    p_p1.paragraph_format.space_before = Pt(6)
    r = p_p1.add_run("Ketua Tim Penguji\n\n\n\n\n_________________________\n")
    make_run_pure_black(r, "Times New Roman", Pt(12), bold=True)
    r_nidn = p_p1.add_run("NIDN: _________________")
    make_run_pure_black(r_nidn, "Times New Roman", Pt(12))

    p_p2 = c_p2.paragraphs[0]
    p_p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_p2.paragraph_format.line_spacing = 1.15
    p_p2.paragraph_format.first_line_indent = Cm(0)
    p_p2.paragraph_format.space_before = Pt(6)
    r = p_p2.add_run("Anggota Penguji 1\n\n\n\n\n_________________________\n")
    make_run_pure_black(r, "Times New Roman", Pt(12), bold=True)
    r_nidn = p_p2.add_run("NIDN: _________________")
    make_run_pure_black(r_nidn, "Times New Roman", Pt(12))

    p_p3 = c_p3.paragraphs[0]
    p_p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_p3.paragraph_format.line_spacing = 1.15
    p_p3.paragraph_format.first_line_indent = Cm(0)
    p_p3.paragraph_format.space_before = Pt(12)
    r = p_p3.add_run("Anggota Penguji 2 / Pembimbing\n\n\n\n\nDr. Fredella Colline, S.E., M.M.\n")
    make_run_pure_black(r, "Times New Roman", Pt(12), bold=True)
    r_nidn = p_p3.add_run("NIDN: [NIDN_DOSEN]")
    make_run_pure_black(r_nidn, "Times New Roman", Pt(12))

    p_p4 = c_p4.paragraphs[0]
    p_p4.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_p4.paragraph_format.line_spacing = 1.15
    p_p4.paragraph_format.first_line_indent = Cm(0)
    p_p4.paragraph_format.space_before = Pt(12)
    r = p_p4.add_run("Mengetahui,\nKetua Program Studi S1 Manajemen\n\n\n\n\nRita Amelinda, S.E., M.M.\n")
    make_run_pure_black(r, "Times New Roman", Pt(12), bold=True)
    r_nidn = p_p4.add_run("NIDN: [NIDN_KAPRODI]")
    make_run_pure_black(r_nidn, "Times New Roman", Pt(12))


def build_full_proposal(skip_chapter3: bool = False, skip_frontmatter: bool = False):
    """Build the full thesis proposal DOCX.

    Args:
        skip_chapter3: If True, omit Bab 3 (review/bimbingan mode).
        skip_frontmatter: If True, omit the 6 formal frontmatter pages
            (Pernyataan Keaslian, Persetujuan, Pengesahan, Kata Pengantar,
            Abstrak, Abstract). Document starts directly with Daftar Isi.
            Page numbering resets: Daftar Isi = i, Bab 1 = 1.
    """
    # Resolve base_dir relative to this script's location
    script_dir = Path(__file__).resolve().parent
    base_dir = script_dir.parent / "01_Naskah_Utama"
    if not base_dir.exists():
        # Fallback: original hardcoded path
        base_dir = Path(r"z:\SKRIPSII\SKRIPSI-arthur\01_Naskah_Utama")

    if skip_frontmatter:
        if skip_chapter3:
            output_docx = base_dir / "Proposal_Arthur_NoBab3_NoFrontmatter.docx"
        else:
            output_docx = base_dir / "Proposal_Arthur_PokemonTCG_NoFrontmatter.docx"
    elif skip_chapter3:
        output_docx = base_dir / "Proposal_Arthur_NoBab3.docx"
    else:
        output_docx = base_dir / "Proposal_Arthur_PokemonTCG.docx"
    img_rerangka = base_dir / "images" / "gambar_rerangka_penelitian.png"
    img_alur = base_dir / "images" / "diagram_alur_penelitian.png"
    img_fig11 = base_dir / "images" / "gambar1_1_media_franchise_ranking.png"
    img_fig12 = base_dir / "images" / "gambar1_2_pokemon_tcg_production_growth.png"
    img_fig13 = base_dir / "images" / "gambar1_3_psa_grading_price_disparity.png"

    print(f"[*] Starting Publication-Grade Word Proposal Generation...")
    doc = Document()

    # Configure document base styles to match FEB UKRIDA 2023
    try:
        style_normal = doc.styles['Normal']
        style_normal.font.name = 'Times New Roman'
        style_normal.font.size = Pt(12)
        style_normal.font.color.rgb = RGBColor(0, 0, 0)
    except Exception as e:
        print(f"[WARN] Could not customize Normal style: {e}")

    try:
        style_footer = doc.styles['Footer']
        style_footer.font.name = 'Times New Roman'
        style_footer.font.size = Pt(10)
        style_footer.font.bold = True
        style_footer.font.color.rgb = RGBColor(0, 0, 0)
        style_footer.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    except Exception as e:
        print(f"[WARN] Could not customize Footer style: {e}")

    # Configure Heading styles with explicit OpenXML pure black (no themeColor)
    for level, style_name in [(1, 'Heading 1'), (2, 'Heading 2'), (3, 'Heading 3')]:
        try:
            h_style = doc.styles[style_name]
            h_style.font.name = 'Times New Roman'
            h_style.font.size = Pt(12)
            h_style.font.bold = True
            h_style.font.color.rgb = RGBColor(0, 0, 0)
            h_style.paragraph_format.line_spacing = 1.5
            h_style.paragraph_format.keep_with_next = True
            h_style.paragraph_format.first_line_indent = Cm(0)
            if level == 1:
                h_style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
                h_style.paragraph_format.space_before = Pt(0)
                h_style.paragraph_format.space_after = Pt(12)
            elif level == 2:
                h_style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
                h_style.paragraph_format.space_before = Pt(12)
                h_style.paragraph_format.space_after = Pt(6)
            elif level == 3:
                h_style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
                h_style.paragraph_format.space_before = Pt(6)
                h_style.paragraph_format.space_after = Pt(3)

            rPr = h_style.element.get_or_add_rPr()
            for c in rPr.findall(qn('w:color')):
                rPr.remove(c)
            rPr.append(parse_xml(f'<w:color {nsdecls("w")} w:val="000000"/>'))
            for rf in rPr.findall(qn('w:rFonts')):
                rPr.remove(rf)
            rPr.append(parse_xml(f'<w:rFonts {nsdecls("w")} w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>'))
        except Exception as e:
            print(f"[WARN] Could not customize style {style_name}: {e}")

    # Register and configure official TOC styles (TOC 1, TOC 2, TOC 3) with right tab stops & dot leaders
    toc_styles_data = [
        ('TOC 1', Pt(11), True, Cm(0)),
        ('TOC 2', Pt(11), False, Cm(0.6)),
        ('TOC 3', Pt(10.5), False, Cm(1.2))
    ]
    for toc_name, fsize, fbold, findent in toc_styles_data:
        try:
            try:
                toc_style = doc.styles.add_style(toc_name, docx.enum.style.WD_STYLE_TYPE.PARAGRAPH)
            except Exception:
                toc_style = doc.styles[toc_name]
            toc_style.font.name = 'Times New Roman'
            toc_style.font.size = fsize
            toc_style.font.bold = fbold
            toc_style.font.color.rgb = RGBColor(0, 0, 0)
            toc_style.paragraph_format.line_spacing = 1.15
            toc_style.paragraph_format.space_before = Pt(0)
            toc_style.paragraph_format.space_after = Pt(2)
            toc_style.paragraph_format.left_indent = findent
            toc_style.paragraph_format.first_line_indent = Cm(0)
            toc_style.paragraph_format.right_indent = Cm(0)

            pPr = toc_style.element.get_or_add_pPr()
            for tb in pPr.findall(qn('w:tabs')):
                pPr.remove(tb)
            tabs_elm = parse_xml(f'<w:tabs {nsdecls("w")}><w:tab w:val="right" w:leader="dot" w:pos="7938"/></w:tabs>')
            pPr.append(tabs_elm)

            rPr = toc_style.element.get_or_add_rPr()
            for c in rPr.findall(qn('w:color')):
                rPr.remove(c)
            rPr.append(parse_xml(f'<w:color {nsdecls("w")} w:val="000000"/>'))
        except Exception as e:
            print(f"[WARN] Could not setup {toc_name}: {e}")

    # ------------------------------------------------------------------------
    # SECTION 1: HALAMAN SAMPUL / COVER (hal. i - unnumbered)
    # ------------------------------------------------------------------------
    sec_cover = doc.sections[0]
    sec_cover.page_width = Cm(21.0)
    sec_cover.page_height = Cm(29.7)
    sec_cover.top_margin = Cm(3.0)
    sec_cover.bottom_margin = Cm(3.0)
    sec_cover.left_margin = Cm(4.0)
    sec_cover.right_margin = Cm(3.0)

    # Empty unlinked footer for cover
    sec_cover.different_first_page_header_footer = True
    footer_cover = sec_cover.first_page_footer
    p_fc = footer_cover.paragraphs[0]
    p_fc.text = ""

    # Cover Logo
    img_pentagram = base_dir / "images" / "ukrida_pentagram.png"
    if img_pentagram.exists():
        p_logo = doc.add_paragraph()
        p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo.paragraph_format.space_before = Pt(0)
        p_logo.paragraph_format.space_after = Pt(18)
        p_logo.paragraph_format.first_line_indent = Cm(0)
        p_logo.add_run().add_picture(str(img_pentagram), width=Cm(3.2))

    # Cover Content
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(18)
    r = p.add_run("PROPOSAL SKRIPSI")
    r.font.name = "Times New Roman"
    r.font.size = Pt(14)
    r.font.bold = True

    # Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(12)
    p_title.paragraph_format.space_after = Pt(24)
    p_title.paragraph_format.line_spacing = 1.15

    title_parts = [
        ("PENGARUH ", False),
        ("HEDONIC MOTIVATION", True),
        (", ", False),
        ("DESIRE FOR COMPLETENESS", True),
        (", DAN ", False),
        ("SPECULATIVE MOTIVE", True),
        (" TERHADAP ", False),
        ("IMPULSIVE BUYING", True),
        (" BOOSTER PACK KARTU POKÉMON TCG DENGAN ", False),
        ("SELF-CONTROL", True),
        (" SEBAGAI VARIABEL MODERASI", False)
    ]
    for text_val, is_italic in title_parts:
        run = p_title.add_run(text_val)
        run.font.name = "Times New Roman"
        run.font.size = Pt(14)
        run.font.bold = True
        run.font.italic = is_italic

    # Subtitle
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_before = Pt(18)
    p_sub.paragraph_format.space_after = Pt(24)
    p_sub.paragraph_format.line_spacing = 1.15
    r = p_sub.add_run("Diajukan Kepada Program Studi S1 Manajemen\nUntuk Menyusun Skripsi Sarjana Manajemen (S.M.)")
    r.font.name = "Times New Roman"
    r.font.size = Pt(12)

    # Author
    p_auth = doc.add_paragraph()
    p_auth.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_auth.paragraph_format.space_before = Pt(24)
    p_auth.paragraph_format.space_after = Pt(36)
    p_auth.paragraph_format.line_spacing = 1.15
    r1 = p_auth.add_run("Diajukan Oleh:\n\n")
    r1.font.name = "Times New Roman"
    r1.font.size = Pt(12)
    r2 = p_auth.add_run("Arthur Reezan\n(312023002)")
    r2.font.name = "Times New Roman"
    r2.font.size = Pt(12)
    r2.font.bold = True

    # Institution Footer
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.space_before = Pt(48)
    p_inst.paragraph_format.space_after = Pt(0)
    p_inst.paragraph_format.line_spacing = 1.15
    r_inst = p_inst.add_run(
        "PROGRAM STUDI S1 MANAJEMEN\n"
        "FAKULTAS EKONOMI DAN BISNIS\n"
        "UNIVERSITAS KRISTEN KRIDA WACANA\n"
        "JAKARTA 2026"
    )
    r_inst.font.name = "Times New Roman"
    r_inst.font.size = Pt(12)
    r_inst.font.bold = True

    # ------------------------------------------------------------------------
    # SECTION 2: FRONTMATTER (Halaman ii s.d. x - Roman Numerals)
    # ------------------------------------------------------------------------
    sec_front = doc.add_section(WD_SECTION.NEW_PAGE)
    sec_front.page_width = Cm(21.0)
    sec_front.page_height = Cm(29.7)
    sec_front.top_margin = Cm(3.0)
    sec_front.bottom_margin = Cm(3.0)
    sec_front.left_margin = Cm(4.0)
    sec_front.right_margin = Cm(3.0)
    sec_front.header.is_linked_to_previous = False
    sec_front.footer.is_linked_to_previous = False

    if skip_frontmatter:
        # No formal pages: Daftar Isi starts at roman i
        add_page_number_to_footer(sec_front, is_roman=True, start_num=1)
    else:
        add_page_number_to_footer(sec_front, is_roman=True, start_num=2)

    # ------------------------------------------------------------------------
    # SECTION 2: FRONTMATTER
    # ------------------------------------------------------------------------
    id_data = [
        ("Nama Mahasiswa", ":", "Arthur Reezan"),
        ("NIM", ":", "312023002"),
        ("Program Studi", ":", "Program Studi S1 Manajemen"),
        ("Konsentrasi", ":", "Manajemen Keuangan")
    ]

    if not skip_frontmatter:
        if not skip_chapter3:
            # Full proposal requires formal approval sheets
            build_formal_approval_sheets(doc, id_data)
            add_frontmatter_heading(doc, "KATA PENGANTAR", page_break=True)
        else:
            # NoBab3 proposal (review/bimbingan mode) starts directly with Kata Pengantar
            add_frontmatter_heading(doc, "KATA PENGANTAR", page_break=False)

    if not skip_frontmatter:
        add_body_paragraph(doc, "Puji dan syukur penulis panjatkan ke hadirat Tuhan Yang Maha Esa atas kasih, anugerah, dan penyertaan-Nya yang senantiasa melimpah, sehingga penulis dapat menyelesaikan penyusunan proposal skripsi yang berjudul **“PENGARUH HEDONIC MOTIVATION, DESIRE FOR COMPLETENESS, DAN SPECULATIVE MOTIVE TERHADAP IMPULSIVE BUYING BOOSTER PACK KARTU POKÉMON TCG DENGAN SELF-CONTROL SEBAGAI VARIABEL MODERASI”** dengan baik, lancar, dan tepat waktu.")
        add_body_paragraph(doc, "Proposal skripsi ini disusun sebagai salah satu tahapan akademik yang diwajibkan dalam rangka menempuh ujian seminar proposal guna menyelesaikan studi pada Program Studi S1 Manajemen, Konsentrasi Manajemen Keuangan, Fakultas Ekonomi dan Bisnis, Universitas Kristen Krida Wacana (UKRIDA), Jakarta.")
        add_body_paragraph(doc, "Dalam proses penyusunan naskah proposal ini, penulis mendapatkan banyak bimbingan, arahan metodologis, dukungan moril, serta fasilitas dari berbagai pihak. Oleh karena itu, dengan penuh rasa hormat dan kerendahan hati, penulis menyampaikan terima kasih dan apresiasi yang setinggi-tingginya kepada:")

        kp_points = [
            "Dr. Fredella Colline, S.E., M.M., CFP®, PFM, CHCP-A, selaku Dosen Pembimbing Skripsi, yang telah dengan luar biasa sabar, teliti, kritis, dan penuh dedikasi meluangkan waktu serta mencurahkan tenaga dan pikiran dalam membimbing, mengarahkan, dan menyempurnakan naskah proposal ini sejak tahap awal perumusan gagasan hingga penyusunan naskah komprehensif.",
            "Rita Amelinda, S.E., M.M., selaku Ketua Program Studi S1 Manajemen FEB UKRIDA, atas segala arahan, kemudahan proses administratif, dan bimbingan akademik yang diberikan.",
            "Bapak dan Ibu Dosen Penguji Seminar Proposal, yang telah bersedia meluangkan waktu untuk menguji, memberikan koreksi kritis, serta masukan yang konstruktif guna menyempurnakan naskah penelitian ini.",
            "Seluruh Dosen dan Staf Pengajar FEB UKRIDA, yang telah membagikan ilmu pengetahuan, wawasan analisis keuangan, serta etika profesional selama masa perkuliahan penulis.",
            "Kedua Orang Tua dan Keluarga Tercinta, atas doa yang tiada putus, limpahan kasih sayang, ketulusan pengorbanan, serta dorongan moral dan material yang menjadi sumber kekuatan utama bagi penulis.",
            "Rekan-rekan Mahasiswa Manajemen FEB UKRIDA Angkatan 2023 dan sahabat seperjuangan, atas diskusi yang membangun, motivasi, dan kerja sama selama proses perkuliahan.",
            "Komunitas Kolektor dan Pemain Pokémon TCG di Indonesia, yang telah memberikan gambaran nyata mengenai fenomena pasar kartu koleksi di lapangan."
        ]
        for idx, kpt in enumerate(kp_points):
            p_kp = doc.add_paragraph()
            p_kp.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p_kp.paragraph_format.left_indent = Cm(1.25)
            p_kp.paragraph_format.first_line_indent = Cm(-0.63)
            p_kp.paragraph_format.space_before = Pt(0)
            p_kp.paragraph_format.space_after = Pt(3)
            p_kp.paragraph_format.line_spacing = 1.15
            p_kp.add_run(f"{idx+1}.  ").font.bold = True
            p_kp.add_run(kpt)

        add_body_paragraph(doc, "Penulis menyadari bahwa proposal ini masih jauh dari kesempurnaan. Kritik dan saran yang membangun sangat diharapkan demi penyempurnaan karya ilmiah ini ke depan. Semoga proposal skripsi ini dapat memberikan manfaat akademis dan praktis bagi perkembangan kajian ilmu manajemen keuangan perilaku di Indonesia.")

        p_tutup = doc.add_paragraph()
        p_tutup.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p_tutup.paragraph_format.space_before = Pt(18)
        p_tutup.paragraph_format.line_spacing = 1.15
        p_tutup.add_run("Jakarta,                  2026\nPenulis,\n\n\n\n")
        p_tutup.add_run("Arthur Reezan\n").font.bold = True
        p_tutup.add_run("NIM: 312023002")

        # 5. Abstrak Bahasa Indonesia
        add_frontmatter_heading(doc, "ABSTRAK", page_break=True)

        p_j4 = doc.add_paragraph()
        p_j4.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_j4.paragraph_format.space_before = Pt(0)
        p_j4.paragraph_format.space_after = Pt(12)
        p_j4.paragraph_format.line_spacing = 1.15
        rj4 = p_j4.add_run("PENGARUH HEDONIC MOTIVATION, DESIRE FOR COMPLETENESS, DAN SPECULATIVE MOTIVE TERHADAP IMPULSIVE BUYING BOOSTER PACK KARTU POKÉMON TCG DENGAN SELF-CONTROL SEBAGAI VARIABEL MODERASI\n\nArthur Reezan (312023002)\nProgram Studi S1 Manajemen, Fakultas Ekonomi dan Bisnis, Universitas Kristen Krida Wacana\nDosen Pembimbing: Dr. Fredella Colline, S.E., M.M., CFP®, PFM, CHCP-A")
        rj4.font.name = "Times New Roman"
        rj4.font.size = Pt(12)
        rj4.font.bold = True

        p_abs = doc.add_paragraph()
        p_abs.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p_abs.paragraph_format.line_spacing = 1.0
        p_abs.paragraph_format.space_before = Pt(6)
        p_abs.paragraph_format.space_after = Pt(6)
        p_abs.paragraph_format.first_line_indent = Cm(1.25)
        r_abs = p_abs.add_run(
            "Penelitian ini bertujuan untuk menganalisis dan menguji secara empiris pengaruh hedonic motivation (motivasi hedonis), "
            "desire for completeness (hasrat kelengkapan koleksi), dan speculative motive (motif spekulasi finansial) terhadap impulsive buying "
            "(pembelian impulsif) booster pack kartu Pokémon Trading Card Game (Pokémon TCG) fisik resmi berbahasa Indonesia, serta menguji peran kontrol diri "
            "(self-control) sebagai variabel moderasi dalam memperlemah pengaruh ketiga variabel anteseden tersebut. Penelitian ini menggunakan pendekatan kuantitatif "
            "asosiatif dengan desain survei cross-sectional. Data primer dikumpulkan melalui penyebaran kuesioner daring berbasis skala Likert 5 poin kepada responden "
            "yang dipilih melalui teknik purposive sampling. Kriteria inklusi sampel adalah konsumen atau kolektor Warga Negara Indonesia (WNI) berusia minimal 17 tahun "
            "yang pernah membeli booster pack Pokémon TCG fisik resmi dalam rentang waktu 6–12 bulan terakhir. Jumlah sampel yang ditargetkan adalah 120 hingga 150 responden, "
            "mengacu pada rekomendasi ukuran sampel Green (1991) dan Cohen (1988) untuk mencapai kekuatan uji statistik (statistical power) yang memadai pada model regresi "
            "linear berganda. Metode analisis data menggunakan analisis regresi berganda dan Moderated Regression Analysis (MRA) dengan prosedur pemusatan rata-rata "
            "(mean-centering) guna mereduksi potensi multikolinearitas non-esensial antara variabel prediktor dengan produk interaksinya (Aiken dan West, 1991; Ghozali, 2018), yang diolah menggunakan perangkat lunak "
            "IBM SPSS Statistics. Penelitian ini menawarkan kebaruan teoritis (novelty) dengan mengintegrasikan kerangka psikologi lingkungan Stimulus-Organism-Response (S-O-R), "
            "psikologi kolektor (Zeigarnik Effect dan The Completing the Set Effect), teori regulasi diri (Self-Regulation Theory), serta prinsip-prinsip keuangan perilaku "
            "(behavioral finance) pada fenomena komoditas hobi fisik bernilai spekulatif tinggi. Hasil penelitian ini diharapkan memberikan kontribusi empiris bagi konsumen "
            "muda dalam menjaga kontrol diri finansial, serta masukan aplikatif bagi komunitas hobi dan pemangku kebijakan edukasi keuangan generasi muda di Indonesia."
        )
        r_abs.font.name = "Times New Roman"
        r_abs.font.size = Pt(12)

        p_kw = doc.add_paragraph()
        p_kw.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p_kw.paragraph_format.line_spacing = 1.15
        p_kw.paragraph_format.space_before = Pt(6)
        p_kw.paragraph_format.first_line_indent = Cm(0)
        r_kw_pre = p_kw.add_run("Kata Kunci: ")
        r_kw_pre.font.name = "Times New Roman"
        r_kw_pre.font.size = Pt(12)
        r_kw_pre.font.bold = True
        r_kw_body = p_kw.add_run("Impulsive Buying, Hedonic Motivation, Desire for Completeness, Speculative Motive, Self-Control, Moderated Regression Analysis, Pokémon TCG, Keuangan Perilaku (Behavioral Finance).")
        r_kw_body.font.name = "Times New Roman"
        r_kw_body.font.size = Pt(12)
        r_kw_body.font.italic = True

        # 6. Abstract English
        add_frontmatter_heading(doc, "ABSTRACT", page_break=True)

        p_j5 = doc.add_paragraph()
        p_j5.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_j5.paragraph_format.space_before = Pt(0)
        p_j5.paragraph_format.space_after = Pt(12)
        p_j5.paragraph_format.line_spacing = 1.15
        rj5 = p_j5.add_run("THE EFFECT OF HEDONIC MOTIVATION, DESIRE FOR COMPLETENESS, AND SPECULATIVE MOTIVE ON IMPULSIVE BUYING OF POKÉMON TCG BOOSTER PACKS WITH SELF-CONTROL AS A MODERATING VARIABLE\n\nArthur Reezan (312023002)\nUndergraduate Program in Management, Faculty of Economics and Business, UKRIDA\nThesis Advisor: Dr. Fredella Colline, S.E., M.M., CFP®, PFM, CHCP-A")
        rj5.font.name = "Times New Roman"
        rj5.font.size = Pt(12)
        rj5.font.bold = True

        p_abs_en = doc.add_paragraph()
        p_abs_en.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p_abs_en.paragraph_format.line_spacing = 1.0
        p_abs_en.paragraph_format.space_before = Pt(6)
        p_abs_en.paragraph_format.space_after = Pt(6)
        p_abs_en.paragraph_format.first_line_indent = Cm(1.25)
        r_abs_en = p_abs_en.add_run(
            "This research aims to analyze and empirically test the effects of hedonic motivation, desire for completeness, and speculative motive "
            "on the impulsive buying behavior of official Indonesian-language physical Pokémon Trading Card Game (Pokémon TCG) booster packs, as well as to evaluate "
            "the moderating role of self-control in weakening the relationships between these three antecedent variables and impulsive buying. "
            "This study adopts an associative quantitative approach utilizing a cross-sectional survey design. Primary data are gathered via self-administered online "
            "questionnaires employing a 5-point Likert scale, distributed to respondents selected through purposive sampling. The sample inclusion criteria comprise "
            "Indonesian citizens aged 17 and above who have purchased official physical booster packs within the past 6 to 12 months. The targeted sample size ranges from "
            "120 to 150 respondents, consistent with the statistical power criteria established by Green (1991) and Cohen (1988) for multiple regression frameworks. "
            "The empirical model is estimated using multiple linear regression and Moderated Regression Analysis (MRA) with mean-centering procedures to reduce non-essential "
            "multicollinearity between predictor variables and their interaction products (Aiken dan West, 1991; Ghozali, 2018), executed via IBM SPSS Statistics software. This study provides theoretical novelty by synthesizing the "
            "Stimulus-Organism-Response (S-O-R) paradigm, collector psychology (the Zeigarnik Effect and The Completing the Set Effect), Self-Regulation Theory, and behavioral finance "
            "principles in the context of tangible alternative assets exhibiting volatile secondary market premiums. The findings are expected to offer practical insights for young "
            "consumers in exercising financial discipline regarding discretionary collectibles and provide strategic inputs for community organizers and financial educators targeting Generation Z."
        )
        r_abs_en.font.name = "Times New Roman"
        r_abs_en.font.size = Pt(12)
        r_abs_en.font.italic = True

        p_kw_en = doc.add_paragraph()
        p_kw_en.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p_kw_en.paragraph_format.line_spacing = 1.15
        p_kw_en.paragraph_format.space_before = Pt(6)
        p_kw_en.paragraph_format.first_line_indent = Cm(0)
        r_kw_en_pre = p_kw_en.add_run("Keywords: ")
        r_kw_en_pre.font.name = "Times New Roman"
        r_kw_en_pre.font.size = Pt(12)
        r_kw_en_pre.font.bold = True
        r_kw_en_body = p_kw_en.add_run("Impulsive Buying, Hedonic Motivation, Desire for Completeness, Speculative Motive, Self-Control, Moderated Regression Analysis, Pokémon TCG, Behavioral Finance.")
        r_kw_en_body.font.name = "Times New Roman"
        r_kw_en_body.font.size = Pt(12)
        r_kw_en_body.font.italic = True

    # 7. Daftar Isi
    add_daftar_isi_heading(doc, page_break=True)

    toc_items_nobab3 = [
        ("DAFTAR TABEL", "ix"),
        ("DAFTAR GAMBAR", "x"),
        ("BAB 1 PENDAHULUAN", "1"),
        ("  1.1 Latar Belakang Penelitian", "1"),
        ("  1.2 Perumusan Masalah", "16"),
        ("  1.3 Tujuan Penelitian", "17"),
        ("  1.4 Manfaat Penelitian", "17"),
        ("      1.4.1 Manfaat Teoritis", "17"),
        ("      1.4.2 Manfaat Praktis", "18"),
        ("BAB 2 KAJIAN PUSTAKA DAN PENGEMBANGAN HIPOTESIS", "19"),
        ("  2.1 Landasan Teori", "19"),
        ("      2.1.1 Grand Theory: Keuangan Perilaku (Behavioral Finance)", "19"),
        ("      2.1.2 Supporting Theory: Teori Stimulus-Organism-Response (S-O-R)", "19"),
        ("      2.1.3 Supporting Theory: Psikologi Kolektor dan Collection-Goal Tipping Point Effect", "20"),
        ("      2.1.4 Supporting Theory: Teori Regulasi Diri (Self-Regulation Theory)", "20"),
        ("  2.2 Kajian Variabel Penelitian", "20"),
        ("      2.2.1 Variabel Dependen (Y): Impulsive Buying (Pembelian Impulsif)", "20"),
        ("      2.2.2 Variabel Independen (X1): Hedonic Motivation (Motivasi Hedonis)", "21"),
        ("      2.2.3 Variabel Independen (X2): Desire for Completeness (Hasrat Kelengkapan Koleksi)", "21"),
        ("      2.2.4 Variabel Independen (X3): Speculative Motive (Motif Spekulasi Finansial)", "21"),
        ("      2.2.5 Variabel Moderasi (M): Self-Control (Kontrol Diri)", "22"),
        ("  2.3 Penelitian Sebelumnya", "22"),
        ("  2.4 Pengembangan Hipotesis", "25"),
        ("      2.4.1 Pengaruh Hedonic Motivation terhadap Impulsive Buying", "25"),
        ("      2.4.2 Pengaruh Desire for Completeness terhadap Impulsive Buying", "25"),
        ("      2.4.3 Pengaruh Speculative Motive terhadap Impulsive Buying", "26"),
        ("      2.4.4 Pengaruh Moderasi Self-Control terhadap Hubungan Hedonic Motivation dan Impulsive Buying", "26"),
        ("      2.4.5 Pengaruh Moderasi Self-Control terhadap Hubungan Desire for Completeness dan Impulsive Buying", "27"),
        ("      2.4.6 Pengaruh Moderasi Self-Control terhadap Hubungan Speculative Motive dan Impulsive Buying", "28"),
        ("  2.5 Rerangka Penelitian", "28"),
        ("DAFTAR PUSTAKA", "30")
    ]

    toc_items_full = [
        ("DAFTAR TABEL", "xii"),
        ("DAFTAR GAMBAR", "xiii"),
        ("BAB 1 PENDAHULUAN", "1"),
        ("  1.1 Latar Belakang Penelitian", "1"),
        ("  1.2 Perumusan Masalah", "16"),
        ("  1.3 Tujuan Penelitian", "17"),
        ("  1.4 Manfaat Penelitian", "17"),
        ("      1.4.1 Manfaat Teoritis", "17"),
        ("      1.4.2 Manfaat Praktis", "18"),
        ("BAB 2 KAJIAN PUSTAKA DAN PENGEMBANGAN HIPOTESIS", "19"),
        ("  2.1 Landasan Teori", "19"),
        ("      2.1.1 Grand Theory: Keuangan Perilaku (Behavioral Finance)", "19"),
        ("      2.1.2 Supporting Theory: Teori Stimulus-Organism-Response (S-O-R)", "19"),
        ("      2.1.3 Supporting Theory: Psikologi Kolektor dan Collection-Goal Tipping Point Effect", "20"),
        ("      2.1.4 Supporting Theory: Teori Regulasi Diri (Self-Regulation Theory)", "20"),
        ("  2.2 Kajian Variabel Penelitian", "20"),
        ("      2.2.1 Variabel Dependen (Y): Impulsive Buying (Pembelian Impulsif)", "20"),
        ("      2.2.2 Variabel Independen (X1): Hedonic Motivation (Motivasi Hedonis)", "21"),
        ("      2.2.3 Variabel Independen (X2): Desire for Completeness (Hasrat Kelengkapan Koleksi)", "21"),
        ("      2.2.4 Variabel Independen (X3): Speculative Motive (Motif Spekulasi Finansial)", "21"),
        ("      2.2.5 Variabel Moderasi (M): Self-Control (Kontrol Diri)", "22"),
        ("  2.3 Penelitian Sebelumnya", "22"),
        ("  2.4 Pengembangan Hipotesis", "25"),
        ("      2.4.1 Pengaruh Hedonic Motivation terhadap Impulsive Buying", "25"),
        ("      2.4.2 Pengaruh Desire for Completeness terhadap Impulsive Buying", "25"),
        ("      2.4.3 Pengaruh Speculative Motive terhadap Impulsive Buying", "26"),
        ("      2.4.4 Pengaruh Moderasi Self-Control terhadap Hubungan Hedonic Motivation dan Impulsive Buying", "26"),
        ("      2.4.5 Pengaruh Moderasi Self-Control terhadap Hubungan Desire for Completeness dan Impulsive Buying", "27"),
        ("      2.4.6 Pengaruh Moderasi Self-Control terhadap Hubungan Speculative Motive dan Impulsive Buying", "28"),
        ("  2.5 Rerangka Penelitian", "28"),
        ("BAB 3 METODE PENELITIAN", "30"),
        ("  3.1 Jenis dan Sumber Data", "30"),
        ("      3.1.1 Batasan Penelitian dan Ruang Lingkup Operasional", "30"),
        ("  3.2 Populasi dan Sampel", "31"),
        ("      3.2.1 Populasi dan Identifikasi Sumber Komunitas", "31"),
        ("      3.2.2 Sampel dan Justifikasi Kriteria Inklusi", "32"),
        ("      3.2.3 Penentuan Ukuran Sampel", "33"),
        ("      3.2.4 Justifikasi Komparatif Pemilihan Teknik Sampling", "33"),
        ("  3.3 Model Penelitian", "34"),
        ("  3.4 Operasionalisasi Variabel", "35"),
        ("  3.5 Metode Analisis Data", "40"),
        ("      3.5.1 Justifikasi Komparatif Pemilihan Metode Analisis", "40"),
        ("      3.5.2 Penyusunan Skor Komposit dan Uji Kualitas Data", "41"),
        ("      3.5.3 Uji Asumsi Klasik", "41"),
        ("      3.5.4 Estimasi Regresi Hirarkis dan MRA", "42"),
        ("      3.5.5 Uji Koefisien Determinasi (R2) dan Uji F Perubahan", "42"),
        ("      3.5.6 Uji Hipotesis dan Analisis Kemiringan Bersyarat (Simple Slopes)", "42"),
        ("  3.6 Diagram Alur Penelitian", "43"),
        ("  3.7 Jadwal Pelaksanaan Penelitian", "44"),
        ("DAFTAR PUSTAKA", "45")
    ]

    toc_items = toc_items_nobab3 if skip_chapter3 else toc_items_full
    target_right = Cm(14.0)  # exact right margin (21.0 - 4.0 - 3.0 = 14.0 cm = 7938 dxa)

    for title_toc, page_toc in toc_items:
        if title_toc.startswith("      "):
            style_name = 'TOC 3'
            left_indent = Cm(1.2)
            f_size = Pt(10.5)
            f_bold = False
        elif title_toc.startswith("  "):
            style_name = 'TOC 2'
            left_indent = Cm(0.6)
            f_size = Pt(11)
            f_bold = False
        else:
            style_name = 'TOC 1'
            left_indent = Cm(0)
            f_size = Pt(11)
            f_bold = True

        p_toc = doc.add_paragraph(style=style_name)
        p_toc.paragraph_format.line_spacing = 1.15
        p_toc.paragraph_format.space_before = Pt(0)
        p_toc.paragraph_format.space_after = Pt(2)
        p_toc.paragraph_format.left_indent = left_indent
        p_toc.paragraph_format.first_line_indent = Cm(0)
        p_toc.paragraph_format.right_indent = Cm(0)
        _clear_latent_tab_stops(p_toc)
        _add_dot_tab_7938(p_toc)

        clean_title = title_toc.strip()
        r_t = p_toc.add_run(clean_title)
        make_run_pure_black(r_t, "Times New Roman", f_size, bold=f_bold)

        r_p = p_toc.add_run(f"\t{page_toc}")
        make_run_pure_black(r_p, "Times New Roman", f_size, bold=f_bold)

    # 8. Daftar Tabel
    add_frontmatter_heading(doc, "DAFTAR TABEL", page_break=True)

    lot_items_nobab3 = [
        ("Tabel 1.1", "Matriks Kesenjangan Penelitian Empiris (Research Gap) pada 7 Subjek Hubungan Model Penelitian", "13"),
        ("Tabel 1.1", "Matriks Kesenjangan Penelitian Empiris (Research Gap) pada 7 Subjek Hubungan Model Penelitian (lanjutan)", "14"),
        ("Tabel 1.1", "Matriks Kesenjangan Penelitian Empiris (Research Gap) pada 7 Subjek Hubungan Model Penelitian (lanjutan)", "15"),
        ("Tabel 2.1", "Ringkasan Penelitian Sebelumnya", "22")
    ]
    lot_items_full = [
        ("Tabel 1.1", "Matriks Kesenjangan Penelitian Empiris (Research Gap) pada 7 Subjek Hubungan Model Penelitian", "13"),
        ("Tabel 1.1", "Matriks Kesenjangan Penelitian Empiris (Research Gap) pada 7 Subjek Hubungan Model Penelitian (lanjutan)", "14"),
        ("Tabel 1.1", "Matriks Kesenjangan Penelitian Empiris (Research Gap) pada 7 Subjek Hubungan Model Penelitian (lanjutan)", "15"),
        ("Tabel 2.1", "Ringkasan Penelitian Sebelumnya", "22"),
        ("Tabel 3.1", "Skala Pengukuran Likert 5 Poin", "30"),
        ("Tabel 3.2", "Operasionalisasi Variabel Penelitian", "36"),
        ("Tabel 3.3", "Jadwal Pelaksanaan Kegiatan Penelitian (Tahun 2026)", "44")
    ]
    lot_items = lot_items_nobab3 if skip_chapter3 else lot_items_full
    for tab_num, tab_title, tab_page in lot_items:
        p_lot = doc.add_paragraph(style='TOC 1')
        p_lot.paragraph_format.line_spacing = 1.15
        p_lot.paragraph_format.space_before = Pt(0)
        p_lot.paragraph_format.space_after = Pt(4)
        p_lot.paragraph_format.left_indent = Cm(0)
        p_lot.paragraph_format.first_line_indent = Cm(0)
        p_lot.paragraph_format.right_indent = Cm(0)
        _clear_latent_tab_stops(p_lot)
        _add_dot_tab_7938(p_lot)

        r_num = p_lot.add_run(f"{tab_num}.  ")
        make_run_pure_black(r_num, "Times New Roman", Pt(11), bold=True)

        r_title = p_lot.add_run(tab_title)
        make_run_pure_black(r_title, "Times New Roman", Pt(11), bold=False)

        r_page = p_lot.add_run(f"\t{tab_page}")
        make_run_pure_black(r_page, "Times New Roman", Pt(11), bold=False)

    # 9. Daftar Gambar
    add_frontmatter_heading(doc, "DAFTAR GAMBAR", page_break=True)

    lof_items_nobab3 = [
        ("Gambar 1.1", "Peringkat 10 Waralaba Media Berpendapatan Tertinggi di Dunia Sepanjang Masa", "2"),
        ("Gambar 1.2", "Pertumbuhan Kumulatif Produksi Kartu Pokémon TCG Global Tahun 2019–2024", "3"),
        ("Gambar 1.3", "Disparitas Harga Pasar Sekunder Kartu Pokémon Mentah (Ungraded) vs. Bersertifikasi PSA 10 Gem Mint Seri Shining Fates", "5"),
        ("Gambar 2.1", "Model Rerangka Konseptual Penelitian", "29")
    ]
    lof_items_full = [
        ("Gambar 1.1", "Peringkat 10 Waralaba Media Berpendapatan Tertinggi di Dunia Sepanjang Masa", "2"),
        ("Gambar 1.2", "Pertumbuhan Kumulatif Produksi Kartu Pokémon TCG Global Tahun 2019–2024", "3"),
        ("Gambar 1.3", "Disparitas Harga Pasar Sekunder Kartu Pokémon Mentah (Ungraded) vs. Bersertifikasi PSA 10 Gem Mint Seri Shining Fates", "5"),
        ("Gambar 2.1", "Model Rerangka Konseptual Penelitian", "29"),
        ("Gambar 3.1", "Diagram Alur Pelaksanaan Penelitian", "43")
    ]
    lof_items = lof_items_nobab3 if skip_chapter3 else lof_items_full
    for fig_num, fig_title, fig_page in lof_items:
        p_lof = doc.add_paragraph(style='TOC 1')
        p_lof.paragraph_format.line_spacing = 1.15
        p_lof.paragraph_format.space_before = Pt(0)
        p_lof.paragraph_format.space_after = Pt(4)
        p_lof.paragraph_format.left_indent = Cm(0)
        p_lof.paragraph_format.first_line_indent = Cm(0)
        p_lof.paragraph_format.right_indent = Cm(0)
        _clear_latent_tab_stops(p_lof)
        _add_dot_tab_7938(p_lof)

        r_num = p_lof.add_run(f"{fig_num}.  ")
        make_run_pure_black(r_num, "Times New Roman", Pt(11), bold=True)

        r_title = p_lof.add_run(fig_title)
        make_run_pure_black(r_title, "Times New Roman", Pt(11), bold=False)

        r_page = p_lof.add_run(f"\t{fig_page}")
        make_run_pure_black(r_page, "Times New Roman", Pt(11), bold=False)

    # ------------------------------------------------------------------------
    # SECTION 3: BAGIAN INTI / MAIN TEXT (BAB 1 s.d. BAB 3 & DAFTAR PUSTAKA)
    # Arabic Numerals (1, 2, 3...)
    # ------------------------------------------------------------------------
    sec_main = doc.add_section(WD_SECTION.NEW_PAGE)
    sec_main.page_width = Cm(21.0)
    sec_main.page_height = Cm(29.7)
    sec_main.top_margin = Cm(3.0)
    sec_main.bottom_margin = Cm(3.0)
    sec_main.left_margin = Cm(4.0)
    sec_main.right_margin = Cm(3.0)
    sec_main.header.is_linked_to_previous = False
    sec_main.footer.is_linked_to_previous = False
    add_page_number_to_footer(sec_main, is_roman=False, start_num=1)

    print("[*] Ingesting body text from validated Markdown reference...")
    md_file = base_dir / "PROPOSAL_SKRIPSI_POKEMON_TCG.md"
    with open(md_file, "r", encoding="utf-8") as f:
        md_text = f.read()

    # Split markdown into BAB 1, BAB 2, BAB 3, and DAFTAR PUSTAKA
    parts = re.split(r'\n#+\s+(BAB\s+\d+.*?|DAFTAR PUSTAKA.*?)\n', md_text)
    
    has_inserted_fig11 = False
    has_inserted_fig12 = False
    has_inserted_fig13 = False
    has_inserted_fig21 = False
    has_inserted_fig31 = False

    # Process each section
    ref_bookmarks = {}
    for idx in range(1, len(parts), 2):
        sec_header = parts[idx].strip()
        sec_content = parts[idx+1] if idx+1 < len(parts) else ""

        # Skip Bab 3 entirely when requested
        if skip_chapter3 and sec_header.startswith("BAB") and "3" in sec_header.split()[1:2]:
            print(f"    -> SKIPPING (no-chapter3 mode): {sec_header}")
            continue

        print(f"    -> Building: {sec_header}")
        if sec_header.startswith("BAB"):
            add_heading_1(doc, sec_header, page_break=False if idx == 1 else True)
        elif "DAFTAR PUSTAKA" in sec_header:
            add_heading_1(doc, "DAFTAR PUSTAKA", page_break=True)
            dp_paras = build_daftar_pustaka(doc, sec_content) or []
            bbl_keys = _parse_bbl_keys(base_dir / "Proposal_Arthur_PokemonTCG.bbl")
            if bbl_keys and len(dp_paras) == len(bbl_keys):
                for _p, _k in zip(dp_paras, bbl_keys):
                    _CITE_BM_SEQ[0] += 1
                    _add_bookmark(_p, 'Ref_' + re.sub(r'\W', '_', _k), _CITE_BM_SEQ[0])
                print('[*] DP bookmark: %d entri.' % len(dp_paras))
            else:
                print('[WARN] DP %d vs bbl %d — bookmark dilewati (anti salah-taut).'
                      % (len(dp_paras), len(bbl_keys)))
            ref_bookmarks = {k: 'Ref_' + re.sub(r'\W', '_', k) for k in bbl_keys} \
                if bbl_keys and len(dp_paras) == len(bbl_keys) else {}
            continue

        # Parse subsections, paragraphs, lists, tables, and images
        lines = sec_content.split('\n')
        line_idx = 0
        while line_idx < len(lines):
            line = lines[line_idx].rstrip()
            line_str = line.strip()

            if not line_str:
                line_idx += 1
                continue

            # Skip markdown dividers (---)
            if line_str == '---' or line_str == '***':
                line_idx += 1
                continue

            # Skip code blocks (``` ... ```)
            if line_str.startswith('```'):
                line_idx += 1
                while line_idx < len(lines) and not lines[line_idx].strip().startswith('```'):
                    line_idx += 1
                if line_idx < len(lines):
                    line_idx += 1 # skip closing ```
                continue

            # Heading 2 (## 1.1 ...)
            if line_str.startswith('## '):
                title_h2 = line_str[3:].strip()
                add_heading_2(doc, title_h2)
                line_idx += 1
                continue

            # Heading 3 (### 1.2.1 ...)
            if line_str.startswith('### '):
                title_h3 = line_str[4:].strip()
                add_heading_3(doc, title_h3)
                line_idx += 1
                continue

            # LaTeX Figure block handling (Gambar 1.1, 1.2, 1.3, 2.1, 3.1)
            if r'\begin{figure}' in line_str:
                fig_lines = [lines[line_idx]]
                while line_idx + 1 < len(lines) and r'\end{figure}' not in lines[line_idx]:
                    line_idx += 1
                    fig_lines.append(lines[line_idx])
                if line_idx < len(lines) and r'\end{figure}' in lines[line_idx]:
                    line_idx += 1
                fig_text = '\n'.join(fig_lines)

                # 1. Gambar 1.1 (Media Franchise Ranking)
                if ("gambar1_1" in fig_text or "media_franchise" in fig_text) and not has_inserted_fig11:
                    has_inserted_fig11 = True
                    if img_fig11.exists():
                        p_img = doc.add_paragraph()
                        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        p_img.paragraph_format.space_before = Pt(12)
                        p_img.paragraph_format.space_after = Pt(4)
                        p_img.paragraph_format.first_line_indent = Cm(0)
                        p_img.add_run().add_picture(str(img_fig11), width=Cm(13.5))

                        p_cap = doc.add_paragraph()
                        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        p_cap.paragraph_format.space_before = Pt(2)
                        p_cap.paragraph_format.space_after = Pt(2)
                        p_cap.paragraph_format.first_line_indent = Cm(0)
                        p_cap.add_run("Gambar 1.1. Peringkat 10 Waralaba Media Berpendapatan Tertinggi di Dunia Sepanjang Masa").font.bold = True

                        p_src = doc.add_paragraph()
                        p_src.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        p_src.paragraph_format.space_before = Pt(0)
                        p_src.paragraph_format.space_after = Pt(12)
                        p_src.paragraph_format.first_line_indent = Cm(0)
                        r_s = p_src.add_run("Sumber: Statista Research dan Laporan Keuangan Tahunan Korporat (2024).")
                        r_s.font.size = Pt(10)
                        r_s.font.italic = True

                # 2. Gambar 1.2 (Pokemon Card Production Growth)
                elif ("gambar1_2" in fig_text or "pokemon_card_growth" in fig_text or "production_growth" in fig_text) and not has_inserted_fig12:
                    has_inserted_fig12 = True
                    if img_fig12.exists():
                        p_img = doc.add_paragraph()
                        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        p_img.paragraph_format.space_before = Pt(12)
                        p_img.paragraph_format.space_after = Pt(4)
                        p_img.paragraph_format.first_line_indent = Cm(0)
                        p_img.add_run().add_picture(str(img_fig12), width=Cm(13.5))

                        p_cap = doc.add_paragraph()
                        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        p_cap.paragraph_format.space_before = Pt(2)
                        p_cap.paragraph_format.space_after = Pt(2)
                        p_cap.paragraph_format.first_line_indent = Cm(0)
                        p_cap.add_run("Gambar 1.2. Pertumbuhan Kumulatif Produksi Kartu Pokémon TCG Global Tahun 2019–2024").font.bold = True

                        p_src = doc.add_paragraph()
                        p_src.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        p_src.paragraph_format.space_before = Pt(0)
                        p_src.paragraph_format.space_after = Pt(12)
                        p_src.paragraph_format.first_line_indent = Cm(0)
                        r_s = p_src.add_run("Sumber: The Pokémon Company Corporate Business Data (2024).")
                        r_s.font.size = Pt(10)
                        r_s.font.italic = True

                # 3. Gambar 1.3 (PriceCharting PSA Grading Price Disparity)
                elif ("gambar1_3" in fig_text or "psa_grading_disparity" in fig_text or "pricecharting_disparity" in fig_text or "pricecharting" in fig_text or "psa_grading" in fig_text) and not has_inserted_fig13:
                    has_inserted_fig13 = True
                    if img_fig13.exists():
                        p_img = doc.add_paragraph()
                        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        p_img.paragraph_format.space_before = Pt(12)
                        p_img.paragraph_format.space_after = Pt(4)
                        p_img.paragraph_format.first_line_indent = Cm(0)
                        p_img.add_run().add_picture(str(img_fig13), width=Cm(13.5))

                        p_cap = doc.add_paragraph()
                        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        p_cap.paragraph_format.space_before = Pt(2)
                        p_cap.paragraph_format.space_after = Pt(2)
                        p_cap.paragraph_format.first_line_indent = Cm(0)
                        p_cap.add_run("Gambar 1.3. Disparitas Harga Pasar Sekunder Kartu Pokémon Mentah (Ungraded) vs. Bersertifikasi PSA 10 Gem Mint Seri Shining Fates").font.bold = True

                        p_src = doc.add_paragraph()
                        p_src.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        p_src.paragraph_format.space_before = Pt(0)
                        p_src.paragraph_format.space_after = Pt(12)
                        p_src.paragraph_format.first_line_indent = Cm(0)
                        r_s = p_src.add_run("Sumber: PriceCharting Market Database – Pokémon Shining Fates Price Guide (2024).")
                        r_s.font.size = Pt(10)
                        r_s.font.italic = True

                # 4. Gambar 2.1 (Kerangka Pemikiran)
                elif ("rerangka" in fig_text or "Model Rerangka" in fig_text) and not has_inserted_fig21:
                    has_inserted_fig21 = True
                    if img_rerangka.exists():
                        p_img = doc.add_paragraph()
                        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        p_img.paragraph_format.space_before = Pt(12)
                        p_img.paragraph_format.space_after = Pt(4)
                        p_img.paragraph_format.first_line_indent = Cm(0)
                        p_img.add_run().add_picture(str(img_rerangka), width=Cm(14.0))

                        p_cap = doc.add_paragraph()
                        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        p_cap.paragraph_format.space_before = Pt(2)
                        p_cap.paragraph_format.space_after = Pt(2)
                        p_cap.paragraph_format.first_line_indent = Cm(0)
                        p_cap.add_run("Gambar 2.1. Model Rerangka Konseptual Penelitian").font.bold = True

                        p_src = doc.add_paragraph()
                        p_src.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        p_src.paragraph_format.space_before = Pt(0)
                        p_src.paragraph_format.space_after = Pt(12)
                        p_src.paragraph_format.first_line_indent = Cm(0)
                        r_s = p_src.add_run("Keterangan: Garis lurus menunjukkan pengaruh langsung (H1, H2, H3); Garis putus-putus menunjukkan efek moderasi kontrol diri yang memperlemah (H4, H5, H6).")
                        r_s.font.size = Pt(10)
                        r_s.font.italic = True

                # 5. Gambar 3.1 (Diagram Alur Pelaksanaan Penelitian)
                elif ("alur_penelitian" in fig_text or "Diagram Alur" in fig_text or "tikzpicture" in fig_text) and not has_inserted_fig31:
                    has_inserted_fig31 = True
                    if img_alur.exists():
                        p_img = doc.add_paragraph()
                        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        p_img.paragraph_format.space_before = Pt(12)
                        p_img.paragraph_format.space_after = Pt(4)
                        p_img.paragraph_format.first_line_indent = Cm(0)
                        p_img.add_run().add_picture(str(img_alur), width=Cm(13.0))

                        p_cap = doc.add_paragraph()
                        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        p_cap.paragraph_format.space_before = Pt(2)
                        p_cap.paragraph_format.space_after = Pt(2)
                        p_cap.paragraph_format.first_line_indent = Cm(0)
                        p_cap.add_run("Gambar 3.1. Diagram Alur Pelaksanaan Penelitian").font.bold = True

                        p_src = doc.add_paragraph()
                        p_src.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        p_src.paragraph_format.space_before = Pt(0)
                        p_src.paragraph_format.space_after = Pt(12)
                        p_src.paragraph_format.first_line_indent = Cm(0)
                        r_s = p_src.add_run("Sumber: Dikembangkan oleh penulis untuk tahapan operasional penelitian, 2026.")
                        r_s.font.size = Pt(10)
                        r_s.font.italic = True
                continue

            # LaTeX Table block handling for Tabel 1.1 (Matriks Research Gap / longtable)
            if r'\begin{longtable}' in line_str or (line_str.startswith(r'\begingroup') and line_idx + 4 < len(lines) and any(r'\begin{longtable}' in lines[j] for j in range(line_idx, min(line_idx+5, len(lines))))):
                # Consume lines until \endgroup or end of longtable block
                while line_idx < len(lines):
                    curr = lines[line_idx].strip()
                    line_idx += 1
                    if r'\endgroup' in curr:
                        break
                    if r'\end{longtable}' in curr:
                        # Check if flushleft source follows
                        if line_idx < len(lines) and (r'\begin{flushleft}' in lines[line_idx] or r'\footnotesize' in lines[line_idx]):
                            while line_idx < len(lines) and r'\endgroup' not in lines[line_idx]:
                                line_idx += 1
                            if line_idx < len(lines):
                                line_idx += 1
                        break
                build_tabel_research_gap(doc)
                continue

            # LaTeX Table block handling for Tabel 3.3 (Jadwal Kegiatan)
            if r'\begin{table}' in line_str:
                while line_idx < len(lines) and r'\end{table}' not in lines[line_idx]:
                    line_idx += 1
                if line_idx < len(lines):
                    line_idx += 1

                # Insert Tabel 3.3
                build_tabel_jadwal(doc)
                continue

            # Image detection for Gambar 1.1 (Media Franchise Ranking)
            if ("gambar1_1_media_franchise_ranking" in line_str or "Gambar 1.1" in line_str) and not has_inserted_fig11:
                has_inserted_fig11 = True
                if img_fig11.exists():
                    p_img = doc.add_paragraph()
                    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    p_img.paragraph_format.space_before = Pt(12)
                    p_img.paragraph_format.space_after = Pt(4)
                    p_img.paragraph_format.first_line_indent = Cm(0)
                    p_img.add_run().add_picture(str(img_fig11), width=Cm(13.5))

                    p_cap = doc.add_paragraph()
                    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    p_cap.paragraph_format.space_before = Pt(2)
                    p_cap.paragraph_format.space_after = Pt(2)
                    p_cap.paragraph_format.first_line_indent = Cm(0)
                    p_cap.add_run("Gambar 1.1. Peringkat 10 Waralaba Media Berpendapatan Tertinggi di Dunia Sepanjang Masa").font.bold = True

                    p_src = doc.add_paragraph()
                    p_src.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    p_src.paragraph_format.space_before = Pt(0)
                    p_src.paragraph_format.space_after = Pt(12)
                    p_src.paragraph_format.first_line_indent = Cm(0)
                    r_s = p_src.add_run("Sumber: Statista Research dan Laporan Keuangan Tahunan Korporat (2024).")
                    r_s.font.size = Pt(10)
                    r_s.font.italic = True
                line_idx += 1
                while line_idx < len(lines):
                    nxt = lines[line_idx].strip()
                    if nxt.startswith('*Sumber') or nxt.startswith('Sumber') or nxt.startswith('**Gambar 1.1') or not nxt or nxt.startswith('</div>') or nxt.startswith('<div'):
                        line_idx += 1
                    else:
                        break
                continue

            # Image detection for Gambar 1.2 (Pokemon Card Production Growth)
            if ("gambar1_2_pokemon_tcg_production_growth" in line_str or "Gambar 1.2" in line_str) and not has_inserted_fig12:
                has_inserted_fig12 = True
                if img_fig12.exists():
                    p_img = doc.add_paragraph()
                    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    p_img.paragraph_format.space_before = Pt(12)
                    p_img.paragraph_format.space_after = Pt(4)
                    p_img.paragraph_format.first_line_indent = Cm(0)
                    p_img.add_run().add_picture(str(img_fig12), width=Cm(13.5))

                    p_cap = doc.add_paragraph()
                    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    p_cap.paragraph_format.space_before = Pt(2)
                    p_cap.paragraph_format.space_after = Pt(2)
                    p_cap.paragraph_format.first_line_indent = Cm(0)
                    p_cap.add_run("Gambar 1.2. Pertumbuhan Kumulatif Produksi Kartu Pokémon TCG Global Tahun 2019–2024").font.bold = True

                    p_src = doc.add_paragraph()
                    p_src.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    p_src.paragraph_format.space_before = Pt(0)
                    p_src.paragraph_format.space_after = Pt(12)
                    p_src.paragraph_format.first_line_indent = Cm(0)
                    r_s = p_src.add_run("Sumber: The Pokémon Company Corporate Business Data, 2024.")
                    r_s.font.size = Pt(10)
                    r_s.font.italic = True
                line_idx += 1
                while line_idx < len(lines):
                    nxt = lines[line_idx].strip()
                    if nxt.startswith('*Sumber') or nxt.startswith('Sumber') or nxt.startswith('**Gambar 1.2') or not nxt or nxt.startswith('</div>') or nxt.startswith('<div'):
                        line_idx += 1
                    else:
                        break
                continue

            # Image detection for Gambar 1.3 (PSA Grading Price Disparity)
            if ("gambar1_3_psa_grading_price_disparity" in line_str or "Gambar 1.3" in line_str) and not has_inserted_fig13:
                has_inserted_fig13 = True
                if img_fig13.exists():
                    p_img = doc.add_paragraph()
                    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    p_img.paragraph_format.space_before = Pt(12)
                    p_img.paragraph_format.space_after = Pt(4)
                    p_img.paragraph_format.first_line_indent = Cm(0)
                    p_img.add_run().add_picture(str(img_fig13), width=Cm(13.5))

                    p_cap = doc.add_paragraph()
                    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    p_cap.paragraph_format.space_before = Pt(2)
                    p_cap.paragraph_format.space_after = Pt(2)
                    p_cap.paragraph_format.first_line_indent = Cm(0)
                    p_cap.add_run("Gambar 1.3. Disparitas Harga Rata-rata Pasar Sekunder Kartu Pokémon Mentah (Raw) vs. Bersertifikasi PSA 10 Gem Mint").font.bold = True

                    p_src = doc.add_paragraph()
                    p_src.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    p_src.paragraph_format.space_before = Pt(0)
                    p_src.paragraph_format.space_after = Pt(12)
                    p_src.paragraph_format.first_line_indent = Cm(0)
                    r_s = p_src.add_run("Sumber: PSA (Professional Sports Authenticator) Population Report dan Auction Prices Realized (2024).")
                    r_s.font.size = Pt(10)
                    r_s.font.italic = True
                line_idx += 1
                while line_idx < len(lines):
                    nxt = lines[line_idx].strip()
                    if nxt.startswith('*Sumber') or nxt.startswith('Sumber') or nxt.startswith('**Gambar 1.3') or not nxt or nxt.startswith('</div>') or nxt.startswith('<div'):
                        line_idx += 1
                    else:
                        break
                continue

            # Image detection for Gambar 2.1 (Kerangka Pemikiran)
            if ("Model Rerangka Konseptual" in line_str or line_str.startswith("**Gambar 2.1") or line_str.startswith("Gambar 2.1")) and not has_inserted_fig21:
                has_inserted_fig21 = True
                if img_rerangka.exists():
                    p_img = doc.add_paragraph()
                    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    p_img.paragraph_format.space_before = Pt(12)
                    p_img.paragraph_format.space_after = Pt(4)
                    p_img.paragraph_format.first_line_indent = Cm(0)
                    p_img.add_run().add_picture(str(img_rerangka), width=Cm(14.0))

                    p_cap = doc.add_paragraph()
                    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    p_cap.paragraph_format.space_before = Pt(2)
                    p_cap.paragraph_format.space_after = Pt(2)
                    p_cap.paragraph_format.first_line_indent = Cm(0)
                    p_cap.add_run("Gambar 2.1. Model Rerangka Konseptual Penelitian").font.bold = True

                    p_src = doc.add_paragraph()
                    p_src.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    p_src.paragraph_format.space_before = Pt(0)
                    p_src.paragraph_format.space_after = Pt(12)
                    p_src.paragraph_format.first_line_indent = Cm(0)
                    r_s = p_src.add_run("Keterangan: Garis lurus menunjukkan pengaruh langsung (H1, H2, H3); Garis putus-putus menunjukkan efek moderasi kontrol diri yang memperlemah (H4, H5, H6).")
                    r_s.font.size = Pt(10)
                    r_s.font.italic = True

                # Skip any redundant caption or notes following in markdown
                line_idx += 1
                while line_idx < len(lines):
                    nxt = lines[line_idx].strip()
                    if nxt.startswith('*Keterangan') or nxt.startswith('Keterangan') or nxt.startswith('---') or not nxt:
                        line_idx += 1
                    else:
                        break
                continue

            # Table Detection in Markdown (| col1 | col2 |)
            if line_str.startswith('|') and '|' in line_str[1:]:
                # Gather full table lines
                table_lines = []
                while line_idx < len(lines) and lines[line_idx].strip().startswith('|'):
                    table_lines.append(lines[line_idx].strip())
                    line_idx += 1
                build_apa7_table(doc, table_lines)
                continue

            # Equations ($$...$$ or multi-line $$)
            if line_str.startswith('$$'):
                if line_str.endswith('$$') and len(line_str) > 2:
                    eq_formula = line_str[2:-2].strip()
                    line_idx += 1
                else:
                    eq_lines = [line_str[2:].strip()]
                    line_idx += 1
                    while line_idx < len(lines):
                        nxt = lines[line_idx].strip()
                        if nxt.endswith('$$'):
                            eq_lines.append(nxt[:-2].strip())
                            line_idx += 1
                            break
                        else:
                            eq_lines.append(nxt)
                            line_idx += 1
                    eq_formula = " ".join(eq_lines).strip()
                add_equation_paragraph(doc, eq_formula)
                continue
            elif line_str.startswith('$') and line_str.endswith('$') and len(line_str) > 10:
                eq_formula = line_str.strip('$').strip()
                add_equation_paragraph(doc, eq_formula)
                line_idx += 1
                continue

            # Numbered lists (1. 2. 3.)
            m_num = re.match(r'^(\d+[\.\)]|[a-zA-Z][\.\)])\s+(.*)', line_str)
            if m_num:
                prefix = m_num.group(1)
                body = m_num.group(2)
                p_li = doc.add_paragraph()
                p_li.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                p_li.paragraph_format.left_indent = Cm(1.25)
                p_li.paragraph_format.first_line_indent = Cm(-0.63)
                p_li.paragraph_format.space_before = Pt(0)
                p_li.paragraph_format.space_after = Pt(2)
                p_li.paragraph_format.line_spacing = 1.5
                r_num = p_li.add_run(f"{prefix}  ")
                r_num.font.bold = True
                clean_body = clean_academic_text(body)
                parse_markdown_runs(p_li, clean_body)
                line_idx += 1
                continue

            # Bullet points (- or *)
            if line_str.startswith('- ') or line_str.startswith('* '):
                body = line_str[2:].strip()
                p_li = doc.add_paragraph()
                p_li.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                p_li.paragraph_format.left_indent = Cm(1.25)
                p_li.paragraph_format.first_line_indent = Cm(-0.4)
                p_li.paragraph_format.space_before = Pt(0)
                p_li.paragraph_format.space_after = Pt(2)
                p_li.paragraph_format.line_spacing = 1.5
                r_b = p_li.add_run("•  ")
                r_b.font.bold = True
                clean_body = clean_academic_text(body)
                parse_markdown_runs(p_li, clean_body)
                line_idx += 1
                continue

            # Blockquote (> ...)
            if line_str.startswith('>'):
                body = line_str.lstrip('>').strip()
                p_bq = doc.add_paragraph()
                p_bq.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                p_bq.paragraph_format.left_indent = Cm(1.5)
                p_bq.paragraph_format.right_indent = Cm(0.5)
                p_bq.paragraph_format.space_before = Pt(2)
                p_bq.paragraph_format.space_after = Pt(2)
                p_bq.paragraph_format.line_spacing = 1.15
                clean_body = clean_academic_text(body)
                parse_markdown_runs(p_bq, clean_body)
                line_idx += 1
                continue

            # Raw LaTeX \caption{...} (mis. longtable Tabel 1.1) -> caption tubuh
            # via peta judul LOT (anti-bocor sintaks LaTeX mentah ke DOCX)
            m_cap = re.match(r'^\\caption\{(.*)\}\s*(\\label\{[^}]*\})?\s*(\\\\)?\s*$', line_str)
            if m_cap:
                cap_title = m_cap.group(1).strip()
                cap_num = None
                for _tn, _tt, _tp in lot_items:
                    if cap_title[:30].lower() in _tt.lower() or _tt[:30].lower() in cap_title.lower():
                        cap_num = _tn
                        break
                p_tcap = doc.add_paragraph()
                p_tcap.alignment = WD_ALIGN_PARAGRAPH.LEFT
                p_tcap.paragraph_format.space_before = Pt(12)
                p_tcap.paragraph_format.space_after = Pt(4)
                p_tcap.paragraph_format.keep_with_next = True
                if cap_num:
                    r_cn = p_tcap.add_run(f"{cap_num}: ")
                    make_run_pure_black(r_cn, "Times New Roman", Pt(12), bold=True)
                parse_markdown_runs(p_tcap, cap_title)
                line_idx += 1
                continue

            # Intercept Tabel 1.1 markdown table if already synchronized into markdown table
            if re.match(r'^\*{0,2}Tabel\s+1\.1\b', line_str):
                # Check if followed by markdown table (| ... |)
                temp_idx = line_idx + 1
                while temp_idx < len(lines) and not lines[temp_idx].strip():
                    temp_idx += 1
                if temp_idx < len(lines) and lines[temp_idx].strip().startswith('|'):
                    # Advance past the whole table and any source note
                    line_idx = temp_idx
                    while line_idx < len(lines) and (lines[line_idx].strip().startswith('|') or not lines[line_idx].strip() or lines[line_idx].strip().startswith('*Sumber') or lines[line_idx].strip().startswith('Sumber')):
                        line_idx += 1
                    build_tabel_research_gap(doc)
                    continue

            # Table Caption Detection in Markdown (**Tabel X.Y ...**)
            if re.match(r'^\*{0,2}Tabel\s+\d+\.\d+', line_str):
                p_tcap = add_body_paragraph(doc, line_str, indent=False)
                p_tcap.alignment = WD_ALIGN_PARAGRAPH.LEFT
                p_tcap.paragraph_format.space_before = Pt(12)
                p_tcap.paragraph_format.space_after = Pt(4)
                p_tcap.paragraph_format.keep_with_next = True
                line_idx += 1
                continue

            # Skip rogue LaTeX tokens / unparsed environment artifacts from leaking into body paragraphs
            if any(line_str.startswith(tk) for tk in [
                r'\begingroup', r'\endgroup', r'\small', r'\footnotesize',
                r'\toprule', r'\midrule', r'\bottomrule', r'\endhead', r'\endfoot', r'\endlastfoot',
                r'\begin{flushleft}', r'\end{flushleft}', r'\begin{longtable}', r'\end{longtable}',
                r'\multicolumn', r'\addlinespace'
            ]) or r'\begin{longtable}' in line_str or r'\end{longtable}' in line_str:
                line_idx += 1
                continue

            # Standard paragraph
            add_body_paragraph(doc, line_str)
            line_idx += 1

    # Close any active Word processes that might lock the target file
    try:
        import subprocess
        subprocess.run(["powershell", "-Command", "Stop-Process -Name WINWORD -Force -ErrorAction SilentlyContinue"], check=False)
    except Exception:
        pass

    print("[*] Performing Document-Wide Pure Black & Typography Enforcement Pass...")
    link_lot_lof_entries(doc)
    aux_map = _parse_aux_cites(base_dir / "Proposal_Arthur_PokemonTCG.aux")
    if ref_bookmarks and aux_map:
        link_citations_to_dp(doc, aux_map, ref_bookmarks)
    else:
        print('[WARN] sitasi hyperlink dilewati (bookmark/aux tak lengkap).')
    link_static_toc_entries(doc)
    for p in doc.paragraphs:
        for r in p.runs:
            if not r.text:
                continue
            r.font.color.rgb = RGBColor(0, 0, 0)
            rPr = r._r.get_or_add_rPr()
            for c in rPr.findall(qn('w:color')):
                rPr.remove(c)
            rPr.append(parse_xml(f'<w:color {nsdecls("w")} w:val="000000"/>'))
            if r.font.name != "Cambria Math":
                for rf in rPr.findall(qn('w:rFonts')):
                    rPr.remove(rf)
                rPr.append(parse_xml(f'<w:rFonts {nsdecls("w")} w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>'))
    for tbl in doc.tables:
        for row in tbl.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    for r in p.runs:
                        r.font.color.rgb = RGBColor(0, 0, 0)
                        rPr = r._r.get_or_add_rPr()
                        for c in rPr.findall(qn('w:color')):
                            rPr.remove(c)
                        rPr.append(parse_xml(f'<w:color {nsdecls("w")} w:val="000000"/>'))

    # Save document
    doc.save(str(output_docx))
    print(f"\n[SUCCESS] Document saved cleanly to: {output_docx}")

    # Inject and update native Word TableOfContents component
    inject_native_word_toc(output_docx)

    return output_docx


def inject_native_word_toc(docx_path):
    """Inserts native Microsoft Word TableOfContents component via Word COM.
    Ensures full compatibility with Google Docs Table of Contents widget and dot leaders."""
    win_path = str(docx_path).replace('/', '\\')
    ps_script = f"""
$docxPath = "{win_path}"
$word = New-Object -ComObject Word.Application
$word.Visible = $false
try {{
    $doc = $word.Documents.Open($docxPath)
    
    # Configure TOC styles (toc 1, toc 2, toc 3) for Times New Roman 12pt, Pure Black
    $stylesToFormat = @(
        @("toc 1", 12, $true, 0),
        @("toc 2", 12, $false, 18),
        @("toc 3", 11, $false, 36)
    )
    foreach ($item in $stylesToFormat) {{
        $sName = $item[0]
        $fSize = $item[1]
        $fBold = $item[2]
        $indent = $item[3]
        try {{
            $st = $doc.Styles.Item($sName)
            $st.Font.Name = "Times New Roman"
            $st.Font.Size = $fSize
            $st.Font.Bold = $fBold
            $st.Font.ColorIndex = 1
            $st.ParagraphFormat.LineSpacingRule = 0
            $st.ParagraphFormat.SpaceBefore = 0
            $st.ParagraphFormat.SpaceAfter = 2
            $st.ParagraphFormat.LeftIndent = $indent
        }} catch {{}}
    }}
    
    # Locate DAFTAR ISI paragraph
    for ($i = 1; $i -le $doc.Paragraphs.Count; $i++) {{
        $pText = $doc.Paragraphs.Item($i).Range.Text.Trim()
        if ($pText -eq "DAFTAR ISI") {{
            $pStart = $i + 1
            $pEnd = $pStart
            for ($j = $pStart; $j -le $doc.Paragraphs.Count; $j++) {{
                $nextText = $doc.Paragraphs.Item($j).Range.Text.Trim()
                if ($nextText -eq "DAFTAR TABEL") {{
                    $pEnd = $j - 1
                    break
                }}
            }}
            # Delete static TOC paragraphs between DAFTAR ISI and DAFTAR TABEL
            if ($pEnd -ge $pStart) {{
                $rangeToDelete = $doc.Range($doc.Paragraphs.Item($pStart).Range.Start, $doc.Paragraphs.Item($pEnd).Range.End)
                $rangeToDelete.Delete()
            }}
            
            # Insert TWO paragraphs after DAFTAR ISI:
            # 1 for TOC field container, 1 buffer before DAFTAR TABEL to prevent merging
            $insertRange = $doc.Paragraphs.Item($i).Range
            $insertRange.Collapse(0)
            $insertRange.InsertParagraphAfter()
            $insertRange.InsertParagraphAfter()
            $tocRange = $doc.Paragraphs.Item($i + 1).Range
            
            $toc = $doc.TablesOfContents.Add($tocRange, $true, 1, 3, $false, "", $true, $true, "", $true, $true)
            $toc.Update()
            
            # Unlink TOC field: converts dynamic TOC into clean static text,
            # eliminating Word's grey field shading while preserving exact page numbers and dot leaders
            $toc.Range.Fields.Unlink()
            break
        }}
    }}
    
    # Enforce absolute page break before DAFTAR TABEL and DAFTAR GAMBAR and clean empty buffer paragraphs
    for ($k = 1; $k -le $doc.Paragraphs.Count; $k++) {{
        $txt = $doc.Paragraphs.Item($k).Range.Text.Trim()
        if ($txt -eq "DAFTAR TABEL" -or $txt -eq "DAFTAR GAMBAR") {{
            if ($k -gt 1) {{
                $prevText = $doc.Paragraphs.Item($k - 1).Range.Text.Trim()
                if ($prevText -eq "") {{
                    $doc.Paragraphs.Item($k - 1).Range.Delete()
                    $k--
                }}
            }}
            $doc.Paragraphs.Item($k).Format.PageBreakBefore = $true
        }}
    }}
    
    $doc.Save()
    $doc.Close()
}} catch {{
    Write-Error $_
}} finally {{
    $word.Quit()
}}
"""
    temp_ps = Path(tempfile.gettempdir()) / f"inject_toc_{os.getpid()}.ps1"
    temp_ps.write_text(ps_script, encoding="utf-8")
    try:
        subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", str(temp_ps)], check=True, capture_output=True, text=True)
        print(f"[SUCCESS] Native Word Table of Contents injected & updated cleanly for: {docx_path.name}")
    except Exception as e:
        print(f"[WARN] Could not run Word COM TOC injection: {e}")
    finally:
        if temp_ps.exists():
            try:
                temp_ps.unlink()
            except Exception:
                pass

    # Re-enforce direct <w:outlineLvl> tags and run font properties on headings
    try:
        doc_post = Document(str(docx_path))
        for p in doc_post.paragraphs:
            style_name = p.style.name if p.style else ""
            if "Heading 1" in style_name:
                set_paragraph_outline_level(p, 0)
            elif "Heading 2" in style_name:
                set_paragraph_outline_level(p, 1)
            elif "Heading 3" in style_name:
                set_paragraph_outline_level(p, 2)
            if any(h in style_name for h in ["Heading 1", "Heading 2", "Heading 3"]):
                for r in p.runs:
                    r.font.name = "Times New Roman"
                    r.font.size = Pt(12)
                    r.font.bold = True
                    r.font.color.rgb = RGBColor(0, 0, 0)
        # Sanitasi residu Word-COM pada entri TOC: bookmark yatim tak-tertutup
        # + webHidden (disembunyikan Google Docs) membuat entri lenyap saat
        # konversi Docs. noProof dipertahankan (anti garis merah ejaan).
        try:
            _plist = list(doc_post.paragraphs)
            _isi = next((i for i, _pp in enumerate(_plist) if _pp.text.strip() == 'DAFTAR ISI' and '\t' not in _pp.text), None)
            _dtb = None
            if _isi is not None:
                for _j in range(_isi + 1, len(_plist)):
                    _pp = _plist[_j]
                    try:
                        _sn = _pp.style.name
                    except Exception:
                        _sn = ''
                    if _pp.text.strip() == 'DAFTAR TABEL' and _sn.startswith('Heading'):
                        _dtb = _j
                        break
            _n_san = 0
            if _isi is not None and _dtb is not None:
                for _pp in _plist[_isi + 1:_dtb]:
                    if '\t' not in (_pp.text or ''):
                        continue
                    for _el in list(_pp._p.iter()):
                        if _el.tag in (qn('w:bookmarkStart'), qn('w:bookmarkEnd')):
                            _el.getparent().remove(_el)
                            _n_san += 1
                        elif _el.tag == qn('w:webHidden'):
                            _el.getparent().remove(_el)
                            _n_san += 1
            print(f"[*] TOC sanitasi: {_n_san} residu COM dibersihkan (bookmark yatim/webHidden).")
        except Exception as e:
            print(f"[WARN] Sanitasi TOC gagal: {e}")
        # Pasca-COM: tautkan ulang entri TOC statis hasil Word (Unlink menghapus
        # hyperlink bawaan). Gaya 'toc 1/2/3' cocok case-insensitive; bookmark
        # TOC_* heading dipakai ulang (idempoten); teks dijamin identik.
        try:
            n_toc_post = link_static_toc_entries(doc_post)
            print(f"[*] TOC pasca-COM: {n_toc_post} entri terhubung ulang (statis ber-hyperlink).")
        except Exception as e:
            print(f"[WARN] TOC pasca-COM gagal: {e}")
        # Pedoman FEB 2023 "huruf berwarna hitam pekat dan seragam": netralkan
        # rStyle Hyperlink (biru + garis bawah) bawaan Word pada hyperlink TOC.
        # Lingkup HANYA DAFTAR ISI (hyperlink URL biru di DP dipertahankan).
        # Preseden kakak tingkat: TOC statis hitam tanpa warna tema.
        try:
            _plist = list(doc_post.paragraphs)
            _isi = next((i for i, _pp in enumerate(_plist) if _pp.text.strip() == 'DAFTAR ISI' and '\t' not in _pp.text), None)
            _dtb = None
            if _isi is not None:
                for _j in range(_isi + 1, len(_plist)):
                    _pp = _plist[_j]
                    try:
                        _sn = _pp.style.name
                    except Exception:
                        _sn = ''
                    if _pp.text.strip() == 'DAFTAR TABEL' and _sn.startswith('Heading'):
                        _dtb = _j
                        break
            _n_blk = 0
            if _isi is not None and _dtb is not None:
                for _pp in _plist[_isi + 1:_dtb]:
                    if '\t' not in (_pp.text or ''):
                        continue
                    for _h in list(_pp._p.iter()):
                        if _h.tag != qn('w:hyperlink'):
                            continue
                        for _r in list(_h):
                            if _r.tag != qn('w:r'):
                                continue
                            _rPr = _r.find(qn('w:rPr'))
                            if _rPr is None:
                                _rPr = OxmlElement('w:rPr')
                                _r.insert(0, _rPr)
                            for _rs in list(_rPr.findall(qn('w:rStyle'))):
                                if (_rs.get(qn('w:val')) or '').lower() == 'hyperlink':
                                    _rPr.remove(_rs)
                            for _uu in list(_rPr.findall(qn('w:u'))):
                                _rPr.remove(_uu)
                            _cc = _rPr.find(qn('w:color'))
                            if _cc is None:
                                _cc = OxmlElement('w:color')
                                _rPr.append(_cc)
                            _cc.set(qn('w:val'), '000000')
                            _n_blk += 1
            print(f"[*] TOC hitam pekat: {_n_blk} run hyperlink dinetralkan (tanpa biru/underline).")
        except Exception as e:
            print(f"[WARN] Penetrasi hitam TOC gagal: {e}")
        doc_post.save(str(docx_path))
    except Exception as e:
        print(f"[WARN] Could not re-enforce outline levels: {e}")




def build_apa7_table(doc, table_lines):
    """Parses markdown table lines and converts into an APA 7th style docx table."""
    data_rows = []
    for line in table_lines:
        if re.match(r'^\|[\s\-:|]+\|$', line):
            continue
        cells = [c.strip() for c in line.split('|')[1:-1]]
        if cells:
            data_rows.append(cells)

    if not data_rows:
        return

    num_cols = len(data_rows[0])
    tbl = doc.add_table(rows=len(data_rows), cols=num_cols)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER

    total_width_cm = 14.0 # Text width between 4cm left and 3cm right on 21cm page
    col_w_cm = total_width_cm / num_cols

    for r_idx, row in enumerate(data_rows):
        tbl_row = tbl.rows[r_idx]
        is_header = (r_idx == 0)
        for c_idx, cell_text in enumerate(row[:num_cols]):
            cell = tbl_row.cells[c_idx]
            cell.width = Cm(col_w_cm)
            set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
            if is_header:
                set_cell_shading(cell, "F2F2F2")

            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if (is_header or c_idx in [0, num_cols-1]) else WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.first_line_indent = Cm(0)

            # Parse bold / italics
            clean_cell = clean_academic_text(cell_text)
            tokens = re.split(r'(\*\*.*?\*\*|\*.*?\*)', clean_cell)
            for token in tokens:
                if not token:
                    continue
                if token.startswith('**') and token.endswith('**'):
                    run = p.add_run(token[2:-2].replace('*', ''))
                    run.font.bold = True
                elif token.startswith('*') and token.endswith('*'):
                    run = p.add_run(token[1:-1].replace('*', ''))
                    run.font.italic = True
                else:
                    clean_st = token.replace('*', '')
                    if clean_st:
                        run = p.add_run(clean_st)
                    else:
                        continue
                run.font.name = "Times New Roman"
                run.font.size = Pt(10 if is_header else 9.5)
                if is_header:
                    run.font.bold = True

    apply_apa7_table_borders(tbl)
    p_sp = doc.add_paragraph()
    p_sp.paragraph_format.space_before = Pt(4)
    p_sp.paragraph_format.space_after = Pt(6)


def build_tabel_jadwal(doc):
    """Builds Tabel 3.3: Jadwal Pelaksanaan Kegiatan Penelitian (Tahun 2026)."""
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_cap.paragraph_format.space_before = Pt(12)
    p_cap.paragraph_format.space_after = Pt(4)
    p_cap.paragraph_format.first_line_indent = Cm(0)
    p_cap.add_run("Tabel 3.3. Jadwal Pelaksanaan Kegiatan Penelitian (Tahun 2026)").font.bold = True

    headers = ["No", "Tahapan Kegiatan Penelitian", "B1", "B2", "B3", "B4", "B5", "B6"]
    data = [
        ("1", "Identifikasi fenomena pasar dan perumusan topik", "•", "", "", "", "", ""),
        ("2", "Studi kepustakaan dan telaah literatur jurnal", "•", "•", "", "", "", ""),
        ("3", "Penyusunan naskah proposal penelitian (Bab 1–3)", "", "•", "•", "", "", ""),
        ("4", "Bimbingan intensif dan revisi proposal skripsi", "", "•", "•", "", "", ""),
        ("5", "Pelaksanaan Seminar Proposal Skripsi", "", "", "•", "", "", ""),
        ("6", "Uji coba instrumen kuesioner (pilot test n=30)", "", "", "", "•", "", ""),
        ("7", "Pengumpulan data lapangan survei utama (n=120–150)", "", "", "", "•", "•", ""),
        ("8", "Tabulasi data dan pengolahan statistik via SPSS", "", "", "", "", "•", ""),
        ("9", "Penyusunan laporan Bab 4 (Analisis) dan Bab 5 (Penutup)", "", "", "", "", "•", "•"),
        ("10", "Ujian Sidang Skripsi dan Komprehensif", "", "", "", "", "", "•")
    ]

    tbl = doc.add_table(rows=1+len(data), cols=8)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER

    col_widths = [Cm(1.0), Cm(7.0), Cm(1.0), Cm(1.0), Cm(1.0), Cm(1.0), Cm(1.0), Cm(1.0)]

    # Header
    for c_idx, h_text in enumerate(headers):
        cell = tbl.rows[0].cells[c_idx]
        cell.width = col_widths[c_idx]
        set_cell_margins(cell, top=80, bottom=80, left=60, right=60)
        set_cell_shading(cell, "F2F2F2")
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.15
        r = p.add_run(h_text)
        r.font.name = "Times New Roman"
        r.font.size = Pt(10)
        r.font.bold = True

    # Data Rows
    for r_idx, row_vals in enumerate(data):
        row = tbl.rows[r_idx + 1]
        for c_idx, val in enumerate(row_vals):
            cell = row.cells[c_idx]
            cell.width = col_widths[c_idx]
            set_cell_margins(cell, top=60, bottom=60, left=60, right=60)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT if c_idx == 1 else WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.15
            r = p.add_run(val)
            r.font.name = "Times New Roman"
            r.font.size = Pt(9.5)
            if val == "•":
                r.font.bold = True

    apply_apa7_table_borders(tbl)

    p_src = doc.add_paragraph()
    p_src.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_src.paragraph_format.space_before = Pt(2)
    p_src.paragraph_format.space_after = Pt(12)
    p_src.paragraph_format.first_line_indent = Cm(0)
    r_s = p_src.add_run("Keterangan: B1 = Bulan ke-1; B2 = Bulan ke-2; B3 = Bulan ke-3; B4 = Bulan ke-4; B5 = Bulan ke-5; B6 = Bulan ke-6 tahun akademik 2026.")
    r_s.font.name = "Times New Roman"
    r_s.font.size = Pt(9.5)
    r_s.font.italic = True


def build_tabel_research_gap(doc):
    """Builds Tabel 1.1: Matriks Kesenjangan Penelitian Empiris (Research Gap) pada 7 Subjek Hubungan Model Penelitian."""
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_cap.paragraph_format.space_before = Pt(12)
    p_cap.paragraph_format.space_after = Pt(4)
    p_cap.paragraph_format.first_line_indent = Cm(0)
    p_cap.paragraph_format.keep_with_next = True
    r_c = p_cap.add_run("Tabel 1.1: Matriks Kesenjangan Penelitian Empiris (Research Gap) pada 7 Subjek Hubungan Model Penelitian")
    make_run_pure_black(r_c, "Times New Roman", Pt(11), bold=True)

    headers = [
        "No",
        "Subjek Hubungan",
        "Kelompok Temuan Positif / Meredam",
        "Kelompok Temuan Negatif / Lemah",
        "Inti Kesenjangan Kausal (The Why)"
    ]
    data = [
        (
            "1",
            "X₁ → Y (Hedonic Motivation ke Impulsive Buying)",
            "Arnold dan Reynolds (2003); Gültekin dan Özer (2012); Pranggabayu dan Andjarwati (2022); Gong et al. (2024); Tirtayasa et al. (2020); Zheng et al. (2019) (Pengaruh positif signifikan; penelusuran hedonis memicu dorongan impulsif).",
            "Batas konseptual Thaler (1985); Thaler dan Shefrin (1981) (Dorongan tertahan batasan anggaran/mental budgeting; bukan klaim n.s. pada kolektibel).",
            "Perbedaan elastisitas anggaran dan dominasi orientasi utiliter vs afektif konsumen."
        ),
        (
            "2",
            "X₂ → Y (Desire for Completeness ke Impulsive Buying)",
            "Gao et al. (2014); Barasz et al. (2017); Dewi et al. (2026) (Pengaruh positif signifikan; ketegangan psikologis set memicu akselerasi transaksi).",
            "Argumen teoritis Long dan Schiffman (2000); Spero dan Stone (2004) (Kolektor matang menolak produk acak dan memilih kartu satuan; bukan klaim n.s.).",
            "Perbedaan tingkat kematangan kolektor (collector maturity) dan kalkulasi probabilitas kemasan acak."
        ),
        (
            "3",
            "X₃ → Y (Speculative Motive ke Impulsive Buying)",
            "Baur et al. (2018); Aryadi dan Lingga (2026) (analogi: Y=partisipasi investasi TCG); Colline (2024) (analogi: herding investor Indonesia, kualitatif n=5; teori Shiller (2000) sebagai grand theory).",
            "Analogi saham Barber dan Odean (2008); Fama (1970) (Kesadaran risiko menahan spontanitas; bukan bukti n.s. kolektibel).",
            "Asimetri informasi pasar dan bias ilusi kendali keuntungan vs evaluasi risiko kerugian modal."
        ),
        (
            "4",
            "M → Y (Self-Control ke Impulsive Buying)",
            "Baumeister (2002); Tangney et al. (2004); Vohs dan Faber (2007); Sultan et al. (2012) (Pengaruh negatif signifikan; regulasi diri disiplin menunda kepuasan belanja).",
            "Batas konseptual Hirschman dan Holbrook (1982); Stern (1962) (Cognitive bypass saat stimulus intens; bukan uji regresi).",
            "Keterbatasan kapasitas energi kognitif (ego depletion) saat menghadapi stimulus lingkungan toko yang intens."
        ),
        (
            "5",
            "X₁ · M → Y (Moderasi M pada X₁ → Y)",
            "Lienardy dan Panasea (2026) (MRA: H4 diterima, buffer); Katauke et al. (2023) (regulasi-literasi, tak langsung).",
            "Gagal-moderasi: Apidana dan Kholifah (2022) (p=0,597) + Artadita dan Firmialy (2024) (β=0,092, n.s.) + teori regulatory failure.",
            "Ambang batas intensitas stimulus hedonis yang melampaui kapasitas kontrol volisional."
        ),
        (
            "6",
            "X₂ · M → Y (Moderasi M pada X₂ → Y)",
            "Parsial/tak langsung: Artadita dan Firmialy (2024) (kontrol kognitif signifikan pada taraf 10%, moderasi keseluruhan DITOLAK); Apidana dan Kholifah (2022) (buffer lifestyle, adjacent).",
            "Teori obsesi Belk (1995); Barasz et al. (2017) + gagal-moderasi koleksi Artadita dan Firmialy (2024) (H3 ditolak).",
            "Tingkat keterikatan emosional kolektor (involvement); hobi kasual vs fanatisme koleksi mendalam."
        ),
        (
            "7",
            "X₃ · M → Y (Moderasi M pada X₃ → Y)",
            "Tak langsung: Katauke et al. (2023) (literasi menekan impulsivitas) + mekanisme Planner-Doer.",
            "Argumen teoritis Shiller (2000); Aryadi dan Lingga (2026) (Euforia/herding melumpuhkan rem; bukan uji X₃ · M).",
            "Tekanan sosial komunitas, bias herding, dan ketakutan tertinggal momentum keuntungan (FOMO)."
        )
    ]

    tbl = doc.add_table(rows=1+len(data), cols=5)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    col_widths = [Cm(0.8), Cm(2.8), Cm(3.7), Cm(3.7), Cm(3.0)]
    set_col_widths_fixed(tbl, col_widths)

    # Header
    for c_idx, h_text in enumerate(headers):
        cell = tbl.rows[0].cells[c_idx]
        set_cell_margins(cell, top=60, bottom=60, left=50, right=50)
        set_cell_shading(cell, "F2F2F2")
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.15
        r = p.add_run(h_text)
        make_run_pure_black(r, "Times New Roman", Pt(9.5), bold=True)

    # Data Rows
    for r_idx, row_vals in enumerate(data):
        row = tbl.rows[r_idx + 1]
        for c_idx, val in enumerate(row_vals):
            cell = row.cells[c_idx]
            set_cell_margins(cell, top=50, bottom=50, left=50, right=50)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if c_idx == 0 else WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.first_line_indent = Cm(0)
            clean_val = clean_academic_text(val)
            parse_markdown_runs(p, clean_val, base_size=Pt(9.0), base_bold=False)

    apply_apa7_table_borders(tbl)

    p_src = doc.add_paragraph()
    p_src.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_src.paragraph_format.space_before = Pt(2)
    p_src.paragraph_format.space_after = Pt(12)
    p_src.paragraph_format.first_line_indent = Cm(0)
    r_s = p_src.add_run("Sumber: Data diolah dari sintesis kajian literatur empiris terdahulu (2026).")
    make_run_pure_black(r_s, "Times New Roman", Pt(9.0), italic=True)


def _clear_latent_tab_stops(paragraph):
    """Hapus tab-stop bawaan latent style (penyebab dot-leader hilang di Word)."""
    pPr = paragraph._p.get_or_add_pPr()
    tabs = pPr.find(qn('w:tabs'))
    if tabs is not None:
        pPr.remove(tabs)


def _add_dot_tab_7938(paragraph):
    """Satu tab-stop kanan 14.0cm (7938 dxa) + dot leader — spek inviolable."""
    pPr = paragraph._p.get_or_add_pPr()
    tabs = OxmlElement('w:tabs')
    tab = OxmlElement('w:tab')
    tab.set(qn('w:val'), 'right')
    tab.set(qn('w:leader'), 'dot')
    tab.set(qn('w:pos'), '7938')
    tabs.append(tab)
    pPr.append(tabs)


_LOTLOF_BM_SEQ = [1000]
_CITE_BM_SEQ = [2000]


def _add_bookmark(paragraph, name, bid):
    # LibreOffice-strict: <w:pPr> wajib anak pertama <w:p>, jadi bookmark
    # disisipkan SESUDAH pPr (Word toleran, LibreOffice mengabaikan bookmark
    # yang sebelum pPr sehingga hyperlink Ref_/Cap_ mati di LibreOffice).
    bs = OxmlElement('w:bookmarkStart')
    bs.set(qn('w:id'), str(bid))
    bs.set(qn('w:name'), name)
    be = OxmlElement('w:bookmarkEnd')
    be.set(qn('w:id'), str(bid))
    pPr = paragraph._p.find(qn('w:pPr'))
    if pPr is not None:
        idx = list(paragraph._p).index(pPr) + 1
        paragraph._p.insert(idx, bs)
    else:
        paragraph._p.insert(0, bs)
    paragraph._p.append(be)


def link_lot_lof_entries(doc):
    """Post-pass: bookmark caption tubuh + hyperlink entri LOT/LOF (tetap hitam)."""
    cap_re = re.compile(r'^(Tabel|Gambar)\s+(\d+)\.(\d+)\b')
    WNS = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

    def _para_text(p):
        return ''.join((n.text or '') for n in p._p.iterfind('.//w:t', namespaces=WNS))

    targets = {}
    for p in doc.paragraphs:
        try:
            st_name = p.style.name
        except Exception:
            st_name = ''
        if st_name.lower().startswith('toc'):
            continue
        t = _para_text(p).strip()
        m = cap_re.match(t)
        if not m:
            continue
        if '<w:hyperlink' in p._p.xml or 'w:fldChar' in p._p.xml:
            continue
        key = '%s %s.%s' % (m.group(1), m.group(2), m.group(3))
        if key in targets:
            continue
        _LOTLOF_BM_SEQ[0] += 1
        bid = _LOTLOF_BM_SEQ[0]
        name = 'Cap_%s_%s_%s' % (m.group(1), m.group(2), m.group(3))
        _add_bookmark(p, name, bid)
        targets[key] = name

    n_linked = 0
    for p in doc.paragraphs:
        try:
            st_name = p.style.name
        except Exception:
            st_name = ''
        if not st_name.lower().startswith('toc'):
            continue
        if '<w:hyperlink' in p._p.xml or 'w:fldChar' in p._p.xml:
            continue
        t = _para_text(p).strip()
        m = cap_re.match(t)
        if not m:
            continue
        key = '%s %s.%s' % (m.group(1), m.group(2), m.group(3))
        if key not in targets:
            continue
        h = OxmlElement('w:hyperlink')
        h.set(qn('w:anchor'), targets[key])
        h.set(qn('w:history'), '1')
        for r in list(p._p.findall(qn('w:r'))):
            h.append(r)
        p._p.append(h)
        n_linked += 1
    print('[*] LOT/LOF hyperlink: %d caption ditandai, %d entri terhubung.' % (len(targets), n_linked))
    return n_linked


_TOC_BM_SEQ = [5000]


def _norm_toc_title(s: str) -> str:
    sub_map = str.maketrans({
        '₁': '1', '₂': '2', '₃': '3', '₄': '4', '₅': '5',
        '₆': '6', '₇': '7', '₈': '8', '₉': '9', '₀': '0',
        '¹': '1', '²': '2', '³': '3', 'ᵢ': 'i',
        '−': '-', '–': '-', '—': '-',
    })
    s = s.translate(sub_map)
    s = re.sub(r'\s+', ' ', s.strip()).upper().replace('R²', 'R2')
    return s


def link_static_toc_entries(doc):
    """Post-pass LibreOffice: bookmark Heading + hyperlink entri Daftar Isi statis.

    Word COM TOC injection sering gagal di mesin tanpa MS Word sehingga Daftar Isi
    tertinggal sebagai teks statis tanpa hyperlink (Ctrl+Klik mati di LibreOffice),
    sedangkan Daftar Tabel/Gambar tetap bisa diklik (Cap_*). Fungsi ini membuat TOC
    statis tetap klikabel: tiap Heading 1/2/3 diberi bookmark TOC_*, lalu tiap entri
    TOC di antara DAFTAR ISI s.d. DAFTAR TABEL dibungkus <w:hyperlink>. Teks 100%
    identik, format hitam tetap, idempoten.
    """
    existing = set()
    max_id = 0
    for p in list(doc.paragraphs):
        for el in p._p.iter():
            if el.tag == qn('w:bookmarkStart'):
                existing.add(el.get(qn('w:name')))
            if el.tag in (qn('w:bookmarkStart'), qn('w:bookmarkEnd')):
                try:
                    max_id = max(max_id, int(el.get(qn('w:id'))))
                except (TypeError, ValueError):
                    pass
    _TOC_BM_SEQ[0] = max(_TOC_BM_SEQ[0], max_id + 1)
    hmap = {}
    for p in doc.paragraphs:
        try:
            st = p.style.name
        except Exception:
            st = ''
        if not st.startswith('Heading'):
            continue
        title = p.text.strip()
        if not title:
            continue
        own = [el.get(qn('w:name')) for el in p._p.iter() if el.tag == qn('w:bookmarkStart')]
        if own:
            hmap[_norm_toc_title(title)] = own[0]
            continue
        slug = re.sub(r'\W+', '_', title.strip(), flags=re.UNICODE)
        slug = re.sub(r'_+', '_', slug).strip('_')[:60] or 'SEC'
        name = f"TOC_{slug.upper()}"
        suffix = 1
        base = name
        while name in existing:
            suffix += 1
            name = f"{base}_{suffix}"
        existing.add(name)
        _add_bookmark(p, name, _TOC_BM_SEQ[0])
        _TOC_BM_SEQ[0] += 1
        hmap[_norm_toc_title(title)] = name
    paras = list(doc.paragraphs)
    isi_idx = next((i for i, p in enumerate(paras) if p.text.strip() == 'DAFTAR ISI'), None)
    if isi_idx is None:
        return 0
    tabel_idx = next((i for i in range(isi_idx + 1, len(paras))
                      if paras[i].text.strip() == 'DAFTAR TABEL'
                      and getattr(paras[i].style, 'name', '').startswith('Heading')), len(paras))
    n = 0
    for p in paras[isi_idx + 1:tabel_idx]:
        try:
            st = p.style.name
        except Exception:
            st = ''
        if not st.lower().startswith('toc'):
            continue
        if '<w:hyperlink' in p._p.xml or 'w:fldChar' in p._p.xml:
            continue
        before = p.text
        if not before.strip():
            continue
        title_part = before.rsplit('\t', 1)[0].strip() if '\t' in before else before.strip()
        target = hmap.get(_norm_toc_title(title_part))
        if target is None:
            continue
        runs = [r for r in list(p._p) if r.tag == qn('w:r')]
        if not runs:
            continue
        h = OxmlElement('w:hyperlink')
        h.set(qn('w:anchor'), target)
        h.set(qn('w:history'), '1')
        idx0 = list(p._p).index(runs[0])
        for r in runs:
            h.append(r)
        p._p.insert(idx0, h)
        assert p.text == before, 'TOC text changed!'
        n += 1
    print('[*] TOC statis hyperlink: %d entri Daftar Isi terhubung (LibreOffice-safe).' % n)
    return n


def _parse_aux_cites(aux_path):
    """{key: (author_raw, year)} dari .aux \\bibcite (bentuk display natbib)."""
    from pathlib import Path as _P
    try:
        aux = _P(aux_path).read_text(encoding='utf-8')
    except OSError:
        return {}
    out = {}
    for key, year, author in re.findall(r'\\bibcite\{([^}]+)\}\{\{\d+\}\{(\d{4})\}\{(.*?)\}\}', aux):
        a = author.strip('{}').replace('~', ' ')
        a = (a.replace(r'{\"u}', 'ü').replace(r'{\"O}', 'Ö')
              .replace(r"{\'e}", 'é').replace(r"\'e", 'é')
              .replace('{', '').replace('}', ''))
        out[key.strip()] = (a.strip(), year)
    return out


def _parse_bbl_keys(bbl_path):
    from pathlib import Path as _P
    try:
        bbl = _P(bbl_path).read_text(encoding='utf-8')
    except OSError:
        return []
    return [k.strip() for k in re.findall(r'\\bibitem\[[^\]]*\]\{([^}]+)\}', bbl)]


def _add_bookmark(paragraph, name, bid):
    # LibreOffice-strict: <w:pPr> wajib anak pertama <w:p>, jadi bookmark
    # disisipkan SESUDAH pPr (Word toleran, LibreOffice mengabaikan bookmark
    # yang sebelum pPr sehingga hyperlink Ref_/Cap_ mati di LibreOffice).
    bs = OxmlElement('w:bookmarkStart')
    bs.set(qn('w:id'), str(bid))
    bs.set(qn('w:name'), name)
    be = OxmlElement('w:bookmarkEnd')
    be.set(qn('w:id'), str(bid))
    pPr = paragraph._p.find(qn('w:pPr'))
    if pPr is not None:
        idx = list(paragraph._p).index(pPr) + 1
        paragraph._p.insert(idx, bs)
    else:
        paragraph._p.insert(0, bs)
    paragraph._p.append(be)


_CITE_BM_SEQ = [3000]


def _author_regex(author_raw):
    """Regex fragmen display penulis: 'A and B'->dan/and/&; 'X et al.'; korporat."""
    a = author_raw.replace('~', ' ').strip()
    a = re.sub(r'\s+', ' ', a)
    if 'et al' in a.lower():
        base = re.split(r'\bet\s*al\b', a, flags=re.I)[0].strip(' .')
        return re.escape(base) + r'\s+et al\.+'
    parts = re.split(r'\s+and\s+', a, flags=re.I)
    if len(parts) == 2:
        return re.escape(parts[0].strip()) + r'\s+(?:dan|and|&)\s+' + re.escape(parts[1].strip())
    return re.escape(a)


def link_citations_to_dp(doc, aux_map, ref_bookmarks):
    """Post-pass: hyperlink setiap sitasi tubuh ke bookmark entri DP (tetap hitam).

    Pola: (Penulis, Tahun) multi, Penulis (Tahun), dan bare multi-kata.
    Melewati: heading/TOC, field Word, rentang hyperlink eksisting, seksi DP.
    """
    import copy as _copy
    W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
    NS = {'w': W}

    # Batas seksi DP: hyperlink hanya SEBELUM heading DAFTAR PUSTAKA
    dp_idx = None
    paras = list(doc.paragraphs)
    for i, p in enumerate(paras):
        try:
            st = p.style.name
        except Exception:
            st = ''
        if st.startswith('Heading') and p.text.strip() == 'DAFTAR PUSTAKA':
            dp_idx = i
            break

    WR = qn('w:r')
    WT = qn('w:t')
    WTAB = qn('w:tab')
    WBR = qn('w:br')

    def _para_map(p):
        """(full, seq) dgn full == p.text persis; seq = (teks, run|None, tnode|None).

        Hanya w:t di bawah w:r LANGSUNG yg splittable. Segala teks lain
        (oMath, instr, del) = atomik. None bila tak konsisten -> lewati.
        """
        seq = []
        for node in p._p.iter():
            par = node.getparent()
            if node.tag == WT and par is not None and par.tag == WR \
                    and par.getparent() is p._p:
                seq.append((node.text or '', par, node))
            elif node.tag in (WTAB, WBR) and par is not None and par.tag == WR \
                    and par.getparent() is p._p:
                seq.append(('\t' if node.tag == WTAB else '\n', None, None))
            elif node.tag.endswith('}t') and (node.text or ''):
                # teks non-direct (hyperlink bersarang, oMath, instr): atomik
                seq.append((node.text, None, None))
        full = ''.join(t for t, _, _ in seq)
        if full != p.text:
            return None, None
        return full, seq

    def _split_seq(p, seq, off):
        """Belah run pada offset global off (dlm koordinat seq)."""
        import copy as _c
        WTloc = qn('w:t')
        XS = '{http://www.w3.org/XML/1998/namespace}space'
        pos = 0
        for (t, r, nd) in seq:
            if r is None or nd is None:
                pos += len(t)
                continue
            if pos < off < pos + len(t):
                k = off - pos
                try:
                    at = list(r).index(nd)
                except ValueError:
                    return False
                new_run = _c.deepcopy(r)
                for sib in list(new_run)[:at]:
                    new_run.remove(sib)
                first = new_run[0] if len(new_run) else None
                if first is None or first.tag != WTloc:
                    return False
                first.text = t[k:]
                first.set(XS, 'preserve')
                nd.text = t[:k]
                nd.set(XS, 'preserve')
                for sib in list(r)[at + 1:]:
                    r.remove(sib)
                idx = list(p._p).index(r)
                p._p.insert(idx + 1, new_run)
                return True
            pos += len(t)
        return True

    def _wrap_span(p, s, e, anchor):
        """Bungkus rentang [s,e) p.text dalam hyperlink internal.

        Invarian keras: teks paragraf tak boleh berubah; bila berubah,
        paragraf dipulihkan dari snapshot dan False dikembalikan.
        """
        import copy as _c
        before_text = p.text
        before_xml = _c.deepcopy(p._p)
        try:
            # 1. peta seq; tolak bila span menyentuh unit atomik
            mapped = _para_map(p)
            if mapped[0] is None or mapped[0] != before_text:
                return False
            _, seq = mapped
            pos = 0
            for (t, r, _nd) in seq:
                if pos < e and pos + len(t) > s and r is None:
                    return False
                pos += len(t)
            # 2. belah di e lalu s (kanan dulu agar offset kiri valid)
            _split_seq(p, seq, e)
            mapped2 = _para_map(p)
            if mapped2[0] is None:
                raise RuntimeError('map-e')
            _, seq = mapped2
            _split_seq(p, seq, s)
            mapped3 = _para_map(p)
            if mapped3[0] is None:
                raise RuntimeError('map-s')
            _, seq = mapped3
            # 3. kumpulkan run langsung yg sepenuhnya di dalam [s,e)
            pos = 0
            inside = []
            for (t, r, _nd) in seq:
                if r is not None and s <= pos and pos + len(t) <= e and len(t) > 0:
                    if not inside or inside[-1] is not r:
                        inside.append(r)
                pos += len(t)
            if not inside:
                return False
            # verifikasi cakupan persis
            covered = before_text[s:e]
            got = ''
            for r in inside:
                for n in r.iterfind('.//w:t', namespaces={'w': W}):
                    got += n.text or ''
                got += '\t' * len(r.findall(qn('w:tab')))
            if got != covered:
                return False
            h = OxmlElement('w:hyperlink')
            h.set(qn('w:anchor'), anchor)
            h.set(qn('w:history'), '1')
            idx = list(p._p).index(inside[0])
            for r in inside:
                h.append(r)
            p._p.insert(idx, h)
            if p.text != before_text:
                p._p.getparent().replace(p._p, before_xml)
                return False
            return True
        except Exception:
            try:
                p._p.getparent().replace(p._p, before_xml)
            except Exception:
                pass
            return False

    # Susun pola per kunci (terpanjang dulu agar multi-cite menang)
    matchers = []
    seg_matchers = []
    for key, (author_raw, year) in aux_map.items():
        if key not in ref_bookmarks:
            continue
        au = _author_regex(author_raw)
        multiword = (' ' in author_raw.replace('~', ' ').strip()) or ('et al' in author_raw.lower())
        matchers.append((key, re.compile(r'\(\s*' + au + r'\s*,\s*' + year + r'\s*\)'), 'paren'))
        matchers.append((key, re.compile(au + r'\s*\(\s*' + year + r'\s*\)'), 'narr'))
        if multiword:
            matchers.append((key, re.compile(au + r'\s*,\s*' + year), 'bare'))
        # segmen di dalam grup multi-sitasi "(A, 2000; B, 2010)": semua kunci
        seg_matchers.append((key, re.compile(au + r'\s*,\s*' + year)))
    matchers.sort(key=lambda m: -len(m[1].pattern))
    seg_matchers.sort(key=lambda m: -len(m[1].pattern))
    paren_group_rx = re.compile(r'\([^()]{2,300}\)')

    all_paras = list(doc.paragraphs)
    for tbl in doc.tables:
        for row in tbl.rows:
            for cell in row.cells:
                all_paras.extend(cell.paragraphs)

    n_linked = 0
    for idx, p in enumerate(all_paras):
        if dp_idx is not None and idx < len(paras) and idx >= dp_idx and p in paras:
            continue
        try:
            st = p.style.name
        except Exception:
            st = ''
        if st.startswith(('TOC', 'Heading')):
            continue
        if 'w:fldChar' in p._p.xml:
            continue
        # Anti-self-link: lewati entri DP (sudah ber-bookmark Ref_*) agar pola
        # naratif korporat ("PriceCharting (2024)") di awal entri tidak menaut
        # ke bookmark dirinya sendiri — Word COM menghapus bookmark yang
        # menaungi hyperlink internal ke dirinya (orphan Ref_*).
        _has_dp_bm = False
        for _el in p._p.iter():
            if _el.tag == qn('w:bookmarkStart') and (_el.get(qn('w:name')) or '').startswith('Ref_'):
                _has_dp_bm = True
                break
        if _has_dp_bm:
            continue
        text = p.text
        if not text or '(' not in text and 'et al' not in text:
            # tetap izinkan bare multiword tanpa paren
            if not re.search(r'et al\.| dan \d{4}| and \d{4}', text):
                continue
        spans = []
        used = [False] * len(text)
        for key, rx, _kind in matchers:
            for m in rx.finditer(text):
                s, e = m.span()
                if any(used[s:e]):
                    continue
                for i in range(s, e):
                    used[i] = True
                spans.append((s, e, key))
        # segmen multi-sitasi: pecah grup "(...)" per ';' lalu cocokkan per kunci
        for g in paren_group_rx.finditer(text):
            gs, ge = g.span()
            if all(used[gs:ge]):
                continue
            for seg in g.group(0)[1:-1].split(';'):
                seg = seg.strip()
                if not seg:
                    continue
                for key, rx in seg_matchers:
                    m = rx.search(seg)
                    if not m:
                        continue
                    # offset absolut eksak dalam teks paragraf
                    base = gs + 1
                    rel = g.group(0)[1:-1].find(seg)
                    s = base + rel + seg.find(m.group(0))
                    e = s + len(m.group(0))
                    if e > len(text) or any(used[s:e]):
                        continue
                    if text[s:e] != m.group(0):
                        continue
                    for i in range(s, e):
                        used[i] = True
                    spans.append((s, e, key))
                    break
        if not spans:
            continue
        for s, e, key in sorted(spans, reverse=True):
            if _wrap_span(p, s, e, ref_bookmarks[key]):
                n_linked += 1
    print('[*] Sitasi hyperlink: %d tautan ke Daftar Pustaka.' % n_linked)
    return n_linked


def add_hyperlink(paragraph, url, text, color="0563C1", underline=True):
    """Adds an active, clickable hyperlink to a paragraph in python-docx using OpenXML."""
    try:
        import docx.opc.constants
        part = paragraph.part
        r_id = part.relate_to(url, docx.opc.constants.RELATIONSHIP_TYPE.HYPERLINK, is_external=True)

        hyperlink = parse_xml(f'<w:hyperlink xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" r:id="{r_id}" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"/>')
        new_run = parse_xml(f'<w:r xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"/>')
        rPr = parse_xml(f'<w:rPr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"/>')

        if color:
            c = parse_xml(f'<w:color xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" w:val="{color}"/>')
            rPr.append(c)
        if underline:
            u = parse_xml(f'<w:u xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" w:val="single"/>')
            rPr.append(u)

        rFonts = parse_xml(f'<w:rFonts xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>')
        rPr.append(rFonts)
        sz = parse_xml(f'<w:sz xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" w:val="24"/>')
        rPr.append(sz)

        new_run.append(rPr)
        text_node = parse_xml(f'<w:t xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">{text}</w:t>')
        new_run.append(text_node)
        hyperlink.append(new_run)
        paragraph._p.append(hyperlink)
        return hyperlink
    except Exception as e:
        # Fallback to standard styled run if XML fails
        r = paragraph.add_run(text)
        r.font.name = "Times New Roman"
        r.font.size = Pt(12)
        r.font.underline = True
        return r


def build_daftar_pustaka(doc, content):
    """Builds FEB UKRIDA 2023 compliant bibliography with 1.25cm hanging indent without numbering.

    Mengembalikan daftar paragraf entri (urutan = urutan .bbl) untuk bookmark.
    """
    built = []
    lines = content.split('\n')
    for line in lines:
        line_str = line.strip()
        if not line_str or line_str.startswith('#'):
            continue

        # Strip any leading numbers or bullets (e.g. "1. ", "12. ", "- ", "• ")
        line_str = re.sub(r'^\d+[\.\)]\s*', '', line_str)
        line_str = re.sub(r'^[\*\-•]\s*', '', line_str)
        line_str = line_str.strip()

        if not line_str:
            continue

        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.left_indent = Cm(1.25)
        p.paragraph_format.first_line_indent = Cm(-1.25)

        clean_bib = clean_academic_text(line_str)

        # Detect URL in the bibliography entry (e.g. https://...)
        url_match = re.search(r'(https?://[^\s<>"]+)', clean_bib)
        if url_match:
            url = url_match.group(1).rstrip('.')
            prefix = clean_bib[:url_match.start()].rstrip()
            parse_markdown_runs(p, prefix)
            p.add_run(" ")
            add_hyperlink(p, url, url, color="0563C1", underline=True)
            suffix = clean_bib[url_match.end():].strip()
            if suffix:
                p.add_run(" " + suffix)
        else:
            parse_markdown_runs(p, clean_bib)
        built.append(p)
    return built


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Build FEB UKRIDA Proposal DOCX")
    parser.add_argument(
        "--no-chapter3",
        action="store_true",
        help="Skip Bab 3 (Metode Penelitian) — output: Proposal_Arthur_NoBab3.docx"
    )
    parser.add_argument(
        "--no-frontmatter",
        action="store_true",
        help=(
            "Skip 6 halaman formal frontmatter (Pernyataan, Persetujuan, Pengesahan, "
            "Kata Pengantar, Abstrak, Abstract). "
            "DOCX utama mulai dari Daftar Isi (hal. i) dan Bab 1 (hal. 1). "
            "Output: Proposal_Arthur_PokemonTCG_NoFrontmatter.docx"
        )
    )
    args = parser.parse_args()
    build_full_proposal(skip_chapter3=args.no_chapter3, skip_frontmatter=args.no_frontmatter)
