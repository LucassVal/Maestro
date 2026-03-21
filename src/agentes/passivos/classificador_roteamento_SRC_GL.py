import os
import json
import re

# [CORE] CORTEX - CLASSIFICADOR v47.7
# Intelligent routing based on complexity triage and Tiered MCP Governance.

class ClassificadorPrompts:
    def __init__(self):
        self.config_path = "config/prompts_agents.json"
        self.cortex_path = "config/cortex.json"
        self._carregar_config()

    def _carregar_config(self):
        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                self.config = json.load(f)
            with open(self.cortex_path, "r", encoding="utf-8") as f:
                self.cortex = json.load(f)
        except Exception as e:
            print(f"[ERR] Classificador failed to load configs: {e}")
            self.config = {}
            self.cortex = {}

    def triage_complexity(self, text):
        """Classifica se a tarefa é simples (embaixador) ou estratégica (alto comando)."""
        simple_keywords = ['horas', 'tempo', 'ajuda', 'como', 'o que é', 'explique', 'olá', 'bom dia']
        complex_keywords = ['crie', 'gere', 'audite', 'refatore', 'analise', 'documento', 'script', 'missão']

        text_lower = text.lower()
        # Se contiver palavras complexas, ou NÃO contiver palavras simples -> High Command
        if any(kw in text_lower for kw in complex_keywords):
            return "high_command"
        if any(kw in text_lower for kw in simple_keywords):
            return "ambassador"
        
        return "high_command" # Default para segurança estratégica

    def has_read_only_permission(self, agent_slug):
        """Verifica se o agente tem permissão apenas de leitura no manifesto."""
        try:
            tier_info = self.cortex.get("tier_config", {}).get("tiers", {}).get(agent_slug, {})
            manifest_path = tier_info.get("mcp_manifest")
            
            if not manifest_path or not os.path.exists(manifest_path):
                return False
                
            with open(manifest_path, "r", encoding="utf-8") as f:
                manifest = json.load(f)
                
            return manifest.get("mcp_access") == "READ_ONLY"
        except:
            return False

    def rotear(self, prompt):
        """Executa o roteamento hierárquico v47.7."""
        target = self.triage_complexity(prompt)
        
        if target == "ambassador":
            # O Embaixador pode responder se tiver permissão de leitura (mínimo necessário)
            if self.has_read_only_permission("ambassador"):
                return "ambassador", self.config.get("embaixador")
            else:
                return "high_command", self.config.get("alto_comando")
        
        return "high_command", self.config.get("alto_comando")

    def classificar(self, prompt):
        """Mantém compatibilidade com v46.x (Keywords)."""
        prompt_low = prompt.lower()
        categorias_detectadas = []
        for key, data in self.config.items():
            if key in ["diretrizes_globais", "lucas"]: continue
            keywords = data.get("palavras_chave", [])
            if any(k in prompt_low for k in keywords):
                categorias_detectadas.append(key)
        return categorias_detectadas if categorias_detectadas else ["high_command"]

    def montar_prompt(self, target_agent, prompt_original):
        """Builds the agent-specific prompt based on target."""
        agent_config = self.config.get(target_agent)
        if not agent_config:
            # Fallback para Alto Comando se o target sumiu
            agent_config = self.config.get("alto_comando", {})

        template = agent_config.get("prompt_template", "{entrada}")
        prompt_final = template.replace("{entrada}", prompt_original)
        return prompt_final, agent_config

if __name__ == "__main__":
    cl = ClassificadorPrompts()
    print(f"Triage 'horas': {cl.rotear('Que horas são?')}")
    print(f"Triage 'crie script': {cl.rotear('Crie um script de backup')}")