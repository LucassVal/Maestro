# [MISSION] PARRUDO: ESTRUTURA DE COMANDO SOTA 2026

Ecossistema de orquestração de IAs locais focado em resiliência, autonomia e segurança (Airlock).

## [BUILD] Arquitetura v16.7 (Regente & Event-Driven)

O sistema opera sob o modelo de **Agentes Desacoplados** coordenados por um **Regente Central**.

### Componentes Principais:
1.  **`operario coringa.py` (O Regente)**: Maestro que carrega agentes Majors dinamicamente.
2.  **`event_store.py` (Event Bus)**: Barramento Pub/Sub para comunicação assíncrona entre módulos.
3.  **`cortex.json`**: O "DNA" do sistema, definindo tiers de IA, modelos e prompts.
4.  **`parrudo_core.py`**: O coração da comunicação com o Ollama API.

## 🤖 Como Adicionar um Novo Agente (Major)

Para criar um novo agente de elite:
1.  Crie um arquivo `agente_<nome>.py`.
2.  Implemente a função obrigatória: `executar(entrada: dict) -> dict`.
3.  Registre o agente no dicionário `AGENTES` do `operario coringa.py`.

## [LOCK] Segurança e Governança
-   **Airlock**: Comandos de terminal exigem aprovação humana via `proposta_acao.py`.
-   **Constituição**: Todos os agentes operam sob as leis definidas em `CONSTITUICAO.md`.

## [STATS] Auditoria
-   **Retroativa**: Integridade de 98% nas Fases 01-44 validada em Março/2026.
-   **Fleet Audit**: Monitoramento de latência e status de saúde da frota Ollama.
