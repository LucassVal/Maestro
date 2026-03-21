# Parrudo Conscience Exporter - GL v1.0
import json
import os
import shutil
from datetime import datetime ROOT_DIR = "c:/Users/Lucas Val rio/Desktop/MODELO GENIO LLM"
EXPORT_DIR = "c:/Users/Lucas Val rio/Desktop/EXPORTS_GENIO" def export_conscience(): print("[BRAIN] Exportando Consci ncia do G nio...") if not os.path.exists(EXPORT_DIR): os.makedirs(EXPORT_DIR) timestamp = datetime.now().strftime("%Y%m%d_%H%M%S") snapshot_path = os.path.join(EXPORT_DIR, f"snapshot_{timestamp}") os.makedirs(snapshot_path) # Arquivos vitais files_to_copy = [ "GENIO_FILE_REGISTRE_.md", "config/cortex.json", "config/prompts_agents.json", ".panda/memory/master_roadmap.json" ] for f in files_to_copy: src = os.path.join(ROOT_DIR, f) if os.path.exists(src): dest = os.path.join(snapshot_path, os.path.basename(f)) shutil.copy(src, dest) print(f" Copiado: {f}") print(f"[OK] Consci ncia exportada para: {snapshot_path}") if __name__ == "__main__": export_conscience()
