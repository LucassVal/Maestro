#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
extrator_txt_soldado_SRC_GL.py Soldado de extração de Texto Puro.
"""
import os
from .extrator_base_SRC_GL import ExtratorBase

class ExtratorTXT(ExtratorBase):
    def __init__(self):
        super().__init__(nome="ExtratorTXT")

    def executar(self, entrada):
        caminho = entrada.get("caminho")
        valido, msg = self.validar_arquivo(caminho)
        if not valido:
            return {"status": "ERROR", "error": msg}
        try:
            with open(caminho, "r", encoding="utf-8", errors="ignore") as f:
                texto = f.read()
            return {
                "status": "SUCCESS",
                "texto": texto,
                "metadados": {"tamanho": len(texto), "formato": "TXT"}
            }
        except Exception as e:
            return {"status": "ERROR", "error": str(e)}

def executar(entrada):
    return ExtratorTXT().executar(entrada)
