r"""verify_no_ai_markers.py — Layer 3: audit NOL penanda AI di file final.

Rule: .agents/rules/mandatory_no_ai_markers.md (M1–M9 vs allowlist §3).
Memindai teks render (bukan sumber): DOCX utama + DOCX modular, PDF skripsi,
PDF panduan belajar, PPTX sempro. Exit 0 = PASS, 1 = BUILD DIRTY.
Stdlib + python-docx + python-pptx (+ pypdf bila ada, else pdftotext, else skip).
"""

import re
import shutil
import subprocess
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
MAIN_DOCX = ROOT / "01_Naskah_Utama" / "Proposal_Arthur_PokemonTCG.docx"
MODULAR = ROOT / "01_Naskah_Utama" / "01_Lembar_Persetujuan_Proposal"
THESIS_PDF = ROOT / "01_Naskah_Utama" / "Proposal_Arthur_PokemonTCG.pdf"
GUIDE_PDF = ROOT / "02_Persiapan_Sidang" / "PANDUAN_BELAJAR_PROPOSAL.pdf"
PPTX = (ROOT / "02_Persiapan_Sidang" / "ppt_seminar_proposal"
        / "Proposal_Arthur_Sempro_PokemonTCG.pptx")

# Pola terlarang (M1–M9). Urutan penting: $$ dulu sebelum $.
FORBIDDEN = [
    ("M1-display-math", r"\$\$.+?\$\$"),
    ("M1-inline-math", r"\$[A-Za-z\\][^$\n]{0,120}?\$"),
    ("M1-lone-dollar-letter", r"\$[A-Za-z]"),
    ("M2-latex-cmd", r"\\(alpha|beta|gamma|delta|cdot|times|ge|le|bar|"
     r"begin|end|emph|textbf|caption|label|text|quad|hline|frac|sqrt|sum|"
     r"partial|epsilon|rightarrow|leftarrow|Rightarrow|multicolumn|toprule|"
     r"midrule|bottomrule|centering|small|footnotesize|url|ref|cite)"),
    ("M3-md-bold", r"\*\*.+?\*\*"),
    ("M3-md-italic", r"(?<!\*)\*[A-Za-z][^*]{1,60}?\*(?!\*)"),
    ("M4-backtick", r"`"),
    ("M5-md-header", r"(?m)^#{1,6} "),
    ("M6-checkbox", r"- \[[ x]\]"),
    ("M7-stray-backslash", r"\\(?![nrt])"),
    ("M9-placeholder", r"\{\{.+?\}\}|\[Insert|Lovrem ipsum|Lorem ipsum|\bTODO\b"),
]

# Allowlist §3: (nama, pola) — kecualikan SEBELUM menilai temuan.
ALLOW = [
    ("currency", r"US\$"),
    ("card-code", r"#(SV)?\d+[A-Za-z]?\b"),
    ("rank-num", r"peringkat #\d+"),
    ("centered-star", r"(?<![A-Za-z])[XM]\d?\*(?![A-Za-z*])"),
]

EMOJI_RE = re.compile(
    "[\U0001F300-\U0001FAFF\u2600-\u27BF\u2B00-\u2BFF\uFE0F]")


def _strip_allowed(text):
    clean = text
    for _, pat in ALLOW:
        clean = re.sub(pat, "", clean)
    return clean


def check_text(label, text, formal=True):
    """Kembalikan daftar (marker, konteks). formal=True -> emoji ikut dilarang."""
    hits = []
    clean = _strip_allowed(text)
    for name, pat in FORBIDDEN:
        for m in re.finditer(pat, clean):
            s = max(0, m.start() - 50)
            ctx = clean[s:m.end() + 30].replace("\n", " / ")
            hits.append((name, ctx[:110]))
            if len(hits) > 25:
                return hits
    if formal:
        for m in EMOJI_RE.finditer(text):
            s = max(0, m.start() - 50)
            hits.append(("M8-emoji",
                         text[s:m.end() + 30].replace("\n", " / ")[:110]))
            if len(hits) > 25:
                return hits
    return hits


def docx_text(path):
    import docx
    d = docx.Document(str(path))
    parts = [p.text for p in d.paragraphs]
    for tb in d.tables:
        for r in tb.rows:
            for c in r.cells:
                parts.append(c.text)
    return "\n".join(parts)


def pdf_text(path):
    try:
        from pypdf import PdfReader
        return "\n".join(p.get_text() or "" for p in
                         PdfReader(str(path)).pages)
    except Exception:
        pass
    if shutil.which("pdftotext"):
        import tempfile
        with tempfile.NamedTemporaryFile(suffix=".txt",
                                         delete=False) as tf:
            subprocess.run(["pdftotext", "-layout", str(path), tf.name],
                           check=True)
            return Path(tf.name).read_text(encoding="utf-8",
                                           errors="replace")
    return None


def pptx_text(path):
    from pptx import Presentation
    out = []
    for s in Presentation(str(path)).slides:
        for sh in s.shapes:
            if sh.has_text_frame:
                out.append(sh.text)
            if sh.has_table:
                for r in sh.table.rows:
                    for c in r.cells:
                        out.append(c.text)
    return "\n".join(out)


def main():
    print("=" * 70)
    print("AUDIT: Zero AI Markers (M1-M9 vs allowlist)")
    print("=" * 70)
    total = 0
    targets = [
        ("DOCX utama", MAIN_DOCX, "docx", True),
        ("PDF skripsi", THESIS_PDF, "pdf", True),
        ("PDF panduan", GUIDE_PDF, "pdf", False),
        ("PPTX sempro", PPTX, "pptx", False),
    ]
    if MODULAR.exists():
        for f in sorted(MODULAR.glob("0*.docx")):
            targets.append((f"modular/{f.name}", f, "docx", True))
    for label, path, kind, formal in targets:
        if not path.exists():
            print(f"  [SKIP] {label}: file tak ada")
            continue
        try:
            text = {"docx": docx_text, "pdf": pdf_text,
                    "pptx": pptx_text}[kind](path)
        except Exception as e:  # noqa: BLE001
            print(f"  [SKIP] {label}: {e}")
            continue
        if text is None:
            print(f"  [SKIP] {label}: ekstraktor PDF tak tersedia")
            continue
        hits = check_text(label, text, formal)
        total += len(hits)
        print(f"  [{'FAIL' if hits else 'OK'}] {label} "
              f"({len(text)} chars, {len(hits)} temuan)")
        for name, ctx in hits[:6]:
            print(f"       {name}: ...{ctx}")
    print("=" * 70)
    if total:
        print(f"[BUILD DIRTY] {total} penanda AI — perbaiki di generator.")
        return 1
    print("[PASS] Zero AI markers di semua file final.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
