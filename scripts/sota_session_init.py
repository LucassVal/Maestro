#!/ pylance
# -*- coding: utf-8 -*-
"""
sota_session_init.py Inicializador de Contexto SOTA v44.0.
Prepara o Antigravity (Gemini) com os documentos fundamentais.
""" import os
import json FILES_TO_READ = [ "GENIO_FILE_REGISTRE_.md", "docs/MANUAL_OLLAMA_SOTA.md", "docs/PROTOCOLO_TRABALHO_SOTA.md", "config/cortex.json", ".panda/memory/daemon_status.json"
] def inicializar_sessao(): print("[BRAIN] INICIANDO SESS O SOTA v44.0...") print("---") contexto_resumo = [] for file in FILES_TO_READ: if os.path.exists(file): print(f"[READ] Lendo: {file}") # Aqui poder amos formatar um prompt gigante, mas o objetivo listar o que a IA DEVE ler. contexto_resumo.append(file) else: print(f"[WARN] Arquivo n o encontrado: {file}") print("\n[OK] Contexto Mapeado. Antigravity est pronto para a miss o.") return contexto_resumo if __name__ == "__main__": inicializar_sessao()
