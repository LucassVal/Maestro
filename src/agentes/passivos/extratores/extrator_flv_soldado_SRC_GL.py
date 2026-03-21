import os

def executar(entrada):
    caminho = entrada.get("caminho", "desconhecido")
    print(f"[SENSOR-FLV] Analisando frame de FLV em {caminho}...")
    return {
        "status": "SUCCESS",
        "conteudo": "Extraído metadados do formato FLV (Simulado SOTA)",
        "metadados": {"formato": "FLV", "size": os.path.getsize(caminho) if os.path.exists(caminho) else 0}
    }
