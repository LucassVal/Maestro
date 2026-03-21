#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from .extrator_base_SRC_GL import ExtratorBase

try:
    import pandas as pd
except ImportError:
    pd = None

class ExtratorCSV(ExtratorBase):
    def __init__(self):
        super().__init__(nome="ExtratorCSV")

    def executar(self, entrada):
        caminho = entrada.get("caminho")
        valido, msg = self.validar_arquivo(caminho)
        if not valido:
            return {"status": "ERROR", "error": msg}
        
        if not pd:
            return {"status": "ERROR", "error": "Biblioteca pandas não instalada."}

        try:
            df = pd.read_csv(caminho)
            return {
                "status": "SUCCESS",
                "conteudo": df.to_json(orient="records"),
                "metadados": {"linhas": len(df), "colunas": list(df.columns), "formato": "CSV"}
            }
        except Exception as e:
            return {"status": "ERROR", "error": str(e)}

def executar(entrada):
    return ExtratorCSV().executar(entrada)
