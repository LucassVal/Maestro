import ollama

def executar(entrada):
    """
    Agente de Autocorreção SOTA.
    Recebe um erro ou código quebrado e tenta fix.
    """
    erro = entrada.get("prompt", "")
    modelo = entrada.get("modelo", "qwen2.5-coder:7b")
    
    print(f"[REPAIR] Agente de Autocorreção buscando solução para o bug...")
    
    try:
        resposta = ollama.generate(model=modelo, prompt=f"Conserte este erro/código: {erro}")
        return {
            "status": "ok",
            "agente": "autocorrecao",
            "resposta": resposta.get('response', "Erro na autocorreção.")
        }
    except Exception as e:
        return {"status": "erro", "agente": "autocorrecao", "mensagem": str(e)}