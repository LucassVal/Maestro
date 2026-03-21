import ollama

def executar(entrada):
    """
    Agente Estratégico SOTA.
    Planejamento de alto nível.
    """
    prompt = entrada.get("prompt", "")
    modelo = entrada.get("modelo", "qwen2.5-coder:7b")
    
    print(f"[STRATEGY] Agente Estratégico analisando viabilidade e roadmap...")
    
    try:
        resposta = ollama.generate(model=modelo, prompt=f"Atue como estrategista militar/técnico: {prompt}")
        return {
            "status": "ok",
            "agente": "estrategico",
            "resposta": resposta.get('response', "Erro na estratégia.")
        }
    except Exception as e:
        return {"status": "erro", "agente": "estrategico", "mensagem": str(e)}