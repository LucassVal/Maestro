import ollama

def executar(entrada):
    """
    Agente Tradutor SOTA.
    Tradução técnica e semântica.
    """
    texto = entrada.get("prompt", "")
    modelo = entrada.get("modelo", "llama3.2:1b")
    idioma = entrada.get("idioma", "pt-br")
    
    print(f"[TRANSLATE] Traduzindo conteúdo para {idioma}...")
    
    try:
        resposta = ollama.generate(model=modelo, prompt=f"Traduza para {idioma}: {texto}")
        return {
            "status": "ok",
            "agente": "tradutor",
            "resposta": resposta.get('response', "Erro na tradução.")
        }
    except Exception as e:
        return {"status": "erro", "agente": "tradutor", "mensagem": str(e)}
