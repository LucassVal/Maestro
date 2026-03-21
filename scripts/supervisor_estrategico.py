import ollama
import os
import json
import glob
import time

# [COUNCIL] SUPERVISOR ESTRATÉGICO v1.1
# Analisa o event_store e gera sugestões de evolução via Qwen 3 (Alto Comando).

EVENT_DIR = os.path.join(".panda", "memory", "eventos_sistema_CORE_GL")
SUGESTOES_DIR = os.path.join(".panda", "sugestoes")

def carregar_logs_recentes(limit=5):
    """Carrega os logs das últimas 'limit' missões."""
    if not os.path.exists(EVENT_DIR):
        return ""
    # Encontra arquivos de missão (MISSAO_*.json)
    arquivos = glob.glob(os.path.join(EVENT_DIR, "*.json"))
    arquivos.sort(key=os.path.getmtime, reverse=True)
    resumo = "--- RELATÓRIO DE MISSÕES RECENTES ---\n\n"
    missoes_vistas = set()
    for f in arquivos:
        try:
            with open(f, "r", encoding="utf-8") as file:
                ev = json.load(file)
                m_id = ev.get("missao_id") or os.path.basename(f)
                if m_id not in missoes_vistas:
                    resumo += f"ID: {m_id}\nTIPO: {ev.get('tipo')}\nDADOS: {json.dumps(ev.get('dados'), ensure_ascii=False)[:300]}...\n\n"
                    missoes_vistas.add(m_id)
                if len(missoes_vistas) >= limit:
                    break
        except:
            continue
    return resumo

def analisar_estrategia():
    print("[[COUNCIL]] Alto Command (Qwen 3) despertando...")
    logs = carregar_logs_recentes()
    if not logs:
        print("[[WARN]] Nenhum log encontrado para análise.")
        return "Nenhum log disponível."
    
    # Prompt para o Alto Command
    prompt = f"Analise o seguinte resumo de logs e sugira 3 melhorias táticas ou novas bibliotecas para o repositório:\n\n{logs}"
    
    try:
        print("[[BRAIN]] Qwen 3 analisando padrões em CPU/RAM...")
        response = ollama.generate(model="alto-comando", prompt=prompt)
        sugestao_texto = response.get("response", "Erro na análise.")
        
        # Salva sugestão
        if not os.path.exists(SUGESTOES_DIR):
            os.makedirs(SUGESTOES_DIR)
        
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        sug_file = os.path.join(SUGESTOES_DIR, f"sugestao_{timestamp}.txt")
        with open(sug_file, "w", encoding="utf-8") as f:
            f.write(sugestao_texto)
        
        print(f"[[OK]] Análise concluída. Sugestão salva em: {sug_file}")
        return sugestao_texto
    except Exception as e:
        err_msg = f"OLLAMA ERROR: {e}"
        print(f"[[ERR]] {err_msg}")
        return err_msg

if __name__ == "__main__":
    analisar_estrategia()
