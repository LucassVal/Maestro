import ollama

def executar(entrada):
    """
    Agente Supervisor SOTA.
    Gestão de tarefas e conformidade.
    """
    prompt = entrada.get("prompt", "")
    modelo = entrada.get("modelo", "qwen2.5-coder:7b")
    
    print(f"[SUPERVISOR] Auditando execução e conformidade SOTA...")
    
    try:
        resposta = ollama.generate(model=modelo, prompt=f"Atue como supervisor de projeto: {prompt}")
        return {
            "status": "ok",
            "agente": "supervisor",
            "resposta": resposta.get('response', "Erro na supervisão.")
        }
    except Exception as e:
        return {"status": "erro", "agente": "supervisor", "mensagem": str(e)}