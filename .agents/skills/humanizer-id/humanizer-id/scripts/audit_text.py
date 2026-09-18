#!/usr/bin/env python3
"""Non-mutating editorial cues and lexical preservation checks; Python stdlib only.

No authorship inference, semantic-equivalence claim, or automatic rewriting.
"""
import argparse
from collections import Counter
import json
from pathlib import Path
import re
import sys


PATTERNS = [
    ("H01", r"\b(?:tonggak (?:penting|revolusioner)|terobosan revolusioner|mengubah paradigma)\b", "Periksa bukti dampak; ungkapan ini mungkin tepat dalam konteks."),
    ("H02", r"\b(?:para ahli|banyak penelitian|berbagai penelitian|penelitian menunjukkan)\b", "Periksa sumber dan cakupan atribusi di konteks sekitar."),
    ("H03", r"\b(?:solusi sempurna|sangat inovatif|revolusioner|game.changing|cutting.edge)\b", "Periksa apakah pujian mempunyai kriteria dan bukti."),
    ("H04", r"\b(?:di era (?:digital|modern)|seiring (?:dengan )?perkembangan zaman|dalam rangka|penting untuk (?:dicatat|diketahui))\b", "Periksa apakah pembuka memuat informasi yang diperlukan."),
    ("H05", r"\b(?:sebagai (?:sebuah )?(?:model bahasa|AI)|berikut (?:adalah )?versi revisi|semoga (?:ini )?membantu|tentu[!,] saya)\b", "Bedakan artefak percakapan dari kutipan atau pengungkapan AI yang sah."),
    ("H06", "—", "Tanda pisah sah dalam konteks tertentu; periksa fungsi dan frekuensinya."),
    ("H07", r"\*\*[^*\n]+\*\*|\\textbf\{[^{}\n]+\}", "Periksa apakah penekanan membantu struktur atau terlalu sering."),
    ("H09", r"\b(?:masa depan yang (?:lebih )?cerah|membuka peluang yang tak terbatas|potensi yang luar biasa)\b", "Periksa apakah penutup menambah implikasi yang benar-benar didukung."),
    ("H10", r"\b(?:komprehensif|krusial|holistik|transformatif)\b", "Pemicu pembacaan ulang, bukan kata terlarang."),
]


def mask_blocks(text):
    """Mask fenced code and common LaTeX verbatim blocks while retaining offsets."""
    lines = text.splitlines(keepends=True)
    result = []
    fence = None
    fence_len = 0
    verbatim = None
    for line in lines:
        marker = re.match(r"^\s{0,3}(`{3,}|~{3,})(.*)$", line.rstrip("\r\n"))
        begin = re.search(r"\\begin\{(verbatim\*?|lstlisting|minted)\}", line)
        mask = bool(fence or verbatim or marker or begin)
        if fence:
            if marker and marker[1][0] == fence and len(marker[1]) >= fence_len and not marker[2].strip():
                fence = None
        elif verbatim:
            if "\\end{" + verbatim + "}" in line:
                verbatim = None
        elif marker:
            fence, fence_len = marker[1][0], len(marker[1])
        elif begin:
            verbatim = begin[1]
            if "\\end{" + verbatim + "}" in line:
                verbatim = None
        result.append(re.sub(r"[^\r\n]", " ", line) if mask else line)
    return "".join(result)


def scan(text):
    visible = mask_blocks(text)
    findings = []
    for category, pattern, note in PATTERNS:
        for match in re.finditer(pattern, visible, flags=re.IGNORECASE):
            start = match.start()
            findings.append({
                "category": category,
                "line": text.count("\n", 0, start) + 1,
                "column": start - text.rfind("\n", 0, start),
                "text": text[start:match.end()],
                "note": note,
            })
    findings.sort(key=lambda row: (row["line"], row["column"], row["category"]))
    return {
        "mode": "scan", "findings": findings,
        "limit": "Pemicu editorial saja. Tidak mencakup semua kategori, bukan deteksi kepengarangan atau pemeriksaan EYD lengkap.",
    }


TOKEN_PATTERNS = {
    "numbers": r"(?<![\w])[-+−]?\d+(?:[.,]\d+)*(?:[eE][+-]?\d+)?(?:\s*[%‰])?(?![\w])",
    "latex_references": r"\\(?:[A-Za-z]*cite[A-Za-z]*|ref|eqref|autoref|pageref|label|url|href)\*?(?:\[[^\]\n]*\]){0,2}\{[^{}\n]+\}",
    "numeric_citations": r"\[\d+(?:\s*[,;–-]\s*\d+)*\]",
    "urls": r"https?://[^\s<>\]\)}]+",
    "inline_code": r"`[^`\n]+`",
}


def compare(original, revised):
    differences = {}
    for kind, pattern in TOKEN_PATTERNS.items():
        before = Counter(re.findall(pattern, original))
        after = Counter(re.findall(pattern, revised))
        removed = before - after
        added = after - before
        if removed or added:
            differences[kind] = {"removed": dict(removed), "added": dict(added)}
    return {
        "mode": "compare", "differences": differences,
        "manual_semantic_review_required": True,
        "limit": "Perbandingan token saja. Tidak memverifikasi negasi, satuan, pasangan angka, author-year, cakupan sitasi, atau kesetaraan makna.",
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="mode", required=True)
    scanner = commands.add_parser("scan", help="Temukan pemicu editorial untuk diperiksa manusia.")
    scanner.add_argument("file", type=Path)
    comparator = commands.add_parser("compare", help="Bandingkan token terlindungi secara leksikal.")
    comparator.add_argument("original", type=Path)
    comparator.add_argument("revised", type=Path)
    args = parser.parse_args(argv)
    try:
        if args.mode == "scan":
            result = scan(args.file.read_text(encoding="utf-8-sig"))
        else:
            result = compare(args.original.read_text(encoding="utf-8-sig"), args.revised.read_text(encoding="utf-8-sig"))
    except (OSError, UnicodeError) as error:
        parser.error(str(error))
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
