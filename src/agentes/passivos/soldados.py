import os
import json
import glob
import shutil
import time
import subprocess
import tempfile
import urllib.request
import hashlib

# [MISSION] SOLDADOS NATIVOS v2.0 - ELITE SQUAD
# Core passive functions (Zero VRAM)
from src.agentes.passivos.terminal_soldier_SOTA_v45 import terminal_soldier_SOTA as terminal_soldado_SRC_GL
from src.agentes.passivos.openvsx_soldado_SRC_GL import openvsx_soldado_SRC_GL

def ler_arquivo(caminho, **kwargs):
    """Reads a text file."""
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error: {e}"

def escrever_arquivo(caminho, conteudo, **kwargs):
    """Writes content to a file."""
    try:
        with open(caminho, 'w', encoding='utf-8') as f:
            f.write(conteudo)
            return "Success"
    except Exception as e:
        return f"Error: {e}"

def executar_codigo(codigo, timeout=10, **kwargs):
    """Executes Python code safely."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write(codigo)
        tmpname = f.name
    try:
        res = subprocess.run(['python', tmpname], capture_output=True, text=True, timeout=timeout)
        return {
            "stdout": res.stdout,
            "stderr": res.stderr,
            "exit_code": res.returncode
        }
    except subprocess.TimeoutExpired:
        return {"error": "Timeout", "stdout": "", "stderr": "Execution exceeded time limit."}
    finally:
        if os.path.exists(tmpname):
            try: os.unlink(tmpname)
            except: pass

# Cache Configuration
CACHE_DIR = os.path.join(".panda", "cache", "pesquisa")
CACHE_DURACAO_HORAS = 24

def _salvar_cache(chave, dados):
    if not os.path.exists(CACHE_DIR): os.makedirs(CACHE_DIR, exist_ok=True)
    caminho = os.path.join(CACHE_DIR, f"{chave}.json")
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump({"timestamp": time.time(), "dados": dados}, f, ensure_ascii=False)

def _carregar_cache(chave, max_age_horas=CACHE_DURACAO_HORAS):
    caminho = os.path.join(CACHE_DIR, f"{chave}.json")
    if not os.path.exists(caminho): return None
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            cache = json.load(f)
        if time.time() - cache["timestamp"] > max_age_horas * 3600: return None
        return cache["dados"]
    except: return None

def pesquisar_web(query, max_resultados=5, usar_cache=True, **kwargs):
    """Web search via DuckDuckGo with automatic cache."""
    if usar_cache:
        chave = hashlib.md5(query.encode()).hexdigest()
        cache = _carregar_cache(chave)
        if cache: return cache

    try:
        url = f"https://api.duckduckgo.com/?q={urllib.parse.quote(query)}&format=json&no_html=1&skip_disambig=1"
        req = urllib.request.Request(url, headers={"User-Agent": "ParrudoBot/1.0"})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            resultados = []
            
            if data.get("AbstractText"):
                resultados.append({"titulo": data.get("Heading", "Summary"), "link": data.get("AbstractURL", ""), "snippet": data.get("AbstractText")})
            
            for topic in data.get("RelatedTopics", [])[:max_resultados]:
                if isinstance(topic, dict) and "Text" in topic:
                    resultados.append({"titulo": "Related Topic", "link": topic.get("FirstURL", ""), "snippet": topic.get("Text")})
            
            if not resultados: resultados = [{"titulo": "No results", "link": "", "snippet": "No direct information found."}]
            
            if usar_cache: _salvar_cache(chave, resultados)
            return resultados
    except Exception as e:
        return [{"titulo": "Error", "link": "", "snippet": f"Connection failure: {e}"}]

def listar_arquivos(pasta=".", extensao="*", **kwargs):
    """Lists files in a folder with extension filter."""
    padrao = os.path.join(pasta, f"*.{extensao}") if extensao != "*" else os.path.join(pasta, "*")
    return glob.glob(padrao)

def info_sistema(**kwargs):
    """Returns basic system info."""
    import platform
    return {
        "os": platform.system(),
        "node": platform.node(),
        "arch": platform.machine()
    }

# Soldier Mapping
FUNCOES_SOLDADO = {
    "ler_arquivo": ler_arquivo,
    "escrever_arquivo": escrever_arquivo,
    "listar_arquivos": listar_arquivos,
    "info_sistema": info_sistema,
    "validar_json": json.loads,
    "executar_codigo": executar_codigo,
    "pesquisar_web": pesquisar_web,
    "terminal": lambda cmd: terminal_soldado_SRC_GL.executar(cmd),
    "openvsx": lambda query: openvsx_soldado_SRC_GL.buscar_extensao(query)
}
