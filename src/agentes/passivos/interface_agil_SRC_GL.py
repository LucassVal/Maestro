import os
import json

# [INTERFACE] AGILE INTERFACE v45.3 - GL
# Fast-track for simple prompts and UI orchestration.

def processar_entrada(prompt):
    """Identifies if a prompt is simple enough for agile processing."""
    print(f"[[INTERFACE]] Analyzing agile path for: {prompt[:30]}...")
    return {"complexidade": "baixa", "recomendacao": "direto"}

def preparar_para_supremo(prompt, resumo):
    """Formats the data for the Strategic Agent."""
    return f"Mission: {prompt}\nContext: {resumo}"