import os
import json
import time
from operario_coringa import regente_global
import event_store def rodar_teste_simples(): print("[BOOST] Teste Simples do Bibliotec rio...") missao_id = f"TESTE_SIMPLES_{int(time.time())}" # Prompt que deve ser classificado como simples/conversa e terminar r pido prompt = "Ol Parrudo, apenas responda 'OK' para este teste de auditoria." print(f"[RADAR] Disparando miss o {missao_id}...") regente_global.iniciar_missao(prompt, missao_id=missao_id) print("\n Verificando logs...") eventos = event_store.obter_cronologia(missao_id) tipos = [e['tipo'] for e in eventos] expected = ["BIBLIOTECARIO_PRE", "MissaoIniciada", "MissaoConcluida", "BIBLIOTECARIO_POS"] for t in expected: status = "[OK]" if t in tipos else "[ERR]" print(f"{status} {t}") if __name__ == "__main__": rodar_teste_simples()
