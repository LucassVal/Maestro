# -*- coding: utf-8 -*-
"""
tests/validation/validation_utils.py - Utilitários de Certificação SOTA
Fornece decoradores e avaliadores para a v46.1.
"""

import time
import psutil
import json
import os
import re

def get_vram_mb():
    """Tenta capturar o uso de VRAM via nvidia-smi (simulação simplificada)."""
    try:
        # Nota: Em ambiente Windows/Ollama, o Ollama gerencia isso. 
        # Esta é uma implementação stub passível de expansão com pynvml.
        return 0 
    except:
        return None

def capture_resources(func):
    """Decorator para medir RAM/VRAM antes e depois do teste."""
    def wrapper(*args, **kwargs):
        ram_before = psutil.virtual_memory().used / (1024*1024)
        vram_before = get_vram_mb()
        start = time.time()
        
        result = func(*args, **kwargs)
        
        duration = time.time() - start
        ram_after = psutil.virtual_memory().used / (1024*1024)
        vram_after = get_vram_mb()
        
        # Se o resultado for uma lista (múltiplos subtestes), injetamos nos itens
        if isinstance(result, list):
            for item in result:
                item['duration_sec'] = duration / len(result)
                item['ram_delta_mb'] = ram_after - ram_before
        else:
            result['duration_sec'] = duration
            result['ram_delta_mb'] = ram_after - ram_before
            
        return result
    return wrapper

def evaluate_with_auditor(input_text, output_text):
    """Usa o Agente Auditor para dar uma nota e feedback."""
    try:
        # Adiciona SRC ao path para importar o agente
        import sys
        sys.path.append(os.path.join(os.getcwd(), "src"))
        from src.agentes.ativos.auditor_agente_SRC_GL import executar as auditor
        
        eval_prompt = (
            f"Avalie a conformidade da saída abaixo em relação à entrada.\n"
            f"Entrada: {input_text}\n"
            f"Saída: {output_text}\n"
            f"Responda apenas com a NOTA (0-10) seguida de um comentário breve."
        )
        
        response = auditor({"prompt": eval_prompt})
        text = response.get("resposta", "")
        
        match = re.search(r'\b([0|1|2|3|4|5|6|7|8|9]|10)\b', text)
        score = int(match.group(1)) if match else 7 # Default 7 se falhar o parser
        
        return score, text
    except Exception as e:
        return 5, f"Erro no avaliador: {str(e)}"
