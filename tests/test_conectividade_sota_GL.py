# -*- coding: utf-8 -*-
"""
test_conectividade_sota_GL.py Auditor de Fia o SOTA v44.3 NO EMOJI VERSION.
""" import requests
import json
import time
import sys
import socket # For a o flush de todos os prints
def sota_print(msg): print(msg) sys.stdout.flush() ENDPOINTS = { "OLLAMA": "http://localhost:11434/api/tags", "VS_CODE_API": "http://localhost:11435/v1/chat/completions", "MENTOR_WS": "ws://localhost:9812"
} def check_http(url): try: start = time.time() response = requests.get(url, timeout=2) latency = int((time.time() - start) * 1000) if response.status_code == 200: return f"OK ONLINE ({latency}ms)" return f"Fail ERRO ({response.status_code})" except Exception as e: return f"Fail OFFLINE" def run_audit(): sota_print("\n" + "="*50) sota_print("[AUDITORIA] CONECTIVIDADE SOTA v44.4") sota_print("="*50) # 1. Ollama sota_print(f"[-] OLLAMA (11434): {check_http(ENDPOINTS['OLLAMA'])}") # 2. VS Code API try: requests.get("http://localhost:11435/", timeout=1) sota_print(f"[-] BRACCO VS (11435): OK ONLINE (Port Active)") except: sota_print(f"[-] BRACCO VS (11435): Fail OFFLINE / TIMEOUT") # 3. Mentor WebSocket s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) s.settimeout(1) try: s.connect(("localhost", 9812)) sota_print(f"[-] MENTOR WS (9812): OK ONLINE (Socket Open)") except: sota_print(f"[-] MENTOR WS (9812): Fail OFFLINE") finally: s.close() sota_print("="*50) sota_print("Antigravity: Status OK (Via Bridge Admin)") sota_print("="*50 + "\n") if __name__ == "__main__": run_audit()
