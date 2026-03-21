# [GUARD] PROTOCOLO DE ELEVAÇÃO SOTA v44.3

Para que o Gênio LLM opere como um organismo soberano, o nível de privilégio deve ser **ADMINISTRADOR**. Sem isso, o Windows bloqueia acessos vitais (Python em Program Files, portas de rede, escrita em logs de sistema).

---

## [BOOST] PASSO A PASSO PARA ELEVAÇÃO (LUCAS)

1.  **Fechar o VS Code / Host Atual**.
2.  **Abrir o VS Code como Administrador**:
    -   Clique com o botão direito no ícone do VS Code.
    -   Selecione **"Executar como Administrador"**.
3.  **Validar a Elevação**: Run the command below in the terminal:
    ```powershell
    python tests/check_admin_GL.py
    ```

---

## 🛠️ POR QUE GASTAR TEMPO COM ISSO?
- **Acesso ao Python SOTA**: Evita erros de "Operação requer elevação" ao rodar modelos pesados.
- **Daemons de Fundo**: Permite que `colono` e `night_watcher` rodem sem serem derrubados pelo OS.
- **Soberania de Rede**: Abre portas de API (11435, 9812) com maior estabilidade.

---

## [DNA] VERIFICADOR DE PRIVILÉGIOS (`tests/check_admin_GL.py`)
Eu criei esse script para nos dar o "Pulso de Autoridade". 

---
*Gênio LLM: Poder Total. Soberania Absoluta.*
