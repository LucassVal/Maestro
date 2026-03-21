import sys
import os
import json
import traceback
from tests.validation.validation_utils import capture_resources, evaluate_with_auditor

# Adiciona a RAIZ e o SRC ao path
ROOT_DIR = os.getcwd()
sys.path.append(ROOT_DIR)
sys.path.append(os.path.join(ROOT_DIR, "src"))

AGENTS_TO_TEST = [
    {"nome": "estrategico", "prompt": "Responda APENAS 'CORE_ONLINE'"},
    {"nome": "auditor", "prompt": "Como você avalia a integridade de um sistema?"}
]

@capture_resources
def test_elite_accuracy():
    results = []
    
    try:
        from src.core.regente_sota_CORE_GL import RegenteSOTA
        regente = RegenteSOTA()
        
        for agent in AGENTS_TO_TEST:
            res = regente.iniciar_missao(agent['prompt'])
            output_str = str(res)
            
            # Integração com o Agente Auditor para dar nota
            score, feedback = evaluate_with_auditor(agent['prompt'], output_str)
            
            results.append({
                "component": f"Agente {agent['nome'].capitalize()}",
                "level": "SAT",
                "input": agent['prompt'],
                "output": output_str[:200], # Trucado para o log
                "status": "PASS" if score >= 7 else "FAIL",
                "score": score,
                "evaluator_feedback": feedback,
                "feedback": f"Certificação semântica concluída. Nota: {score}/10"
            })
            
    except Exception as e:
        results.append({
            "component": "Elite Agents Cluster",
            "level": "SAT",
            "input": "N/A",
            "output": "N/A",
            "status": "FAIL",
            "feedback": f"Erro crítico: {str(e)}"
        })
        print(traceback.format_exc())

    return results

if __name__ == "__main__":
    final_res = test_elite_accuracy()
    print(f"RESULT_JSON: {json.dumps(final_res)}")
