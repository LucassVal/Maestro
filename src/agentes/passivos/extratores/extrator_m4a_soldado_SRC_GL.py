import os

def executar(entrada):
    caminho = entrada.get("caminho", "desconhecido")
    print(f"[SENSOR-M4A] Analisando stream de M4A em {caminho}...")
    return {
        "status": "SUCCESS",
        "conteudo": "Extraído dados do formato M4A (Simulado SOTA)",
        "metadados": {"formato": "M4A", "size": os.path.getsize(caminho) if os.path.exists(caminho) else 0}
    }
