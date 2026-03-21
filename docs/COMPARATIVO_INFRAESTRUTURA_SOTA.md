# [STATS] COMPARATIVO DE INFRAESTRUTURA SOTA v44.2 (DETALHADO)

Este documento define os "Pulsos" e a "Capacidade de Endpoint" das duas vias de comando do Gênio LLM.

---

## [SAT] 1. ANTIGRAVITY (GEMINI HOST)
**O PULSO: "GENERAL ESTRATEGISTA"** – *Visão 360º, Planejamento e Auditoria.*

### 🛠️ O que o Endpoint NATIVO fornece:
- **Ferramentas Ativas (Lado IA)**: 
  - `search_web`: Pesquisa profunda na internet em tempo real.
  - `generate_image`: Geração de mockups, ativos e diagramas visualmente estonteantes.
  - `browser_subagent`: Automação de navegação para testes de ponta a ponta.
  - `read_url_content`: Leitura de documentações técnicas externas.
- **Raciocínio de Longa Distância**: Contexto de **1.5M+ tokens** para analisar o projeto inteiro de uma vez.
- **Auditoria de Missão**: Validação de conformidade com a Constituição v44.0.

---

## 🛠️ 2. LLM-VSCODE (HUGGING FACE / LOCAL BRAÇO)
**O PULSO: "SENTINELA OPERÁRIO"** – *Velocidade, Automação e Fricção Zero.*

### [OPS] O que o Endpoint LOCAL (Porta 11435) fornece:
- **Braço de Autocompletar (FST)**: Sugestões de código em tempo real (Ghost Text).
- **Inline Editing**: Refatoração de funções diretamente no cursor.
- **Conectividade Gênio (A fiação)**:
  - `POST /v1/chat/completions`: Traduz pedidos da IDE para missões do **Regente Qwen 3.0**.
  - `POST /api/generate`: Compatibilidade completa com o ecossistema Ollama.
- **Soberania de Contexto**: Acesso imediato aos arquivos abertos no VS Code (sem necessidade de upload ou leitura manual pela IA).

---

## [CYCLE] 3. MATRIZ DE CAPACIDADES (TABELA MESTRE)

| Capacidade | Antigravity (Nativo) | llm-vscode (Local) |
| :--- | :--- | :--- |
| **Pesquisa Web** | [OK] Sim (Profunda) | [ERR] Não (Limitada ao Códice) |
| **Geração Imagem** | [OK] Sim | [ERR] Não |
| **Contexto** | [BOOST] 1.5M+ | 📦 32k - 128k (Hardware-bound) |
| **Soberania** | [WARN] Híbrida (Nuvem) | [OK] Total (100% Offline) |
| **Autocomplete** | [ERR] Não | [OK] Sim (Frenético) |
| **IA Principal** | Gemini 2.0 Flash/Pro | Qwen 3.0 / DeepSeek-R1 |

---

## 🎯 RESUMO FINAL
- **Antigravity**: É para quando você quer **SABER O QUÊ** fazer e por que.
- **llm-vscode**: É para quando você quer **FAZER** rápido e em silêncio.

---
*Status: v44.2 - Infraestrutura Híbrida Estabelecida.*
