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
            "cpu_percent": 90
        }
        if not os.path.exists(".panda/logs"):
            os.makedirs(".panda/logs")

    def log_event(self, level, msg):
        ts = time.strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_path, "a", encoding="utf-8") as f:
            f.write(f"[{ts}] [{level}] {msg}\n")

    def get_gpu_stats(self):
        try:
            cmd = "nvidia-smi --query-gpu=memory.used,memory.total,temperature.gpu --format=csv,noheader,nounits"
            res = subprocess.check_output(cmd, shell=True).decode().strip()
            used, total, temp = map(int, res.split(", "))
            vram_p = (used / total) * 100
            return {"vram_p": vram_p, "temp": temp, "used": used}
        except:
            return None

    def get_system_health(self):
        """Returns standard system metrics."""
        return {
            "cpu_percent": psutil.cpu_percent(interval=None),
            "ram_percent": psutil.virtual_memory().percent,
            "disk_percent": psutil.disk_usage('/').percent
        }

    def check_health(self):
        stats = self.get_gpu_stats()
        alerts = []
        if stats:
            if stats["vram_p"] > self.thresholds["vram_percent"]:
                alerts.append(f"CRITICAL VRAM: {stats['vram_p']:.1f}% used!")
            if stats["temp"] > self.thresholds["gpu_temp"]:
                alerts.append(f"HIGH TEMP: {stats['temp']} C!")
        
        system_stats = self.get_system_health()
        if system_stats["cpu_percent"] > self.thresholds["cpu_percent"]:
            alerts.append(f"HIGH CPU: {system_stats['cpu_percent']}%")

        for alert in alerts:
            self.log_event("WARNING", alert)
            
        return stats, alerts

if __name__ == "__main__":
    monitor = HealthMonitor()
    stats, alerts = monitor.check_health()
    print(f"Stats: {stats} | Alerts: {alerts}")
