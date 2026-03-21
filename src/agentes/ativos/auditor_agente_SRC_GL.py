# -*- coding: utf-8 -*-
"""
src/agentes/ativos/auditor_agente_SRC_GL.py - Elite Logic Accountant
Specialist: Pure Logic and Audit. SOTA version.
"""

from src.core import kernel_genio_CORE_GL as kernel

def executar(entrada):
    """
    Standardized interface for Auditor Agent.
    Evaluates inputs, outputs, and logical consistency.
    """
    prompt = entrada.get("prompt", "")
    # Default elite model from cortex, but allow override
    modelo = entrada.get("modelo") 
    
    print(f"[AUDIT] Audit session started...")
    
    # Mission Logic
    # Using the standardized kernel.chat for reliable connectivity
    response_text = kernel.chat(prompt, modelo=modelo)
    
    if "Error" in response_text or "Unavailable" in response_text:
        return {
            "status": "error",
            "agente": "auditor",
            "resposta": f"Audit failed: {response_text}"
        }
    
    return {
        "status": "ok",
        "agente": "auditor",
        "resposta": response_text
    }
