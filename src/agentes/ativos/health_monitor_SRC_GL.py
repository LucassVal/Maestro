import psutil
import os

def executar(entrada):
    """
    Agente de Monitoramento de Saúde (Health Monitor).
    Coleta métricas de hardware em tempo real.
    """
    print(f"[HEALTH] Coletando telemetria de hardware...")
    
    try:
        cpu = psutil.cpu_percent(interval=0.1)
        ram = psutil.virtual_memory()
        
        return {
            "status": "ok",
            "agente": "health_monitor",
            "metrics": {
                "cpu_percent": cpu,
                "ram_percent": ram.percent,
                "ram_available_mb": ram.available / (1024 * 1024),
                "os": os.name
            }
        }
    except Exception as e:
        return {"status": "error", "agente": "health_monitor", "mensagem": str(e)}
