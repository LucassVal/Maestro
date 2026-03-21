#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import json
from .extrator_base_SRC_GL import ExtratorBase

try:
    import yaml
except ImportError:
    yaml = None

class ExtratorYAML(ExtratorBase):
    def __init__(self):
        super().__init__(nome="ExtratorYAML")

    def executar(self, entrada):
        caminho = entrada.get("caminho")
        valido, msg = self.validar_arquivo(caminho)
        if not valido:
            return {"status": "ERROR", "error": msg}
        
        if not yaml:
            return {"status": "ERROR", "error": "Biblioteca pyyaml não instalada."}

        try:
            with open(caminho, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
            return {
                "status": "SUCCESS",
                "conteudo": json.dumps(data, indent=2),
                "metadados": {"formato": "YAML"}
            }
        except Exception as e:
            return {"status": "ERROR", "error": str(e)}

def executar(entrada):
    return ExtratorYAML().executar(entrada)
