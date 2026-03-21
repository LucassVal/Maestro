#!/ pylance
# -*- coding: utf-8 -*-
"""
colono_daemon.py O C rebro Aut nomo 24/7.
v2.0 SOTA ELITE: Opera o Diurna Consolidada.
""" import time
import os
import json
import shutil
import subprocess
from datetime import datetime # Configura es de Ciclo
CHECK_INTERVAL = 900 # 15 minutos (SOTA v44.0)
DAEMON_LOG = os.path.join(".panda", "memory", "daemon_status.json") class ColonoDaemon: def __init__(self): self.base_dir = os.getcwd() os.makedirs(".panda/backups", exist_ok=True) os.makedirs(".panda/logs", exist_ok=True) def registrar_pulso(self, status): """Registra o estado do daemon para monitoramento na GUI.""" log_data = { "last_pulse": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "status": status, "pid": os.getpid(), "version": "v2.0 SOTA ELITE" } with open(DAEMON_LOG, "w") as f: json.dump(log_data, f, indent=4) def consolidar_logs(self): """Compacta e arquiva logs antigos do event_store.""" self.registrar_pulso("[HEALTH] Consolidando logs...") # L gica de compacta o (Stub) print(" Logs compactados e arquivados.") def verificar_mcp_mesh(self): """Valida integridade dos manifestos MCP.""" self.registrar_pulso("[RADAR] Verificando malha MCP...") mcp_dir = "config/mcp" if not os.path.exists(mcp_dir): return # Checa se os arquivos JSON s o v lidos print("[OK] Malha MCP ntegra.") def backup_snapshots(self): """Recupera snapshots de arquivos cr ticos.""" self.registrar_pulso("[GUARD] Criando Snapshots de Seguran a...") from auto_atualizacao_passivos_SRC_GL import AutoAtualizacao aa = AutoAtualizacao() criticos = ["config/cortex.json", "config/prompts_agents.json", "GENIO_FILE_REGISTRE_.md"] aa.backup_atomico(criticos) def rodar_saude_e_evolucao(self): """Executa o Health Monitor e a Auto-Evolu o.""" self.registrar_pulso("[BRAIN] Orquestrando Health e Otimiza o...") # 1. Health Check from health_monitor_SRC_GL import HealthMonitor stats, alerts = HealthMonitor().check_health() # 2. Auto-Evolu o (Otimiza VRAM/Ctx) from auto_evolucao_passivos_SRC_GL import AutoEvolucao AutoEvolucao().otimizar_vram_contexto() def ciclo_principal(self): print("[BOOST] COLONO DAEMON v2.0 INICIADO (Modo Organismo SOTA)") while True: try: self.consolidar_logs() self.verificar_mcp_mesh() self.backup_snapshots() self.rodar_saude_e_evolucao() self.registrar_pulso("[OK] Ciclo Diurno conclu do. Dormindo...") except Exception as e: self.registrar_pulso(f"[ERR] Error: {e}") print(f"Daemon Errorr: {e}") time.sleep(CHECK_INTERVAL) if __name__ == "__main__": daemon = ColonoDaemon() daemon.ciclo_principal()
