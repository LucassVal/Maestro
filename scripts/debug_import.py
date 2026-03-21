import sys
import os
import importlib
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
sys.path.append(str(BASE_DIR))

agent_path = "src.agentes.ativos.auditor_agente_SRC_GL"
print(f"Testing import of {agent_path}...")

try:
    mod = importlib.import_module(agent_path)
    print("SUCCESS: Module imported.")
    if hasattr(mod, "executar"):
        print("SUCCESS: 'executar' found.")
    else:
        print("FAIL: 'executar' NOT found.")
except Exception as e:
    print(f"FAIL: {str(e)}")
    import traceback
    traceback.print_exc()
