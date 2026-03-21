#!/ pylance
# -*- coding: utf-8 -*-
"""
ponte_insights_SRC_GL.py O Sensor de Transbordo SOTA v44.3.
Monitora .panda/bridge/insights/ e injeta intelig ncia estrat gica no VS Code.
""" import os
import time
import json
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from src.core.eventos_sistema_CORE_GL import registrar_evento
from src.agentes.passivos.extensao_vs_bridge_SRC_GL import VSCodeBridge class InsightHandler(FileSystemEventHandler): def __init__(self, bridge): self.bridge = bridge self.processed_dir = ".panda/bridge/insights/processed" os.makedirs(self.processed_dir, exist_ok=True) def on_created(self, event): if not event.is_directory and event.src_path.endswith('.json'): time.sleep(0.5) # Buffer para escrita completa self._processar_insight(event.src_path) def _processar_insight(self, path): try: with open(path, 'r', encoding='utf-8') as f: insight = json.load(f) print(f"[INSIGHT] Detected: {insight.get('conteudo')[:50]}...") registrar_evento("INSIGHT_RECEBIDO", None, {"insight": insight}) # Encaminha para o VS Code Bridge cmd_id = str(int(time.time())) self.bridge._responder(cmd_id, {"tipo": "sugestao", "dados": insight}) # Move para processados dest = os.path.join(self.processed_dir, os.path.basename(path)) shutil.move(path, dest) print(f"[OK] Insight processed and moved to {dest}") except Exception as e: print(f"[ERR] [INSIGHT] Error ao processar: {e}") def iniciar_monitoramento(): path = ".panda/bridge/insights" os.makedirs(path, exist_ok=True) bridge = VSCodeBridge() event_handler = InsightHandler(bridge) observer = Observer() observer.schedule(event_handler, path, recursive=False) observer.start() print(f"[BRIDGE] Insight Sensor Active: Monitoring {path}...") try: while True: time.sleep(1) except KeyboardInterrupt: observer.stop() observer.join() if __name__ == "__main__": iniciar_monitoramento()
