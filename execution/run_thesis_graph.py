r"""
run_thesis_graph.py — Orchestrator Layer 3 untuk Universal Thesis Graph of Agents.

Menjalankan gerbang verifikasi A8 (G1-G7) secara berurutan dengan laporan
ringkas. Stdlib-only (tanpa dependensi pihak ketiga), 100% portable.

Pemakaian (dari repo root):
    py execution/run_thesis_graph.py --list
    py execution/run_thesis_graph.py --gate parity
    py execution/run_thesis_graph.py --gate G1,G4,G5
    py execution/run_thesis_graph.py --gate extended --fail-fast
    py execution/run_thesis_graph.py --gate parity --report out.md

Aturan Karpathy yang ditegakkan:
    - SKIP tidak pernah dihitung PASS (dilaporkan eksplisit, exit code != 0).
    - Urutan gerbang deterministik; --fail-fast berhenti di FAIL pertama.
    - Skrip yang hilang = SKIP (bukan PASS), agar tidak ada skipped-check
      yang diklaim lolos.

Exit code: 0 jika semua PASS, 1 jika ada FAIL/SKIP.
"""

import argparse
import subprocess
import sys
from pathlib import Path

# G1-G7 = gerbang parity A8 (wajib). EXT = pemeriksaan tambahan opsional.
GATES = [
    ("G1", "Mendeley 6-way parity", "verify_mendeley_integrity.py", "A8"),
    ("G2", "Live URL zero-hallucination", "verify_live_urls.py", "A8"),
    ("G3", "UKRIDA compliance 7 pilar", "verify_ukrida_compliance.py", "A8"),
    ("G4", "Tipografi DOCX pure-black + TOC", "verify_docx_typography.py", "A8"),
    ("G5", "Paritas PDF<->DOCX", "verify_pdf_docx_parity.py", "A8"),
    ("G6", "Outline heading Word", "verify_word_outline.py", "A8"),
    ("G7", "Sumber buku LibGen", "verify_book_sources.py", "A8"),
]

EXTENDED = [
    ("X1", "Forensik format + typo", "verify_format_and_typos.py", "A8"),
    ("X3", "Header PDF massal", "verify_pdf_headers.py", "A3"),
    ("X4", "Layout section Word", "verify_word_layout.py", "A8"),
]

PRESETS = {
    "parity": [g[0] for g in GATES],
    "extended": [g[0] for g in GATES] + [g[0] for g in EXTENDED],
    "all": [g[0] for g in GATES] + [g[0] for g in EXTENDED],
}


def find_repo_root(start: Path) -> Path:
    """Naik ke atas sampai menemukan 01_Naskah_Utama (repo root)."""
    cur = start.resolve()
    for _ in range(8):
        if (cur / "01_Naskah_Utama").is_dir() and (cur / "execution").is_dir():
            return cur
        if cur.parent == cur:
            break
        cur = cur.parent
    return start.resolve()


def run_gate(script: Path) -> tuple:
    """Jalankan satu skrip verifier. Return (status, tail_output)."""
    if not script.exists():
        return ("SKIP", f"script tidak ditemukan: {script.name}")
    try:
        proc = subprocess.run(
            [sys.executable, str(script)],
            cwd=str(script.parent.parent),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=600,
        )
    except subprocess.TimeoutExpired:
        return ("FAIL", "timeout 600s terlampaui")
    except OSError as exc:
        return ("FAIL", f"gagal dieksekusi: {exc}")
    out = (proc.stdout or "") + (proc.stderr or "")
    tail = "\n".join(out.strip().splitlines()[-5:]) if out.strip() else "(tanpa output)"
    if proc.returncode == 0:
        return ("PASS", tail)
    return ("FAIL", tail)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Orchestrator Graph of Agents A8")
    parser.add_argument("--list", action="store_true", help="tampilkan daftar gerbang")
    parser.add_argument("--gate", default="parity",
                        help="parity|extended|all atau daftar G-ID koma (mis. G1,G4)")
    parser.add_argument("--fail-fast", action="store_true",
                        help="berhenti di FAIL/SKIP pertama")
    parser.add_argument("--report", default=None, help="tulis laporan markdown ke path")
    args = parser.parse_args(argv)

    catalog = {g[0]: g for g in GATES + EXTENDED}

    if args.list:
        print("Gerbang tersedia (A8 parity G1-G7 + extended X1-X4):")
        for gid, name, script, owner in GATES + EXTENDED:
            print(f"  {gid}  {name}  [{script}]  owner={owner}")
        print("Preset: parity | extended | all")
        return 0

    key = args.gate.strip()
    if key in PRESETS:
        selected = PRESETS[key]
    else:
        selected = [s.strip().upper() for s in key.split(",") if s.strip()]
        unknown = [s for s in selected if s not in catalog]
        if unknown:
            print(f"[ERROR] Gerbang tak dikenal: {', '.join(unknown)}", file=sys.stderr)
            return 1

    root = find_repo_root(Path(__file__).parent)
    print(f"Repo root : {root}")
    print(f"Gerbang   : {', '.join(selected)}")
    print("-" * 64)

    results = []
    for gid in selected:
        _, name, script, owner = catalog[gid]
        print(f"[{gid}] {name} ... ", end="", flush=True)
        status, tail = run_gate(root / "execution" / script)
        print(status)
        results.append((gid, name, script, owner, status, tail))
        if args.fail_fast and status != "PASS":
            print(f"fail-fast: berhenti setelah {gid}={status}")
            break

    n_pass = sum(1 for r in results if r[4] == "PASS")
    n_fail = sum(1 for r in results if r[4] == "FAIL")
    n_skip = sum(1 for r in results if r[4] == "SKIP")
    verdict = "PASS" if (n_fail == 0 and n_skip == 0 and len(results) == len(selected)) else "FAIL"

    print("-" * 64)
    for gid, name, script, owner, status, tail in results:
        print(f"  {gid} {status:4s}  {name}")
    print(f"Hasil: {n_pass} PASS / {n_fail} FAIL / {n_skip} SKIP  =>  [{verdict}]")
    if verdict == "FAIL":
        print("BUILD BROKEN (C-PARITY-1/C-MEND-1): dilarang ke pembimbing sebelum 100% PASS.")

    if args.report:
        lines = ["# Laporan Thesis Graph A8", "",
                 f"Repo: `{root}`", f"Gerbang: {', '.join(selected)}", ""]
        for gid, name, script, owner, status, tail in results:
            lines += [f"## {gid} {status} — {name}",
                      f"Script: `execution/{script}` | Owner: {owner}", "",
                      "```", tail, "```", ""]
        lines.append(f"**Verdict: {verdict}** ({n_pass} PASS / {n_fail} FAIL / {n_skip} SKIP)")
        out_path = Path(args.report)
        out_path.write_text("\n".join(lines), encoding="utf-8")
        print(f"Laporan ditulis: {out_path}")

    return 0 if verdict == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
