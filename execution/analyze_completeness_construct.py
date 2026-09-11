"""
Layer 3 Execution Script: Academic Construct Text Mining & Comparative Analysis
Analyzes seminal and empirical papers for terminologies related to "completeness / completing the set".
"""

import os
import re

try:
    import fitz  # PyMuPDF
except ImportError:
    print("PyMuPDF not installed")
    fitz = None

PAPERS_TO_SCAN = [
    {
        "name": "Barasz et al. (2017) - Pseudo-Set Framing",
        "path": "05_Referensi_Jurnal_PDF/02_Jurnal_Teori_&_Metodologi/2017_Barasz_et_al_Pseudo_Set_Framing.pdf"
    },
    {
        "name": "Tan & Adyantari (2024) - Bisma UNEJ",
        "path": "05_Referensi_Jurnal_PDF/01_Empiris_Utama_2021-2025/2024_Tan_Adyantari_Blind_Box_Impulsive_Bisma.pdf"
    },
    {
        "name": "Dewi et al. (2024) - Locus",
        "path": "05_Referensi_Jurnal_PDF/01_Empiris_Utama_2021-2025/2024_Dewi_et_al_Impulse_Buying_Blind_Box_Indonesia_Locus.pdf"
    },
    {
        "name": "Aryadi & Lingga (2024) - Atlantis Press (TCG Jakarta)",
        "path": "05_Referensi_Jurnal_PDF/01_Empiris_Utama_2021-2025/2024_Aryadi_Lingga_TCG_Collectibles_Jakarta_Springer_Atlantis.pdf"
    }
]

KEYWORDS = [
    r"\bcomplet\w*",
    r"\bdesire to complete\b",
    r"\bdesire for completeness\b",
    r"\bcompleting the set\b",
    r"\bset completion\b",
    r"\baversion to incompleteness\b",
    r"\bneed for completion\b",
    r"\bkelengkapan\b",
    r"\bmelengkapi\b",
    r"\bkoleksi\b",
    r"\bclosure\b"
]

def analyze_papers():
    if not fitz:
        return

    print("="*60)
    print("ANALISIS TERMINOLOGI KONSTRUK 'COMPLETENESS / MELENGKAPI'")
    print("="*60)

    for paper in PAPERS_TO_SCAN:
        p_path = paper["path"]
        if not os.path.exists(p_path):
            print(f"File not found: {p_path}")
            continue

        doc = fitz.open(p_path)
        full_text = ""
        for page in doc:
            full_text += page.get_text("text") + "\n"
        doc.close()

        print(f"\nPaper: {paper['name']} (Total Karakter: {len(full_text):,})")
        print("-" * 50)
        
        matches_summary = {}
        for kw in KEYWORDS:
            found = re.findall(kw, full_text, re.IGNORECASE)
            matches_summary[kw] = len(found)
            if len(found) > 0:
                print(f"  Pola '{kw}': {len(found)} kali")

        # Extract context snippets for specific terms
        for target in ["completing the set", "incompleteness", "desire", "set completion", "kelengkapan", "melengkapi"]:
            snippets = []
            for match in re.finditer(rf"[^\.\n]*\b{target}\b[^\.\n]*\.", full_text, re.IGNORECASE):
                snip = match.group(0).strip().replace("\n", " ")
                if len(snip) > 25 and snip not in snippets:
                    snippets.append(snip)
                if len(snippets) >= 3:
                    break
            if snippets:
                print(f"\n  [Contoh Kutipan untuk '{target}']:")
                for s in snippets:
                    print(f"   > \"{s}\"")

if __name__ == "__main__":
    analyze_papers()
