import ollama

def executar(entrada):
    """
    Interface padronizada para o Agente Pesquisador v45.3
    Especialista em busca e síntese.
    """
    prompt = entrada.get("prompt", "")
    modelo = entrada.get("modelo", "deepseek-r1:7b")
    
    print(f"[SEARCH] Pesquisador iniciando busca semântica...")
    
    try:
        # Simulação de RAG/Search integrada com Ollama
        resposta = ollama.generate(model=modelo, prompt=f"Pesquise e sintetize: {prompt}")
        return {
            "status": "ok",
            "agente": "pesquisador",
            "resposta": resposta.get('response', "Erro na busca.")
        }
    except Exception as e:
        return {"status": "erro", "agente": "pesquisador", "mensagem": str(e)}
