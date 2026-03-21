import os
import json
import time

# [CORE] KERNEL GENIO v46.5 - SOTA DNA
# Global state management and AI model configuration.

CORTEX_FILE = os.path.join("config", "cortex.json")
CONSCIENCIA_FILE = os.path.join("config", "consciencia_global.json")

def get_cortex():
    """Loads the AI Cortex configuration."""
    try:
        if os.path.exists(CORTEX_FILE):
            with open(CORTEX_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
    except: pass
    return {
        "versao": "47.5",
        "hardware_perfil": "NVIDIA RTX",
        "tier_config": {
            "tiers": {
                "elite": "qwen2.5:1.5b",
                "standard": "qwen2.5:1.5b",
                "vision": "ahmadwaqar/smolvlm2-2.2b-instruct"
            }
        }
    }

def consultar_codex(categoria=None, palavra=None):
    """Programmatic access to the SOTA Technical Codex (v47.5)."""
    CODEX_TECNICO = os.path.join("config", "codex_tecnico.json")
    try:
        if os.path.exists(CODEX_TECNICO):
            with open(CODEX_TECNICO, "r", encoding="utf-8") as f:
                data = json.load(f)
                mapping = data.get("registry", {}).get("intent_mapping", [])
                
                for item in mapping:
                    if palavra and item.get("keyword") == palavra:
                        if categoria is None or item.get("category") == categoria:
                            return item
                return None
    except Exception as e:
        print(f"[ERR] Codex API call failed: {e}")
    return None

def carregar_manifesto(caminho):
    """Carrega um manifesto MCP individual para verificação de permissões."""
    try:
        if os.path.exists(caminho):
            with open(caminho, "r", encoding="utf-8") as f:
                return json.load(f)
    except Exception as e:
        print(f"[ERR] Falha ao carregar manifesto {caminho}: {e}")
    return None

def atualizar_consciencia(metricas):
    """Updates the global consciousness status."""
    if not os.path.exists(os.path.dirname(CONSCIENCIA_FILE)):
        os.makedirs(os.path.dirname(CONSCIENCIA_FILE), exist_ok=True)
    
    status = {
        "timestamp": time.time(),
        "metricas": metricas,
        "lock": False
    }
    
    try:
        with open(CONSCIENCIA_FILE, "w", encoding="utf-8") as f:
            json.dump(status, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"[ERR] Failed to update consciousness: {e}")

def chat(prompt, modelo=None, stream=False):
    """Core LLM interaction via Ollama."""
    import requests
    try:
        if modelo is None:
            ctx = get_cortex()
            # Try to get standard model from tier_config
            modelo = ctx.get("tier_config", {}).get("tiers", {}).get("standard", "qwen2.5:1.5b")
            
        url = "http://127.0.0.1:11434/api/generate"
        payload = {"model": modelo, "prompt": prompt, "stream": stream}
        response = requests.post(url, json=payload, timeout=120)
        if response.status_code == 200:
            if stream: return response 
            return response.json().get("response", "")
    except Exception as e:
        return f"Error connecting to Ollama: {e}"
    return "Ollama Unavailable."

# Global system check
if __name__ == "__main__":
    ctx = get_cortex()
    print(f"Cortex Online: {ctx.get('versao')}")
