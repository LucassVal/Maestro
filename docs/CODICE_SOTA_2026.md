# ♾️ O CÓDICE GENIO LLM SOTA 2026: SOBERANIA DIGITAL (v47.3) 🛡️🪐

_Massa Crítica de Conhecimento – Unificação de DNA, Arquitetura Camaleão, Planos e Orquestração Local_

---

## 🏛️ CAPÍTULO I: FUNDAMENTOS, ÉTICA E DNA (O ESPÍRITO)

### 1.1 Cláusulas Pétreas (CONSTITUIÇÃO)
- **Privacidade Absoluta**: Processamento 100% Local-First. Proibição de vazamento de dados sensíveis.
- **Integridade do Hardware**: Operação dentro dos limites térmicos e de VRAM (RTX 3050 4GB).
- **Gestão de Recursos**: Prioridade total à experiência do usuário (Offline Sovereign).
- **Transparência Auditável**: Toda ação é registrada no `event_store`.
- **Airlock de Supervisão**: Nenhuma ação externa sem aprovação manual.

### 1.2 DNA "Camaleão" (White-Label Ready)
O sistema foi projetado para ser **White-Label**, permitindo a distribuição profissional (HUB GOLD) sem rastros do desenvolvimento técnico do Laboratório (LAB).

---

## 🏗️ CAPÍTULO II: ARQUITETURA TÉCNICA (O CORPO)

### 2.1 Estrutura Dual (Soberania Dual)
O Gênio LLM opera em dois níveis:
1.  **LAB (Laboratório)**: Local de desenvolvimento, correção e experimentação.
2.  **GOLD (Produto)**: Versão purificada, White Label, para distribuição final.

### 2.2 Hierarquia Militar (84 Componentes)
Dividido em **4 Tiers** de atuação:
- **T1 - Alto Comando (CPU/GPU)**: `qwen3:8b` – Estratégia e Planejamento.
- **T2 - Comando de Elite (GPU)**: `deepseek-r1:7b` (Auditoria) e `qwen2.5-coder:7b` (Engenharia).
- **T3 - Soldados Ativos (iGPU/CPU)**: `qwen2.5:1.5b` – Roteamento e Classificação.
- **T4 - Sensores e Extratores (iGPU/CPU)**: Sensores SOTA e 20+ Extratores Multimodais.

### 2.3 Arsenal de Extração (20+ Formatos)
O Gênio possui extratores nativos para: `PDF`, `DOCX`, `XLSX`, `CSV`, `HTML`, `CODE`, `PPTX`, `EMAIL`, `SQL`, `XML`, `RTX`, `YAML`, `ARCHIVE`, `LOG`, entre outros.

---

## 🦾 CAPÍTULO III: MECÂNICAS & ALGORITMOS (O COMO)

### 3.1 O Fluxo Camaleão (Purificação)
Através do script `scripts/chameleon_sync.py`, o sistema:
1. Wipa o diretório GOLD antigo.
2. Faz o transbordo apenas do código auditado.
3. Remove caminhos absolutos e identificadores pessoais.
4. Gera manifestos Gold.

### 3.2 Rodízio de VRAM (VRAM Dynamo)
Gerenciamento dinâmico de 4GB VRAM:
- Swap inteligente entre Auditor e Engenheiro em ~1s.
- Offloading para iGPU (Iris Xe) para tarefas de baixa complexidade.

---

## 🏆 CAPÍTULO IV: MANUAL MESTRE OLLAMA (REFERÊNCIA TÉCNICA)

### Modelos Essenciais (Arsenal v46.5)
| Modelo | Função | Hardware |
| :--- | :--- | :--- |
| **qwen3:8b** | Orquestração Estratégica | CPU/16GB |
| **deepseek-r1:7b** | Auditoria e Raciocínio | GPU/4GB |
| **qwen2.5-coder:7b** | Engenharia de Código | GPU/4GB |
| **turbo-commander** | Contexto Longo (128k+) | CPU |
| **astralocr-8b** | Visão Computacional | GPU |

### API REST & Modelfile
- **Endpoint**: `127.0.0.1:11434`
- **Configuração**: Use `num_ctx` para janelas de até 128k e `OLLAMA_KV_CACHE_TYPE` para economia de VRAM.

