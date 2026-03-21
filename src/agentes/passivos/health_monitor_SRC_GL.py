import os
import time
import subprocess
import json
import psutil

class HealthMonitor:
    def __init__(self):
        self.log_path = ".panda/logs/sys_health.log"
        self.thresholds = {
            "vram_percent": 90,
            "gpu_temp": 82, # Celsius
            "cpu_percent": 90,
            "vmem_percent": 85
        }
        if not os.path.exists(".panda/logs"):
            os.makedirs(".panda/logs")

    def log_event(self, level, msg):
        ts = time.strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_path, "a", encoding="utf-8") as f:
            f.write(f"[{ts}] [{level}] {msg}\n")

    def get_gpu_stats(self):
        """Coleta estatísticas de GPUs NVIDIA."""
        try:
            cmd = "nvidia-smi --query-gpu=memory.used,memory.total,temperature.gpu --format=csv,noheader,nounits"
            res = subprocess.check_output(cmd, shell=True).decode().strip()
            if not res: return None
            used, total, temp = map(int, res.split(", "))
            vram_p = (used / total) * 100
            return {"vram_p": vram_p, "temp": temp, "used": used, "total": total}
        except:
            return None

    def get_igpu_info(self):
        """Detecta iGPU Intel Iris via WMIC."""
        try:
            cmd = "wmic path win32_videocontroller get name"
            res = subprocess.check_output(cmd, shell=True).decode().strip()
            return "Iris" in res or "Intel" in res
        except:
            return False

    def get_ollama_status(self):
        """Verifica quais modelos estão carregados no Ollama."""
        try:
            cmd = "ollama ps"
            res = subprocess.check_output(cmd, shell=True).decode().split('\n')
            models = []
            for line in res[1:]: # Skip header
                if line.strip():
                    models.append(line.split()[0])
            return models
        except:
            return []

    def get_system_health(self):
        """Retorna métricas unificadas para o Dashboard 1/10."""
        vmem = psutil.swap_memory()
        ram = psutil.virtual_memory()
        
        return {
            "cpu_percent": psutil.cpu_percent(interval=None),
            "ram_percent": ram.percent,
            "vmem_percent": vmem.percent,
            "disk_percent": psutil.disk_usage('/').percent,
            "llms_active": self.get_ollama_status(),
            "igpu_detected": self.get_igpu_info()
        }

    def check_health(self):
        stats = self.get_gpu_stats()
        system_stats = self.get_system_health()
        alerts = []
        
        if stats:
            if stats["vram_p"] > self.thresholds["vram_percent"]:
                alerts.append(f"CRITICAL VRAM: {stats['vram_p']:.1f}%!")
        
        if system_stats["cpu_percent"] > self.thresholds["cpu_percent"]:
            alerts.append(f"HIGH CPU: {system_stats['cpu_percent']}%")
            
        if system_stats["vmem_percent"] > self.thresholds["vmem_percent"]:
            alerts.append(f"HIGH VMEM: {system_stats['vmem_percent']}%")

        for alert in alerts:
            self.log_event("WARNING", alert)
            
        return {"gpu": stats, "system": system_stats, "alerts": alerts}

if __name__ == "__main__":
    monitor = HealthMonitor()
    report = monitor.check_health()
    print(json.dumps(report, indent=4))
