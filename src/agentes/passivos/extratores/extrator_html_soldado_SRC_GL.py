#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from .extrator_base_SRC_GL import ExtratorBase

try:
    from bs4 import BeautifulSoup
except ImportError:
    BeautifulSoup = None

class ExtratorHTML(ExtratorBase):
    def __init__(self):
        super().__init__(nome="ExtratorHTML")

    def executar(self, entrada):
        caminho = entrada.get("caminho")
        valido, msg = self.validar_arquivo(caminho)
        if not valido:
            return {"status": "ERROR", "error": msg}
        
        if not BeautifulSoup:
            return {"status": "ERROR", "error": "Biblioteca BeautifulSoup4 não instalada."}

        try:
            with open(caminho, "r", encoding="utf-8", errors="ignore") as f:
                soup = BeautifulSoup(f, "html.parser")
                for script in soup(["script", "style"]):
                    script.decompose()
                texto = soup.get_text(separator="\n")
                
                return {
                    "status": "SUCCESS",
                    "conteudo": texto,
                    "metadados": {"titulo": soup.title.string if soup.title else "N/A", "formato": "HTML"}
                }
        except Exception as e:
            return {"status": "ERROR", "error": str(e)}

def executar(entrada):
    return ExtratorHTML().executar(entrada)
