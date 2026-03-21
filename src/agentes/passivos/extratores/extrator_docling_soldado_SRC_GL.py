#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
extrator_docling_soldado_SRC_GL.py Soldado de Extração Estruturada (Docling).
Otimizado para OCR rápido e estruturação de documentos em CPU/iGPU.
"""
import os
from typing import Dict, Any
from .extrator_base_SRC_GL import ExtratorBase

try:
    from docling.document_converter import DocumentConverter
    DOCLING_AVAILABLE = True
except ImportError:
    DOCLING_AVAILABLE = False

class ExtratorDocling(ExtratorBase):
    def __init__(self):
        super().__init__(nome="ExtratorDocling")
        self.converter = DocumentConverter() if DOCLING_AVAILABLE else None

    def executar(self, entrada: Dict[str, Any]) -> Dict[str, Any]:
        if not DOCLING_AVAILABLE:
            return {
                "status": "ERROR",
                "error": "Biblioteca 'docling' não instalada. Execute 'pip install docling'."
            }
        
        caminho = entrada.get("caminho")
        valido, msg = self.validar_arquivo(caminho)
        if not valido:
            return {"status": "ERROR", "error": msg}

        try:
            print(f"   [SOLDADO DOCLING]: Processando estrutura de {os.path.basename(caminho)}...")
            result = self.converter.convert(caminho)
            markdown_content = result.document.export_to_markdown()
            
            texto = f"--- CONTEÚDO ESTRUTURADO (DOCLING) ({os.path.basename(caminho)}) ---\n"
            texto += markdown_content
            
            return {
                "status": "SUCCESS",
                "texto": texto,
                "metadados": {
                    "formato": caminho.split(".")[-1].upper(),
                    "ferramenta": "IBM_DOCLING_V1",
                    "tipo": "STRUCTURED_OCR"
                }
            }
        except Exception as e:
            return {"status": "ERROR", "error": f"Failure no Docling: {str(e)}"}

def executar(entrada):
    return ExtratorDocling().executar(entrada)

if __name__ == "__main__":
    # Teste local
    extrator = ExtratorDocling()
    print(extrator.executar({"caminho": "exemplo.pdf"}))
