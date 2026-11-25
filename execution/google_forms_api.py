#!/usr/bin/env python3
"""
google_forms_api.py
Direct Google Forms API integration for Arthur Reezan's Thesis Survey.
Handles OAuth2 PKCE/Code flow, fetching forms, and batchUpdate via forms.googleapis.com.
"""

import sys
import os
import json
import time
import argparse
import urllib.request
import urllib.parse
import hashlib
import base64
import secrets
from http.server import HTTPServer, BaseHTTPRequestHandler
import webbrowser

CREDENTIALS_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "credentials.json")
TOKEN_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".tmp", "forms_token.json")

# Default fallback credentials (can be overridden by credentials.json, CLI args, or env)
DEFAULT_CLIENT_ID = "264649752574-2ikp96mvk6q0t9lv321tppjqcb88nl9j.apps.googleusercontent.com"
DEFAULT_CLIENT_SECRET = ""
SCOPES = "https://www.googleapis.com/auth/forms.body"
REDIRECT_PORT = 8085
REDIRECT_URI = f"http://localhost:{REDIRECT_PORT}/oauth2callback"

def load_oauth_client():
    """Loads Client ID and Client Secret from credentials.json, env, or defaults."""
    client_id = os.environ.get("GOOGLE_CLIENT_ID")
    client_secret = os.environ.get("GOOGLE_CLIENT_SECRET")

    if client_id:
        return client_id, client_secret or ""

    if os.path.exists(CREDENTIALS_FILE):
        try:
            with open(CREDENTIALS_FILE, "r", encoding="utf-8") as f:
                creds = json.load(f)
            data = creds.get("installed") or creds.get("web") or creds
            cid = data.get("client_id")
            csec = data.get("client_secret", "")
            if cid:
                print(f"Kredensial dimuat dari: {CREDENTIALS_FILE}")
                return cid, csec
        except Exception as e:
            print(f"[WARN] Gagal membaca credentials.json: {e}")

    return DEFAULT_CLIENT_ID, DEFAULT_CLIENT_SECRET

class OAuthCallbackHandler(BaseHTTPRequestHandler):
    auth_code = None

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)

        if "code" in params:
            OAuthCallbackHandler.auth_code = params["code"][0]
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"""
            <html>
            <head><title>Otentikasi Berhasil</title></head>
            <body style="font-family:sans-serif; text-align:center; padding:50px;">
                <h2 style="color:#2e7d32;">&#10004; Otentikasi Google Forms API Berhasil!</h2>
                <p>Anda dapat menutup tab ini dan kembali ke terminal / Antigravity.</p>
            </body>
            </html>
            """)
        else:
            error = params.get("error", ["Unknown error"])[0]
            self.send_response(400)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(f"<h3>Gagal otentikasi: {error}</h3>".encode("utf-8"))

    def log_message(self, format, *args):
        # Mute standard HTTP logging to console
        pass


