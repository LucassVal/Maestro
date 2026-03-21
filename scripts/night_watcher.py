#!/ pylance
# -*- coding: utf-8 -*-
"""
night_watcher.py O Sentinela Pesado.
v2.0 SOTA ELITE: Opera o Noturna e Self-Play.
""" import os
import time
from datetime import datetime class NightWatcher: def __init__(self): self.active_hours = (2, 6) # 02:00 s 06:00 def is_night_time(self): hour = datetime.now().hour return self.active_hours[0] <= hour < self.active_hours[1] def run_heavy_tasks(self): print(" JANELA NOTURNA: Starting Processamento Massivo SOTA...") # 1. Self-Play e Desafios (Inje o de Bugs e Auto-Cura) print("[TEST] Executando Self-Play (Gerador de Desafios)...") os.system("python src/agentes/passivos/desafios_gerador_SRC_GL.py") # 2. RAG Pesado e Indexa o Vetorial print("[DOCS] Atualizando ndice Vetorial e Mem ria Coletiva...") # Simula trigger de indexa o massiva # 3. Radar Global e Mapa SOTA print("[RADAR] Coletando tend ncias globais e gerando SOTA_MAP.md...") os.system("python src/agentes/passivos/radar_global_soldado_SRC_GL.py") print("[OK] Tarefas Noturnas Conclu das.") def watch(self): print(f"[SAT] NIGHT WATCHER v2.0 ATIVO. Janela: {self.active_hours[0]}h-{self.active_hours[1]}h") while True: if self.is_night_time(): self.run_heavy_tasks() # Dorme at o fim da janela ou 1 hora time.sleep(3600) else: print(" Dia detectado. Sentinela em estado de observa o...") time.sleep(900) # Checa a cada 15 min if __name__ == "__main__": watcher = NightWatcher() watcher.watch()
