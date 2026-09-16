r"""
mendeley_connector.py — Layer 3: konektor Mendeley API (OAuth2 + push library).

Alur pakai (sekali saja):
  1. Daftar aplikasi di https://dev.mendeley.com/ (login akun Mendeley/Elsevier
     milikmu) -> catat Client ID + Client Secret. Redirect URI aplikasi HARUS:
     http://localhost:5000/oauth/callback
  2. Salin `.env.example` menjadi `.env`, isi 3 nilai itu.
  3. py execution/mendeley_connector.py --auth     (buka browser, login, izinkan)
  4. py execution/mendeley_connector.py --status   (cek koneksi + hitung dokumen)
  5. py execution/mendeley_connector.py --dry-run  (pratinjau 55 payload, tanpa kirim)
  6. py execution/mendeley_connector.py --push      (buat dokumen yg belum ada)

Catatan jujur: Mendeley TIDAK punya endpoint "import RIS". Push = membuat
55 record dokumen satu-per-satu via POST /documents. Judul yang sudah ada
di library dilewati (cocok string judul). Token disimpan di token.json
(sudah di-.gitignore; JANGAN pernah commit).

Stdlib only (urllib + http.server). Dibuat 16 Sep 2026.
"""

import http.server
import json
import os
import re
import sys
import threading
import urllib.parse
import urllib.request
import urllib.error
import webbrowser
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROOT = Path(__file__).resolve().parent.parent
RIS = ROOT / "06_Referensi_Jurnal_PDF" / "Mendeley_Library_Arthur_PokemonTCG.ris"
ENV_FILE = ROOT / ".env"
TOKEN_FILE = ROOT / "token.json"

AUTH_URL = "https://api.mendeley.com/oauth/authorize"
TOKEN_URL = "https://api.mendeley.com/oauth/token"
API = "https://api.mendeley.com"
DOC_CT = "application/vnd.mendeley-document.1+json"
CALLBACK_PORT = 5000
CALLBACK_PATH = "/oauth/callback"
REDIRECT_URI = f"http://localhost:{CALLBACK_PORT}{CALLBACK_PATH}"

RIS_TO_MENDELEY_TYPE = {
    "JOUR": "journal", "BOOK": "book", "CONF": "conference_proceedings",
    "RPRT": "report", "THES": "thesis", "GEN": "generic",
}

# Header ala-browser: api.mendeley.com dijaga Cloudflare yang menolak
# UA default "Python-urllib" (error 1010). Header ini dipakai di semua
# request token maupun API.
BROWSER_HEADERS = {
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/126.0.0.0 Safari/537.36"),
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
}


def post_form(url, fields):
    body = urllib.parse.urlencode(fields).encode()
    req = urllib.request.Request(url, data=body, method="POST", headers={
        **BROWSER_HEADERS, "Content-Type": "application/x-www-form-urlencoded",
    })
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def load_env():
    env = {}
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text(encoding='utf-8').splitlines():
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                k, v = line.split('=', 1)
                env[k.strip()] = v.strip().strip('"').strip("'")
    for k in ("MENDELEY_CLIENT_ID", "MENDELEY_CLIENT_SECRET", "MENDELEY_REDIRECT_URI"):
        if k in os.environ:
            env[k] = os.environ[k]
    env.setdefault("MENDELEY_REDIRECT_URI", REDIRECT_URI)
    return env


def load_token():
    if TOKEN_FILE.exists():
        return json.loads(TOKEN_FILE.read_text(encoding='utf-8'))
    return {}


def save_token(tok):
    TOKEN_FILE.write_text(json.dumps(tok, indent=2), encoding='utf-8')
    print(f"token tersimpan: {TOKEN_FILE.name} (di-.gitignore, jangan commit)")


