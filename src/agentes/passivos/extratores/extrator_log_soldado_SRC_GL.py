#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
extrator_log_soldado_SRC_GL.py Soldado de extração de Logs.
Realiza uma limpeza e sumarização estruturada.
"""
import os
import sys
import re
from .extrator_base_SRC_GL import ExtratorBase

class ExtratorLog(ExtratorBase):
    def __init__(self):
        super().__init__(nome="ExtratorLog")

    def executar(self, entrada):
        caminho = entrada.get("caminho")
        valido, msg = self.validar_arquivo(caminho)
        if not valido:
            return {"status": "ERROR", "error": msg}
        try:
            with open(caminho, "r", encoding="utf-8", errors="ignore") as f:
                linhas = f.readlines()
            # Lógica de filtragem: remover linhas repetitivas ou focar em erros
            erros = [l for l in linhas if re.search(r"error|fail|critical|exception", l, re.I)]
            contexto = linhas[-50:] # últimas 50 linhas para contexto recente
            texto = "--- RESUMO DE LOGS (DETECÇÃO DE ERROS) ---\n"
            texto += "".join(erros[:20]) + "\n" if erros else "Nenhum erro crítico detectado.\n"
            texto += "--- ULTIMAS 50 LINHAS ---\n"
            texto += "".join(contexto)
            return {
                "status": "SUCCESS",
                "texto": texto,
                "metadados": {"total_linhas": len(linhas), "erros_count": len(erros), "formato": "LOG"}
            }
        except Exception as e:
            return {"status": "ERROR", "error": str(e)}

def executar(entrada):
    return ExtratorLog().executar(entrada)
