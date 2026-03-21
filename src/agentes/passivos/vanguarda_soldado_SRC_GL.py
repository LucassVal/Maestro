import os
import json
import time
import urllib.request
import urllib.parse
from .soldados import pesquisar_web, _salvar_cache, _carregar_cache, listar_arquivos

# SOLDADO DE VANGUARDA v1.0 - EXPLORADOR TECNOLÓGICO
# Focado em GitHub, News e Ranking de Relevância.

def pesquisar_github_avancado(tech, stars=1000, **kwargs):
    """Busca repositórios populares no GitHub para entender tendências."""
    print(f"[ ] Soldado Vanguarda explorando GitHub em busca de {tech}...")
    try:
        query = f"{tech} stars:>{stars} pushed:>2026-01-01"
        url = f"https://api.github.com/search/repositories?q={urllib.parse.quote(query)}&sort=stars&order=desc"
        req = urllib.request.Request(url, headers={"User-Agent": "Parrudo-Vanguarda/1.0"})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            items = data.get("items", [])[:5]
            resultados = []
            for item in items:
                resultados.append({
                    "titulo": item["full_name"],
                    "link": item["html_url"],
                    "snippet": item["description"],
                    "stars": item["stargazers_count"]
                })
            return resultados
    except Exception as e:
        # Fallback para busca web comum se falhar GitHub (ex: rate limit)
        print(f"[!] GitHub API Falhou, usando Web Fallback: {e}")
        return pesquisar_web(f"{tech} trending repositories 2026")

def ranquear_tecnologias():
    """Analisa os eventos_sistema_CORE_GL para descobrir quais techs o Lucas mais usa."""
    print(f"[[STATS]] Analisando o 'Campo de Batalha' para ranquear tecnologias...")
    event_dir = os.path.join(".panda", "memory", "eventos_sistema_CORE_GL")
    if not os.path.exists(event_dir):
        return {}
    counts = {}
    # Lê os últimos 100 eventos de missões
    files = sorted(listar_arquivos(event_dir, "json"), key=os.path.getmtime, reverse=True)[:100]
    for f in files:
        try:
            with open(f, "r", encoding="utf-8") as file:
                data = json.load(file)
                prompt = str(data.get("dados", {}).get("prompt", "")).lower()
                # Techs que queremos monitorar
                techs_alvo = ["python", "react", "next", "java", "node", "rust", "go", "sql", "docker", "aws"]
                for t in techs_alvo:
                    if t in prompt:
                        counts[t] = counts.get(t, 0) + 1
        except:
            continue
    return counts

def atualizar_config_vanguarda():
    """Atualiza o arquivo de configuração com o novo ranking."""
    ranking = ranquear_tecnologias()
    config_path = os.path.join(".panda", "vanguarda_config.json")
    if os.path.exists(config_path):
        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)
            # Atualiza uso nos hubs
            for hub_name, hub_data in config["hubs"].items():
                for tech_name, tech_info in hub_data["especialistas"].items():
                    if tech_name in ranking:
                        tech_info["uso"] = ranking[tech_name]
            # Gera lista de ranking global
            global_ranking = sorted(ranking.items(), key=lambda x: x[1], reverse=True)
            config["ranking_global"] = [x[0] for x in global_ranking]
            with open(config_path, "w", encoding="utf-8") as f:
                json.dump(config, f, indent=4, ensure_ascii=False)
            print(f"[[OK]] Ranking de Vanguarda atualizado: {config['ranking_global'][:5]}")
            return config
    return None

def executar(entrada=None):
    """Interface padrão para o Regente."""
    print("[OK] Vanguarda Online (Explorador Pronto).")
    return "Vanguarda Operacional."

if __name__ == "__main__":
    print(executar())