def api_request(method, path, token, body=None, accept=DOC_CT):
    data = json.dumps(body).encode('utf-8') if body is not None else None
    req = urllib.request.Request(API + path, data=data, method=method, headers={
        **BROWSER_HEADERS,
        "Authorization": f"Bearer {token}",
        "Accept": accept,
        "Content-Type": DOC_CT if body is not None else accept,
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            raw = r.read().decode('utf-8', 'replace')
            return r.status, (json.loads(raw) if raw.strip() else None)
    except urllib.error.HTTPError as e:
        try:
            detail = e.read().decode('utf-8', 'replace')[:500]
        except Exception:
            detail = ''
        return e.code, {"_error": detail}


def refresh_token(env, tok):
    return post_form(TOKEN_URL, {
        "grant_type": "refresh_token",
        "refresh_token": tok["refresh_token"],
        "redirect_uri": env["MENDELEY_REDIRECT_URI"],
        "client_id": env["MENDELEY_CLIENT_ID"],
        "client_secret": env["MENDELEY_CLIENT_SECRET"],
    })


def cmd_auth(env):
    if not env.get("MENDELEY_CLIENT_ID") or not env.get("MENDELEY_CLIENT_SECRET"):
        print("[ERROR] .env belum diisi. Salin .env.example -> .env lalu isi "
              "MENDELEY_CLIENT_ID dan MENDELEY_CLIENT_SECRET dari https://dev.mendeley.com/")
        return 1
    code_holder = {}

    class H(http.server.BaseHTTPRequestHandler):
        def do_GET(self):  # noqa: N802 - http.server convention
            q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            if self.path.startswith(CALLBACK_PATH) and 'code' in q:
                code_holder['code'] = q['code'][0]
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.end_headers()
                self.wfile.write("<h1>Otorisasi berhasil. Kembali ke terminal.</h1>".encode())
            else:
                err = q.get('error', ['ditolak'])[0]
                code_holder['error'] = err
                self.send_response(400)
                self.end_headers()
                self.wfile.write(f"<h1>Otorisasi gagal: {err}</h1>".encode())

        def log_message(self, *a):
            pass

    srv = http.server.HTTPServer(("127.0.0.1", CALLBACK_PORT), H)
    threading.Thread(target=srv.handle_request, daemon=True).start()
    params = urllib.parse.urlencode({
        "client_id": env["MENDELEY_CLIENT_ID"],
        "redirect_uri": env["MENDELEY_REDIRECT_URI"],
        "response_type": "code",
        "scope": "all",
    })
    url = f"{AUTH_URL}?{params}"
    print("Membuka browser untuk otorisasi Mendeley...")
    print("Jika browser tidak terbuka, buka manual:\n  " + url)
    webbrowser.open(url)
    print("Menunggu callback di http://localhost:5000/oauth/callback ... (maks 120 dtk)")
    srv.timeout = 120
    srv.handle_request()
    srv.server_close()
    if 'error' in code_holder or 'code' not in code_holder:
        print(f"[ERROR] {code_holder.get('error', 'timeout / tidak ada kode')}")
        return 1
    try:
        tok = post_form(TOKEN_URL, {
            "grant_type": "authorization_code",
            "code": code_holder['code'],
            "redirect_uri": env["MENDELEY_REDIRECT_URI"],
            "client_id": env["MENDELEY_CLIENT_ID"],
            "client_secret": env["MENDELEY_CLIENT_SECRET"],
        })
    except urllib.error.HTTPError as e:
        print(f"[ERROR] tukar kode gagal HTTP {e.code}: {e.read().decode('utf-8', 'replace')[:300]}")
        return 1
    save_token(tok)
    print("[PASS] otorisasi OK. Lanjut: --status")
    return 0


def parse_ris(path):
    text = path.read_text(encoding='utf-8')
    recs, cur = [], {}
    for line in text.splitlines():
        if len(line) < 6 or '  - ' not in line[:6]:
            continue
        tag, val = line[:2].strip(), line[6:].strip()
        if tag == 'TY':
            cur = {'TY': [val]}
        elif tag == 'ER':
            recs.append(cur)
            cur = {}
        else:
            cur.setdefault(tag, []).append(val)
    return recs


def split_author(a):
    a = a.strip().rstrip(',')
    if ',' in a:
        fam, giv = [x.strip() for x in a.split(',', 1)]
        return {"first_name": giv, "last_name": fam} if giv else {"last_name": fam}
    parts = a.split()
    if len(parts) == 1 or (parts[0][0].isupper() and len(parts[0]) > 3 and parts[0].lower()
                           not in ('the', 'van', 'von', 'de')) and len(parts) <= 3 and a[0].isupper() \
            and not any(c.islower() for c in parts[0]):
        return {"last_name": a}  # korporat / inisial murni
    if len(parts) == 1:
        return {"last_name": a}
    return {"first_name": " ".join(parts[:-1]), "last_name": parts[-1]}


def ris_to_payload(r):
    ty = (r.get('TY', ['GEN'])[0] or 'GEN').upper()
    p = {"type": RIS_TO_MENDELEY_TYPE.get(ty, "generic")}
    if r.get('TI'):
        p["title"] = r['TI'][0]
    if r.get('AU'):
        p["authors"] = [split_author(a) for a in r['AU']]
    if r.get('PY'):
        p["year"] = int(re.search(r'\d{4}', r['PY'][0]).group(0)) if re.search(r'\d{4}', r['PY'][0]) else None
        if p["year"] is None:
            del p["year"]
    if r.get('JO'):
        p["source"] = r['JO'][0]
    elif r.get('BT'):
        p["source"] = r['BT'][0]
    if r.get('PB'):
        p["publisher"] = r['PB'][0]
    if r.get('CY'):
        p["city"] = r['CY'][0]
    if r.get('VL'):
        p["volume"] = r['VL'][0]
    if r.get('IS'):
        p["issue"] = r['IS'][0]
    if r.get('SP'):
        p["pages"] = r['SP'][0] + (f"-{r['EP'][0]}" if r.get('EP') else "")
    if r.get('UR'):
        p["websites"] = r['UR'][:3]
    ids = {}
    if r.get('DO'):
        ids["doi"] = r['DO'][0]
    if ids:
        p["identifiers"] = ids
    return p


def existing_titles(token):
    titles = set()
    path = "/documents?limit=500&view=bib"
    while path:
        st, data = api_request("GET", path, token)
        if st != 200 or not isinstance(data, list):
            print(f"[WARN] list dokumen HTTP {st}; lewati deteksi duplikat.")
            return None
        for d in data:
            if d.get('title'):
                titles.add(d['title'].strip().lower())
        path = None  # 500 cukup untuk library ini; paginasi Link diabaikan eksplisit
    return titles


def cmd_status(env, tok):
    if not tok.get('access_token'):
        print("[ERROR] belum ada token. Jalankan --auth dulu.")
        return 1
    for acc in ("application/vnd.mendeley-profiles.1+json", DOC_CT, "application/json"):
        st, me = api_request("GET", "/profiles/me", tok["access_token"], accept=acc)
        if st == 200:
            break
    if st != 200:
        print(f"[ERROR] /profiles/me HTTP {st}: {me}")
        return 1
    print(f"[PASS] terhubung sebagai: {me.get('display_name', me.get('email', '?'))}")
    st2, docs = api_request("GET", "/documents?limit=1&view=bib", tok["access_token"])
    print(f"      list dokumen: HTTP {st2}")
    return 0


def cmd_push(env, tok, dry, limit=None):
    if not RIS.exists():
        print(f"[ERROR] RIS tidak ada: {RIS}")
        return 1
    recs = parse_ris(RIS)
    print(f"RIS: {len(recs)} record")
    if dry:
        print("--- DRY-RUN: 3 payload pertama (tidak dikirim) ---")
        for r in recs[:3]:
            print(json.dumps(ris_to_payload(r), ensure_ascii=False, indent=1)[:900])
        types = {}
        for r in recs:
            t = RIS_TO_MENDELEY_TYPE.get((r.get('TY', ['GEN'])[0] or 'GEN').upper(), 'generic')
            types[t] = types.get(t, 0) + 1
        print("distribusi type:", types)
        nolink = [r.get('ID', ['?'])[0] for r in recs if not r.get('UR')]
        print("tanpa websites:", nolink if nolink else "NIHIL")
        return 0
    if not tok.get('access_token'):
        print("[ERROR] belum ada token. Jalankan --auth dulu.")
        return 1
    known = existing_titles(tok["access_token"])
    made, skipped, failed = 0, 0, []
    for r in recs[:limit] if limit else recs:
        title = (r.get('TI', [''])[0] or '').strip()
        if known is not None and title.lower() in known:
            skipped += 1
            continue
        st, resp = api_request("POST", "/documents", tok["access_token"], ris_to_payload(r))
        if st in (200, 201):
            made += 1
            if known is not None:
                known.add(title.lower())
        else:
            failed.append((r.get('ID', ['?'])[0], st, str(resp)[:200]))
    print(f"Hasil: {made} dibuat, {skipped} sudah-ada(dilewati), {len(failed)} gagal")
    for f in failed[:10]:
        print("  GAGAL:", f)
    return 0 if not failed else 1


def cmd_sync_links(env, tok, dry=False):
    """PATCH websites+identifiers dokumen yg judulnya cocok RIS (tanpa buat baru)."""
    if not RIS.exists():
        print(f"[ERROR] RIS tidak ada: {RIS}")
        return 1
    recs = parse_ris(RIS)
    st, docs = api_request("GET", "/documents?limit=500&view=bib", tok["access_token"])
    if st != 200 or not isinstance(docs, list):
        print(f"[ERROR] list dokumen HTTP {st}")
        return 1
    by_title = {}
    for d in docs:
        if d.get('id') and d.get('title'):
            by_title[d['title'].strip().lower()] = d['id']
    upd, skip, fail = 0, 0, []
    for r in recs:
        title = (r.get('TI', [''])[0] or '').strip()
        did = by_title.get(title.lower())
        key = r.get('ID', ['?'])[0]
        if not did:
            skip += 1
            continue
        body = {}
        if r.get('UR'):
            body["websites"] = r['UR'][:3]
        if r.get('DO'):
            body["identifiers"] = {"doi": r['DO'][0]}
        if not body:
            skip += 1
            continue
        if dry:
            upd += 1
            continue
        st2, resp = api_request("PATCH", f"/documents/{did}", tok["access_token"], body)
        if st2 in (200, 201):
            upd += 1
        else:
            fail.append((key, st2, str(resp)[:200]))
    mode = "DRY-RUN" if dry else "HASIL"
    print(f"{mode}: {upd} link diupdate, {skip} dilewati (tak cocok/tanpa link), {len(fail)} gagal")
    for f in fail[:10]:
        print("  GAGAL:", f)
    return 0 if not fail else 1


def cmd_prune(env, tok, dry=False):
    """Hapus dokumen cloud yg judulnya tak ada di RIS (entri basi pasca-ganti sumber)."""
    if not RIS.exists():
        print(f"[ERROR] RIS tidak ada: {RIS}")
        return 1
    want = set()
    for r in parse_ris(RIS):
        if r.get('TI'):
            want.add(r['TI'][0].strip().lower())
    st, docs = api_request("GET", "/documents?limit=500&view=bib", tok["access_token"])
    if st != 200 or not isinstance(docs, list):
        print(f"[ERROR] list dokumen HTTP {st}")
        return 1
    stale = [(d['id'], d.get('title', '?')) for d in docs
             if d.get('id') and (d.get('title') or '').strip().lower() not in want]
    if dry:
        print(f"DRY-RUN: {len(stale)} entri basi akan dihapus:")
        for _, t in stale[:10]:
            print(f"  - {t[:80]}")
        return 0
    fails = 0
    for did, t in stale:
        st2, _ = api_request("DELETE", f"/documents/{did}", tok["access_token"])
        if st2 not in (200, 204):
            fails += 1
            print(f"  GAGAL hapus [{st2}]: {t[:70]}")
        else:
            print(f"  dihapus: {t[:70]}")
    print(f"HASIL: {len(stale)-fails} dihapus, {fails} gagal")
    return 0 if not fails else 1


def main(argv):
    if len(argv) < 2 or argv[1] in ('-h', '--help'):
        print(__doc__)
        return 0
    env = load_env()
    cmd = argv[1]
    if cmd == '--auth':
        return cmd_auth(env)
    tok = load_token()
    if cmd == '--status':
        return cmd_status(env, tok)
    if cmd == '--dry-run':
        return cmd_push(env, tok, dry=True)
    if cmd == '--push':
        limit = int(argv[2].split('=')[1]) if len(argv) > 2 and argv[2].startswith('--limit=') else None
        return cmd_push(env, tok, dry=False, limit=limit)
    if cmd == '--sync-links':
        return cmd_sync_links(env, tok, dry='--dry' in argv)
    if cmd == '--prune':
        return cmd_prune(env, tok, dry='--dry' in argv)
    print(f"perintah tak dikenal: {cmd} (lihat --help)")
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
