#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
testar_agente_visao.py Valida o dos Olhos do G nio.
""" import os
import sys
import json # Adiciona caminhos do projeto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.join(BASE_DIR, "src", "agentes", "passivos", "extratores")) try: from extrator_imagem_soldado_SRC_GL import ExtratorImagem
except ImportError: print("[ERR] Failure ao importar ExtratorImagem. Verifique os caminhos.") sys.exit(1) def testar_visao(): print("[VISION] STARTING SOTA VISION TEST...") extrator = ExtratorImagem() # Criar um placeholder ou usar uma imagem existente se o usu rio tiver (vamos assumir placeholder para fuma a) # Na verdade, o teste real requer uma imagem. Vamos tentar detectar se h alguma imagem no projeto. test_image = os.path.join(BASE_DIR, "parrudo.ico") # Usar o cone como teste de fuma a (embora seja .ico) if os.path.exists(test_image): print(f" Analisando arquivo de teste: {test_image}") resultado = extrator.executar({"caminho": test_image}) if resultado["status"] == "SUCCESS": print("[OK] SUCCESS: Vision operational.") print(f"[NOTE] Descri o: {resultado['texto'][:200]}...") else: print(f"[ERR] ERRO: {resultado.get('error')}") else: print("[WARN] Arquivo de teste 'parrudo.ico' n o encontrado. Teste abortado.") if __name__ == "__main__": testar_visao()
