import pystray
from PIL import Image, ImageDraw
import threading
import time
import os
import sys
import subprocess
from src.agentes.passivos.health_monitor_SRC_GL import HealthMonitor

class AgenteZeroTray:
    def __init__(self):
        self.monitor = HealthMonitor()
        self.icon = None
        self.running = True
        self.status_text = "Gênio LLM - SOTA v47.6"

    def create_image(self):
        # Gera um ícone azul neon para o Gênio
        image = Image.new('RGB', (64, 64), color=(2, 6, 23)) # #020617
        dc = ImageDraw.Draw(image)
        dc.ellipse((10, 10, 54, 54), fill=(56, 189, 248)) # #38BDF8
        dc.text((22, 20), "G", fill=(255, 255, 255))
        return image

    def get_bar(self, percent):
        """Gera uma barra 1/10 para visualização rápida."""
        blocks = int(percent / 10)
        return "[" + "#" * blocks + "." * (10 - blocks) + "]"

    def update_loop(self):
        while self.running:
            try:
                report = self.monitor.check_health()
                sys_stats = report.get("system", {})
                gpu_stats = report.get("gpu")
                
                # Monta a telemetria 1/10
                tp = []
                tp.append(f"CP: {self.get_bar(sys_stats.get('cpu_percent', 0))} {sys_stats.get('cpu_percent', 0)}%")
                tp.append(f"RM: {self.get_bar(sys_stats.get('ram_percent', 0))} {sys_stats.get('ram_percent', 0)}%")
                tp.append(f"VM: {self.get_bar(sys_stats.get('vmem_percent', 0))} {sys_stats.get('vmem_percent', 0)}%")
                
                if gpu_stats:
                    tp.append(f"GP: {self.get_bar(gpu_stats.get('vram_p', 0))} {gpu_stats.get('vram_p', 0):.1f}%")
                
                llms = sys_stats.get("llms_active", [])
                tp.append(f"LLM: {' | '.join(llms[:2]) if llms else 'IDLE'}")
                
                self.status_text = "\n".join(tp)
                if self.icon:
                    self.icon.title = f"Gênio LLM - Fiscal 1/10\n{self.status_text}"
            except Exception as e:
                print(f"[ERR] Tray Update: {e}")
            
            time.sleep(5)

    def on_action(self, icon, item):
        action = str(item)
        if action == "Open GUI":
            subprocess.Popen([sys.executable, "src/interfaces/genio_gui_SRC_GL.py"])
        elif action == "Reset Core":
            subprocess.Popen([sys.executable, "scripts/genio_master_init_GL.py"])
        elif action == "Sync Gold":
            subprocess.Popen([sys.executable, "scripts/chameleon_sync.py"])
        elif action == "Exit":
            self.running = False
            icon.stop()

    def run(self):
        menu = pystray.Menu(
            pystray.MenuItem("Open GUI", self.on_action),
            pystray.MenuItem("Reset Core", self.on_action),
            pystray.MenuItem("Sync Gold", self.on_action),
            pystray.MenuItem("Exit", self.on_action)
        )
        self.icon = pystray.Icon("GenioTray", self.create_image(), "Gênio LLM - SOTA v47.6", menu)
        
        # Inicia thread de atualização
        threading.Thread(target=self.update_loop, daemon=True).start()
        
        print("[OK] Agente Zero Tray Iniciado (Dashboard 1/10 Ativo)")
        self.icon.run()

if __name__ == "__main__":
    tray = AgenteZeroTray()
    tray.run()