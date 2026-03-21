import os
import json
import platform
import subprocess
import shutil

# [WIZARD] CONFIGURATION ASSISTANT v46.0 - GL
# Detects hardware and optimizes cortex.json for Genio LLM.

def get_ram():
    """Returns total RAM in GB."""
    try:
        import psutil
        return round(psutil.virtual_memory().total / (1024**3))
    except ImportError:
        # Fallback using system command
        if platform.system() == "Windows":
            out = subprocess.check_output("wmic ComputerSystem get TotalPhysicalMemory", shell=True).decode()
            ram_bytes = int(out.split()[1])
            return round(ram_bytes / (1024**3))
    return 8

def get_gpu_vram():
    """Detects NVIDIA VRAM in GB or returns 0 for iGPU."""
    try:
        out = subprocess.check_output("nvidia-smi --query-gpu=memory.total --format=csv,noheader,nounits", shell=True).decode()
        return round(int(out.strip()) / 1024)
    except:
        return 0

def optimize_cortex():
    ram = get_ram()
    vram = get_gpu_vram()
    
    print(f"--- [WIZARD] GENIO HARDWARE DETECTION ---")
    print(f"[HW] RAM Detected: {ram}GB")
    print(f"[HW] VRAM Detected: {vram}GB")
    
    cortex = {
        "versao": "46.0",
        "hardware_perfil": "Iris iGPU" if vram < 4 else "NVIDIA RTX",
        "cpu_usage": "Parrudo" if ram >= 16 else "Economy",
        "gpu_layers": 32 if vram >= 8 else (16 if vram >= 4 else 0),
        "turbo_context": ram * 100000 # Approximation
    }
    
    config_path = "config/cortex.json"
    os.makedirs("config", exist_ok=True)
    
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(cortex, f, indent=4)
    
    print(f"[SUCCESS] optimized cortex.json saved to {config_path}")
    print(f"[SOTA] Hardware optimized for {cortex['hardware_perfil']} mode.")

if __name__ == "__main__":
    optimize_cortex()