---

## 📟 CAPÍTULO V: REGISTRO MASTER & GOVERNANÇA

### Matriz de Testes (Resiliência)
- **MIST**: Funcional unitário.
- **STORM**: Integração complexa.
- **TSUNAMI**: Stress de carga e contexto.
- **BOOST**: Performance SOTA.

### Repositórios de Soberania
- **Privado**: [RESTRITO] (Versão LAB).
- **Público**: `Genio-LLM` (Versão GOLD White Label).

---

---

## ⚙️ CAPÍTULO VI: MERGULHO PROFUNDO (MECÂNICAS DE INTERAÇÃO)

### 6.1 Loop de Autocorreção R2D2 (O Mecanismo de Cura)
O sistema não apenas executa; ele aprende com o erro. O fluxo é:
1. **Detecção**: O Evaluator identifica falha no terminal ou no retorno da LLM.
2. **Reflexão (Search)**: O Agente R2D2 gera um `hash` do erro e busca no `.panda/learned/` por soluções anteriores.
3. **Patch**: Caso não exista, ele pesquisa logs de sistema e tenta aplicar um "Hotfix".
4. **Learning**: Após sucesso (score ≥ 8/10), a solução é indexada para uso futuro.
   - *Exemplo*: Erro de biblioteca Python ausente gera instalação automática via `pip` e registro na biblioteca de correções.

### 6.2 VRAM Dynamo & Prioridade (Gestão de Calor)
O Gênio gerencia 4GB de VRAM através do `vram_optimizer`:
- **Rodízio**: Alterna entre Agente Engenheiro (Escrita) e Auditor (Revisão).
- **Prioridade**: Tarefas em andamento (Foreground) barram novas alocações por 500ms para evitar OOM (Out of Memory).
- **Offloading**: Quando a VRAM atinge 90%, o sistema move o KV Cache para RAM/CPU.

### 6.3 Conselho de Guerra & Consenso (O Moderador)
Invocável via comando `conselho: [prompt]`, esta mecânica utiliza:
- **Votação Ponderada**: Cada agente tem um peso baseado em sua taxa de sucesso histórica.
- **Síntese**: O Moderador (Gemma 2) analisa as divergências entre Qwen e DeepSeek e gera um "Veredito Consolidado".

### 6.4 Airlock: O Protocolo de Segurança Ativa
Nenhum comando destrutivo (RM, DEL, GIT PUSH) ocorre sem supervisão:
1. **Interceptação**: O sensor detecta comando de risco.
2. **Proposta (JSON)**: Gera um arquivo em `config/proposals/pending/`.
3. **Aprovação**: O usuário recebe notificação na GUI/CLI e "carimba" a ação.

### 6.5 Mecânicas de Acesso ao Codex e Normatização

#### 6.5.1 O Codex como Fonte de Verdade
O Codex (`GENIO_FILE_REGISTRE_.md`) é o coração autodescritivo do sistema. Ele não é apenas um documento estático; é consumido por agentes em tempo real para:
- **Localizar componentes**: Cada agente ou sensor consulta o Codex para saber onde encontrar outros módulos via Path Agnostic discovery.
- **Validar dependências**: Antes de iniciar uma missão, o regente verifica no Codex se todos os agentes necessários estão disponíveis e certificados.
- **Orientar novos agentes**: O próprio sistema pode ler o Codex para se auto‑configurar e entender a topologia da rede.

#### 6.5.2 Acesso Programático e Léxico
- **Memória em Cache**: O `agente_bibliotecario` mantém uma cópia em memória do Codex e a atualiza automaticamente quando o arquivo físico é modificado.
- **API Interna**: O `kernel_genio` expõe a função `consultar_codex(categoria, nome)` que retorna o caminho absoluto/relativo e as capacidades de um componente.
- **Roteamento Semântico**: O `classificador_roteamento` usa o Codex para mapear palavras‑chave a agentes especializados, garantindo a normatização do léxico técnico.

