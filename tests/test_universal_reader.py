#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test_universal_reader.py Smoke Test para o Arsenal de 20 Formatos.
""" import os
import sys # Adiciona caminhos
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, "src", "agentes", "ativos")) try: from vanguarda_agente_SRC_GL import VanguardaAgente
except ImportError: print("[ERR] Failure ao importar VanguardaAgente.") sys.exit(1) def criar_arquivos_teste(): test_dir = os.path.join(BASE_DIR, "tests", "data_smoke") os.makedirs(test_dir, exist_ok=True) # 1. TXT with open(os.path.join(test_dir, "teste.txt"), "w") as f: f.write("Este um teste de leitura TXT nativa.") # 2. CSV with open(os.path.join(test_dir, "teste.csv"), "w") as f: f.write("id,nome,valor\n1,G nio,Master\n2,Lucas,Elite") # 3. HTML with open(os.path.join(test_dir, "teste.html"), "w") as f: f.write("<html><body><h1>Teste GL</h1><p>Conte do HTML plano.</p></body></html>") # 4. JS (C digo) with open(os.path.join(test_dir, "teste.js"), "w") as f: f.write("function teste() { console.log('Hello GL'); }") return test_dir def rodar_testes(): v = VanguardaAgente() test_dir = criar_arquivos_teste() formatos = ["teste.txt", "teste.csv", "teste.html", "teste.js"] print(f"[LAB] Starting Smoke Test em {test_dir}...") for arquivo in formatos: caminho = os.path.join(test_dir, arquivo) print(f"\n--- Testando: {arquivo} ---") try: res = v.executar({"prompt": "O que tem nesse arquivo?", "arquivo": caminho}) if res.get("status") in ["SUCCESS", "FALLBACK"]: print(f"[OK] Success! Resposta: {res['resposta'][:100]}...") else: print(f"[ERR] Error: {res.get('error')}") except Exception as e: print(f" Failure catastr fica: {e}") if __name__ == "__main__": rodar_testes()
