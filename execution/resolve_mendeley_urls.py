r"""
resolve_mendeley_urls.py — Layer 3: resolve missing Mendeley UR links via Crossref.

For every BibTeX entry cited in Proposal_Arthur_PokemonTCG.tex that has
neither `doi` nor `url`, query api.crossref.org by title and accept the
top-1 hit only if title similarity >= 0.80 and year matches (+/-1 when
both known). Each accepted DOI is live-checked via https://doi.org/.

Output: a RESOLVED_URLS Python dict (reviewed by a human before baking
into generate_mendeley_library.py) plus a per-key report. No file is
modified; research/audit only.

Stdlib only. Exit 0 always (report-only); unresolved keys are listed.
"""

import difflib
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROOT = Path(__file__).resolve().parent.parent
BIB = ROOT / "01_Naskah_Utama" / "references.bib"
TEX = ROOT / "01_Naskah_Utama" / "Proposal_Arthur_PokemonTCG.tex"
UA = {"User-Agent": "SkripsiThesisBot/1.0 (mailto:thesis@local); stdlib-urllib"}


def norm(s):
    return re.sub(r'[^a-z0-9 ]', '', s.lower())


def get(url, timeout=25):
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read()
    except Exception as exc:  # noqa: BLE001 - report-only tool
        return 0, str(exc).encode()


def main():
    tex = TEX.read_text(encoding='utf-8')
    cited = set()
    for c in re.findall(r'cite[a-z]*\{([^}]+)\}', tex):
        cited.update(k.strip() for k in c.split(',') if k.strip())
    bib = BIB.read_text(encoding='utf-8')
    blocks = re.findall(r'@(\w+)\{([^,]+),(.*?)(?=@\w+\{|\Z)', bib, re.S)

    targets = []
    for ty, key, body in blocks:
        if key not in cited:
            continue
        if re.search(r'(?m)^\s*(doi|url)\s*=', body):
            continue
        mt = re.search(r'(?m)^\s*title\s*=\s*\{(.*)\},?\s*$', body)
        my = re.search(r'(?m)^\s*year\s*=\s*\{?(\d{4})', body)
        title = (mt.group(1) if mt else '').replace('{', '').replace('}', '')
        title = re.sub(r'\\[a-zA-Z]+\s?', '', title).strip()
        targets.append((key, ty, title, my.group(1) if my else ''))

    print(f"cited={len(cited)} missing-url={len(targets)}")
    resolved = {}
    for key, ty, title, year in targets:
        if not title:
            print(f"- {key}: NO TITLE -> SKIP")
            continue
        q = urllib.parse.quote(title)
        st, raw = get(f"https://api.crossref.org/works?query.bibliographic={q}&rows=3"
                      f"&select=DOI,title,author,published,score,URL")
        if st != 200:
            print(f"- {key}: crossref HTTP {st} -> SKIP")
            continue
        try:
            items = json.loads(raw.decode('utf-8', 'replace'))['message']['items']
        except Exception:
            print(f"- {key}: bad JSON -> SKIP")
            continue
        if not items:
            print(f"- {key}: no hits -> SKIP")
            continue
        top = items[0]
        ct = (top.get('title') or [''])[0]
        sim = difflib.SequenceMatcher(None, norm(title), norm(ct)).ratio()
        cy = ''
        try:
            cy = str((top.get('published') or {}).get('date-parts', [[0]])[0][0])
        except Exception:
            pass
        year_ok = (not year or not cy or cy == '0' or abs(int(year) - int(cy)) <= 1)
        doi = top.get('DOI', '')
        if sim >= 0.80 and year_ok and doi:
            st2, _ = get(f"https://doi.org/{doi}", timeout=20)
            live = st2 in (200, 301, 302, 303, 307, 308, 403)
            flag = "LIVE" if live else f"DEAD({st2})"
            print(f"+ {key}: sim={sim:.2f} yr={year}/{cy} {flag} https://doi.org/{doi}")
            print(f"    crossref-title: {ct[:90]}")
            if live:
                resolved[key] = f"https://doi.org/{doi}"
        else:
            print(f"- {key}: REJECT sim={sim:.2f} yr={year}/{cy} doi={doi}")
            print(f"    crossref-title: {ct[:90]}")
        time.sleep(1)

    print("\nRESOLVED_URLS = {")
    for k, u in resolved.items():
        print(f'    "{k}": "{u}",')
    print("}")
    print(f"\nresolved {len(resolved)}/{len(targets)}")


if __name__ == "__main__":
    main()
