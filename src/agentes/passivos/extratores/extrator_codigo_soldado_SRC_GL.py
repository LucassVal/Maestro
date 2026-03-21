#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from .extrator_base_SRC_GL import ExtratorBase

class ExtratorCodigo(ExtratorBase):
    def __init__(self):
        super().__init__(nome="ExtratorCodigo")

    def executar(self, entrada):
        caminho = entrada.get("caminho")
        valido, msg = self.validar_arquivo(caminho)
        if not valido:
            return {"status": "ERROR", "error": msg}

        try:
            with open(caminho, "r", encoding="utf-8", errors="ignore") as f:
                conteudo = f.read()
            
            ext = os.path.splitext(caminho)[1].lower()
            return {
                "status": "SUCCESS",
                "conteudo": conteudo,
                "metadados": {"extensao": ext, "formato": "CODE"}
            }
        except Exception as e:
            return {"status": "ERROR", "error": str(e)}

def executar(entrada):
    return ExtratorCodigo().executar(entrada)
