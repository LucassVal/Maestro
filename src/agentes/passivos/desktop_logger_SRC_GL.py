# Desktop Logger Soldado - SOTA v46.2
import os
from datetime import datetime

LOG_FILE = os.path.join(".panda", "logs", "system.log")
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

def log_connection(source, target, payload, status, latency=0):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] [CONN] {source} -> {target} | STATUS: {status} | LAT: {latency}ms | DATA: {str(payload)[:100]}"
    print(log_line)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_line + "\n")

def executar(entrada):
    msg = entrada.get("prompt", "Evento genérico")
    log_connection("AGENT_CMD", "SYSTEM", msg, "OK")
    return {"status": "ok", "log_saved": True, "file": LOG_FILE}
