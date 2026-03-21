import os

def executar(entrada):
    caminho = entrada.get("caminho", "desconhecido")
    print(f"[SENSOR-MP4] Analisando frame de MP4 em {caminho}...")
    return {
        "status": "SUCCESS",
        "conteudo": "Extraído metadados do formato MP4 (Simulado SOTA)",
        "metadados": {"formato": "MP4", "size": os.path.getsize(caminho) if os.path.exists(caminho) else 0}
    }
