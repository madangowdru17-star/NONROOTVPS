import sys
import subprocess
import io
import os
import time
import threading
import sqlite3
import json
from pathlib import Path
from flask import Flask, jsonify

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

from mitmproxy import http
from common.utils import aes_decrypt, encrypt_api, get_available_room, CrEaTe_ProTo
from common.ifix_injector import injector

# ============ RAILWAY CONFIGURATION ============
WEB_PORT = 8080
PROXY_PORT = 8081
DB_PATH = os.getenv('DB_PATH', '/tmp/nonrootvps')

# Create temp directory for Railway persistent storage
Path(DB_PATH).mkdir(parents=True, exist_ok=True)
DB_FILE = os.path.join(DB_PATH, "ifix_data.db")

print(f"[*] Railway Configuration:")
print(f"    - Web Server Port: {WEB_PORT}")
print(f"    - Proxy Port: {PROXY_PORT}")
print(f"    - Database Path: {DB_FILE}")

# ============ FLASK APP ============
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "proxy": "running",
        "mods": "5 active",
        "anti_ban": "7 shields",
        "version": "5.2.0-ULTRA",
        "server": "NONROOTVPS Railway"
    })

@app.route('/version')
def version():
    return jsonify({
        "version": "5.2.0",
        "status": "ok",
        "proxy": "nonrootvps"
    })

@app.route('/ping')
def ping():
    return "pong"

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return jsonify({
        "status": "proxy_running",
        "path": path,
        "message": "NONROOTVPS proxy is active"
    })

# ============ DATABASE FUNCTIONS ============
def init_db():
    conn = sqlite3.connect(DB_FILE, timeout=30.0)
    c = conn.cursor()
    c.execute("PRAGMA journal_mode=WAL;")
    c.execute("CREATE TABLE IF NOT EXISTS authorized_users (user_id TEXT PRIMARY KEY, added_by INTEGER, added_at INTEGER, expires_at INTEGER DEFAULT -1)")
    c.execute("CREATE TABLE IF NOT EXISTS access_whitelist (user_id TEXT PRIMARY KEY, region TEXT, name TEXT, expiry INTEGER)")
    c.execute("CREATE TABLE IF NOT EXISTS session_cache (server_name TEXT, user_id TEXT, last_seen INTEGER, PRIMARY KEY (server_name, user_id))")
    c.execute("CREATE TABLE IF NOT EXISTS mod_logs (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id TEXT, ip TEXT, country TEXT, region TEXT, city TEXT, ts INTEGER, status TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS allowed_channels (channel_id INTEGER PRIMARY KEY)")
    conn.commit()
    conn.close()
    print(f"[✓] Database initialized at {DB_FILE}")

init_db()

SESSION_TTL_SECONDS = 24 * 60 * 60

def is_expiry_valid(expiry_ts) -> bool:
    if not expiry_ts:
        return True
    return int(time.time()) <= int(expiry_ts)

def checkUserAccess(user_id: str) -> bool:
    try:
        conn = sqlite3.connect(DB_FILE, timeout=30.0)
        c = conn.cursor()
        now = int(time.time())

        c.execute("SELECT expires_at FROM authorized_users WHERE user_id=?", (user_id,))
        res = c.fetchone()
        if res:
            expires_at = res[0]
            if expires_at is None or expires_at == -1 or expires_at > now:
                conn.close()
                return True

        c.execute("SELECT expiry FROM access_whitelist WHERE user_id=?", (user_id,))
        res = c.fetchone()
        if res and is_expiry_valid(res[0]):
            conn.close()
            return True

        c.execute("SELECT 1 FROM session_cache WHERE user_id=? AND last_seen >= ?", (user_id, now - SESSION_TTL_SECONDS))
        found = c.fetchone() is not None
        conn.close()
        return found
    except Exception as e:
        print(f"[DB ERROR] checkUserAccess: {e}")
        return False

def cleanup_expired_sessions():
    while True:
        try:
            conn = sqlite3.connect(DB_FILE, timeout=30.0)
            c = conn.cursor()
            now = int(time.time())
            c.execute("DELETE FROM authorized_users WHERE expires_at != -1 AND expires_at < ?", (now,))
            c.execute("DELETE FROM access_whitelist WHERE expiry IS NOT NULL AND expiry < ?", (now,))
            if c.rowcount > 0:
                conn.commit()
                print(f"[*] Auto-removed expired sessions")
            conn.close()
        except Exception as e:
            print(f"[!] Expiry Cleanup Error: {e}")
        time.sleep(60)

def start_subservices():
    return []

# ============ MITMPROXY ============
def start_mitm():
    script_path = os.path.abspath(__file__).replace('\\', '\\\\')
    print(f"[*] Starting Mitmproxy on 0.0.0.0:{PROXY_PORT}")
    subprocess.run([
        sys.executable, "-c",
        f"import sys; from mitmproxy.tools.main import mitmdump; sys.argv = ['mitmdump', '-s', '{script_path}', '-p', '{PROXY_PORT}', '--listen-host', '0.0.0.0', '--set', 'block_global=false', '--set', 'ignore_hosts=^(version|freefiremobile-a|cdp|config|rslw0r|firebase).*']; mitmdump()"
    ])

# ============ MAIN ============
if __name__ == "__main__":
    injector.print_injection_banner()

    print("[*] ═══════════════════════════════════════")
    print("[*] NONROOTVPS - Railway Edition")
    print("[*] Starting services...")
    print("[*] ═══════════════════════════════════════")
    
    # Start cleanup thread
    threading.Thread(target=cleanup_expired_sessions, daemon=True).start()
    
    sub_processes = start_subservices()
    
    # Wait for gunicorn to start (it runs in background)
    time.sleep(3)
    
    print(f"[*] Starting Mitmproxy Interceptor Server on port {PROXY_PORT}...")
    try:
        start_mitm()
    finally:
        for p in sub_processes:
            try:
                p.terminate()
            except Exception:
                pass
