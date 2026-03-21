# Parrudo Root Cleaner - GL v1.0
import os
import shutil ROOT_DIR = "c:/Users/Lucas Val rio/Desktop/MODELO GENIO LLM"
TEMP_DIRS = [".pytest_cache", "__pycache__", "tmp"] def clean(): print(" Starting Saneamento de Raiz...") for root, dirs, files in os.walk(ROOT_DIR): for d in dirs: if d in TEMP_DIRS: path = os.path.join(root, d) print(f" Removendo: {path}") shutil.rmtree(path, ignore_errors=True) print("[OK] Saneamento Conclu do.") if __name__ == "__main__": clean()
