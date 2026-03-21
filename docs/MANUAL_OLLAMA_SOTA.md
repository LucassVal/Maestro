# [GLOBAL] MANUAL MESTRE OLLAMA - SOTA 2026

Este manual contém a documentação técnica consolidada do ecossistema Ollama, otimizada para o **Gênio LLM**.

---

## 🏆 Lista Enxuta SOTA 2026 (Essenciais)

| Modelo | Função | Hardware |
| :--- | :--- | :--- |
| **qwen3:8b** | Alto Comando (Orquestração) | GPU/CPU |
| **deepseek-r1:7b** | Agente Auditor (Raciocínio) | GPU/CPU |
| **qwen2.5-coder:7b** | Agente Engenheiro (Código) | GPU/CPU |
| **turbo-commander** | Booster de Texto Longo (128k+) | CPU |
| **granite-docling** | Booster de Documentos (OCR) | CPU |
| **astralocr-8b** | Especialista em Visão Profunda | GPU |
| **smolvlm2-2.2b** | Sensor de Vídeo/Frames | iGPU/CPU |

---


## 🛠️ 1. CLI Reference (Comandos de Linha de Comando)

| Comando | Descrição | Exemplo |
|--------------------|---------|
| `ollama serve` | Inicia o servidor local. | `ollama serve` |
| `ollama run` | Executa um modelo (baixa se necessário). | `ollama run qwen2.5:1.5b` |
| `ollama pull` | Baixa um modelo sem executá-lo. | `ollama pull qwen2-vl` |
| `ollama push` | Envia um modelo customizado para o registro. | `ollama push lucas/meu-modelo` |
| `ollama list` | Lista todos os modelos baixados localmente. | `ollama list` |
| `ollama ps` | Lista os modelos que estão rodando na VRAM/RAM. | `ollama ps` |
| `ollama rm` | Remove um modelo local. | `ollama rm llama3` |
| `ollama cp` | Copia um modelo para criar um novo nome/versão. | `ollama cp qwen qwen-turbo` |
| `ollama create` | Cria um modelo a partir de um `Modelfile`. | `ollama create genio -f Modelfile` |

---


## [RADAR] 2. API REST (Ollama Endpoint)
Porta Padrão: 11434

### `POST /api/generate` (Geração Simples)
Solicita uma resposta para um prompt único.
```json
{
  "model": "qwen2.5:7b",
  "prompt": "Explique o Gênio LLM.",
  "stream": false,
  "options": { "num_ctx": 32768, "temperature": 0.7 }
}
```

### `POST /api/chat` (Geração de Chat)
Mantém histórico e suporta multimodalidade.
```json
{
  "model": "qwen2-vl",
  "messages": [
    { "role": "user", "content": "O que tem nesta imagem?", "images": ["<base64_data>"] }
  ]
}
```

### `POST /api/show`
Retorna detalhes técnicos de um modelo específico.
```json
{ "name": "qwen2.5:7b" }
```

---


## [NOTE] 3. Modelfile Reference (Customização)
de IAs

| Instrução | Descrição | Exemplo |
|-----------|------------------------------------------|-----------------------------|
| `FROM` | Define o modelo base. | `FROM qwen2.5:1.5b` |
| `PARAMETER` | Ajusta hiperparâmetros técnicos. | `PARAMETER num_ctx 128000` |
| `SYSTEM` | Define a personalidade/diretrizes. | `SYSTEM "Você é o general SOTA."` |
| `TEMPLATE` | Define a estrutura do prompt (Prompt Engineering). | `TEMPLATE """{{ .System }}\nUser: {{ .Prompt }}\nAssistant:"""` |
| `MESSAGE` | Adiciona histórico de chat prévio. | `MESSAGE user "Qual sua versão?"` |
| `ADAPTER` | Aplica um LoRA (ajuste fino) externo. | `ADAPTER ./meu-ajuste.bin` |

### Parâmetros Avançados (`PARAMETER`):
- `num_ctx`: Tamanho da janela de contexto (ex: 32768).
- `temperature`: Criatividade (0.0 = exato, 1.0 = criativo).
- `top_k`, `top_p`: Filtragem probabilística de tokens.
- `stop`: Tokens de parada (ex: `"<|im_end|>"`).

---


## [LOCK] 4. Environment Variables (Variáveis de Ambiente):
Configuração de Sistema

- **`OLLAMA_HOST`**: Define IP/Porta (padrão `127.0.0.1:11434`).
- **`OLLAMA_MODELS`**: Caminho onde os modelos são salvos (ex: `D:\ollama_models`).
- **`OLLAMA_NUM_PARALLEL`**: Número de requisições paralelas simultâneas.
- **`OLLAMA_MAX_LOADED_MODELS`**: Quantos modelos mantêm-se na VRAM.
- **`OLLAMA_KV_CACHE_TYPE`**: Define a quantização do cache de contexto (ex: `q4_0` economiza VRAM/RAM significativamente).
- **`OLLAMA_FLASH_ATTENTION`**: Habilita Flash Attention para velocidade extra (se suportado).

---

## [VISION] 5. Notas Multimodais (Qwen2-VL / Llama-Vision)

Para modelos de visão, a imagem deve ser enviada como uma string **Base64** dentro do array `images`. 
- **Checklist de Visão**: 
  - Drivers NVIDIA atualizados (Cuda 11.8+).
  - VRAM livre (mínimo 4GB para 7B-VL).
  - Versão do Ollama 0.3.11+.

---

> [!TIP]
> Use o `agente_especialista_ollama` do Gênio para expandir este manual com novos modelos e técnicas de quantização.

*Documentação consolidada para o Arsenal v46.5 - SOTA 2026*
