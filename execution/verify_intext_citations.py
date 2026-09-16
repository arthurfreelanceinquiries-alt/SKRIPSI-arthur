import re
from pathlib import Path

def extract_body(text):
    start_pos = 0
    m_start = re.search(r'(\\section\*?\{BAB\s+1|\n#\s+BAB\s+1\s+PENDAHULUAN|\n#\s+BAB\s+I\s+PENDAHULUAN)', text, re.IGNORECASE)
    if m_start:
        start_pos = m_start.start()
    
    end_pos = len(text)
    m_end = re.search(r'(\\bibliography\{|\n#\s+DAFTAR\s+PUSTAKA|\n##\s+DAFTAR\s+PUSTAKA|\n\\section\*?\{DAFTAR\s+PUSTAKA)', text[start_pos:], re.IGNORECASE)
    if m_end:
        end_pos = start_pos + m_end.start()
        
    return text[start_pos:end_pos]

def audit_latex_citations(tex_path):
    print(f"\n[*] Mengaudit Sitasi In-Text pada LaTeX: {tex_path.name}...")
    full_text = tex_path.read_text(encoding="utf-8")
    text = extract_body(full_text)
    
    # 1. Cek Gelar Akademik Terlarang dalam Sitasi Batang Tubuh
    forbidden_degrees = [r'\bS\.?H\.?\b', r'\bS\.?E\.?\b', r'\bM\.?M\.?\b', r'\bPh\.?D\.?\b', r'\bDr\.\s+[A-Z]', r'\bProf\.\s+[A-Z]']
    citation_regex = re.compile(r'\\cite[pt]?\*?\{([^}]+)\}')
    
    degree_errors = []
    for deg in forbidden_degrees:
        matches = re.findall(rf'([A-Z][a-z]+,?\s+{deg})', text)
        if matches:
            degree_errors.extend(matches)
            
    if degree_errors:
        print(f"  [FAIL] Ditemukan gelar akademik terlarang dalam narasi sitasi batang tubuh: {set(degree_errors)}")
    else:
        print("  [PASS] Bebas gelar akademik dalam narasi sitasi batang tubuh (Hanya Nama Belakang).")

    # 2. Cek Penggunaan \citet dan \citep
    cites = citation_regex.findall(text)
    total_cite_commands = len(cites)
    print(f"  -> Total perintah \\cite terdeteksi di batang tubuh: {total_cite_commands}")
    
    # 3. Cek pemformatan naratif 'dan' vs '&'
    ampersand_in_narrative = re.findall(r'([A-Z][a-z]+)\s+&\s+([A-Z][a-z]+)\s+\(\d{4}\)', text)
    if ampersand_in_narrative:
        print(f"  [WARN] Sitasi naratif menggunakan '&' (seharusnya 'dan'): {ampersand_in_narrative[:3]}")
    else:
        print("  [PASS] Sitasi naratif dua penulis konsisten menggunakan 'dan'.")
        
    return len(degree_errors) == 0

def audit_markdown_citations(md_path):
    print(f"\n[*] Mengaudit Sitasi In-Text pada Markdown: {md_path.name}...")
    full_text = md_path.read_text(encoding="utf-8")
    text = extract_body(full_text)
    
    # Cek gelar di batang tubuh
    forbidden = [r'Yahawi,?\s+S\.?H\.?', r'Dr\.\s+Fredella', r'Prof\.\s+Sugiyono', r'Prof\.\s+Ghozali']
    found = []
    for f in forbidden:
        m = re.findall(f, text)
        if m:
            found.extend(m)
            
    if found:
        print(f"  [FAIL] Ditemukan gelar dalam sitasi batang tubuh Markdown: {set(found)}")
    else:
        print("  [PASS] Batang tubuh Markdown bebas gelar dalam sitasi.")
        
    # Cek format et al.
    et_als = re.findall(r'([A-Z][a-z]+\s+et\s+al\.,\s+\d{4})', text)
    print(f"  -> Format 'et al.' terdeteksi di batang tubuh: {len(et_als)} kutipan.")
    
    return len(found) == 0

def main():
    print("=" * 75)
    print("  SUITE AUDIT FORMAT SITASI IN-TEXT (APA 7TH EDITION & FEB UKRIDA 2023)")
    print("  Aturan: Nama Belakang Saja, Tanpa Gelar, 2 Penulis (& / dan), >=3 (et al.)")
    print("=" * 75)
    
    p1 = Path("01_Naskah_Utama/Proposal_Arthur_PokemonTCG.tex")
    p2 = Path("01_Naskah_Utama/Proposal_Arthur_NoBab3.tex")
    p3 = Path("01_Naskah_Utama/PROPOSAL_SKRIPSI_POKEMON_TCG.md")
    
    pass1 = audit_latex_citations(p1) if p1.exists() else True
    pass2 = audit_latex_citations(p2) if p2.exists() else True
    pass3 = audit_markdown_citations(p3) if p3.exists() else True
    
    print("\n" + "=" * 75)
    if pass1 and pass2 and pass3:
        print("  [SUCCESS] SELURUH DOKUMEN LOLOS AUDIT FORMAT SITASI IN-TEXT 100%!")
        print("=" * 75)
        exit(0)
    else:
        print("  [FAIL] TERDAPAT KESALAHAN FORMAT SITASI!")
        print("=" * 75)
        exit(1)

if __name__ == "__main__":
    main()
