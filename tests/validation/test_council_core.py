import sys
import os
import json
import traceback
from tests.validation.validation_utils import capture_resources

# Adiciona a RAIZ e o SRC ao path
ROOT_DIR = os.getcwd()
sys.path.append(ROOT_DIR)
sys.path.append(os.path.join(ROOT_DIR, "src"))

@capture_resources
def test_heartbeat():
    results = {
        "component": "Core Heartbeat",
        "level": "COUNCIL",
        "input": "Responda apenas PONG",
        "output": "",
        "status": "FAIL",
        "feedback": ""
    }
    
    try:
        from src.core.regente_sota_CORE_GL import RegenteSOTA
        from src.core import kernel_genio_CORE_GL as kernel
        
        regente = RegenteSOTA()
        _ = kernel.get_cortex()
        
        # Missão Simples
        res = regente.iniciar_missao(results["input"])
        results["output"] = str(res)
        
        # Event Store
        from src.core import eventos_sistema_CORE_GL as eventos
        _ = eventos.obter_cronologia("LAST_SESSION")
        
        results["status"] = "PASS"
        results["feedback"] = "Regente, Kernel e Event Store operacionais."
            
    except Exception as e:
        results["status"] = "FAIL"
        results["feedback"] = f"Erro: {str(e)}"
        print(f"[ERR] {traceback.format_exc()}")

    return results

if __name__ == "__main__":
    final_res = test_heartbeat()
    print(f"RESULT_JSON: {json.dumps(final_res)}")