#### 6.5.3 Exemplo de Uso no Código (Python):
```python
# Exemplo de consulta dinâmica ao Codex para ativação de Agente
from core.kernel_genio import consultar_codex

def ativar_agente_especialista(missao):
    # O sistema traduz a intenção para uma categoria do Codex
    detalhes = consultar_codex(categoria="ativos", nome="agente_engenheiro")
    if detalhes["status"] == "CERTIFICADO":
        caminho = detalhes["path"]
        # Inicia a instância baseada no registro mestre
        print(f"[OK] Agente localizado em: {caminho}")
```

### 6.6 Busca Semântica em Bibliotecas (RAG Interno)
Antes de criar código do zero, o Agente Engenheiro consulta `.panda/libraries/`:
- **Embeddings**: Utiliza `sentence-transformers` para comparar a intenção do usuário com o arsenal existente.
- **Reuso**: Se houver similaridade > 0.85, injeta o trecho de código pronto, economizando tokens e tempo.

### 6.7 Taxonomia de Agentes: Ativos vs Passivos
- **Ativos (Generals)**: Consomem GPU para raciocínio denso (Engenheiro, Auditor).
- **Passivos (Sensors)**: Operam em background via CPU, monitorando eventos (Bibliotecário, Terminal, Radar).
- **Interação**: Passivos alimentam o `event_store` e Ativos consomem esses dados para tomar decisões complexas.

### 6.8 Validação de Integridade (O Bibliotecário)
O `agente_bibliotecario` atua como o sistema imunológico do código:
- **Snapshot Diferencial**: A cada ciclo de 15 minutos (Colono Daemon), o Bibliotecário compara o estado atual com o último `snapshot` estável.
- **Auto-Healing**: Se detectada corrupção de arquivos core (`_SRC_GL.py`), ele restaura o backup imediatamente de `.panda/backups/`.
- **Certificação de Manifesto**: Garante que nenhum agente novo seja ativado sem um manifesto MCP válido e auditado.

### 6.9 Barramento de Eventos (Event Store)
A memória de curto prazo do sistema reside no `event_store.py`:
- **Pub/Sub SOTA**: Permite que Sensores (Passivos) notifiquem Agentes (Ativos) sem acoplamento direto.
- **Imutabilidade**: Todos os eventos (sucesso, erro, mudança de VRAM) são registrados como logs imutáveis.
- **Injeção de Contexto**: O Regente lê os últimos 50 eventos para "dar cor" à próxima tomada de decisão da LLM, reduzindo alucinações.

### 6.10. Mecânicas de Acesso ao Conhecimento (Semantic Routing)
O Gênio LLM utiliza uma camada de abstração semântica para localizar componentes e processar intenções sem depender de caminhos absolutos ou strings estáticas.

#### 1. O Codex como Fonte de Verdade
- **Registro Mestre**: `GENIO_FILE_REGISTRE_.md`.
- **Funcionamento**: O sistema não "chuta" localizações; ele consulta o índice mapeado.
- **Cache de Memória**: O `agente_bibliotecario` mantém um snapshot do Codex em `.panda/memory/codex_index.json` para acesso de ultra-baixa latência.

#### 2. Roteamento Semântico e Normalização
- **Configuração**: `config/codex_tecnico.json` (Palavras-chave -> Categoria).
- **Fluxo de Intent**:
  1. Texto do usuário é normalizado via **Stemmer**.
  2. Consulta ao `codex_tecnico.json` para identificar o Agente Ativo responsável.
  3. Em caso de ambiguidade, o **Qwen 1.5B (Soldado)** atua como classificador de fallback.

#### 3. Padronização JSON SOTA (9 Colunas)
Todos os arquivos de configuração do ecossistema seguem o **Schema SOTA**, que espelha a Matriz de 9 Colunas:
- `metadata`: Governança, Versão e Tier.
- `registry`: Elementos com tags semânticas e nível de autoridade.

#### 4. Acesso Programático (API Interna)
Agentes podem consultar o conhecimento nativo via:
```python
# Exemplo de consulta programática ao Codex
resultado = kernel_genio.consultar_codex(categoria="engenheiro", palavra="refatorar")
```
- **Benefício**: Permite que agentes verifiquem capacidades antes de planejar missões.

---

> _"A ordem é a materialização da inteligência."_  
> **SOTA SUPREME COUNCIL (v47.4)**
