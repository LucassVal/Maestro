# [BOOST] PARRUDO FLEET STRESS TEST v1.6 - VANGUARDA 2026
# Testando a Frota de Elite Otimizada para 4GB VRAM.

$ollamaPath = Join-Path $env:LOCALAPPDATA "Programs\Ollama\ollama.exe"

if (-not (Test-Path $ollamaPath)) {
    # Tenta caminho global se o local falhar
    $ollamaPath = "`"C:\Program Files\Ollama\ollama.exe`""
    if (-not (Test-Path $ollamaPath)) {
        Write-Host "[ERR] ERRO: ollama.exe nao encontrado." -ForegroundColor Red
        exit
    }
}

$models = @(
    "qwen2.5:1.5b", 
    "qwen3:8b",
    "qwen2.5-coder:7b",
    "deepseek-r1:7b",
    "granite3.3:8b"
)

$prompt = "Quanto e 1548 dividido por 12? Responda apenas o numero."

Write-Host "`n--- TESTE DE ESTRESSE: FROTA VANGUARDA 2026 ---"
Write-Host "Verifying Estabilidade e Performance (RTX 3050 - 4GB)`n"
Write-Host "Caminho: $ollamaPath"

$results = @()

foreach ($model in $models) {
    Write-Host "[[TEST]] Testando: $model... " -NoNewline
    
    $start = Get-Date
    try {
        # Usando o caminho absoluto para o ollama.exe
        $resp = & $ollamaPath run $model $prompt
        $end = Get-Date
        $sec = [math]::Round(($end - $start).TotalSeconds, 2)
        
        $results += [PSCustomObject]@{
            Modelo = $model
            Status = "OK"
            Tempo = "$sec s"
            Valor = $resp.Trim()
        }
        Write-Host "OK ($sec s)" -ForegroundColor Green
    }
    catch {
        $results += [PSCustomObject]@{
            Modelo = $model
            Status = "FALHOU"
            Tempo = "---"
            Valor = "Errorrr VRAM/Exec"
        }
        Write-Host "FALHOU" -ForegroundColor Red
    }
}

Write-Host "`n--- RESULTADO ---"
$results | Format-Table -AutoSize
Read-Host "Pressione Enter para concluir"
