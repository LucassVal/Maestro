import os

def executar(entrada):
    caminho = entrada.get("caminho", "desconhecido")
    print(f"[SENSOR-AVI] Analisando frame de AVI em {caminho}...")
    return {
        "status": "SUCCESS",
        "conteudo": "Extraído metadados do formato AVI (Simulado SOTA)",
        "metadados": {"formato": "AVI", "size": os.path.getsize(caminho) if os.path.exists(caminho) else 0}
    }
