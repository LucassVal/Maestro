import os
import subprocess
import sys root = r"."
sys.path.append(os.path.join(root, "src")) critical_files = [ os.path.join(root, "genio_launcher_GL.py"), os.path.join(root, "src", "core", "regente_sota_CORE_GL.py"), os.path.join(root, "src", "agentes", "passivos", "terminal_soldado_SRC_GL.py"), os.path.join(root, "src", "agentes", "passivos", "soldados.py")
] print("--- [[SANITY CHECK]] SOTA v45.3 ---")
for f_path in critical_files: if not os.path.exists(f_path): print(f"[MISSING] {f_path}") continue # Test compilation try: with open(f_path, "r", encoding="utf-8") as f: source = f.read() compile(source, f_path, "exec") print(f"[COMPILED] {os.path.basename(f_path)}") except SyntaxError as e: print(f"[SYNTAX ERROR] {os.path.basename(f_path)} at line {e.lineno}: {e.msg}") print(f" Code snippet: {e.text.strip() if e.text else 'N/A'}") except Exception as e: print(f"[ERROR] {os.path.basename(f_path)}: {e}") print("\n--- [[LOG SYSTEM CHECK]] ---")
log_path = os.path.join(root, ".panda", "logs", "genio_session.log")
if os.path.exists(log_path): print(f"[FOUND] Log file exists at {log_path}")
else: print(f"[NOT FOUND] Log file expected at {log_path}")
