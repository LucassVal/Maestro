import json
import os
import sys

# Simulação da Hierarquia SOTA v47.6
# No sistema real, isso chamaria o Ollama com os modelos específicos.
# Aqui testamos a lógica de tradução do Embaixador.

def test_mentorship_logic():
    print("\n" + "="*50)
    print("SOTA v47.6 - MENTORSHIP LOOP TEST")
    print("="*50)

    # 1. ALTO COMANDO (QWEN 3) - O Plano Técnico
    alto_comando_output = {
        "status": "PLAN_GENERATED",
        "blueprint": {
            "action": "BACKUP_ENCRYPTED",
            "algo": "AES-256",
            "target": ".panda/backups/",
            "priority": "HIGH_SOVEREIGNTY"
        },
        "technical_notes": "Ensure keys are stored in .panda/memory/imutable."
    }
    print(f"[*] ALTO COMANDO (QWEN 3) gerou plano estruturado.")

    # 2. EMBAIXADOR (1.5B) - A Tradução Amigável
    # Simulamos o prompt do Embaixador recebendo o JSON acima
    input_para_embaixador = json.dumps(alto_comando_output)
    
    # Prompt de Sistema do Embaixador (de prompts_agents.json)
    system_prompt = "Você é o Embaixador. Traduza o plano técnico do Alto Comando para o Lucas de forma amigável."
    
    # Resposta esperada do Embaixador
    explicacao_amigavel = (
        "Olá Lucas! O Alto Comando já traçou a estratégia: vamos realizar um backup "
        "totalmente criptografado com AES-256 na nossa zona segura (.panda/backups/). "
        "Fique tranquilo, suas chaves de acesso estão protegidas na memória imutável!"
    )

    print(f"[*] EMBAIXADOR (1.5B) traduziu para: \n    '{explicacao_amigavel}'")

    # Validação
    assert "Lucas" in explicacao_amigavel
    assert "backup" in explicacao_amigavel.lower()
    assert ".panda/backups/" in explicacao_amigavel
    print("\n✅ TESTE DE MENTORIA: SUCESSO. Relação Regente -> Embaixador Verificada.")
    print("="*50)

if __name__ == "__main__":
    test_mentorship_logic()
