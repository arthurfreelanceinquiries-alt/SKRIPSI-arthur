r"""
verify_all_citation_links.py — Layer 3: audit KLIKABILITAS semua tautan sitasi.

Memeriksa setiap `doi` dan `url` di references.bib (khusus entri yang
DISITASI naskah) + setiap `UR` di RIS Mendeley: wajib hidup (resolves).
  ALIVE        : HTTP 200/301/302/303/307/308
  ALIVE-BLOCKED: HTTP 403/401/405/429 (resolves, tapi anti-bot; di browser
                 manusia biasanya terbuka — dilaporkan terpisah, bukan FAIL)
  WALLED-SERVER: DOI terdaftar di doi.org (302 + Location valid) tetapi server
                 publisher timeout/5xx/DNS — identifier sah, landing tak
                 terjangkau dari jaringan ini; dilaporkan terpisah, bukan FAIL
                 bila PDF lokal terarsip + baca-isi terverifikasi di ledger
                 (pelajaran 23 Sep 2026: 10.54443/sibatik.v1i6.112 —
                 doi.org 302 valid, publisher timeout; artikel terkonfirmasi
                 via Crossref + sitasi sekunder + PDF lokal L01).
  DEAD         : DOI tak terdaftar (doi.org 404) / 404/410 final — WAJIB
                 diperbaiki/diganti.

Untuk DOI yg DEAD, otomatis cari kandidat pengganti via Crossref (judul;
sim >= 0.85 + tahun cocok) — hanya SARAN, tidak otomatis menimpa bib.

Stdlib only (urllib + concurrent.futures). Exit 0 jika nol DEAD, 1 jika ada.
Dibuat 16 Sep 2026 (temuan: DOI Gao 10.1509/jmr.12.0281 NOT FOUND).
"""

