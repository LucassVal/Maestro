#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from .extrator_base_SRC_GL import ExtratorBase

try:
    import sqlparse
except ImportError:
    sqlparse = None

class ExtratorSQL(ExtratorBase):
    def __init__(self):
        super().__init__(nome="ExtratorSQL")

    def executar(self, entrada):
        caminho = entrada.get("caminho")
        valido, msg = self.validar_arquivo(caminho)
        if not valido:
            return {"status": "ERROR", "error": msg}
        
        try:
            with open(caminho, "r", encoding="utf-8") as f:
                sql = f.read()
            
            if sqlparse:
                formatted = sqlparse.format(sql, reindent=True, keyword_case='upper')
            else:
                formatted = sql
                
            return {
                "status": "SUCCESS",
                "conteudo": formatted,
                "metadados": {"formato": "SQL", "sqlparse": bool(sqlparse)}
            }
        except Exception as e:
            return {"status": "ERROR", "error": str(e)}

def executar(entrada):
    return ExtratorSQL().executar(entrada)
