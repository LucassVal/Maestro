import os
import json
import sys

# Setup Path for Core Import
sys.path.append(os.path.join(os.getcwd(), "src", "core"))
import kernel_genio_CORE_GL as kernel

def test_json_integrity(file_path):
    print(f"[-] Checking {file_path}...")
    if not os.path.exists(file_path):
        return False, "File not found"
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            
            # Check Metadata
            meta = data.get("metadata", {})
            if not meta.get("version") or not meta.get("sovereignty"):
                return False, "Missing metadata (version/sovereignty)"
            
            # Check Registry for Paths
            registry = data.get("registry", {})
            elements = registry.get("intent_mapping", []) or registry.get("terms", [])
            
            for item in elements:
                path = item.get("path")
                if path:
                    if not os.path.exists(path):
                        print(f"    [!] Internal Path Error: {path} does not exist!")
                        return False, f"Broken link: {path}"
            
            return True, f"OK (v{meta.get('version')})"
    except Exception as e:
        return False, str(e)

def run_sota_audit():
    print("\n" + "="*60)
    print("SOTA v47.5 INTEGRITY AUDIT - GENIO LLM")
    print("="*60)
    
    configs = [
        "config/codex_tecnico.json",
        "config/glossario_tecnico.json",
        "config/cortex.json"
    ]
    
    overall_success = True
    
    # 1. JSON & Path Validation
    for cfg in configs:
        success, msg = test_json_integrity(cfg)
        print(f"[*] {cfg}: {msg}")
        if not success: overall_success = False

    # 2. Kernel API Validation
    print("\n[-] Testing Kernel API (consultar_codex)...")
    try:
        res = kernel.consultar_codex(palavra="criar")
        if res and res.get("category") == "engenheiro":
            print(f"[*] API 'consultar_codex': OK (Mapped to {res.get('path')})")
        else:
            print("[!] API 'consultar_codex': FAIL (Return mismatch)")
            overall_success = False
    except Exception as e:
        print(f"[!] API 'consultar_codex': ERROR ({e})")
        overall_success = False

    print("\n" + "="*60)
    if overall_success:
        print("RESULT: SOTA INTEGRITY VERIFIED ✅")
    else:
        print("RESULT: SOTA INTEGRITY COMPROMISED ❌")
    print("="*60 + "\n")

if __name__ == "__main__":
    run_sota_audit()
