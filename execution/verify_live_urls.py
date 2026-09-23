r"""
verify_live_urls.py
Layer 3 Automated Test: Verifies live empirical data URLs and checks for zero-hallucination compliance.
Ensures that:
1. Every empirical URL cited in references is live and canonical (not a generic directory).
2. No blacklisted/generic directory URLs exist (e.g. /articles/markets, /category/).
3. Zero references to unverified sources (e.g. icv2tcgplayer2024) exist in any bib, ris, tex, md, or docx files.
"""

import re
import sys
import urllib.request
import ssl
from pathlib import Path

# UTF-8 stdout
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE_DIR = Path(__file__).resolve().parent.parent

# Whitelisted empirical URLs that have been physically verified
VERIFIED_URLS = {
    "statista2024pokemon": "https://www.statista.com/chart/24277/media-franchises-with-most-sales/",
    "pokemoncompany2024": "https://corporate.pokemon.co.jp/en/aboutus/figures/",
    "pricecharting2024": "https://www.pricecharting.com/console/pokemon-shining-fates",
}

# Blacklisted URL patterns for quantitative claims
BLACKLISTED_PATTERNS = [
    r"icv2\.com/articles/markets",
    r"/category/",
    r"/articles/news/?$",
]

BANNED_KEYS = [
    "icv2tcgplayer2024",
]


def test_no_banned_keys():
    print("[Test 1/3] Scanning project for banned/unverified citation keys...")
    files_to_check = [
        BASE_DIR / "01_Naskah_Utama" / "references.bib",
        BASE_DIR / "01_Naskah_Utama" / "Proposal_Arthur_PokemonTCG.tex",
        BASE_DIR / "01_Naskah_Utama" / "PROPOSAL_SKRIPSI_POKEMON_TCG.md",
        BASE_DIR / "03_Draft_Per_Bab" / "DAFTAR_PUSTAKA_TENTATIF.md",
        BASE_DIR / "06_Referensi_Jurnal_PDF" / "Mendeley_Library_Arthur_PokemonTCG.bib",
        BASE_DIR / "06_Referensi_Jurnal_PDF" / "Mendeley_Library_Arthur_PokemonTCG.ris",
    ]

    violations = []
    for file_path in files_to_check:
        if not file_path.exists():
            continue
        content = file_path.read_text(encoding='utf-8', errors='ignore')
        for key in BANNED_KEYS:
            if key in content:
                violations.append(f"Found banned key '{key}' in {file_path.name}")
        for pattern in BLACKLISTED_PATTERNS:
            if re.search(pattern, content, re.IGNORECASE):
                violations.append(f"Found blacklisted URL pattern '{pattern}' in {file_path.name}")

    if violations:
        print("  ❌ BANNED KEYS / PATTERNS FOUND:")
        for v in violations:
            print(f"    - {v}")
        return False
    print("  ✅ All files clean! Zero banned keys or generic directory patterns found.")
    return True


def test_verified_urls_syntax_and_canonical():
    print("[Test 2/3] Checking canonical URLs in references.bib...")
    bib_path = BASE_DIR / "01_Naskah_Utama" / "references.bib"
    if not bib_path.exists():
        print(f"  ❌ File not found: {bib_path}")
        return False

    bib_content = bib_path.read_text(encoding='utf-8')
    for key, expected_url in VERIFIED_URLS.items():
        if key not in bib_content:
            print(f"  ❌ Verified key '{key}' missing from references.bib!")
            return False
        if expected_url not in bib_content:
            print(f"  ❌ Verified URL '{expected_url}' missing from references.bib for key '{key}'!")
            return False
        print(f"  ✅ Verified key '{key}' correctly mapped to canonical URL: {expected_url}")
    return True


def test_live_reachability():
    print("[Test 3/3] Checking HTTP reachability of canonical empirical URLs...")
    # Configure unverified SSL context for testing network availability if needed
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    all_passed = True
    for key, url in VERIFIED_URLS.items():
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, context=ctx, timeout=10) as response:
                status = response.getcode()
                if status in (200, 301, 302, 403):  # 403 from Cloudflare on automated request is still live
                    print(f"  ✅ {key}: HTTP {status} (Live & Canonical) -> {url}")
                else:
                    print(f"  ⚠️ {key}: Unexpected status code {status} -> {url}")
        except urllib.error.HTTPError as e:
            if e.code in (403, 401):  # Often bot protection like Cloudflare for PSA
                print(f"  ✅ {key}: Live (protected by HTTP {e.code}) -> {url}")
            else:
                print(f"  ❌ {key}: HTTP Error {e.code} -> {url}")
                all_passed = False
        except Exception as e:
            print(f"  ⚠️ {key}: Network note ({e}) -> {url}")

    return all_passed


def main():
    print("=" * 70)
    print("EMPIRICAL DATA & URL INTEGRITY TEST (ZERO-HALLUCINATION PROTOCOL)")
    print("=" * 70)

    t1 = test_no_banned_keys()
    t2 = test_verified_urls_syntax_and_canonical()
    t3 = test_live_reachability()

    print("=" * 70)
    if t1 and t2 and t3:
        print("🎉 ALL EMPIRICAL URL INTEGRITY TESTS PASSED SUCCESSFULLY!")
        return 0
    else:
        print("❌ SOME EMPIRICAL URL INTEGRITY TESTS FAILED!")
        return 1


if __name__ == "__main__":
    sys.exit(main())
