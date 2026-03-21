import os
import json
import time

# [CORE] EVENT SYSTEM v46.5 - AUDIT READY
# Global registry for AI actions and system states.

LOG_FILE = os.path.join(".panda", "logs", "eventos.json")

def registrar_evento(tipo, missao_id, dados, **kwargs):
    """Registers a system event with millisecond precision."""
    if not os.path.exists(os.path.dirname(LOG_FILE)):
        os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    
    evento = {
        "timestamp": time.time(),
        "data": time.strftime("%Y-%m-%d %H:%M:%S"),
        "tipo": tipo,
        "missao_id": missao_id,
        "dados": dados
    }
    
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(evento, ensure_ascii=False) + "\n")
            
        # Session Persistence for Lucas (Phase 108)
        session_log = os.path.join(".panda", "logs", "genio_session.log")
        with open(session_log, "a", encoding="utf-8") as f:
            f.write(f"[{evento['data']}] {tipo} | {missao_id}: {str(dados)[:200]}\n")
            
    except Exception as e:
        print(f"[ERR] Event logging failure: {e}")

def obter_cronologia(missao_id=None):
    """Retrieves event history, optionally filtered by mission ID."""
    if not os.path.exists(LOG_FILE): return []
    eventos = []
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            for line in f:
                if not line.strip(): continue
                evt = json.loads(line)
                if not missao_id or evt.get("missao_id") == missao_id:
                    eventos.append(evt)
    except: pass
    return eventos

def limpar_historico():
    """Wipes the event log."""
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)