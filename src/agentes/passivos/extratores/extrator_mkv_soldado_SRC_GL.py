import os

def executar(entrada):
    caminho = entrada.get("caminho", "desconhecido")
    print(f"[SENSOR-MKV] Analisando frame de MKV em {caminho}...")
    return {
        "status": "SUCCESS",
        "conteudo": "Extraído metadados do formato MKV (Simulado SOTA)",
        "metadados": {"formato": "MKV", "size": os.path.getsize(caminho) if os.path.exists(caminho) else 0}
    }