def get_stored_token():
    if not os.path.exists(TOKEN_FILE):
        return None
    try:
        with open(TOKEN_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        # Check expiry
        if data.get("expires_at", 0) > time.time() + 60:
            return data.get("access_token")
        # Try refresh if refresh_token available
        if "refresh_token" in data:
            refreshed = refresh_access_token(data["refresh_token"])
            if refreshed:
                return refreshed
    except Exception as e:
        print(f"[WARN] Error reading token: {e}")
    return None


def refresh_access_token(refresh_token):
    print("Memperbarui token akses Google...")
    client_id, client_secret = load_oauth_client()
    url = "https://oauth2.googleapis.com/token"
    payload = urllib.parse.urlencode({
        "client_id": client_id,
        "client_secret": client_secret,
        "refresh_token": refresh_token,
        "grant_type": "refresh_token"
    }).encode("utf-8")

    req = urllib.request.Request(url, data=payload, method="POST")
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            data["refresh_token"] = refresh_token
            data["expires_at"] = time.time() + data.get("expires_in", 3600)
            os.makedirs(os.path.dirname(TOKEN_FILE), exist_ok=True)
            with open(TOKEN_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
            return data["access_token"]
    except Exception as e:
        print(f"[ERROR] Gagal refresh token: {e}")
        return None


def authenticate():
    token = get_stored_token()
    if token:
        print("Token Google Forms API aktif ditemukan.")
        return token

    print("Memulai alur otentikasi OAuth2 Google Forms API...")
    client_id, client_secret = load_oauth_client()

    # Generate PKCE verifier & challenge
    verifier = secrets.token_urlsafe(64)
    digest = hashlib.sha256(verifier.encode('utf-8')).digest()
    challenge = base64.urlsafe_b64encode(digest).decode('utf-8').rstrip('=')

    auth_params = {
        "client_id": client_id,
        "redirect_uri": REDIRECT_URI,
        "response_type": "code",
        "scope": SCOPES,
        "code_challenge": challenge,
        "code_challenge_method": "S256",
        "access_type": "offline",
        "prompt": "consent"
    }
    auth_url = "https://accounts.google.com/o/oauth2/v2/auth?" + urllib.parse.urlencode(auth_params)

    server = HTTPServer(("localhost", REDIRECT_PORT), OAuthCallbackHandler)
    server.timeout = 180  # 3 minutes

    print("\n" + "="*70, flush=True)
    print("SILAKAN KLIK LINK DI BAWAH INI UNTUK OTORISASI GOOGLE FORMS API:", flush=True)
    print(auth_url, flush=True)
    print("="*70 + "\n", flush=True)

    try:
        webbrowser.open(auth_url)
    except Exception:
        pass

    print("Menunggu persetujuan otentikasi di browser...", flush=True)
    while not OAuthCallbackHandler.auth_code:
        server.handle_request()

    auth_code = OAuthCallbackHandler.auth_code
    server.server_close()

    if not auth_code:
        print("[ERROR] Otentikasi dibatalkan atau waktu habis.")
        sys.exit(1)

    print("Menukarkan kode otorisasi dengan access token...")
    token_url = "https://oauth2.googleapis.com/token"
    token_params = {
        "client_id": client_id,
        "code": auth_code,
        "code_verifier": verifier,
        "grant_type": "authorization_code",
        "redirect_uri": REDIRECT_URI
    }
    if client_secret:
        token_params["client_secret"] = client_secret

    payload = urllib.parse.urlencode(token_params).encode("utf-8")

    req = urllib.request.Request(token_url, data=payload, method="POST")
    try:
        with urllib.request.urlopen(req) as resp:
            token_data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="ignore")
        print(f"[ERROR] HTTP {e.code} saat menukar token: {err_body}", flush=True)
        sys.exit(1)

    token_data["expires_at"] = time.time() + token_data.get("expires_in", 3600)
    os.makedirs(os.path.dirname(TOKEN_FILE), exist_ok=True)
    with open(TOKEN_FILE, "w", encoding="utf-8") as f:
        json.dump(token_data, f, indent=2)

    print("Otentikasi berhasil! Token tersimpan di .tmp/forms_token.json")
    return token_data["access_token"]


def extract_form_id(input_str):
    if not input_str:
        return None
    input_str = input_str.strip()
    # Check if URL
    if "docs.google.com/forms" in input_str:
        # Format: https://docs.google.com/forms/d/{formId}/edit or /viewform
        parts = input_str.split("/")
        if "d" in parts:
            d_idx = parts.index("d")
            if d_idx + 1 < len(parts):
                return parts[d_idx + 1]
    return input_str


def get_form(token, form_id):
    url = f"https://forms.googleapis.com/v1/forms/{form_id}"
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    })
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))


def batch_update_form(token, form_id, requests):
    url = f"https://forms.googleapis.com/v1/forms/{form_id}:batchUpdate"
    payload = json.dumps({"requests": requests}).encode("utf-8")
    req = urllib.request.Request(url, data=payload, method="POST", headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    })
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))


