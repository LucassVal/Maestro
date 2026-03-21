import ollama

def executar(entrada):
    """
    Interface padronizada para o Regente v18.5
    entrada: { "prompt": "...", "modelo": "...", "contexto": {...}, "anterior": "..." }
    """
    prompt = entrada.get("prompt", "")
    modelo = entrada.get("modelo", "qwen2.5-coder:7b")
    resultado_anterior = entrada.get("anterior")
    
    print(f"[ ] Agente Engenheiro pronto para codificar. Nível SOTA ativo.")
    
    # Se houver resultado anterior (ex: de uma pesquisa), reforça no sistema
    if resultado_anterior:
        prompt = f"Considere a pesquisa anterior: {str(resultado_anterior)[:500]}\n\n" + prompt
        
    try:
        # Usa o modelo de elite para o código
        resposta = ollama.generate(model=modelo, prompt=prompt)
        return {
            "status": "ok",
            "agente": "engenheiro",
            "resposta": resposta.get('response', "Erro na geração.")
        }
    except Exception as e:
        return {"status": "erro", "agente": "engenheiro", "mensagem": str(e)}
