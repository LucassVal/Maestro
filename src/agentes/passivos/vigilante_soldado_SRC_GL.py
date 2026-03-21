import socket
import os
import shutil
import json
import time

# [VISION] SOLDADO VIGILANTE v1.1 (ZERO-DEPENDENCY)
# Focado em conectividade e integridade infraestrutural usando apenas BUILT-INS.

def testar_ping(host, porta, timeout=2):
    """Verifica se um serviço está ouvindo em determinado host/porta."""
    try:
        with socket.create_connection((host, porta), timeout=timeout):
            return True
    except:
        return False

def verificar_saude_sistema():
    """Executa o 'Check-up' completo usando apenas bibliotecas nativas."""
    # [SAVE] Disco (Built-in em Python 3.3+)
    try:
        usage = shutil.disk_usage(".")
        percentual_disco = (usage.used / usage.total) * 100
        livre_gb = usage.free / (1024**3)
    except:
        percentual_disco = 0
        livre_gb = 0
        
    status = {
        "ollama": testar_ping("127.0.0.1", 11434),
        "mentor_ws": testar_ping("127.0.0.1", 9812),
        "disco": {
            "percentual": round(percentual_disco, 2),
            "livre_gb": round(livre_gb, 2)
        },
        "memoria": "N/A (Requer psutil)",
        "timestamp": time.time()
    }
    print(f"[[VISION]] Vigilante SOTA: Ollama({'[OK]' if status['ollama'] else '[ERR]'}) | Mentor({'[OK]' if status['mentor_ws'] else '[ERR]'}) | Disco({status['disco']['percentual']}% ocupado)")
    return status

def verificar_integridade_arquivos(arquivos_criticos=None):
    """Verifica se arquivos vitais existem e não estão vazios."""
    if not arquivos_criticos:
        arquivos_criticos = [
            "config/cortex.json", 
            "src/core/classificador_roteamento_SRC_GL.py", 
            "src/agentes/passivos/soldados.py"
        ]
    problemas = []
    for arq in arquivos_criticos:
        if not os.path.exists(arq):
            problemas.append(f"AUSENTE: {arq}")
        elif os.path.getsize(arq) == 0:
            problemas.append(f"CORROMPIDO (Vazio): {arq}")
    return problemas

def executar(entrada=None):
    """Interface padrão para o Regente."""
    saude = verificar_saude_sistema()
    erros = verificar_integridade_arquivos()
    if erros:
        return f"Vigilante detectou problemas: {erros}"
    return f"Vigilante Online. Ollama: {'OK' if saude['ollama'] else 'OFF'}"

if __name__ == "__main__":
    print(executar())
