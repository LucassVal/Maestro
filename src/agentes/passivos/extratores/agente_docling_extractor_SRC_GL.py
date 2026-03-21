#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from .extrator_base_SRC_GL import ExtratorBase

class ExtratorDocling(ExtratorBase):
    def __init__(self):
        super().__init__(nome="ExtratorDocling")

    def executar(self, entrada):
        caminho = entrada.get("caminho")
        valido, msg = self.validar_arquivo(caminho)
        if not valido:
            return {"status": "ERROR", "error": msg}
        
        return {
            "status": "SUCCESS",
            "conteudo": f"Docling extraction simulation for: {os.path.basename(caminho)}",
            "metadados": {"formato": "DOCLING"}
        }

def executar(entrada):
    return ExtratorDocling().executar(entrada)
