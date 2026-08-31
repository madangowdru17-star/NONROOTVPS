import sys
import subprocess
import io
import os
import time
import threading
import sqlite3
import copy
import json
import re
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

from mitmproxy import http
from common.utils import aes_decrypt, encrypt_api, get_available_room, CrEaTe_ProTo
from common.ifix_injector import injector

# Railway Environment Variables
RAILWAY_PORT = int(os.getenv('PORT', 8089))
RAILWAY_HOST = os.getenv('RAILWAY_HOST', '0.0.0.0')
DB_PATH = os.getenv('DB_PATH', '/tmp/nonrootvps')

# Create temp directory for Railway persistent storage
Path(DB_PATH).mkdir(parents=True, exist_ok=True)
DB_FILE = os.path.join(DB_PATH, "ifix_data.db")

print(f"[*] Railway Configuration:")
print(f"    - Listen Host: {RAILWAY_HOST}")
print(f"    - Listen Port: {RAILWAY_PORT}")
print(f"    - Database Path: {DB_FILE}")

def start_subservices():
    return []

CHECK_INTERVAL = 1
SESSION_TTL_SECONDS = 24 * 60 * 60
FILE = "ifix.config.json"

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

def is_expiry_valid(expiry_ts) -> bool:
    if not expiry_ts: return True # Permanent
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
    """Background task to remove expired sessions from the database."""
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

def start_mitm():
    script_path = os.path.abspath(__file__).replace('\\', '\\\\')
    print(f"[*] Starting Mitmproxy on {RAILWAY_HOST}:{RAILWAY_PORT}")
    subprocess.run([
        sys.executable, "-c",
        f"import sys; from mitmproxy.tools.main import mitmdump; sys.argv = ['mitmdump', '-s', '{script_path}', '-p', '{RAILWAY_PORT}', '--listen-host', '{RAILWAY_HOST}', '--set', 'block_global=false', '--set', 'ignore_hosts=^(version|freefiremobile-a|cdp|config|rslw0r|firebase).*']; mitmdump()"
    ])

if __name__ == "__main__":
    # Display iFix Injection Engine Startup Banner & Hook Status
    injector.print_injection_banner()

    print("[*] ═══════════════════════════════════════")
    print("[*] NONROOTVPS - Railway Edition")
    print("[*] Starting services...")
    print("[*] ═══════════════════════════════════════")
    
    threading.Thread(target=cleanup_expired_sessions, daemon=True).start()
    
    sub_processes = start_subservices()
    
    try:
        start_mitm()
    finally:
        for p in sub_processes:
            try:
                p.terminate()
            except Exception:
                pass
