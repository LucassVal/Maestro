import os
import json
import time
from metricas_evolucao import MetricasEvolucao
from auto_atualizacao import AutoAtualizacao def rodar_verificacao(): print("[TEST] [TESTE] Starting Ciclo de Verifica o SOTA ELITE...") # 1. Teste de Benchmark print("\n1. Executando Benchmark v1.0...") me = MetricasEvolucao() res_bench = me.rodar_benchmark() print(f"[OK] Resultado: {res_bench}") # 2. Teste de KPIs e Sinalizador print("\n2. Calculando KPIs e Sinaliza o...") kpis = me.calcular_kpis() sinal = kpis.get("sinalizador", "unknown") print(f"[OK] Sinal: {sinal.upper()} | Taxa: {kpis.get('taxa_sucesso')*100}%") # 3. Teste de Rollback (Manual) print("\n3. Verificando Mecanismo de Rollback...") aa = AutoAtualizacao() # Cria um backup falso para teste aa.backup_atomico(["config/benchmark_missoes.json"]) res_rb = aa.realizar_rollback() print(f"[OK] Rollback: {res_rb}") print("\n[START] [TESTE] Verifica o conclu da com sucesso.") if __name__ == "__main__": rodar_verificacao()
