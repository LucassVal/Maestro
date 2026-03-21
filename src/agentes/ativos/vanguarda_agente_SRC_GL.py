import ollama

def executar(entrada):
    """
    Agente Vanguarda SOTA.
    Foca em inovação e novas tecnologias.
    """
    prompt = entrada.get("prompt", "")
    modelo = entrada.get("modelo", "llama3.2:1b")
    
    print(f"[VANGUARD] Explorando fronteiras tecnológicas...")
    
    try:
        resposta = ollama.generate(model=modelo, prompt=f"Atue como vanguardista tecnológico: {prompt}")
        return {
            "status": "ok",
            "agente": "vanguarda",
            "resposta": resposta.get('response', "Erro na vanguarda.")
        }
    except Exception as e:
        return {"status": "erro", "agente": "vanguarda", "mensagem": str(e)}
