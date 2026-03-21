#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
extrator_json_soldado_SRC_GL.py Soldado de extração de JSON.
"""
import os
import json
from .extrator_base_SRC_GL import ExtratorBase

class ExtratorJSON(ExtratorBase):
    def __init__(self):
        super().__init__(nome="ExtratorJSON")

    def executar(self, entrada):
        caminho = entrada.get("caminho")
        valido, msg = self.validar_arquivo(caminho)
        if not valido:
            return {"status": "ERROR", "error": msg}
        try:
            with open(caminho, "r", encoding="utf-8") as f:
                dados = json.load(f)
            texto = json.dumps(dados, indent=2, ensure_ascii=False)
            return {
                "status": "SUCCESS",
                "texto": texto,
                "metadados": {"tamanho": len(texto), "formato": "JSON"}
            }
        except Exception as e:
            return {"status": "ERROR", "error": str(e)}

def executar(entrada):
    return ExtratorJSON().executar(entrada)
