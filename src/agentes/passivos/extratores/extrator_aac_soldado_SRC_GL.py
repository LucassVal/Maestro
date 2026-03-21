import os

def executar(entrada):
    caminho = entrada.get("caminho", "desconhecido")
    print(f"[SENSOR-AAC] Analisando stream de AAC em {caminho}...")
    return {
        "status": "SUCCESS",
        "conteudo": "Extraído dados do formato AAC (Simulado SOTA)",
        "metadados": {"formato": "AAC", "size": os.path.getsize(caminho) if os.path.exists(caminho) else 0}
    }