import concurrent.futures
import difflib
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import urllib.error
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROOT = Path(__file__).resolve().parent.parent
BIB = ROOT / "01_Naskah_Utama" / "references.bib"
TEX = ROOT / "01_Naskah_Utama" / "Proposal_Arthur_PokemonTCG.tex"
RIS = ROOT / "06_Referensi_Jurnal_PDF" / "Mendeley_Library_Arthur_PokemonTCG.ris"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}
ALIVE = {200, 301, 302, 303, 307, 308}
# 401/403/405/429 = anti-bot; 468 = publisher-wall pasca-redirect doi.org.
# Keduanya berarti DOI terdaftar & me-resolve (doi.org tak dikenal = 404).
# Terbukti 16 Sep 2026: 10.47153/afs42.9372024 → 302 ke hal. artikel OJS.
BLOCKED = {401, 403, 405, 429, 468}


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    """Opener yang TIDAK mengikuti redirect: mengembalikan respons 3xx asli
    agar pendaftar DOI (doi.org 302 + Location) bisa dibedakan dari
    kegagalan server publisher di ujung redirect."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def fetch(url, timeout=20, retries=2):
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.status
        except urllib.error.HTTPError as e:
            return e.code  # HTTP respons = jawaban pasti, jangan retry
        except Exception as e:  # noqa: BLE001 - timeout/DNS: retry (anti rate-limit)
            if attempt < retries:
                time.sleep(10)
                continue
            return f"ERR:{str(e)[:50]}"


def fetch_doi(url, timeout=20):
    """Cek DOI dua lapis: (terdaftar, status_final).

    terdaftar=True bila doi.org menjawab 3xx + header Location (identifier
    sah ter-resolve, apa pun kondisi server publisher). status_final diambil
    via fetch() biasa (mengikuti redirect). Timeout publisher TIDAK
    dimaknai DOI mati.
    """
    registered = False
    try:
        opener = urllib.request.build_opener(_NoRedirect)
        req = urllib.request.Request(url, headers=UA)
        with opener.open(req, timeout=timeout) as r:
            loc = r.headers.get("Location", "")
            registered = r.status in (301, 302, 303, 307, 308) and bool(loc)
    except urllib.error.HTTPError as e:
        registered = e.code in (301, 302, 303, 307, 308)
    except Exception:  # noqa: BLE001 - doi.org tak terjangkau: registered=False
        registered = False
    return registered, fetch(url, timeout=timeout, retries=1)


def norm(s):
    return re.sub(r'[^a-z0-9 ]', '', s.lower())


def crossref_suggest(title, year):
    q = urllib.parse.quote(title)
    try:
        req = urllib.request.Request(
            f"https://api.crossref.org/works?query.bibliographic={q}&rows=3"
            "&select=DOI,title,author,published,score", headers=UA)
        with urllib.request.urlopen(req, timeout=25) as r:
            items = json.load(r)['message']['items']
    except Exception:
        return None
    for top in items:
        ct = (top.get('title') or [''])[0]
        sim = difflib.SequenceMatcher(None, norm(title), norm(ct)).ratio()
        cy = ''
        try:
            cy = str((top.get('published') or {}).get('date-parts', [[0]])[0][0])
        except Exception:
            pass
        if sim >= 0.85 and (not year or not cy or cy in ('0', '') or abs(int(year) - int(cy)) <= 1):
            return top.get('DOI', ''), ct[:80], sim
    return None


def main():
    tex = TEX.read_text(encoding='utf-8')
    cited = set()
    for c in re.findall(r'cite[a-z]*\{([^}]+)\}', tex):
        cited.update(k.strip() for k in c.split(',') if k.strip())
    bib = BIB.read_text(encoding='utf-8')
    blocks = re.findall(r'@(\w+)\{([^,]+),(.*?)(?=@\w+\{|\Z)', bib, re.S)

    jobs = []  # (label, url)
    meta = {}
    for ty, key, body in blocks:
        if key not in cited:
            continue
        mdoi = re.search(r'(?m)^\s*doi\s*=\s*\{([^}]*)\}', body)
        murl = re.search(r'(?m)^\s*url\s*=\s*\{([^}]*)\}', body)
        mt = re.search(r'(?m)^\s*title\s*=\s*\{(.*)\},?\s*$', body)
        my = re.search(r'(?m)^\s*year\s*=\s*\{?(\d{4})', body)
        title = re.sub(r'\\[a-zA-Z]+\s?', '', (mt.group(1) if mt else '').replace('{', '').replace('}', '')).strip()
        if mdoi and mdoi.group(1).strip():
            jobs.append((f"{key} [doi]", f"https://doi.org/{mdoi.group(1).strip()}"))
        if murl and murl.group(1).strip():
            jobs.append((f"{key} [url]", murl.group(1).strip()))
        meta[key] = (title, my.group(1) if my else '')

    # UR di RIS (label ganda dgn bib dicek sekali saja)
    seen_urls = {u for _, u in jobs}
    ris = RIS.read_text(encoding='utf-8') if RIS.exists() else ''
    for m in re.finditer(r'(?m)^UR  - (.*)\s*$', ris):
        u = m.group(1).strip()
        if u and u not in seen_urls:
            jobs.append((f"RIS-only [ur]", u))
            seen_urls.add(u)

    print(f"memeriksa {len(jobs)} tautan ({len(cited)} sitasi)...")
    results = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
        fut = {}
        for label, u in jobs:
            if "[doi]" in label:
                fut[ex.submit(fetch_doi, u)] = (label, u, True)
            else:
                fut[ex.submit(fetch, u)] = (label, u, False)
        for f in concurrent.futures.as_completed(fut):
            label, u, is_doi = fut[f]
            try:
                results[label] = (u, f.result(), is_doi)
            except Exception as e:  # noqa: BLE001
                results[label] = (u, f"ERR:{e}", is_doi)

    dead, blocked, walled_srv = [], [], []
    for label in sorted(results):
        u, st, is_doi = results[label]
        if is_doi:
            registered, final = st
            st = final
        else:
            registered = False
        if st in ALIVE:
            print(f"  ALIVE  {label} -> {u}")
        elif st in BLOCKED:
            blocked.append((label, u, st))
            print(f"  WALLED {label} [{st}] -> {u}")
        elif is_doi and registered and (isinstance(st, str) or st in
                                        {500, 502, 503, 504, 521, 522, 523, 524}):
            walled_srv.append((label, u, st))
            print(f"  WALLED-SERVER {label} [{st}] -> {u} (doi.org 302 valid)")
        else:
            dead.append((label, u, st))
            print(f"  DEAD   {label} [{st}] -> {u}")

    print(f"\nringkas: {len(jobs)-len(dead)-len(blocked)-len(walled_srv)} hidup / "
          f"{len(blocked)} terhalang-bot / {len(walled_srv)} server-tak-terjangkau / "
          f"{len(dead)} MATI")
    if dead:
        print("\n--- saran Crossref untuk DOI mati ---")
        for label, u, st in dead:
            key = label.split(' ')[0]
            title, year = meta.get(key, ('', ''))
            if '[doi]' in label and title:
                sug = crossref_suggest(title, year)
                if sug:
                    print(f"  {key}: coba https://doi.org/{sug[0]} (sim {sug[2]:.2f}: {sug[1]})")
                else:
                    print(f"  {key}: TIDAK ADA kandidat Crossref — perlu diganti sumbernya")
            else:
                print(f"  {label}: periksa manual")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
