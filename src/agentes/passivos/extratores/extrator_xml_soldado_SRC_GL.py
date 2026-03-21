#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from .extrator_base_SRC_GL import ExtratorBase

try:
    import lxml.etree as etree
except ImportError:
    import xml.etree.ElementTree as etree

class ExtratorXML(ExtratorBase):
    def __init__(self):
        super().__init__(nome="ExtratorXML")

    def executar(self, entrada):
        caminho = entrada.get("caminho")
        valido, msg = self.validar_arquivo(caminho)
        if not valido:
            return {"status": "ERROR", "error": msg}

        try:
            tree = etree.parse(caminho)
            root = tree.getroot()
            return {
                "status": "SUCCESS",
                "conteudo": etree.tostring(root, encoding="unicode"),
                "metadados": {"tag_raiz": root.tag, "formato": "XML"}
            }
        except Exception as e:
            return {"status": "ERROR", "error": str(e)}

def executar(entrada):
    return ExtratorXML().executar(entrada)
