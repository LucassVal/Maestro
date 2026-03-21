import ollama

def executar(entrada):
    """
    Interface padronizada para o Agente Mentor v46.0
    Foca em orientação estratégica e técnica.
    """
    prompt = entrada.get("prompt", "")
    modelo = entrada.get("modelo", "qwen2.5-coder:7b")
    
    print(f"[MENTOR] Iniciando sessão de mentoria técnica...")
    
    try:
        resposta = ollama.generate(model=modelo, prompt=f"Atue como Mentor SOTA: {prompt}")
        return {
            "status": "ok",
            "agente": "mentor",
            "resposta": resposta.get('response', "Erro na mentoria.")
        }
    except Exception as e:
        return {"status": "erro", "agente": "mentor", "mensagem": str(e)}