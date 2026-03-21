import ollama

def executar(entrada):
    """
    Interface padronizada para o Agente Moderador.
    Gera consenso entre múltiplas saídas.
    """
    prompt = entrada.get("prompt", "")
    modelo = entrada.get("modelo", "deepseek-r1:7b")
    
    print(f"[MODERATOR] Gerando consenso e arbitragem...")
    
    try:
        resposta = ollama.generate(model=modelo, prompt=f"Atue como moderador e gere um consenso: {prompt}")
        return {
            "status": "ok",
            "agente": "moderador",
            "resposta": resposta.get('response', "Erro na moderação.")
        }
    except Exception as e:
        return {"status": "erro", "agente": "moderador", "mensagem": str(e)}
