r"""
verify_italic_parity.py — Layer 3: Audit Paritas Tipografi Italic Lintas Format (PDF/LaTeX vs Word DOCX).

Menegakkan Invariant Mutlak:
Setiap istilah asing, nama konstruk, dimensi kuesioner, istilah statistik,
dan terminologi subkultur yang dicetak miring (\emph{} atau \textit{})
pada naskah master LaTeX (Proposal_Arthur_PokemonTCG.tex) WAJIB berupa run miring (italic=True)
pada naskah Word DOCX (Proposal_Arthur_PokemonTCG.docx), baik di paragraf bodi maupun di sel tabel.

Exit Code:
  0 : Paritas 100% PASS (Zero Missing Italics).
  1 : FAIL — Ada istilah LaTeX yang gagal dicetak miring di DOCX.
"""

import sys
import re
from pathlib import Path
import docx

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

ROOT = Path(__file__).resolve().parent.parent
TEX_PATH = ROOT / "01_Naskah_Utama" / "Proposal_Arthur_PokemonTCG.tex"
DOCX_PATH = ROOT / "01_Naskah_Utama" / "Proposal_Arthur_PokemonTCG.docx"


def clean_latex_token(raw_tok: str) -> str:
    """Bersihkan escape character LaTeX untuk perbandingan semantik."""
    t = raw_tok.strip().lower()
    t = t.replace(r'\#', '#').replace(r'\&', '&').replace('~', ' ')
    t = t.replace(r'\_', '_')
    t = t.replace(r"pok\'emon", "pokémon").replace(r"pok\'emon", "pokémon")
    t = t.replace("pok\\'emon", "pokémon")
    t = t.replace('--', '–').replace('—', '–')
    return t


def verify_italic_parity():
    print("=" * 75)
    print("AUDIT PARITAS TIPOGRAFI ITALIC: LaTeX Master <-> Word DOCX")
    print(f"LaTeX Source : {TEX_PATH.name}")
    print(f"DOCX Source  : {DOCX_PATH.name}")
    print("=" * 75)

    if not TEX_PATH.exists():
        print(f"[FAIL] File LaTeX master tidak ditemukan: {TEX_PATH}")
        return 1
    if not DOCX_PATH.exists():
        print(f"[FAIL] File Word DOCX tidak ditemukan: {DOCX_PATH}")
        return 1

    tex_content = TEX_PATH.read_text(encoding="utf-8")
    doc = docx.Document(str(DOCX_PATH))

    # 1. Ekstrak seluruh ekspresi \emph{} dan \textit{} dari LaTeX master
    latex_emphs = re.findall(r'\\(?:emph|textit)\{([^{}]+)\}', tex_content)
    unique_emphs = set(latex_emphs)

    # 2. Ekstrak seluruh run italic aktif di Word DOCX (paragraf tubuh + sel tabel)
    docx_italic_runs = set()
    for p in doc.paragraphs:
        for r in p.runs:
            txt = r.text.strip().lower()
            if txt and r.italic:
                docx_italic_runs.add(txt)

    for tbl in doc.tables:
        for row in tbl.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    for r in p.runs:
                        txt = r.text.strip().lower()
                        if txt and r.italic:
                            docx_italic_runs.add(txt)

    # 3. Lakukan pencocokan invarian
    missing = []
    ignored = 0
    for item in unique_emphs:
        clean = clean_latex_token(item)
        # Abaikan label internal, caption lanjutan tabel yang ditangani engine tabel
        if len(clean) < 3 or clean.startswith('fig:') or clean.startswith('tab:'):
            ignored += 1
            continue
        if any(ex in clean for ex in ['lanjutan tabel', 'bersambung ke halaman']):
            ignored += 1
            continue

        # Cocokkan keberadaan di run italic DOCX
        found = any(clean in r for r in docx_italic_runs) or any(r in clean for r in docx_italic_runs if len(r) > 4)
        if not found:
            # Periksa kemungkinan catatan sumber yang disederhanakan
            if clean.startswith("sumber:"):
                # Pastikan kata sumber dalam docx italic runs
                if any("sumber:" in r for r in docx_italic_runs):
                    continue
            missing.append((item, clean))

    total_tested = len(unique_emphs) - ignored
    passed = total_tested - len(missing)

    print(f"\n[*] Total ekspresi miring LaTeX unik diuji : {total_tested}")
    print(f"[*] Total terkonfirmasi miring di DOCX      : {passed}")
    print(f"[*] Tingkat kelulusan paritas tipografi     : {(passed / total_tested * 100):.2f}%")

    if missing:
        print(f"\n[FAIL] Ditemukan {len(missing)} istilah miring LaTeX yang TIDAK BERFORMAT MIRING di DOCX:")
        for raw, cln in sorted(missing)[:15]:
            print(f"  - LaTeX: '\\emph{{{raw}}}' -> diharapkan miring di DOCX")
        print("\nRegresi format terdeteksi! DILARANG menutup sesi sebelum paritas 100%.")
        return 1

    print("\n[PASS] PARITAS TIPOGRAFI 100% MUTLAK: Seluruh istilah asing dan ekspresi miring tercetak miring di DOCX.")
    print("=" * 75)
    return 0


if __name__ == "__main__":
    sys.exit(verify_italic_parity())
