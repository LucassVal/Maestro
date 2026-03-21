@echo off
echo.
echo ---   PURGA DA FROTA PARRUDO (LIMPEZA TOTAL) ---
echo.
echo [1/8] Removendo Monstros Instaveis (14B+)...
ollama rm deepseek-r1:14b
ollama rm deepseek-coder-v2:16b
ollama rm qwen3:30b-a3b

echo [2/8] Removendo Modelos Obsoletos (7B/8B/9B Antigos)...
ollama rm mistral:7b
ollama rm granite-code:8b
ollama rm yi-coder:9b
ollama rm deepseek-coder:6.7b

echo [3/8] Removendo Modelos Mini Obsoletos...
ollama rm gemma3:1b
ollama rm moondream:latest

echo [4/8] Faxina Pesada (Pruning)...
ollama prune

echo.
echo ---   LIMPEZA CONCLUIDA! ---
echo Agora seu disco esta pronto para receber a Frota Vanguarda 2026.
pause
