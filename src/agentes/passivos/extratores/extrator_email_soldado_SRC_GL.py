#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
extrator_email_soldado_SRC_GL.py Soldado de extração de E-mails (.msg).
"""
import os
import sys
from .extrator_base_SRC_GL import ExtratorBase
try:
    import extract_msg
except ImportError:
    extract_msg = None

class ExtratorEmail(ExtratorBase):
    def __init__(self):
        super().__init__(nome="ExtratorEmail")

    def executar(self, entrada):
        caminho = entrada.get("caminho")
        valido, msg = self.validar_arquivo(caminho)
        if not valido:
            return {"status": "ERROR", "error": msg}
        if extract_msg is None:
            return {"status": "ERROR", "error": "Biblioteca extract-msg não instalada."}
        try:
            msg_obj = extract_msg.OpenMsg(caminho)
            texto = f"Assunto: {msg_obj.subject}\nDe: {msg_obj.sender}\nData: {msg_obj.date}\n\nCorpo:\n{msg_obj.body}"
            return {
                "status": "SUCCESS",
                "texto": texto,
                "metadados": {"assunto": msg_obj.subject, "formato": "EMAIL"}
            }
        except Exception as e:
            return {"status": "ERROR", "error": str(e)}
