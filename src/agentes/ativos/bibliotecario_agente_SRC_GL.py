import ollama

def executar(entrada):
    """
    Agente Bibliotecário SOTA.
    Foca em organizar informação e documentar.
    """
    prompt = entrada.get("prompt", "")
    modelo = entrada.get("modelo", "llama3.2:1b")
    
    print(f"[LIBRARY] Bibliotecário organizando os arquivos da memória...")
    
    try:
        resposta = ollama.generate(model=modelo, prompt=f"Organize como um bibliotecário: {prompt}")
        return {
            "status": "ok",
            "agente": "bibliotecario",
            "resposta": resposta.get('response', "Erro na organização.")
        }
    except Exception as e:
        return {"status": "erro", "agente": "bibliotecario", "mensagem": str(e)}