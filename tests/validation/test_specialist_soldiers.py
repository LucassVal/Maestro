import sys
import os
import json
import traceback
from tests.validation.validation_utils import capture_resources

# Add ROOT and SRC to path
ROOT_DIR = os.getcwd()
sys.path.append(ROOT_DIR)
sys.path.append(os.path.join(ROOT_DIR, "src"))

@capture_resources
def test_soldiers():
    results = []
    
    try:
        # Test 1: Terminal Soldier
        from src.agentes.passivos.terminal_soldado_SRC_GL import TerminalSoldier
        terminal = TerminalSoldier()
        res_t = terminal.executar("echo SOTA_TEST_OK")
        
        results.append({
            "component": "TerminalSoldier (Airlock)",
            "level": "MISSION",
            "input": "echo SOTA_TEST_OK",
            "output": str(res_t),
            "status": "PASS" if "PENDENTE" in str(res_t) else "FAIL",
            "feedback": "Airlock integration validated." if "PENDENTE" in str(res_t) else "Airlock failure."
        })
            
        # Test 2: Health Monitor
        from src.agentes.passivos.health_monitor_SRC_GL import HealthMonitor
        hm = HealthMonitor()
        status = hm.get_system_health()
        
        results.append({
            "component": "Health Monitor",
            "level": "MISSION",
            "input": "get_system_health",
            "output": json.dumps(status),
            "status": "PASS" if status.get("cpu_percent") is not None else "FAIL",
            "feedback": f"Captured metrics. CPU: {status.get('cpu_percent')}%"
        })
            
    except Exception as e:
        results.append({
            "component": "Specialist Soldiers Cluster",
            "level": "MISSION",
            "input": "N/A",
            "output": "N/A",
            "status": "FAIL",
            "feedback": f"Critical error: {str(e)}"
        })
        print(traceback.format_exc())

    return results

if __name__ == "__main__":
    final_res = test_soldiers()
    print(f"RESULT_JSON: {json.dumps(final_res)}")
