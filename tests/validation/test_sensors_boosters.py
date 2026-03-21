import sys
import os
import json
import traceback
from tests.validation.validation_utils import capture_resources

# Add SRC to path
sys.path.append(os.path.join(os.getcwd(), "src"))

@capture_resources
def test_sensors():
    results = []
    
    try:
        from src.agentes.passivos.extratores.fabrica_extratores_SRC_GL import FabricaExtratores
        fabrica = FabricaExtratores()
        
        # Test 1: Text Extractor
        test_txt = "tests/data_smoke/teste_fumaça.txt"
        
        item_res = {
            "component": "Sensor: Text Extractor",
            "level": "LAB",
            "input": test_txt,
            "output": "",
            "status": "FAIL",
            "feedback": ""
        }
        
        if os.path.exists(test_txt):
            extractor_cls = fabrica.obter_extrator(test_txt)
            if extractor_cls:
                extractor = extractor_cls()
                outcome = extractor.executar({"caminho": test_txt})
                item_res["output"] = outcome.get("texto", "")[:100]
                
                if outcome.get("status") == "SUCCESS":
                    item_res["status"] = "PASS"
                    item_res["feedback"] = "Text extraction validated successfully."
                else:
                    item_res["feedback"] = f"Extraction failed: {outcome.get('erro')}"
            else:
                item_res["feedback"] = "No extractor found for .txt extension."
        else:
            item_res["feedback"] = "Smoke test file missing."
            
        results.append(item_res)
            
    except Exception as e:
        results.append({
            "component": "Multimodal Lab Cluster",
            "level": "LAB",
            "input": "N/A",
            "output": "N/A",
            "status": "FAIL",
            "feedback": f"Critical error: {str(e)}"
        })
        print(traceback.format_exc())

    return results

if __name__ == "__main__":
    final_res = test_sensors()
    print(f"RESULT_JSON: {json.dumps(final_res)}")
