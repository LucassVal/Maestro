import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import os
import json
import threading
import time
import sys

# Standardized Imports v45.3
import src.agentes.passivos.desktop_logger_SRC_GL as desktop_logger
from src.agentes.passivos.terminal_soldier_SOTA_v45 import terminal_soldier_SOTA as terminal_soldado_SRC_GL
from src.agentes.passivos.openvsx_soldado_SRC_GL import openvsx_soldado_SRC_GL

# [COUNCIL] GENIO LLM v27.0 - PARRUDO ENGINE
# 100% Native. Optimized for 4GB VRAM + iGPU Iris.

VERSION = "27.0 SOTA"
APP_NAME = "GENIO LLM - PARRUDO MODE"

class GenioGUI:
    def __init__(self, root):
        self.root = root
        self.root.title(f"{APP_NAME} v{VERSION} (iGPU Iris Ready)")
        self.root.geometry("1100x750")
        self.root.configure(bg="#020617")

        # Premium Colors
        self.bg_side = "#0F172A"
        self.bg_main = "#020617"
        self.accent = "#38BDF8" 
        self.stop_red = "#EF4444" 
        self.gold = "#FDE047"
        self.magenta = "#D946EF"
        self.neon_green = "#22C55E"

        self.root_path = os.getcwd()
        self.setup_ui()
        threading.Thread(target=self.update_stats, daemon=True).start()

    def setup_ui(self):
        # Sidebar
        self.side = tk.Frame(self.root, bg=self.bg_side, width=240, highlightbackground="#1E293B", highlightthickness=1)
        self.side.pack(side="left", fill="y")
        self.side.pack_propagate(False)

        tk.Label(self.side, text="G E N I O", bg=self.bg_side, fg=self.accent, font=("Impact", 28)).pack(pady=(20, 0))

        # Strategic Buttons
        tk.Button(self.side, text="[MISSION] START MISSION", bg=self.gold, fg="#0F172A", font=("Arial", 11, "bold"), 
                  command=self.run_mission, borderwidth=0, cursor="hand2").pack(pady=(30, 5), padx=20, fill="x")
        
        tk.Button(self.side, text="[COUNCIL] SUMMON COUNCIL", bg="#7C3AED", fg="white", font=("Arial", 10, "bold"), 
                  command=self.run_council, borderwidth=0, cursor="hand2").pack(pady=5, padx=20, fill="x")

        # Main Workspace (Tabs)
        self.main_container = tk.Frame(self.root, bg=self.bg_main)
        self.main_container.pack(side="right", expand=True, fill="both", padx=20, pady=20)

        self.notebook = ttk.Notebook(self.main_container)
        self.notebook.pack(expand=True, fill="both")

        # --- TAB 1: COMMAND ---
        self.tab_comando = tk.Frame(self.notebook, bg=self.bg_main)
        self.notebook.add(self.tab_comando, text=" [CHAT] COMMAND ")
        
        self.chat = scrolledtext.ScrolledText(self.tab_comando, bg="#0F172A", fg="#E2E8F0", font=("Consolas", 11))
        self.chat.pack(expand=True, fill="both", pady=(0, 10))
        self.chat.insert("end", f"--- {APP_NAME} v{VERSION} ACTIVE ---\n")

        input_frame = tk.Frame(self.tab_comando, bg=self.bg_main)
        input_frame.pack(fill="x")
        self.entry = tk.Entry(input_frame, bg="#1E293B", fg="white", font=("Arial", 13), borderwidth=0)
        self.entry.pack(side="left", expand=True, fill="x", ipady=10)
        self.entry.bind("<Return>", lambda e: self.send())
        tk.Button(input_frame, text="SEND [BOOST]", bg=self.accent, fg="#0F172A", command=self.send, font=("Arial", 10, "bold")).pack(side="right", padx=10)

    def run_mission(self):
        task = self.entry.get()
        if not task: return
        self.entry.delete(0, tk.END)
        self.chat.insert("end", f"\n[[MISSION]] GENIO MISSION: {task}\n")
        from src.core import regente_sota_CORE_GL as regente
        threading.Thread(target=lambda: regente.iniciar_missao(task), daemon=True).start()

    def run_council(self):
        task = self.entry.get()
        if not task: return
        self.entry.delete(0, tk.END)
        self.chat.insert("end", f"\n[[COUNCIL]] COUNCIL SESSION: {task}\n")
        from src.core import regente_sota_CORE_GL as regente
        threading.Thread(target=lambda: regente.iniciar_missao(f"conselho {task}"), daemon=True).start()

    def send(self):
        text = self.entry.get()
        if not text: return
        self.chat.insert("end", f"\n[USER] YOU: {text}\n")
        self.entry.delete(0, tk.END)
        if "council" in text.lower() or "conselho" in text.lower():
            self.run_council()
        else:
            self.run_mission()

    def update_stats(self):
        while True:
            time.sleep(10)

if __name__ == "__main__":
    root = tk.Tk()
    GenioGUI(root)
    root.mainloop()
