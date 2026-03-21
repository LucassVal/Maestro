#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
testar_extratores.py Valida o do Arsenal de Extra o.
""" import os
import sys # Caminhos
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.join(BASE_DIR, "src", "agentes", "passivos", "extratores")) try: from fabrica_extratores_SRC_GL import FabricaExtratores
except ImportError: print("[ERR] Error ao importar FabricaExtratores.") sys.exit(1) def criar_fixtures(): fix_dir = os.path.join(BASE_DIR, "tests", "fixtures") os.makedirs(fix_dir, exist_ok=True) files = { "doc.xml": "<root><data>Teste XML</data></root>", "query.sql": "SELECT * FROM usuarios WHERE id = 1;", "config.yaml": "projeto: Genio\nversao: 40.0", "doc.rtf": "{\\rtf1\\ansi Teste RTF}", "script.py": "print('Hello World')", "app.log": "2026-03-20 INFO: Sistema iniciado\n2026-03-20 ERROR: Failure cr tica detectada", "data.csv": "col1,col2\nval1,val2" } for name, content in files.items(): with open(os.path.join(fix_dir, name), "w", encoding="utf-8") as f: f.write(content) return fix_dir def rodar_testes(): fix_dir = criar_fixtures() print(f"[LAB] Testando Arsenal de Extra o em {fix_dir}...") for arquivo in os.listdir(fix_dir): caminho = os.path.join(fix_dir, arquivo) print(f"\n Testando arquivo: {arquivo}") try: extrator_classe = FabricaExtratores.obter_extrator(caminho) if not extrator_classe: print(f"[WARN] Nenhum extrator encontrado para {arquivo}") continue extrator = extrator_classe() res = extrator.executar({"caminho": caminho}) if res["status"] == "SUCCESS": print(f"[OK] Success: {res.get('metadados')}") print(f" Preview: {res['texto'][:50]}...") else: print(f"[ERR] Error: {res.get('error')}") except Exception as e: print(f" Failure: {e}") if __name__ == "__main__": rodar_testes()
