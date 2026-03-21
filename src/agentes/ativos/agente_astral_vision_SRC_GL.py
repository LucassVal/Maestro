import ollama

def executar(entrada):
    """
    Agente Astral Vision (Visão Computacional simulada via LLM multimodal).
    """
    prompt = entrada.get("prompt", "")
    modelo = entrada.get("modelo", "qwen2.5-coder:7b") # Fallback stable
    
    print(f"[ASTRAL] Processando dados visuais...")
    
    try:
        # Nota: Necessita de ollama compatível com multimodal para imagem real
        # Aqui simulamos a descrição técnica
        resposta = ollama.generate(model=modelo, prompt=f"Diferencie e descreva os elementos visuais deste contexto: {prompt}")
        return {
            "status": "ok",
            "agente": "astral_vision",
            "resposta": resposta.get('response', "Erro no processamento visual.")
        }
    except Exception as e:
        return {"status": "erro", "agente": "astral_vision", "mensagem": str(e)}
