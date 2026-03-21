#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
extrator_archive_soldado_SRC_GL.py Soldado de extração de Arquivos (ZIP).
"""
import os
import sys
import zipfile
from .extrator_base_SRC_GL import ExtratorBase

class ExtratorArchive(ExtratorBase):
    def __init__(self):
        super().__init__(nome="ExtratorArchive")

    def executar(self, entrada):
        caminho = entrada.get("caminho")
        valido, msg = self.validar_arquivo(caminho)
        if not valido:
            return {"status": "ERROR", "error": msg}
        try:
            with zipfile.ZipFile(caminho, 'r') as z:
                lista_arquivos = z.namelist()
            texto = f"Arquivo: {os.path.basename(caminho)}\nConteúdo:\n"
            texto += "\n".join([f"- {arq}" for arq in lista_arquivos])
            return {
                "status": "SUCCESS",
                "texto": texto,
                "metadados": {"arquivos_count": len(lista_arquivos), "formato": "ARCHIVE"}
            }
        except Exception as e:
            return {"status": "ERROR", "error": str(e)}

def executar(entrada):
    return ExtratorArchive().executar(entrada)
