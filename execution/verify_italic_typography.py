import re
from pathlib import Path

TERMS = [
    "impulsive buying",
    "hedonic motivation",
    "desire for completeness",
    "speculative motive",
    "self-control",
    "trading card game",
    "booster pack",
    "cross-sectional",
    "purposive sampling",
    "mean-centering",
    "moderated regression analysis",
    "simple slopes",
    "behavioral finance",
    "zeigarnik effect",
    "pseudo-set framing",
    "completing the set effect",
    "card grading",
    "tamper-evident slab"
]

def is_inside_command(text, pos, commands=("\\emph", "\\textit", "\\url", "\\cite", "\\citep", "\\citet", "\\citealp", "\\label", "\\ref")):
    for cmd in commands:
        start = 0
        cmd_open = cmd + "{"
        while True:
            idx = text.find(cmd_open, start)
            if idx == -1 or idx >= pos:
                break
            depth = 1
            i = idx + len(cmd_open)
            while i < len(text) and depth > 0:
                if text[i] == '{':
                    depth += 1
                elif text[i] == '}':
                    depth -= 1
                i += 1
            if idx <= pos < i:
                return True
            start = idx + 1
    return False

def check_latex_italics(tex_path):
    print(f"\n[*] Mengaudit Tipografi Italic pada LaTeX: {tex_path.name}...")
    text = tex_path.read_text(encoding="utf-8")
    
    # Cari awal Bab 1 dan akhir Bab 3
    m_start = re.search(r'\\section\*?\{BAB\s+1', text, re.IGNORECASE)
    start_pos = m_start.start() if m_start else 0
    m_end = re.search(r'\\bibliography\{', text[start_pos:], re.IGNORECASE)
    end_pos = start_pos + m_end.start() if m_end else len(text)
    body = text[start_pos:end_pos]
    
    unitalicized = []
    for term in TERMS:
        pattern = rf'\b{re.escape(term)}\b'
        for m in re.finditer(pattern, body, re.IGNORECASE):
            pos = m.start()
            if not is_inside_command(body, pos):
                snippet = body[max(0, pos-20):min(len(body), m.end()+20)].replace('\n', ' ')
                unitalicized.append((term, snippet.strip()))
                
    if unitalicized:
        print(f"  [WARN] Ditemukan {len(unitalicized)} istilah berpotensi belum di-italic:")
        for t, snip in unitalicized[:5]:
            print(f"    - '{t}' dalam: ...{snip}...")
    else:
        print("  [PASS] 100% istilah kunci bahasa asing telah tercetak miring (\\emph{}).")
        
    return len(unitalicized)

def main():
    print("=" * 75)
    print("  SUITE AUDIT TIPOGRAFI ITALIC ISTILAH ASING (PEDOMAN FEB UKRIDA 2023)")
    print("=" * 75)
    
    p1 = Path("01_Naskah_Utama/Proposal_Arthur_PokemonTCG.tex")
    p2 = Path("01_Naskah_Utama/Proposal_Arthur_NoBab3.tex")
    
    w1 = check_latex_italics(p1) if p1.exists() else 0
    w2 = check_latex_italics(p2) if p2.exists() else 0
    
    print("\n" + "=" * 75)
    if w1 == 0 and w2 == 0:
        print("  [SUCCESS] TIPOGRAFI ITALIC SEMPURNA! SELURUH ISTILAH ASING DICETAK MIRING.")
    else:
        print(f"  [INFO] Total potensi perluasan italic: {w1 + w2} lokasi.")
    print("=" * 75)

if __name__ == "__main__":
    main()
