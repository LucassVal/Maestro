#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from .extrator_base_SRC_GL import ExtratorBase

class ExtratorVideo(ExtratorBase):
    def __init__(self):
        super().__init__(nome="ExtratorVideo")

    def executar(self, entrada):
        caminho = entrada.get("caminho")
        valido, msg = self.validar_arquivo(caminho)
        if not valido:
            return {"status": "ERROR", "error": msg}
        
        return {
            "status": "SUCCESS",
            "conteudo": f"Vídeo detectado: {os.path.basename(caminho)}",
            "metadados": {"formato": "VIDEO"}
        }

def executar(entrada):
    return ExtratorVideo().executar(entrada)
