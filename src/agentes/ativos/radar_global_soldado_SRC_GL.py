import ollama

def executar(entrada):
    """
    Agente Radar Global.
    Monitoramento de tendências e notícias.
    """
    prompt = entrada.get("prompt", "")
    modelo = entrada.get("modelo", "deepseek-r1:7b")
    
    print(f"[RADAR] Monitorando tendências globais...")
    
    try:
        resposta = ollama.generate(model=modelo, prompt=f"Analise tendências sobre: {prompt}")
        return {
            "status": "ok",
            "agente": "radar_global",
            "resposta": resposta.get('response', "Erro no radar.")
        }
    except Exception as e:
        return {"status": "erro", "agente": "radar_global", "mensagem": str(e)}
