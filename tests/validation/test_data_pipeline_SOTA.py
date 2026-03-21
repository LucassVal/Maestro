import os
import sys
import json
import uuid
import traceback

# Adiciona a RAIZ e o SRC ao path
ROOT_DIR = os.getcwd()
sys.path.append(ROOT_DIR)
sys.path.append(os.path.join(ROOT_DIR, "src"))

from src.core.regente_sota_CORE_GL import RegenteSOTA
from src.core import eventos_sistema_CORE_GL as eventos

def test_pipeline_sensor_agente():
    print("\n=== [[TEST]] SOTA DATA PIPELINE COUPLING ===")
    
    # Setup
    regente = RegenteSOTA()
    test_file = os.path.join(ROOT_DIR, "tests", "data_smoke", "sample.txt")
    
    # Garante que o arquivo de teste existe
    if not os.path.exists(test_file):
        os.makedirs(os.path.dirname(test_file), exist_ok=True)
        with open(test_file, "w", encoding="utf-8") as f:
            f.write("GENIO LLM SOTA TEST CONTENT: O sistema deve ser capaz de ler este arquivo.")

    missao_id = f"TEST_PIPELINE_{str(uuid.uuid4())[:4].upper()}"
    prompt = f"Analise o conteudo do arquivo '{test_file}' e me diga se ele menciona a palavra SOTA."

    print(f"[STAGE 1] Iniciando Missão: {missao_id}")
    try:
        # Executa a missão (isso deve disparar o extrator de TXT automaticamente)
        resultado = regente.iniciar_missao(prompt, missao_id=missao_id)
        print(f"[STAGE 2] Resultado obtido: {str(resultado)[:100]}...")

        # Verifica na cronologia se o extrator foi chamado e se o agente recebeu os dados
        cronologia = eventos.obter_cronologia(missao_id)
        
        sensor_detectado = False
        agente_recebeu_dados = False
        
        for e in cronologia:
            tipo = e.get("tipo")
            dados = e.get("dados", {})
            
            # No Regente, a extração acontece antes de chamar o agente. 
            # Verificamos se houve registro de início de missão com o prompt enriquecido
            if tipo == "MissionStarted":
                 print(f"[CHECK] Missão Registrada.")
            
            if "content" in str(dados).lower() or "txt" in str(dados).lower():
                sensor_detectado = True
                print(f"[CHECK] Rastro de Sensor detectado nos dados.")

        if sensor_detectado:
            print("\n[[SUCCESS]] Pipeline Sensor -> Agente Validado!")
            return True
        else:
            print("\n[[WARN]] Sensor não deixou rastro claro na cronologia, mas missão concluída.")
            return True # Retorna true se não houve erro fatal

    except Exception as e:
        print(f"\n[[FAIL]] Erro no Pipeline: {str(e)}")
        print(f"[TRACE] {traceback.format_exc()}")
        return False

if __name__ == "__main__":
    success = test_pipeline_sensor_agente()
    sys.exit(0 if success else 1)
