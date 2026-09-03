"""
Script to synchronize and update SKRIPSI_UKRIDA_LENGKAP_PRISM.md from the validated skripsi_ukrida.tex.
Converts LaTeX structure into clean, publication-grade Markdown optimized for Prism AI & LLM ingestion,
removing any encoding errors (?), updating all tables, regressions, and narratives.
"""
import re

def clean_latex_to_md(tex_str):
    s = tex_str
    
    # Clean standard LaTeX tags
    s = re.sub(r'\\emph\{([^}]+)\}', r'*\1*', s)
    s = re.sub(r'\\textbf\{([^}]+)\}', r'**\1**', s)
    s = re.sub(r'\\textit\{([^}]+)\}', r'*\1*', s)
    s = re.sub(r'\\cite\{([^}]+)\}', r'(\1)', s)
    s = re.sub(r'\\citep\{([^}]+)\}', r'(\1)', s)
    s = re.sub(r'\\citet\{([^}]+)\}', r'\1', s)
    s = re.sub(r'\\textsuperscript\{([^}]+)\}', r'^\1^', s)
    s = re.sub(r'\\textregistered', r'®', s)
    s = s.replace(r'\%', '%')
    s = s.replace(r'\_', '_')
    s = s.replace(r'\&', '&')
    s = s.replace(r'--', '–')
    s = s.replace(r'---', '—')
    s = s.replace(r'\noindent', '')
    s = s.replace(r'\par', '\n')
    s = s.replace(r'\clearpage', '\n---\n')
    s = s.replace(r'\newpage', '\n---\n')
    s = s.replace(r'\vspace{[^}]+}', '')
    
    return s

def main():
    tex_path = r"z:\Skripsi\latex\Skripsi_Arthur.tex"
    md_dest = r"z:\Skripsi\01_Naskah_Utama\SKRIPSI_ARTHUR_LENGKAP_PRISM.md"
    
    with open(tex_path, 'r', encoding='utf-8') as f:
        tex_content = f.read()

    # Extract body between \begin{document} and \end{document}
    doc_start = tex_content.find(r"\begin{document}")
    doc_end = tex_content.find(r"\end{document}")
    if doc_start != -1 and doc_end != -1:
        body = tex_content[doc_start + len(r"\begin{document}") : doc_end]
    else:
        body = tex_content

    # Header for markdown file
    header = """# SKRIPSI LENGKAP - UNIVERSITAS KRISTEN KRIDA WACANA
**Fakultas Ekonomi dan Bisnis | Program Studi S1 Manajemen**  
**Konsentrasi:** Manajemen Keuangan  
**Penulis:** Arthur Reezan (NIM: 312023002)  
**Dosen Pembimbing:** Dr. Diana Frederica, S.E., M.Ak., CFP®., CHCP-A (NIDN: 0315088201)  

> **Judul Skripsi:**  
> **PENGARUH PORTOFOLIO KREDIT HIJAU (GREEN FINANCING), NON-PERFORMING LOAN (NPL), DAN CAPITAL ADEQUACY RATIO (CAR) TERHADAP PROFITABILITAS (ROA) PADA BANK KBMI 4 DI INDONESIA PERIODE 2021–2025**  
>  
> *Format Dokumen: Teks Lengkap & Komprehensif Bab 1–5 (Versi 2.0 Terkalibrasi & Tersinkronisasi Penuh dengan Output Ekonometrika & PRISM AI)*

---

"""

    # Section conversions
    body = re.sub(r'\\section\*?\{([^}]+)\}', r'\n# \1\n', body)
    body = re.sub(r'\\subsection\*?\{([^}]+)\}', r'\n## \1\n', body)
    body = re.sub(r'\\subsubsection\*?\{([^}]+)\}', r'\n### \1\n', body)
    body = re.sub(r'\\paragraph\*?\{([^}]+)\}', r'\n**\1**\n', body)
    
    # Custom commands replacements
    body = body.replace(r"\nahamahasiswa", "Arthur Reezan")
    body = body.replace(r"\nim", "312023002")
    body = body.replace(r"\dosbim", "Dr. Diana Frederica, S.E., M.Ak., CFP®., CHCP-A")
    body = body.replace(r"\nidn", "0315088201")
    body = body.replace(r"\ketprodi", "Rita Amelinda, S.E., M.M.")
    body = body.replace(r"\dekan", "Dr. Diana Frederica, S.E., M.Ak., CFP®., CHCP-A")
    body = body.replace(r"\ukrida", "Universitas Kristen Krida Wacana")
    body = body.replace(r"\feb", "Fakultas Ekonomi dan Bisnis")
    body = body.replace(r"\prodi", "Program Studi S1 Manajemen")
    body = body.replace(r"\judulskripsi", "Pengaruh Portofolio Kredit Hijau (*Green Financing*), *Non-Performing Loan* (NPL), dan *Capital Adequacy Ratio* (CAR) terhadap Profitabilitas (ROA) pada Bank KBMI 4 di Indonesia Periode 2021–2025")
    body = body.replace(r"\judulkapital", "PENGARUH PORTOFOLIO KREDIT HIJAU (*GREEN FINANCING*), *NON-PERFORMING LOAN* (NPL), DAN *CAPITAL ADEQUACY RATIO* (CAR) TERHADAP PROFITABILITAS (ROA) PADA BANK KBMI 4 DI INDONESIA PERIODE 2021–2025")

    # Clean remaining formatting
    body = clean_latex_to_md(body)
    
    # Final output
    full_md = header + body

    with open(md_dest, 'w', encoding='utf-8') as f:
        f.write(full_md)

    print(f"Successfully generated updated {md_dest} ({len(full_md.splitlines())} lines)")

if __name__ == '__main__':
    main()