def update_kuesioner(form_id):
    token = authenticate()
    form_id = extract_form_id(form_id)
    print(f"\nMemeriksa Google Form ID: {form_id}...")

    form_data = get_form(token, form_id)
    print(f"Judul Form: {form_data.get('info', {}).get('title', 'Tanpa Judul')}")

    items = form_data.get("items", [])
    print(f"Jumlah elemen ditemukan: {len(items)}")

    requests = []
    found_s3 = None
    found_p5 = None

    for idx, item in enumerate(items):
        title = item.get("title", "")
        # Match S3
        if "S3" in title or ("jakarta barat" in title.lower() and "domisili" in title.lower()):
            found_s3 = (idx, item)
        # Match P5
        if "P5" in title or "kanal" in title.lower() or "tempat pembelian" in title.lower():
            found_p5 = (idx, item)

    # 1. Update S3
    if found_s3:
        idx, item = found_s3
        print(f"Ditemukan S3 di posisi #{idx + 1}: '{item.get('title')}'")
        new_s3_title = "S3. Apakah Anda memiliki MINIMAL SALAH SATU keterkaitan dengan wilayah Jakarta Barat berikut? (Contoh: tinggal/kost di Jakbar, ATAU kuliah/kerja di Jakbar seperti UKRIDA atau Untar, ATAU pernah/rutin berbelanja atau bermain kartu Pokemon di toko/mall/LGS Jakarta Barat)"

        # Prepare update
        q_item = item.get("questionItem", {})
        q = q_item.get("question", {})
        q_id = q.get("questionId")

        req_s3 = {
            "updateItem": {
                "item": {
                    "itemId": item["itemId"],
                    "title": new_s3_title
                },
                "location": {"index": idx},
                "updateMask": "title"
            }
        }
        requests.append(req_s3)
    else:
        print("[WARN] Butir S3 tidak ditemukan berdasarkan judul.")

    # 2. Update P5
    if found_p5:
        idx, item = found_p5
        print(f"Ditemukan P5 di posisi #{idx + 1}: '{item.get('title')}'")
        new_p5_title = "P5. Kanal / Tempat Pembelian Utama yang Paling Sering Anda Gunakan"
        new_options = [
            {"value": "Marketplace daring / E-commerce (Tokopedia, Shopee, Blibli, TikTok Shop, dll.)"},
            {"value": "Toko Hobi Lokal / LGS resmi (Tanjung Duren / Central Park / Mall Taman Anggrek / Puri Indah, dll.)"},
            {"value": "Minimarket / Ritel modern (Indomaret / Alfamart / Gramedia / Toys Kingdom)"},
            {"value": "Transaksi langsung / COD komunitas sesama pemain"},
            {"value": "Lainnya"}
        ]

        q_item = item.get("questionItem", {})
        q = q_item.get("question", {})

        req_p5 = {
            "updateItem": {
                "item": {
                    "itemId": item["itemId"],
                    "title": new_p5_title,
                    "questionItem": {
                        "question": {
                            "questionId": q.get("questionId"),
                            "choiceQuestion": {
                                "type": q.get("choiceQuestion", {}).get("type", "RADIO"),
                                "options": new_options
                            }
                        }
                    }
                },
                "location": {"index": idx},
                "updateMask": "title,questionItem.question.choiceQuestion.options"
            }
        }
        requests.append(req_p5)
    else:
        print("[WARN] Butir P5 tidak ditemukan berdasarkan judul.")

    if not requests:
        print("[ERROR] Tidak ada butir S3 atau P5 yang dapat diperbarui.")
        return False

    print(f"\nMengirim {len(requests)} pembaruan batchUpdate ke Google Forms API...")
    res = batch_update_form(token, form_id, requests)
    print("✅ PEMBARUAN BERHASIL!")
    print(f"URL Edit Forms : https://docs.google.com/forms/d/{form_id}/edit")
    print(f"URL Publik     : {form_data.get('responderUri', f'https://docs.google.com/forms/d/e/{form_id}/viewform')}")
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Google Forms API Manager Arthur Reezan")
    parser.add_argument("action", choices=["auth", "update", "get"], help="Aksi: auth, update, atau get")
    parser.add_argument("--form-id", help="URL Form atau Form ID Google Forms")

    args = parser.parse_args()

    if args.action == "auth":
        authenticate()
    elif args.action == "get":
        if not args.form_id:
            print("Gunakan: python google_forms_api.py get --form-id <ID_ATAU_URL>")
            sys.exit(1)
        token = authenticate()
        fid = extract_form_id(args.form_id)
        f = get_form(token, fid)
        print(json.dumps(f, indent=2))
    elif args.action == "update":
        if not args.form_id:
            print("Gunakan: python google_forms_api.py update --form-id <ID_ATAU_URL>")
            sys.exit(1)
        update_kuesioner(args.form_id)
