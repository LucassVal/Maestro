import os
import sys
import time
import subprocess
from datetime import datetime

# [BOOT] GENIO LAUNCHER v45.3 - GL 
# Persistent Session Logging System

# Environment Configuration
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(ROOT_DIR, ".panda", "logs")
SESSION_LOG = os.path.join(LOG_DIR, "genio_session.log")

# Add src to python path
sys.path.append(os.path.join(ROOT_DIR, "src"))

def setup_logs():
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR, exist_ok=True)
    
    with open(SESSION_LOG, "a", encoding="utf-8") as f:
        f.write(f"\n--- [BOOT] SESSION STARTED: {datetime.now()} ---\n")

def log_session(message):
    timestamp = datetime.now().strftime("%H:%M:%S")
    with open(SESSION_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")

def run_mission(prompt):
    setup_logs()
    log_session(f"MISSION_START: {prompt}")
    
    try:
        # Import Regent only after Path is set
        from src.core import regente_sota_CORE_GL as regente
        
        start_time = time.time()
        print(f"[[GENIO]] Initiating Mission: {prompt}")
        
        # Execute via Regent
        resultado = regente.iniciar_missao(prompt)
        
        duration = time.time() - start_time
        log_session(f"MISSION_COMPLETE: Success in {duration:.2f}s")
        print(f"\n[[SUCCESS]] Mission Completed in {duration:.2f}s")
        print("-" * 50)
        print(resultado)
        print("-" * 50)
        
    except Exception as e:
        log_session(f"ERROR: {str(e)}")
        print(f"[[ERROR]] Launcher failure: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        run_mission(query)
    else:
        print("GENIO LLM v45.3 [ONLINE]")
        print("Usage: python genio_launcher_GL.py \"mission prompt\"")