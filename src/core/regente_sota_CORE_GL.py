import os
import json
import uuid
import time
from src.core import eventos_sistema_CORE_GL as eventos_sistema_CORE_GL
from src.core import kernel_genio_CORE_GL as parrudo_core
from src.agentes.passivos import interface_agil_SRC_GL as interface_agil
from src.agentes.ativos import estrategico_agente_SRC_GL as estrategico_agente_SRC_GL
from src.agentes.passivos import openvsx_soldado_SRC_GL as openvsx_soldado_SRC_GL
from src.agentes.passivos.classificador_roteamento_SRC_GL import ClassificadorPrompts
from src.agentes.passivos.extratores.fabrica_extratores_SRC_GL import FabricaExtratores
from src.agentes.ativos import bibliotecario_agente_SRC_GL as bibliotecario
import importlib

# [COUNCIL] AGENT REGISTRY (MAJORS)
AGENTES_FIXOS = {
    "estrategico": estrategico_agente_SRC_GL,
    "vsx": openvsx_soldado_SRC_GL
}

class RegenteSOTA:
    def __init__(self):
        self.classificador = ClassificadorPrompts()
        self.agentes_cache = AGENTES_FIXOS.copy()
        self.bibliotecario = bibliotecario
        self.limite_direto_mb = 50
        self.limite_fracionamento_mb = 500
    
    def decidir_processamento(self, caminhos):
        if not caminhos: return "modo_vazio"
        volume_total_mb = sum(os.path.getsize(c) for c in caminhos if os.path.exists(c)) / (1024 * 1024)
        num_arquivos = len(caminhos)
        print(f"[STATS] VOLUME ANALYSIS: {num_arquivos} files | {volume_total_mb:.2f} MB")
        if volume_total_mb < self.limite_direto_mb and num_arquivos < 100:
            return "modo_direto"
        elif volume_total_mb < self.limite_fracionamento_mb and num_arquivos < 1000:
            return "modo_fracionamento_leve"
        else:
            return "modo_assincrono_massivo"
    
    def executar_com_r2d2(self, tarefa, contexto):
        resultado = self.iniciar_missao(tarefa) 
        from src.agentes.ativos import avaliador_agente_SRC_GL as avaliador
        avaliacao = avaliador.executar({"resposta": str(resultado), "criterios": "as requested by user", "contexto": contexto})
        if not avaliacao.get("aprovado", True):
            from src.agentes.ativos import autocorrecao_agente_SRC_GL as autocorrigir
            dados_correcao = {"missao_id": "R2D2_REFINEMENT", "resposta_original": str(resultado), "feedback": avaliacao.get("feedback"), "tentativa": 1}
            resultado_corrigido = autocorrigir.executar(dados_correcao)
            return resultado_corrigido.get("resposta")
        return resultado
    
    def obter_memoria_recente(self, missao_id, n=3):
        eventos = eventos_sistema_CORE_GL.obter_cronologia(missao_id)
        if not eventos: return "No recent history."
        relevantes = [e for e in eventos if e.get("tipo") in ["TarefaConcluida", "MissaoConcluida", "MissaoClassificada"]]
        fatiados = relevantes[-n:]
        resumo = []
        for e in fatiados:
            tipo = e.get("tipo")
            dados = e.get("dados", {})
            if tipo == "MissaoClassificada":
                resumo.append(f"Intent: {dados.get('categoria')}")
            else:
                res = str(dados.get('resultado', dados.get('res', '')))[:150]
                resumo.append(f"Result: {res}...")
        return "\n".join(resumo)

    def enriquecer_prompt(self, prompt_base, memoria, perfil, cortex, resultado_anterior=None):
        try:
            with open("config/prompts_agents.json", "r", encoding="utf-8") as f:
                prompts_data = json.load(f)
            diretrizes = prompts_data.get("diretrizes_globais", {}).get("instrucao", "")
        except:
            diretrizes = "Golden Rule: Consult GENIO_FILE_REGISTRE_.md and update memory after mission."

        if "_meta" in perfil:
            fingerprint = perfil.get('linguistic_fingerprint', {})
            principios = perfil.get('operating_principles', {})
            preferencias = (
                f"Voice: {fingerprint.get('tone')} | "
                f"DNA: {perfil.get('system_kernel', {}).get('cognitive_architecture')} | "
                f"Principles: {list(principios.keys()) if isinstance(principios, dict) else principios}"
            )
        else:
            preferencias = (
                f"Profile: {perfil.get('nome')} | "
                f"Language: {perfil.get('linguagem_preferida')} | "
                f"Style: {perfil.get('estilo_codigo')}"
            )
        
        contexto_sota = (
            f"\n[GLOBAL GUIDELINES SOTA]\n{diretrizes}\n"
            f"\n[RECENT MEMORY]\n{memoria}\n"
            f"[CONSULTANT DNA (LUCAS)]\n{preferencias}\n"
            f"[CORTEX SYSTEM]\nVersion: {cortex.get('versao')} | Tiers: {list(cortex.get('tier_config', {}).get('tiers', {}).keys())}"
        )
        if resultado_anterior:
            contexto_sota += f"\n[PREVIOUS STEP RESULT]\n{str(resultado_anterior)[:500]}"
        return f"{prompt_base}\n{contexto_sota}"

    def iniciar_missao(self, prompt_usuario, missao_id=None, max_tentativas=2):
        ctx_full = parrudo_core.get_cortex()
        if not missao_id:
            missao_id = f"MISSION_{str(uuid.uuid4())[:8].upper()}"
            eventos_sistema_CORE_GL.registrar_evento("MissionStarted", missao_id, {"prompt": prompt_usuario})
        
        if "conselho" in prompt_usuario.lower() or "debate" in prompt_usuario.lower():
            return self.executar_conselho(prompt_usuario, missao_id)

        self.bibliotecario.executar({"modo": "pre_missao", "missao_id": missao_id})
        print(f"\n--- [[COUNCIL]] REGENT REACTIVE SOTA ELITE (ID: {missao_id}) ---")
        
        caminhos_encontrados = self._extrair_caminhos(prompt_usuario)
        contexto_multimodal = ""
        if caminhos_encontrados:
            print(f"[SCAN] [BOOSTER] Detected {len(caminhos_encontrados)} files. Starting extraction...")
            for caminho in caminhos_encontrados:
                extrator = FabricaExtratores.obter_extrator(caminho)
                if extrator:
                    instancia = extrator()
                    res = instancia.executar({"caminho": caminho, "pergunta": prompt_usuario})
                    if res.get("status") == "SUCCESS":
                        contexto_multimodal += f"\n--- [CONTENT: {os.path.basename(caminho)}] ---\n"
                        contexto_multimodal += res.get("texto", str(res.get("conteudo", "")))
        
        if contexto_multimodal:
            prompt_usuario = f"{prompt_usuario}\n\n[EXTRACTED DATA (BOOSTERS)]\n{contexto_multimodal}"

        modo = self.decidir_processamento(caminhos_encontrados)
        print(f"[GOAL] OPERATION MODE: {modo.upper()}")
        categorias = self.classificador.classificar(prompt_usuario)
        
        if modo == "modo_assincrono_massivo":
             return "Task scheduled for asynchronous processing."

        if not categorias:
            resumo_interface = interface_agil.processar_entrada(prompt_usuario)
            missao_refinada = interface_agil.preparar_para_supremo(prompt_usuario, resumo_interface)
            return AGENTES_FIXOS["estrategico"].executar({"missao_id": missao_id, "dados": missao_refinada})

        resultado_anterior = self._executar_fluxo_standard(categorias, prompt_usuario, missao_id, max_tentativas, ctx_full, modo)
        self.bibliotecario.executar({"modo": "pos_missao", "missao_id": missao_id})
        return resultado_anterior

    def _extrair_caminhos(self, prompt):
        import re
        caminhos = re.findall(r'["\'](.*?\.\w+)["\']', prompt)
        return [c for c in caminhos if os.path.exists(c)]

    def executar_conselho(self, prompt_usuario, missao_id):
        eventos_sistema_CORE_GL.registrar_evento("COUNCIL_STARTED", missao_id, {"prompt": prompt_usuario})
        especialistas = ["engenheiro", "auditor", "pesquisador"]
        contribuicoes = {}
        for esp in especialistas:
            contribuicoes[f"cadeira_{esp}"] = f"Technical analysis from {esp} for: {prompt_usuario}"
        from src.agentes.ativos import moderador_agente_SRC_GL as moderador_agente_SRC_GL
        resultado = moderador_agente_SRC_GL.executar({"missao_id": missao_id, "comando_original": prompt_usuario, "contribuicoes": contribuicoes})
        eventos_sistema_CORE_GL.registrar_evento("COUNCIL_FINISHED", missao_id, {"resultado": resultado.get("consenso")})
        return resultado.get("consenso")

    def _executar_fluxo_standard(self, categorias, prompt_usuario, missao_id, max_tentativas, ctx_full, modo="modo_direto"):
        resultado_anterior = None
        perfil = self.classificador.lucas
        for idx, cat in enumerate(categorias):
            print(f"[ ] Stage {idx+1}/{len(categorias)}: Processing '{cat}'...")
            eventos_sistema_CORE_GL.registrar_evento("AGENT_STARTED", missao_id, {"etapa": cat})
            tentativa = 0
            aprovado = False
            while tentativa <= max_tentativas and not aprovado:
                tentativa += 1
                memoria = self.obter_memoria_recente(missao_id)
                prompt_base, dados_agente = self.classificador.montar_prompt(cat, prompt_usuario)
                prompt_final = self.enriquecer_prompt(prompt_base, memoria, perfil, ctx_full, resultado_anterior)
                agente_arq = dados_agente.get("agente", "").replace(".py", "")
                try:
                    if agente_arq not in self.agentes_cache:
                        try:
                            modulo = importlib.import_module(f"src.agentes.ativos.{agente_arq}")
                        except ImportError:
                            try:
                                modulo = importlib.import_module(f"src.agentes.passivos.{agente_arq}")
                            except ImportError:
                                modulo = importlib.import_module(agente_arq)
                        self.agentes_cache[agente_arq] = modulo
                    agente = self.agentes_cache[agente_arq]
                    resultado_atual = agente.executar({"prompt": prompt_final, "modelo": dados_agente.get("modelo"), "contexto": dados_agente, "missao_id": missao_id, "anterior": resultado_anterior, "modo_operacao": modo})
                    if isinstance(resultado_atual, dict) and resultado_atual.get("workflow") == "reflexivo":
                        prompts = resultado_atual.get("prompts", [])
                        ultimo_resultado = ""
                        for s_idx, p_stage in enumerate(prompts):
                            stage_input = f"{p_stage}\n\n[PREVIOUS DATA]\n{ultimo_resultado}"
                            ultimo_resultado = parrudo_core.chat(stage_input, modelo=dados_agente.get("modelo"))
                        resultado_atual = ultimo_resultado
                    from src.agentes.ativos import avaliador_agente_SRC_GL as avaliador_agente_SRC_GL
                    avaliacao = avaliador_agente_SRC_GL.executar({"resposta": str(resultado_atual), "criterios": "as requested by user", "contexto": cat})
                    agente_modulo = None
                    entrada = {"missao_id": missao_id, "comando": prompt_usuario, "resposta": resultado_atual, "avaliacao": avaliacao}
                    intention = cat.lower() 
                    if intention in ["react", "python", "nodejs"]:
                        from src.agentes.ativos import vanguarda_agente_SRC_GL as vanguarda_agente_SRC_GL
                        agente_modulo = vanguarda_agente_SRC_GL
                        entrada["especialista"] = intention
                    from src.agentes.ativos import supervisor_agente_SRC_GL as supervisor_agente_SRC_GL
                    resultado_supervisionado = supervisor_agente_SRC_GL.executar(entrada)
                    if avaliacao.get("aprovado") or tentativa > max_tentativas:
                        aprovado = True
                        resultado_anterior = resultado_supervisionado
                    else:
                        from src.agentes.ativos import autocorrecao_agente_SRC_GL as autocorrecao_agente_SRC_GL
                        resultado_corrigido = autocorrecao_agente_SRC_GL.executar({"missao_id": missao_id, "resposta_original": str(resultado_atual), "feedback": avaliacao.get("feedback"), "tentativa": tentativa})
                        resultado_anterior = resultado_corrigido.get("resposta")
                except Exception as e:
                    print(f"[ERR] Critical Error in '{cat}': {e}")
                    break
            eventos_sistema_CORE_GL.registrar_evento("AGENT_FINISHED", missao_id, {"etapa": cat})
            eventos_sistema_CORE_GL.registrar_evento("TarefaConcluida", missao_id, {"categoria": cat, "agente": agente_arq, "res": str(resultado_anterior)[:200]})
        eventos_sistema_CORE_GL.registrar_evento("MissaoConcluida", missao_id, {"resultado_final": str(resultado_anterior)[:500]})
        return resultado_anterior

regente_global = RegenteSOTA()
def iniciar_missao(prompt_usuario, missao_id=None):
    return regente_global.iniciar_missao(prompt_usuario, missao_id)
