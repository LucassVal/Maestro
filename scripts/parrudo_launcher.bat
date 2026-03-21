@echo off
setlocal
title PARRUDO CENTER BOOTER v15.2

:: Navega para o diret rio do script
cd /d "%~dp0"

echo [[SAT]] INICIANDO PARRUDO CENTER v15.2...
echo [ ] DIRETORIO: %cd%

:: Define o interpretador absoluto como prioridade
set "ABSOLUTE_PYTHON=C:\Program Files\Python312\python.exe"

if exist "%ABSOLUTE_PYTHON%" (
    echo [ ] Usando interpretador em: %ABSOLUTE_PYTHON%
    "%ABSOLUTE_PYTHON%" parrudo_gui.py
) else (
    echo [[WARN]] Interpretador absoluto nao encontrado. Tentando via PATH...
    python parrudo_gui.py
)

if %errorlevel% neq 0 (
    echo.
    echo [[ERR]] ERRO CRITICO: Nao foi possivel iniciar a GUI.
    echo Tentando capturar erro via CMD...
    pause
)
exit
