import os
import json
import src.agentes.passivos.genio_core_SRC_GL as genio_core

def materializar_agente(nome_agente, especialidade, objetivo):
    """
    Motor de Auto-Expansão v16.5: Cria um novo script e atualiza o córtex.
    """
    print(f"[ ] Materializando Agente: {nome_agente}...")
    
    # 1. Gerar o Código do Agente (Template Base)
    script_path = f"src/agentes/passivos/agente_{nome_agente}_SRC_GL.py"
    template = f'''import src.agentes.passivos.genio_core_SRC_GL as genio_core
import src.interfaces.event_store_SRC_GL as event_store

def executar(entrada=None):
    print(f"[ ] Agente {nome_agente} em operação...")
    ctx = genio_core.get_cortex()
    modelo = ctx.get("jogadores_do_imperio", {{}}).get("{nome_agente}", {{}}).get("modelo_elite", "qwen2.5:1.5b")
    prompt = f"SISTEMA: Atue como {especialidade}. OBJETIVO: {objetivo}"
    res = genio_core.query_ollama(modelo, prompt)
    return res.get("response", "Erro na execução.")

if __name__ == "__main__":
    executar()
'''
    with open(script_path, "w", encoding="utf-8") as f:
        f.write(template)

    # 2. Atualizar cortex.json
    cortex = genio_core.get_cortex()
    if "jogadores_do_imperio" not in cortex:
        cortex["jogadores_do_imperio"] = {}
        
    cortex["jogadores_do_imperio"][nome_agente] = {
        "especialidade": especialidade,
        "modelo_elite": "qwen2.5:1.5b",
        "rank": "Cabo",
        "objetivo_padrao": objetivo
    }
    
    with open("config/cortex.json", "w", encoding="utf-8") as f:
        json.dump(cortex, f, indent=4, ensure_ascii=False)
        
    print(f"[OK] Agente {nome_agente} materializado e registrado no Córtex!")

def executar(entrada=None):
    """Interface padrão para o Regente."""
    if entrada and "nome" in entrada:
        return materializar_agente(entrada["nome"], entrada.get("especialidade", "Geral"), entrada.get("objetivo", "Executar ordens."))
    return "Aguardando parâmetros de materialização..."

if __name__ == "__main__":
    # Exemplo: Criar um batedor de segurança
    materializar_agente("vigia_rede", "Segurança de Rede", "Monitorar logs de conexão e alertar sobre IPs suspeitos.")