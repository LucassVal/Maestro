import os

def executar(entrada):
    caminho = entrada.get("caminho", "desconhecido")
    print(f"[SENSOR-MOV] Analisando frame de MOV em {caminho}...")
    return {
        "status": "SUCCESS",
        "conteudo": "Extraído metadados do formato MOV (Simulado SOTA)",
        "metadados": {"formato": "MOV", "size": os.path.getsize(caminho) if os.path.exists(caminho) else 0}
    }
