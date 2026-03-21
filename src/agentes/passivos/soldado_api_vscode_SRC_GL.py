#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
soldado_api_vscode_SRC_GL.py - O Braço de Conexão IDE.
v44.2: Fornece um endpoint compatível para extensões como llm-vscode.
"""
import os
import json
import time
from flask import Flask, request, jsonify

app = Flask(__name__)
BRIDGE_DIR = ".panda/vs_bridge"
os.makedirs(BRIDGE_DIR, exist_ok=True)

@app.route("/v1/chat/completions", methods=["POST"])
@app.route("/api/generate", methods=["POST"])
def generate():
    """Recebe pedidos do VS Code e encaminha para o Regente via Bridge."""
    data = request.json
    print(f"[RADAR] API VS CODE: Recebido pedido de {request.path}")
    
    cmd_id = str(int(time.time()))
    payload = {
        "id": cmd_id,
        "comando": "vscode_query",
        "args": data
    }
    
    cmd_file = os.path.join(BRIDGE_DIR, "vs_bridge_cmd.json")
    with open(cmd_file, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=4)
        
    resp_file = os.path.join(BRIDGE_DIR, f"resposta_{cmd_id}.json")
    for _ in range(10):  # 10 segundos de timeout
        if os.path.exists(resp_file):
            with open(resp_file, "r", encoding="utf-8") as f:
                resp_data = json.load(f)
            os.remove(resp_file)
            return jsonify(resp_data.get("resultado", {}))
        time.sleep(1)
        
    return jsonify({"error": "Timeout na comunicação com o Regente"}), 504

def executar(entrada=None):
    """Interface padrão para o Regente."""
    return "[OK] API VS Code Soldier está ativo. Aguardando conexões IDE."

if __name__ == "__main__":
    print("[API] VS CODE SOLDIER API: Listening on port 11435...")
    app.run(port=11435)
