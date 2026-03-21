import os
import sys
import json
import time
import requests
import importlib.util
from datetime import datetime

# Setup paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(BASE_DIR, 'src')
sys.path.append(SRC_DIR)

LOG_FILE = os.path.join(BASE_DIR, '.panda', 'logs', 'mega_audit.log')
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

def log(msg):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {msg}"
    print(line)
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(line + '\n')

def check_ollama():
    log("--- CHECKING OLLAMA MODELS ---")
    try:
        response = requests.get("http://localhost:11434/api/tags")
        if response.status_code == 200:
            models = [m['name'] for m in response.json().get('models', [])]
            log(f"Ollama Online. Models found: {len(models)}")
            required = ['qwen2.5-coder:7b', 'deepseek-r1:7b', 'llama3.2:1b', 'qwen3:latest']
            for r in required:
                status = "OK" if any(r in m for m in models) else "MISSING"
                log(f"  - Model {r}: {status}")
        else:
            log(f"Ollama Status Error: {response.status_code}")
    except Exception as e:
        log(f"Ollama Connection Failed: {str(e)}")

def check_imports(subfolder):
    log(f"--- CHECKING IMPORTS: {subfolder} ---")
    folder_path = os.path.join(SRC_DIR, 'agentes', subfolder)
    if not os.path.exists(folder_path):
        log(f"Folder NOT FOUND: {folder_path}")
        return

    files = [f for f in os.listdir(folder_path) if f.endswith('.py') and not f.startswith('__')]
    for file in files:
        module_name = file[:-3]
        try:
            # Use importlib to avoid side effects if possible
            spec = importlib.util.find_spec(f"agentes.{subfolder}.{module_name}")
            if spec:
                log(f"  - [OK] {file}")
            else:
                log(f"  - [FAIL] {file} (Spec not found)")
        except ImportError as e:
            log(f"  - [ERR] {file}: {str(e)}")
        except Exception as e:
            log(f"  - [ERR] {file}: Unexpected Error")

def check_core():
    log("--- CHECKING CORE COMPONENTS ---")
    core_files = ['regente_sota_CORE_GL', 'kernel_genio_CORE_GL', 'eventos_sistema_CORE_GL', 'metricas_evolucao_CORE_GL']
    for cf in core_files:
        try:
            spec = importlib.util.find_spec(f"core.{cf}")
            if spec:
                log(f"  - [OK] {cf}")
            else:
                log(f"  - [FAIL] {cf}")
        except Exception as e:
            log(f"  - [ERR] {cf}: {str(e)}")

if __name__ == "__main__":
    log("=== GENIO LLM MEGA AUDIT v45.4 STARTING ===")
    check_ollama()
    check_core()
    check_imports('ativos')
    check_imports('passivos')
    log("=== AUDIT COMPLETED ===")
