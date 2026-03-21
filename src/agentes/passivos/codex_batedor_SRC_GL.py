import os
import re
import json
from pathlib import Path

BASE_DIR = Path(".")
CODEX_PATH = BASE_DIR / ".panda" / "codex_tecnico.json"

def extrair_termos_arquivo(caminho):
    termos = set()
    ext = os.path.splitext(caminho)[1]
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            conteudo = f.read()
            if ext == ".py":
                # Captura classes e funções
                encontrados = re.findall(r"(?:class|def)\s+([a-zA-Z0-9_]+)", conteudo)
                for t in encontrados:
                    if not t.startswith("_"):
                        termos.add(t.lower())
            elif ext == ".md":
                # Captura títulos de markdown
                encontrados = re.findall(r"^#+\s+(.+)$", conteudo, re.MULTILINE)
                for t in encontrados:
                    palavras = re.findall(r"\b[a-zA-Z]{4,}\b", t)
                    termos.update([p.lower() for p in palavras])
    except Exception as e:
        print(f"Erro ao ler {caminho}: {e}")
    return termos

def atualizar_codex():
    if not CODEX_PATH.exists():
        CODEX_PATH.parent.mkdir(parents=True, exist_ok=True)
        with open(CODEX_PATH, "w", encoding="utf-8") as f:
            json.dump({}, f)

    with open(CODEX_PATH, "r", encoding="utf-8") as f:
        codex = json.load(f)

    ignore = [".git", "__pycache__", ".panda", ".gemini", "node_modules"]
    novos_termos_detectados = set()
    
    for root, dirs, files in os.walk(str(BASE_DIR / "src")):
        dirs[:] = [d for d in dirs if d not in ignore]
        for file in files:
            if file.endswith((".py", ".md")):
                caminho = os.path.join(root, file)
                novos_termos_detectados.update(extrair_termos_arquivo(caminho))

    termos_existentes = set(codex.keys())
    count = 0
    for termo in novos_termos_detectados:
        if termo not in termos_existentes and len(termo) > 3:
            codex[termo] = "engenheiro"
            count += 1
            
    if count > 0:
        with open(CODEX_PATH, "w", encoding="utf-8") as f:
            json.dump(codex, f, indent=2, ensure_ascii=False)
        return f"[OK] Codex atualizado! {count} novos termos incorporados."
    return "Codex já está em sincronia."

def executar(entrada=None):
    """Interface padrão para o Regente."""
    return atualizar_codex()

if __name__ == "__main__":
    print(executar())
