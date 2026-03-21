#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
stress_test_1m_gpu.py Teste de ultra contexto (1M tokens) com modelo Turbo Commander na GPU.
Uso: python tests/hardware/stress_test_1m_gpu.py
""" import time
import os
import sys
import json
import psutil
import requests
import subprocess # Adiciona caminhos do projeto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.join(BASE_DIR, "src", "agentes", "ativos")) # Tenta importar o agente de vanguarda
try: from vanguarda_agente_SRC_GL import VanguardaAgente
except ImportError: print("[ERR] Agente de vanguarda n o encontrado. Verifique o caminho.") sys.exit(1) # ============================================
# Fun es auxiliares
# ============================================
def get_gpu_memory(): """Retorna o uso de VRAM em MB (via nvidia-smi) ou None se falhar.""" try: result = subprocess.run( ['nvidia-smi', '--query-gpu=memory.used', '--format=csv,nounits,noheader'], capture_output=True, text=True, check=True ) return int(result.stdout.strip()) except: return None def download_book(): """Baixa um livro de dom nio p blico para usar como texto de teste.""" url = "https://www.gutenberg.org/cache/epub/1342/pg1342.txt" # Orgulho e Preconceito print("[IN] Baixando livro de teste...") try: r = requests.get(url, timeout=30) r.encoding = 'utf-8' return r.text except Exception as e: print(f"[WARN] Failure no download: {e}. Usando texto sint tico.") # Fallback: gera texto repetitivo com alguma varia o return "SOTA o estado da arte. " * 50000 def estimate_tokens(text): """Estimativa grosseira de tokens (caracteres / 4).""" return len(text) // 4 # ============================================
# Teste principal
# ============================================
def stress_test_1m_gpu(): print("[HOT] STRESS TEST 1M TOKENS (TURBO COMMANDER GPU) [HOT]") # 1. Obt m texto de teste texto_base = download_book() # Repete at atingir ~1M tokens (estimativa) tokens_estimados = estimate_tokens(texto_base) repeticoes = max(1, 1_000_000 // tokens_estimados) texto_massivo = texto_base * repeticoes tokens_reais = estimate_tokens(texto_massivo) print(f"[STATS] Tokens estimados: {tokens_reais:,}") # 2. Prepara agente for amos uso da GPU no modelo v = VanguardaAgente() # Se o agente permitir par metros extras, podemos passar options # Exemplo: options = {"num_gpu": 1, "num_ctx": 1048576} # 3. Monitoramento inicial mem_antes = psutil.virtual_memory().used / (1024*1024) gpu_antes = get_gpu_memory() print(f"[STATS] RAM inicial: {mem_antes:.0f} MB | VRAM: {gpu_antes if gpu_antes else 'N/A'} MB") # 4. Executa a consulta com prompt longo print("[WAIT] Processando 1M tokens...") inicio = time.time() try: resposta = v.executar({ "prompt": texto_massivo + "\n\nCom base no texto acima, quem a personagem principal e qual sua principal caracter stica? Responda em uma frase." }) status = resposta.get("status", "UNKNOWN") resultado = resposta.get("resposta", "") except Exception as e: print(f"[ERR] Error durante execu o: {e}") return duracao = time.time() - inicio print(f"[TIME] Dura o: {duracao:.2f} segundos") # 5. Monitoramento final mem_depois = psutil.virtual_memory().used / (1024*1024) gpu_depois = get_gpu_memory() print(f"[STATS] RAM final: {mem_depois:.0f} MB | VRAM: {gpu_depois if gpu_depois else 'N/A'} MB") # 6. Coleta m tricas report = { "timestamp": time.ctime(), "success": status == "SUCCESS", "tokens_estimados": tokens_reais, "duracao_seg": duracao, "mem_delta_mb": mem_depois - mem_antes, "vram_antes_mb": gpu_antes, "vram_depois_mb": gpu_depois, "vram_delta_mb": (gpu_depois - gpu_antes) if gpu_antes and gpu_depois else None, "virtual_mem_peak": psutil.virtual_memory().percent, "primeiros_200_chars": resultado[:200] if resultado else "" } # 7. Salva resultado bench_dir = os.path.join(BASE_DIR, ".panda", "benchmarks") os.makedirs(bench_dir, exist_ok=True) bench_file = os.path.join(bench_dir, "stress_test_1m_gpu_results.json") with open(bench_file, "w", encoding="utf-8") as f: json.dump(report, f, indent=4, ensure_ascii=False) print(f"\n[OK] Teste conclu do. Resultado salvo em {bench_file}") if status == "SUCCESS": print("[NOTE] Primeiros 200 caracteres da resposta:\n", resultado[:200]) if __name__ == "__main__": stress_test_1m_gpu()
