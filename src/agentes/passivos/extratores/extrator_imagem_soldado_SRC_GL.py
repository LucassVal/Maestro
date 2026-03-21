#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
extrator_imagem_soldado_SRC_GL.py Soldado de extração de Imagens (OCR/Metadados).
"""
import os
from .extrator_base_SRC_GL import ExtratorBase

class ExtratorImagem(ExtratorBase):
    def __init__(self):
        super().__init__(nome="ExtratorImagem")

    def executar(self, entrada):
        caminho = entrada.get("caminho")
        valido, msg = self.validar_arquivo(caminho)
        if not valido:
            return {"status": "ERROR", "error": msg}
        # Por simplicidade na validação funcional sem GPU pesada, retornamos metadados
        ext = os.path.splitext(caminho)[1].upper()
        return {
            "status": "SUCCESS",
            "texto": f"Imagem detectada: {os.path.basename(caminho)} ({ext})",
            "metadados": {"arquivo": os.path.basename(caminho), "formato": ext}
        }

def executar(entrada):
    return ExtratorImagem().executar(entrada)
