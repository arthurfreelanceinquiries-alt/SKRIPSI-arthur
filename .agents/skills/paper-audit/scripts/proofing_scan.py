#!/usr/bin/env python3
"""Read-only heuristic candidate scan; findings always require human review.

Text inputs use UTF-8 (an optional BOM is accepted). PDF extraction requires
the optional pypdf package. No commands or links in input files are executed.
Exit status: 0 = complete scan, 2 = failed or incomplete extraction/input.
Candidate presence alone does not change the exit status.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys
from typing import Any


TEXT_SUFFIXES = {".txt", ".md", ".tex", ".bib"}
URL = re.compile(r"(?:https?://|www\.)\S+", re.IGNORECASE)
# Runs of at least three dots and the Unicode ellipsis are intentionally
# excluded (including sentence-ending four-dot ellipses). Decimal points are
# single dots, so they cannot match this rule.
DUPLICATE_PUNCTUATION = re.compile(r"[,;:!?](?:[,;:!?]|(?<=,)[ \t]+,)+|(?<!\.)\.{2}(?!\.)")
PROGRAMMING_NAMES = re.compile(
    r"\b(?:Javascript|Typescript|Github|Gitlab|Nodejs|Numpy|Scipy|Pytorch|Tensorflow)\b"
)
# This is deliberately a shallow, same-line detector, not a TeX/math parser.
ARCTAN_RATIO = re.compile(
    r"(?<![\w])(?:\\)?(?:arctan|atan)\s*(?:\\left\s*)?"
    r"(?:\([^\n)]{0,120}/[^\n)]{0,120}\)"
    r"|\{[^\n}]{0,120}/[^\n}]{0,120}\}"
    r"|(?:\(\s*)?\\(?:d?frac)\s*\{[^{}\n]+\}\s*\{[^{}\n]+\})",
    re.IGNORECASE,
)


def diagnostic(severity: str, code: str, message: str, page: int | None = None) -> dict[str, Any]:
    item: dict[str, Any] = {"severity": severity, "code": code, "message": message}
    if page is not None:
        item["page"] = page
    return item


def read_segments(path: Path) -> tuple[list[tuple[int | None, str]], list[dict[str, Any]]]:
    """Return (page, extracted text) segments and all extraction diagnostics."""
    diagnostics: list[dict[str, Any]] = []
    if not path.is_file():
        return [], [diagnostic("error", "file_missing", "Input is not an existing regular file.")]
    suffix = path.suffix.lower()
    if suffix in TEXT_SUFFIXES:
        try:
            content = path.read_text(encoding="utf-8-sig")
        except (OSError, UnicodeError) as exc:
            return [], [diagnostic("error", "text_read_failed", f"Cannot read UTF-8 text: {exc}")]
        if not content.strip():
            diagnostics.append(diagnostic("warning", "text_empty", "Input contains no non-whitespace text."))
        return [(None, content)], diagnostics
    if suffix != ".pdf":
        return [], [diagnostic("error", "unsupported_format", "Supported formats: .txt, .md, .tex, .bib, .pdf.")]
    try:
        from pypdf import PdfReader
    except ImportError:
        return [], [diagnostic("error", "pdf_dependency_missing", "PDF scanning requires the optional pypdf package; no PDF text was scanned.")]
    try:
        reader = PdfReader(str(path))
        page_count = len(reader.pages)
    except Exception as exc:
        return [], [diagnostic("error", "pdf_open_failed", f"Cannot open PDF: {exc}")]
    segments = []
    if page_count == 0:
        diagnostics.append(diagnostic("warning", "pdf_no_pages", "PDF contains no pages to scan."))
    for index in range(page_count):
        page_number = index + 1
        try:
            content = reader.pages[index].extract_text()
            if content is not None and not isinstance(content, str):
                raise TypeError("PDF extractor returned a non-text value")
        except Exception as exc:
            diagnostics.append(diagnostic("warning", "pdf_page_extraction_failed", f"Page text extraction failed: {exc}", page_number))
            continue
        if not content or not content.strip():
            diagnostics.append(diagnostic("warning", "pdf_page_empty", "No text extracted from this page; visual/OCR review may be needed.", page_number))
            continue
        segments.append((page_number, content))
    return segments, diagnostics


def line_candidates(line: str, programming_capitalization: bool) -> list[dict[str, Any]]:
    """Return source-ordered candidates, masking URLs without shifting columns."""
    masked = URL.sub(lambda match: " " * len(match.group()), line)
    rules = [
        ("duplicate_punctuation", DUPLICATE_PUNCTUATION,
         "Repeated punctuation may be intentional; inspect the surrounding text."),
        ("arctan_ratio", ARCTAN_RATIO,
         "Check the intended angle range, denominator-zero case, and quadrant handling. A ratio inside arctan may be correct; do not automatically replace it with atan2."),
    ]
    if programming_capitalization:
        rules.append(("programming_capitalization", PROGRAMMING_NAMES,
                      "Check the intended product/library spelling and local style; capitalization varies with context."))
    candidates = []
    for rule, pattern, message in rules:
        for match in pattern.finditer(masked):
            start = max(0, match.start() - 60)
            end = min(len(line), match.end() + 60)
            candidates.append({
                "kind": "candidate", "rule": rule, "column": match.start() + 1,
                "matched_text": line[match.start():match.end()],
                "context": line[start:end], "message": message,
            })
    return sorted(candidates, key=lambda item: (item["column"], item["rule"]))


def scan_file(path: str | Path, max_hits: int = 100, programming_capitalization: bool = False) -> dict[str, Any]:
    """Scan an input without altering it; max_hits limits output, not detection."""
    if max_hits < 0:
        raise ValueError("max_hits must be nonnegative")
    path = Path(path)
    segments, diagnostics = read_segments(path)
    candidates: list[dict[str, Any]] = []
    total = 0
    for page, content in segments:
        for line_number, line in enumerate(content.splitlines(), start=1):
            for candidate in line_candidates(line, programming_capitalization):
                total += 1
                if len(candidates) < max_hits:
                    candidate["line"] = line_number
                    if page is not None:
                        candidate["page"] = page
                    candidates.append(candidate)
    status = "error" if any(item["severity"] == "error" for item in diagnostics) else "incomplete" if diagnostics else "complete"
    return {
        "schema_version": 1,
        "input": str(path),
        "status": status,
        "notice": "All findings are heuristic candidates, not proof of errors. A complete scan is not a clean bill of health. PDF line/column locations refer to extracted text, not visual layout.",
        "max_hits": max_hits,
        "programming_capitalization": programming_capitalization,
        "total_candidates": total,
        "returned_candidates": len(candidates),
        "truncated": total > len(candidates),
        "omitted_candidates": total - len(candidates),
        "candidates": candidates,
        "diagnostics": diagnostics,
    }


def nonnegative_int(value: str) -> int:
    try:
        result = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("must be a nonnegative integer") from exc
    if result < 0:
        raise argparse.ArgumentTypeError("must be a nonnegative integer")
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--max-hits", type=nonnegative_int, default=100,
                        help="Maximum displayed candidates; 0 reports counts only (default: 100).")
    parser.add_argument("--json", action="store_true", help="Emit structured results including diagnostics.")
    parser.add_argument("--programming-capitalization", action="store_true",
                        help="Include optional product/library capitalization candidates.")
    args = parser.parse_args(argv)
    result = scan_file(args.input, args.max_hits, args.programming_capitalization)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Candidate scan: {result['status']}; {result['total_candidates']} candidate(s), "
              f"{result['returned_candidates']} shown, {result['omitted_candidates']} omitted by --max-hits.")
        print(result["notice"])
        for item in result["candidates"]:
            location = f"page {item['page']}, " if "page" in item else ""
            location += f"line {item['line']}, column {item['column']}"
            print(f"CANDIDATE [{item['rule']}] {location}: {item['matched_text']!r}")
            print(f"  {item['message']}")
        for item in result["diagnostics"]:
            location = f" (page {item['page']})" if "page" in item else ""
            print(f"{item['severity'].upper()} [{item['code']}]{location}: {item['message']}", file=sys.stderr)
    return 0 if result["status"] == "complete" else 2


if __name__ == "__main__":
    raise SystemExit(main())
