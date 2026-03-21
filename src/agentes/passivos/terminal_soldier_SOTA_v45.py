import subprocess
import shlex
import time
import os
import json
from typing import Dict
import src.agentes.passivos.desktop_logger_SRC_GL as desktop_logger

class TerminalSoldier:
    def __init__(self):
        self.timeout = 60  
        self.blocked_commands = [
            'rm -rf /', 'shutdown', 'format', 'dd', 
            'del /s /q c:\\', 'rd /s /q c:\\'
        ]
        
    def executar(self, comando: str, modo_seguro: bool = True) -> Dict:
        """Registers a command proposal in the Airlock for human approval."""
        from proposta_acao import PropostaAcao
        pa = PropostaAcao()
        
        # 1. Basic Sanitization
        for cmd_bloqueado in self.blocked_commands:
            if cmd_bloqueado in comando.lower():
                return {"erro": f"BLOCKING CRITICAL COMMAND: {cmd_bloqueado}"}
        
        # 2. Create Proposal in Airlock
        prop_id = pa.criar_proposta(
            tipo="terminal_command",
            categoria="seguranca",
            dados={"comando": comando, "host": "local"}
        )
        
        desktop_logger.log_connection("AIRLOCK", "PROPOSAL", comando, "PENDING", 0)
        
        return {
            "status": "PENDENTE_APROVACAO",
            "proposta_id": prop_id,
            "mensagem": f"Command registered in Airlock ({prop_id}). Waiting for human approval."
        }

    def executar_final(self, proposta_id: str) -> Dict:
        """Executes a command that has already been approved in the proposals system."""
        from proposta_acao import PropostaAcao
        pa = PropostaAcao()
        
        # Check status
        path = os.path.join(".panda/propostas", f"{proposta_id}.json")
        if not os.path.exists(path): return {"erro": "Proposal not found"}
        
        with open(path, "r", encoding="utf-8") as f:
            p = json.load(f)
            
        if p["status"] != "aprovado":
            return {"erro": f"Command not approved. Current status: {p['status']}"}
        
        comando = p["dados"]["comando"]
        start_time = time.time()
        
        try:
            desktop_logger.log_connection("LOCAL_SHELL", "EXEC_APPROVED", comando, "STARTING", 0)
            processo = subprocess.run(
                ["powershell", "-Command", comando],
                capture_output=True,
                text=True,
                timeout=self.timeout,
                encoding='latin1'
            )
            
            response_time = time.time() - start_time
            return {
                "stdout": processo.stdout,
                "stderr": processo.stderr,
                "codigo": processo.returncode,
                "tempo": response_time
            }
        except Exception as e:
            return {"erro": str(e)}

# Global instance
terminal_soldier_SOTA = TerminalSoldier()
