#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
extrator_base_SRC_GL.py - Classe base para soldados de extração de texto.
"""
import os
import sys

class ExtratorBase:
    def __init__(self, nome="ExtratorBase"):
        self.nome = nome

    def validar_arquivo(self, caminho):
        if not os.path.exists(caminho):
            return False, f"Arquivo não encontrado: {caminho}"
        return True, "OK"

    def executar(self, entrada):
        """
        entrada: { "caminho": "..." }
        retorno: { "status": "SUCCESS", "conteudo": "...", "metadados": {...} }
        """
        raise NotImplementedError("O método executar deve ser implementado pela subclasse.")
