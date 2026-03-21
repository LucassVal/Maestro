#   SENTINEL v6.1 - DISPATCHER AUTOMATION (QWEN 3)
# 100% LOCAL | SIGMA COMPLIANT | ZERO SELECTION MODE

$ProjectRoot = Get-Location

# --- [  DASHBOARD] ---
function Write-Dashboard {
    $Time = Get-Date -Format "HH:mm:ss"
    Clear-Host
    Write-Host " $($(' ' * 70)) " -ForegroundColor Gray
    Write-Host "    [VOLT] SENTINEL v6.1   PARRUDO DISPATCHER   $Time   [GLOBAL] ARQUITETO ATIVO  " -ForegroundColor Cyan
    Write-Host " $($(' ' * 70)) " -ForegroundColor Gray
    Write-Host "  O Qwen 3 agora decide automaticamente quem executa sua tarefa.        " -ForegroundColor Gray
    Write-Host " $($(' ' * 70)) " -ForegroundColor Gray
}

while($true) {
    Write-Dashboard
    $msg = Read-Host "Mande sua tarefa (ou 'audit' para diagnostico, 'exit' para sair)"
    
    if ($msg -eq "exit") { break }
    if ($msg -eq "audit") { 
        # Roda a Super Auditoria
        Write-Host "[[SCAN]] Starting Auditoria..." -ForegroundColor Yellow
        # Logic here...
    } else {
        # Manda pro Dispatcher Autom tico
        python "operario coringa.py" "$msg"
        Read-Host "`nTarefa concluida. Aperte Enter para voltar ao HUD."
    }
}