import ollama
import json
import re

def executar(entrada):
    """
    Agente Avaliador SOTA v46.1.
    Valida a qualidade da resposta do Gênio.
    """
    prompt_original = entrada.get("prompt_original", "")
    resposta_agente = entrada.get("resposta_agente", "")
    modelo = entrada.get("modelo", "qwen2.5:1.5b")
    
    print(f"[EVALUATOR] Validando resposta contra prompt original...")
    
    prompt_eval = f"""
    Avalie a qualidade desta resposta de IA:
    Prompt Original: {prompt_original}
    Resposta Recebida: {resposta_agente}
    
    Responda EXCLUSIVAMENTE em formato JSON:
    {{"score": 0.0 a 10.0, "feedback": "...", "status": "PASS/FAIL"}}
    """
    
    try:
        resposta = ollama.generate(model=modelo, prompt=prompt_eval)
        raw_resp = resposta.get('response', "")
        
        # Tenta extrair JSON da resposta se houver lixo
        match = re.search(r'\{.*\}', raw_resp, re.DOTALL)
        if match:
            return json.loads(match.group())
        return {
            "score": 5.0,
            "feedback": "Não foi possível extrair JSON da avaliação.",
            "status": "FAIL"
        }
    except Exception as e:
        return {"score": 0, "feedback": str(e), "status": "FAIL"}