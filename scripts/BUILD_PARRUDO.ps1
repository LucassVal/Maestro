#   BUILD PARRUDO CENTER .EXE
# Compila o Parrudo Center v5.0

$ProjectRoot = Get-Location
$Desktop = [System.Environment]::GetFolderPath("Desktop")

Write-Host "--- INICIANDO BUILD PARRUDO CENTER v5.0 ---" -ForegroundColor Cyan

# 1. Compilacao via PyInstaller
# --noconsole: Esconde a janela preta
# --onefile: Empacota tudo em um unico .exe
# --clean: Limpa builds anteriores
& pyinstaller --noconsole --onefile --clean --name "ParrudoCenter" --distpath $Desktop "parrudo_gui.py"

Write-Host "MISSION ACCOMPLISHED: ParrudoCenter.exe is on your Desktop." -ForegroundColor Green
Write-Host "Path: $Desktop\ParrudoCenter.exe" -ForegroundColor White
