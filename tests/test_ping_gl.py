import sys
import os
import time

def log(msg):
    print(msg)
    sys.stdout.flush()
    with open("ping_log_GL.txt", "a", encoding="utf-8") as f:
        f.write(f"[{time.strftime('%H:%M:%S')}] {msg}\n")

# Limpa log anterior
if os.path.exists("ping_log_GL.txt"):
    os.remove("ping_log_GL.txt")

log("[DEBUG] Starting script test_ping_gl.py")

# Ajusta path para encontrar o src
current_dir = os.getcwd()
src_dir = os.path.join(current_dir, "src")
sys.path.append(src_dir)

log(f" PATH: {src_dir}")

try:
    log("[CONN] Attempting to import KernelGenio...")
    from core.kernel_genio_CORE_GL import KernelGenio
    kernel = KernelGenio()
    log("[OK] Import completed.")

    log("[CONN] PING TEST GL - OLLAMA")
    # Testa listagem de modelos
    modelos = kernel.client.list()
    log("[OK] Ollama connection successful.")

    try:
        # Tenta extrair nomes de forma resiliente
        nomes = []
        for m in modelos.get('models', []):
            if isinstance(m, dict):
                nomes.append(m.get('name', m.get('model', 'unk')))
            else:
                nomes.append(getattr(m, 'model', getattr(m, 'name', str(m))))
        log(f" Modelos: {nomes}")
    except:
        log(" Modelos detectados, mas falha ao formatar lista.")

    # Define modelo de teste
    modelo_teste = "llama3.2:latest"
    log(f"[[BRAIN]] Testando Inferência SOTA ({modelo_teste})...")
    res = kernel.gerar(modelo_teste, "Responda apenas: PONG GL FUNCIONANDO")
    log(f"[OK] Resposta do Kernel: {res}")
    log(" SUCESSO: O SISTEMA GL ESTÁ VIVO!")

except Exception as e:
    log(f"[ERR] ERRO CRÍTICO NO PING GL: {e}")
    import traceback
    log(traceback.format_exc())
    sys.exit(1)
