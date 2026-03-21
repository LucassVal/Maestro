import os
import json
import urllib.request
import time
import src.agentes.passivos.desktop_logger_SRC_GL as desktop_logger
from src.interfaces.proposta_acao_SRC_GL import PropostaAcao

class BatedorOportunidades:
    def __init__(self):
        self.libs_dir = ".panda/libraries"
        self.meta_path = ".panda/libraries/meta.json"

    def analisar_e_propor(self):
        """Identifica bibliotecas de elite e propõe compartilhamento."""
        if not os.path.exists(self.meta_path):
            return "Erro: Meta.json não encontrado."
            
        with open(self.meta_path, "r", encoding="utf-8") as f:
            meta = json.load(f)
            
        candidatas = []
        for nome, info in meta.items():
            # Critérios SOTA v10.0: Alta fidelidade e reuso comprovado
            if info.get("sucesso", 0) >= 90 and info.get("usos", 0) >= 5:
                candidatas.append({"nome": nome, "info": info})
        
        if not candidatas:
            return "Nenhuma candidata de elite encontrada no momento."
            
        # Gera proposta para a primeira candidata (MVP)
        target = candidatas[0]
        return self._gerar_proposta_suprema(target)

    def _gerar_proposta_suprema(self, biblioteca):
        """Chama o Supremo para formatar o pacote de contribuição."""
        url = "http://localhost:11434/api/generate"
        prompt = f"""
        Você é o SUPREMO ESTRATEGISTA. Identificamos uma biblioteca de elite:
        Nome: {biblioteca['nome']}
        Info: {biblioteca['info']}
        
        Crie um pacote de contribuição Digital:
        1. Nome do repositório (ex: parrudo-python-utils)
        2. Breve descrição para o README.
        3. Mensagem de commit.
        Responda APENAS em JSON com as chaves: nome_repo, readme_summary, commit_msg.
        """
        data = {"model": "qwen3:8b", "prompt": prompt, "stream": False, "format": "json"}
        start_time = time.time()
        
        try:
            req = urllib.request.Request(url, data=json.dumps(data).encode("utf-8"))
            with urllib.request.urlopen(req) as res:
                response_time = time.time() - start_time
                resp = json.loads(res.read().decode())
                dados_proposta = json.loads(resp["response"])
                
                # Registra a proposta
                pa = PropostaAcao()
                prop_id = pa.criar_proposta(tipo="github_publicar", dados={
                    "lib_origem": biblioteca['nome'],
                    "sugestao": dados_proposta
                })
                return f"Proposta {prop_id} criada para a biblioteca {biblioteca['nome']}."
        except Exception as e:
            return f"Erro ao gerar proposta: {e}"

def executar(entrada=None):
    """Interface padrão para o Regente."""
    bo = BatedorOportunidades()
    return bo.analisar_e_propor()

if __name__ == "__main__":
    print(executar())
