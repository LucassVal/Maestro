import json
from src.agentes.passivos.health_monitor_SRC_GL import HealthMonitor

def test_telemetry_rich():
    print("\n" + "="*50)
    print("SOTA v47.6 - TELEMETRY RICH TEST")
    print("="*50)
    
    monitor = HealthMonitor()
    report = monitor.check_health()
    
    print(f"[*] Report: {json.dumps(report, indent=4)}")
    
    sys_stats = report.get("system", {})
    assert "cpu_percent" in sys_stats
    assert "vmem_percent" in sys_stats
    assert "igpu_detected" in sys_stats
    
    print("\n✅ TESTE DE TELEMETRIA: SUCESSO. Métricas (CPU, VMem, iGPU) Detectadas.")
    print("="*50)

if __name__ == "__main__":
    test_telemetry_rich()
