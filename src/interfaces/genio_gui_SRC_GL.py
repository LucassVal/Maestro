import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import os
import json
import threading
import time
import sys
import subprocess

# Standardized Imports v47.6
from src.agentes.passivos.health_monitor_SRC_GL import HealthMonitor
from src.core.regente_sota_CORE_GL import RegenteSota

# [COUNCIL] GENIO LLM v47.6 - THE EMBASSY
# Premium UI/UX for High Command & Ambassador flow.

VERSION = "47.6 SOTA"
APP_NAME = "GENIO LLM - SOBERANIA"

class GenioGUI:
    def __init__(self, root):
        self.root = root
        self.root.title(f"{APP_NAME} v{VERSION}")
        self.root.geometry("1100x750")
        self.root.configure(bg="#020617")

        self.monitor = HealthMonitor()
        self.regente = RegenteSota()

        # Premium Palette
        self.bg_side = "#0F172A"
        self.bg_main = "#020617"
        self.accent = "#38BDF8" 
        self.gold = "#FDE047"
        self.neon_green = "#22C55E"
        self.critical = "#EF4444"

        self.setup_ui()
        threading.Thread(target=self.real_time_telemetry, daemon=True).start()

    def setup_ui(self):
        # Sidebar (Fiscal 1/10 Overlay)
        self.side = tk.Frame(self.root, bg=self.bg_side, width=280, highlightbackground="#1E293B", highlightthickness=1)
        self.side.pack(side="left", fill="y")
        self.side.pack_propagate(False)

        tk.Label(self.side, text="G E N I O", bg=self.bg_side, fg=self.accent, font=("Impact", 32)).pack(pady=(20, 10))
        tk.Label(self.side, text="SOTA v47.6 | SOVEREIGN", bg=self.bg_side, fg="#64748B", font=("Arial", 9)).pack()

        # Telemetry Labels (FISCAL 1/10)
        self.telemetry_frame = tk.LabelFrame(self.side, text=" [FISCAL 1/10] ", bg=self.bg_side, fg=self.gold, font=("Consolas", 10, "bold"), padx=10, pady=10)
        self.telemetry_frame.pack(pady=20, padx=15, fill="x")

        self.lbl_cpu = tk.Label(self.telemetry_frame, text="CP: [..........] 0%", bg=self.bg_side, fg="white", font=("Consolas", 10), anchor="w")
        self.lbl_cpu.pack(fill="x")
        self.lbl_gpu = tk.Label(self.telemetry_frame, text="GP: [..........] 0%", bg=self.bg_side, fg="white", font=("Consolas", 10), anchor="w")
        self.lbl_gpu.pack(fill="x")
        self.lbl_ram = tk.Label(self.telemetry_frame, text="RM: [..........] 0%", bg=self.bg_side, fg="white", font=("Consolas", 10), anchor="w")
        self.lbl_ram.pack(fill="x")
        self.lbl_vm = tk.Label(self.telemetry_frame, text="VM: [..........] 0%", bg=self.bg_side, fg="white", font=("Consolas", 10), anchor="w")
        self.lbl_vm.pack(fill="x")

        # Action Buttons
        tk.Button(self.side, text="✨ INICIAR MISSÃO", bg=self.accent, fg="#0F172A", font=("Arial", 11, "bold"), 
                  command=self.send, borderwidth=0, cursor="hand2").pack(pady=(20, 5), padx=20, fill="x")
        
        tk.Button(self.side, text="🏺 CONSELHO SOTA", bg="#7C3AED", fg="white", font=("Arial", 10, "bold"), 
                  command=self.run_council, borderwidth=0, cursor="hand2").pack(pady=5, padx=20, fill="x")

        # Chat Area
        self.main_container = tk.Frame(self.root, bg=self.bg_main)
        self.main_container.pack(side="right", expand=True, fill="both", padx=20, pady=20)

        self.chat = scrolledtext.ScrolledText(self.main_container, bg="#0F172A", fg="#E2E8F0", font=("Consolas", 12), borderwidth=0, padx=10, pady=10)
        self.chat.pack(expand=True, fill="both", pady=(0, 10))
        self.chat.tag_configure("user", foreground=self.gold, font=("Consolas", 12, "bold"))
        self.chat.tag_configure("ambassador", foreground=self.accent)
        self.chat.tag_configure("high_command", foreground="#94A3B8", font=("Consolas", 10, "italic"))

        self.chat.insert("end", f"--- {APP_NAME} PORTAL ACTIVE ---\n")
        self.chat.insert("end", "[EMBAIXADOR] Olá Lucas! Sou a sua interface v47.6. O Alto Comando está pronto.\n", "ambassador")

        self.entry = tk.Entry(self.main_container, bg="#1E293B", fg="white", font=("Arial", 14), borderwidth=0, insertbackground="white")
        self.entry.pack(fill="x", ipady=12)
        self.entry.bind("<Return>", lambda e: self.send())

    def get_bar(self, percent):
        blocks = int(percent / 10)
        return "[" + "#" * blocks + "." * (10 - blocks) + "]"

    def real_time_telemetry(self):
        while True:
            try:
                report = self.monitor.check_health()
                sys = report.get("system", {})
                gpu = report.get("gpu", {})
                
                self.lbl_cpu.config(text=f"CP: {self.get_bar(sys.get('cpu_percent', 0))} {sys.get('cpu_percent', 0)}%")
                self.lbl_ram.config(text=f"RM: {self.get_bar(sys.get('ram_percent', 0))} {sys.get('ram_percent', 0)}%")
                self.lbl_vm.config(text=f"VM: {self.get_bar(sys.get('vmem_percent', 0))} {sys.get('vmem_percent', 0)}%")
                
                if gpu:
                    self.lbl_gpu.config(text=f"GP: {self.get_bar(gpu.get('vram_p', 0))} {gpu.get('vram_p', 0):.1f}%")
            except: pass
            time.sleep(2)

    def run_council(self):
        self.entry.insert(0, "/conselho ")
        self.send()

    def send(self):
        text = self.entry.get()
        if not text: return
        self.entry.delete(0, tk.END)
        self.chat.insert("end", f"\n[LUCAS] {text}\n", "user")
        self.chat.see("end")

        threading.Thread(target=self.process_with_mentorship, args=(text,), daemon=True).start()

    def process_with_mentorship(self, input_text):
        # Passo 1: ALTO COMANDO (QWEN 3) planeja
        self.chat.insert("end", "[ALTO COMANDO] Orquestrando plano estratégico...\n", "high_command")
        self.chat.see("end")
        
        # Simulação de resposta estratégica do Alto Comando (ou chamada real ao motor)
        # Para v47.6, usamos um fluxo de prompt:
        try:
            # Aqui chamamos o Regente que agora usa Qwen 3
            plano = self.regente.iniciar_missao(f"planeje: {input_text}")
            
            # Passo 2: EMBAIXADOR (1.5B) traduz
            self.chat.insert("end", "[EMBAIXADOR] Traduzindo diretrizes para interface amigável...\n", "ambassador")
            self.chat.see("end")
            
            # O Embaixador resume o plano técnico
            explicacao = f"Lucas, o Alto Comando planejou o seguinte: {plano[:200]}... e os Soldados já estão em prontidão."
            
            self.chat.insert("end", f"[EMBAIXADOR] {explicacao}\n", "ambassador")
        except Exception as e:
            self.chat.insert("end", f"[ERR] Falha na Mentoria: {e}\n", "high_command")
        
        self.chat.see("end")

if __name__ == "__main__":
    root = tk.Tk()
    app = GenioGUI(root)
    root.mainloop()
