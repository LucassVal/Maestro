#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from .extrator_base_SRC_GL import ExtratorBase

class ExtratorAudio(ExtratorBase):
    def __init__(self):
        super().__init__(nome="ExtratorAudio")

    def executar(self, entrada):
        caminho = entrada.get("caminho")
        valido, msg = self.validar_arquivo(caminho)
        if not valido:
            return {"status": "ERROR", "error": msg}
        
        return {
            "status": "SUCCESS",
            "conteudo": f"Áudio detectado: {os.path.basename(caminho)}",
            "metadados": {"formato": "AUDIO"}
        }

def executar(entrada):
    return ExtratorAudio().executar(entrada)
