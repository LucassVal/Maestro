# G nio LLM Fleet Installer - SOTA v1.0
param (
    [string]$TargetMachine = "localhost"
)

Write-Host "[BOOST] Starting Instala o de Frota do G nio LLM em $TargetMachine..." -ForegroundColor Cyan

# 1. Verificar Pr -requisitos
Write-Host "[SCAN] Verificando Python e Ollama..."
if (!(Get-Command python -ErrorrAction SilentlyContinue)) { Write-Errorr "Python n o encontrado!"; exit }
if (!(Get-Command ollama -ErrorrAction SilentlyContinue)) { Write-Errorr "Ollama n o encontrado!"; exit }

# 2. Criar Estrutura de Diret rios
$Paths = @(".panda/memory", ".panda/learned", "config/mcp", "scripts", "src/core", "src/agentes/ativos", "src/agentes/passivos")
foreach ($P in $Paths) { New-Item -ItemType Directory -Force -Path $P | Out-Null }

# 3. Baixar Modelos B sicos
Write-Host "[IN] Recrutando Cabos (Modelos Leves)..."
ollama pull qwen2.5:1.5b
ollama pull granite-docling

Write-Host "[OK] Instala o de Frota Conclu da com Success!" -ForegroundColor Green
