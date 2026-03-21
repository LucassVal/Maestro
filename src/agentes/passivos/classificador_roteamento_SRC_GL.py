import os
import json
import re

# [CORE] CORTEX - CLASSIFICADOR v46.2
# Intelligent routing based on prompt intent and agent manifest.

class ClassificadorPrompts:
    def __init__(self):
        self.config_path = "config/prompts_agents.json"
        self.lucas_path = "config/perfil_lucas.json"
        self._carregar_config()

    def _carregar_config(self):
        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                self.config = json.load(f)
            with open(self.lucas_path, "r", encoding="utf-8") as f:
                self.lucas = json.load(f)
        except Exception as e:
            print(f"[ERR] Classificador failed to load configs: {e}")
            self.config = {}
            self.lucas = {"nome": "[FOUNDER]", "linguagem_preferida": "pt-BR"}

    def classificar(self, prompt):
        """Classifies the intent based on keywords in prompts_agents.json."""
        prompt_low = prompt.lower()
        categorias_detectadas = []
        
        # Iterate over agents in prompts_agents.json
        for key, data in self.config.items():
            if key in ["diretrizes_globais", "lucas"]: continue
            keywords = data.get("palavras_chave", [])
            if any(k in prompt_low for k in keywords):
                categorias_detectadas.append(key)
                
        return categorias_detectadas if categorias_detectadas else ["generalista"]

    def montar_prompt(self, categoria, prompt_original):
        """Builds the agent-specific prompt and returns its config."""
        agent_config = self.config.get(categoria, {})
        
        if not agent_config:
            # Fallback for unknown categories
            agent_config = {
                "agente": "estrategico_agente_SRC_GL",
                "modelo": "deepseek-r1:7b",
                "prompt_template": "Aja como um estrategista generalista: {entrada}"
            }
        
        template = agent_config.get("prompt_template", "{entrada}")
        prompt_final = template.replace("{entrada}", prompt_original)
        
        return prompt_final, agent_config