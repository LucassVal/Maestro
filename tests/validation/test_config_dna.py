import json
import os
import sys
from tests.validation.validation_utils import capture_resources

CONFIGS = [
    "config/cortex.json",
    "config/prompts_agents.json",
    "GENIO_FILE_REGISTRE_.md"
]

@capture_resources
def test_json_integrity():
    results = []
    
    for path in CONFIGS:
        item_res = {
            "component": f"DNA: {os.path.basename(path)}",
            "level": "CONFIG",
            "input": path,
            "output": "N/A",
            "status": "FAIL",
            "feedback": ""
        }
        
        if not os.path.exists(path):
            item_res["feedback"] = "File missing."
            results.append(item_res)
            continue
            
        try:
            if path.endswith(".json"):
                with open(path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                item_res["status"] = "PASS"
                item_res["feedback"] = "Valid JSON."
                if "cortex.json" in path:
                    # Check for new tier_config structure
                    if not data.get("tier_config"):
                        item_res["status"] = "WARN"
                        item_res["feedback"] += " (Warning: Missing tier_config)"
                    elif not data.get("tier_config", {}).get("tiers"):
                        item_res["status"] = "WARN"
                        item_res["feedback"] += " (Warning: Missing tiers in tier_config)"
            else:
                item_res["status"] = "PASS"
                item_res["feedback"] = "File exists."
        except Exception as e:
            item_res["feedback"] = f"Parse error: {str(e)}"
            
        results.append(item_res)
        
    return results

if __name__ == "__main__":
    final_res = test_json_integrity()
    print(f"RESULT_JSON: {json.dumps(final_res)}")
