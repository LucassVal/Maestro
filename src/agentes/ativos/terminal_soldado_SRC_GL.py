import subprocess
import os

def executar(entrada):
    """
    Soldado de Terminal.
    Executa comandos de sistema com segurança.
    """
    comando = entrada.get("comando", "echo PING")
    args = entrada.get("args", [])
    
    # Detecção de ambiente para compatibilidade
    if os.name == 'nt' and comando == 'ls':
        comando = 'dir'
    
    print(f"[TERMINAL] Executando comando: {comando} {args}")
    
    try:
        # Modo seguro: impede comandos destrutivos
        blacklist = ["rm -rf", "format", "del /s"]
        full_cmd = f"{comando} {' '.join(args)}"
        for forbidden in blacklist:
            if forbidden in full_cmd.lower():
                return {"status": "error", "message": "Comando bloqueado por segurança."}
        
        result = subprocess.run(full_cmd, capture_output=True, text=True, shell=True)
        return {
            "status": "ok",
            "stdout": result.stdout,
            "stderr": result.stderr,
            "exit_code": result.returncode
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}
