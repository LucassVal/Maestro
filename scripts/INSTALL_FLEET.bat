@echo off
echo   CODEX PARRUDO v6.5 - HARDWARE OPTIMIZED FLEET
echo Ajustando Frota para o seu Hardware (4GB VRAM / 16GB RAM)...
echo.

echo [[VOLT]] AGIL (Resposta Instantanea): Qwen 2.5 (1.5b)
ollama pull qwen2.5:1.5b
@echo off
echo.
echo --- [BOOST] PARRUDO FLEET: VANGUARDA 2026 (4GB VRAM) ---
echo.
echo [1/5]   Faxina de Cache (ollama prune)...
ollama prune

echo [2/5] [BRAIN] Recrutando Cerebro SOTA (Qwen 3 8B)...
ollama pull qwen3:8b

echo [3/5]   Recrutando Velocidade IBM (Granite 3.3 8B)...
ollama pull granite3.3:8b

echo [4/5]   Recrutando Especialista Code (Qwen 2.5 Coder 7B)...
ollama pull qwen2.5-coder:7b

echo [5/5] [IDEA] Recrutando Pensador Logico (DeepSeek R1 7B)...
ollama pull deepseek-r1:7b

echo.
echo --- REARMAMENTO VANGUARDA CONCLUIDO! ---
echo Sua GPU RTX 3050 agora possui a elite dos SLMs de 2026.
pause

echo [ ] WATCHDOG R1: DeepSeek R1 (7b ou 8b)
ollama pull deepseek-r1:8b

echo --- Foque nos modelos 7B/8B para maxima performance na RTX 3050 ---
pause
echo O sistema agora rodar  100%% liso sem travar o seu Windows.
pause
