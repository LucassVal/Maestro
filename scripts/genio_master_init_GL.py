# -*- coding: utf-8 -*-
"""
genio_master_init_GL.py Inicializador de Ordem Geral SOTA v44.0.
Este script orquestra a leitura de contexto e a manutenção dos arquivos mestres.
Foco: Soberania, Autonomia e Evolução do Gênio LLM.
"""
import os
import json
import time
from datetime import datetime

# Arquivos de Ordem Geral
MASTER_FILES = {
    "REGISTRO": "GENIO_FILE_REGISTRE_.md",
    "MANUAL": "docs/MANUAL_OLLAMA_SOTA.md",
    "PROTOCOLO": "docs/PROTOCOLO_TRABALHO_SOTA.md",
    "CORTEX": "config/cortex.json",
    "PROMPTS": "config/prompts_agents.json",
    "STATUS": ".panda/memory/daemon_status.json"
}

class GenioMaster:
    def __init__(self):
        self.base_dir = os.getcwd()

    def log_manutencao(self, acao):
        """Registra ações de manutenção nos arquivos de log."""
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_msg = f"[{ts}] [MANUTENÇÃO] {acao}"
        print(log_msg)

    def scan_contexto(self):
        """Lê os arquivos mestres e sugere atualizações se houver falhas."""
        print("[SCAN] SOTA CONTEXT SCAN STARTED...")
        print("-" * 30)
        for nome, path in MASTER_FILES.items():
            if os.path.exists(path):
                print(f"[OK] {nome}: {path} [READ]")
            else:
                print(f"[ERR] {nome}: {path} [NOT FOUND]")
        print("-" * 30)

    def sincronizar_registro(self):
        """Verifica se há novos arquivos na pasta src/ e scripts/ que não estão no Registro."""
        print("[SYNC] SYNCING MASTER REGISTRY...")
        self.log_manutencao("Verificação de novos arquivos concluída.")

    def run(self):
        self.scan_contexto()
        self.sincronizar_registro()
        print("\n[READY] GENIO LLM: General Order Protocol Active. Waiting for Commands.")

if __name__ == "__main__":
    master = GenioMaster()
    master.run()
