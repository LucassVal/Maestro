import os

def executar(entrada):
    caminho = entrada.get("caminho", "desconhecido")
    print(f"[SENSOR-WEBM] Analisando frame de WEBM em {caminho}...")
    return {
        "status": "SUCCESS",
        "conteudo": "Extraído metadados do formato WEBM (Simulado SOTA)",
        "metadados": {"formato": "WEBM", "size": os.path.getsize(caminho) if os.path.exists(caminho) else 0}
    }
