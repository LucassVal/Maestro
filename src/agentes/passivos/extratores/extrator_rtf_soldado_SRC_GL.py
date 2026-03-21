#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
extrator_rtf_soldado_SRC_GL.py Soldado de extração de RTF.
"""
import os
import sys
from .extrator_base_SRC_GL import ExtratorBase
try:
    from striprtf.striprtf import rtf_to_text
except ImportError:
    rtf_to_text = None

class ExtratorRTF(ExtratorBase):
    def __init__(self):
        super().__init__(nome="ExtratorRTF")

    def executar(self, entrada):
        caminho = entrada.get("caminho")
        valido, msg = self.validar_arquivo(caminho)
        if not valido:
            return {"status": "ERROR", "error": msg}
        if rtf_to_text is None:
            return {"status": "ERROR", "error": "Biblioteca striprtf não instalada."}
        try:
            with open(caminho, "r", encoding="utf-8", errors="ignore") as f:
                rtf_content = f.read()
            texto = rtf_to_text(rtf_content)
            return {
                "status": "SUCCESS",
                "texto": texto,
                "metadados": {"tamanho": len(texto), "formato": "RTF"}
            }
        except Exception as e:
            return {"status": "ERROR", "error": str(e)}

def executar(entrada):
    return ExtratorRTF().executar(entrada)
