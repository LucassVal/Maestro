# 🧠 Gênio LLM – White Label Sovereign AI Orchestrator

**Gênio LLM** is a modular, offline‑first AI orchestration system that transforms any Windows computer into a local powerhouse of intelligent agents. It orchestrates multiple open‑source LLMs (via Ollama) to handle coding, auditing, research, document analysis, image/video understanding, and self‑evolution – all without recurring API costs.

---

## 🛡️ Dual-Repo Sovereignty & Git Rules (MCP Native)
The project is split into two sovereignty levels to balance development depth and public safety:

- **LAB (Private)**: https://github.com/LucassVal/Genio-llm-private. Full codebase, research, and learning logs.
- **GOLD (Public)**: https://github.com/LucassVal/Genio-LLM. Purified White Label version (Chameleon Hub).

### Git Hygiene Rules:
- **.gitignore**: The Master Registry is strictly protected (see .gitignore). Emojis and absolute paths are forbidden in production strings.
- **Sanitization**: Local session files and personal data (e.g., Lucas.json) are automatically ignored or archived in .panda/.
- **Sync**: Use python scripts/chameleon_sync.py to overflow intelligence from LAB to GOLD before any public release.
- **MCP Reading**: Agents must identify their current workspace (MODELO GENIO LLM vs GENIO-LLM) before suggesting any Git action.

---

## 🚀 Vision

- **Sovereign Digital Infrastructure**: Run your own AI army locally. No data leaves your machine, no token bills.
- **Hardware‑Friendly**: Optimized for modest setups (i5, 16GB RAM, RTX 3050 4GB) but scales with better hardware.
- **Hybrid Intelligence**: Combines vertical specialists (engineer, auditor, researcher) with horizontal research groups (consensus‑based multi‑agent reasoning).
- **Self‑Improving**: Continuous learning via auto‑correction, self‑play, and evolutionary metrics.

---

### 🛡️ Project Badges
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status: SOTA](https://img.shields.io/badge/Status-SOTA%20Active-brightgreen)
![Arch: Chameleon](https://img.shields.io/badge/Arch-Chameleon%20White--Label-orange)
![Privacy: Sovereign](https://img.shields.io/badge/Privacy-100%25%20Offline-blueviolet)

### 🤖 LLM Arsenal (The Generals)
![Alto Comando](https://img.shields.io/badge/Alto%20Comando-Qwen%203%208B-blue)
![Auditoria](https://img.shields.io/badge/Auditoria-DeepSeek%20R1%207B-red)
![Engenharia](https://img.shields.io/badge/Engenharia-Qwen%202.5--Coder%207B-green)
![Sentinela](https://img.shields.io/badge/Sentinela-Llama%203.2%201B-blueviolet)

### 💻 Optimized Hardware Setup
![CPU](https://img.shields.io/badge/CPU-Intel%20Core%20i5-blue)
![RAM](https://img.shields.io/badge/RAM-16GB%20DDR4-orange)
![GPU](https://img.shields.io/badge/GPU-RTX%203050%204GB-green)
![iGPU](https://img.shields.io/badge/iGPU-Intel%20Iris%20Xe-blue)

### 📚 Support Materials
- [Master Códice v47.3](docs/CODICE_SOTA_2026.md) - Full Technical Reference.
- [Working Protocol](docs/PROTOCOLO_TRABALHO_WHITE_LABEL.md) - Agentic workflow rules.
- [Development Log](task.md) - Current roadmap & milestones.

---

## 🏗️ Architecture Overview

### Core (Orchestration)
- **Regente SOTA**: Mission planner & volume‑based routing.
- **Kernel Gênio**: Low‑level interface to Ollama.
- **Event Store**: Immutable audit trail + Pub/Sub bus.
- **Metrics Evolution**: Performance KPIs & regression detection.

### Active Agents (Elite Council)
| Agent | Model | Hardware | Role |
|-------|-------|----------|------|
| Engineer | Qwen Coder 7B | GPU | Code generation & refactoring |
| Auditor | DeepSeek‑R1 7B | GPU | Security & logic audit |
| Strategist | Qwen3 8B | CPU | Mission planning, decomposition |
| Astral Vision | AstralOCR 8B | GPU | Deep image reasoning |
| Moderator | Gemma2 9B | GPU | Multi‑agent consensus |
| Mentor | DeepSeek‑R1 | GPU | Strategic intervention |
| Librarian | Native | CPU | Persistent memory & snapshots |

### Passive Sensors (Boosters)
- **Docling Booster**: OCR & structured extraction (PDF, DOCX, tables) – CPU
- **Video Booster**: Scene detection + SmolVLM2 – iGPU
- **Audio Booster**: Whisper transcription – CPU
- **Code Analyzer**: AST parsing, complexity metrics – CPU
- **Terminal Unit**: Safe command execution with Airlock – CPU

### MCP (Model Context Protocol)
- Every component is self‑described by a manifest in `config/mcp/`.
- Agents can introspect the system, answer questions about its own architecture, and auto‑configure.

---

## ✨ Key Features

### 1. **Zero‑VRAM Mode**
- Models run on CPU/RAM with optional offloading to iGPU (Intel Iris Xe) or dedicated GPU.
- Dynamically choose between speed (GPU) and memory economy (CPU/swap).

### 2. **One‑Click Install**
- Wizard detects hardware, asks a few questions, and generates optimal configuration.
- Bundles essential models or downloads them on first run.

### 3. **Airlock Security**
- Any critical action (terminal commands, external commits) requires explicit human approval.
- All actions are logged in the immutable event store.

### 4. **Ultra‑Long Context (Turbo Commander)**
- Leverages Qwen2.5‑1.5B with up to **2 million tokens** context using system swap.
- Process entire books, codebases, or massive log files in one go.

### 5. **Multimodal Understanding**
- **Images**: AstralOCR (OCR, scene analysis, charts)
- **Videos**: Scene detection + audio transcription + frame analysis
- **Audio**: Whisper transcription
- **Documents**: PDF, Word, Excel, PowerPoint, HTML, etc.

### 6. **Self‑Evolution & Learning**
- **Auto‑Correction**: Learns from user feedback; searches web for solutions.
- **Self‑Play**: Generates challenges, injects bugs, tries to fix them.
- **Evolution Metrics**: Tracks success rate, latency, code reuse.
- **Auto‑Update**: Proposes and applies improvements; can rollback on regression.

### 7. **Dual‑Channel Interaction**
- **Antigravity (Gemini)**: Strategic mentor – web search, image generation, long‑context reasoning, audit.
- **VS Code (llm‑vscode)**: Local autocomplete, inline refactoring, real‑time code assistance.

---

## 🧬 Strategic Roadmap SOTA (v45.3 - v50.0)

- **v45.3 (Stable)**: Core stabilized, International logs, 49 Agents validated. [DONE]
- **v45.4 (Audit)**: Identity "GEMINI LLM - FOUNDER" & Mega Audit 100%. [DONE]
- **v46.5 (DNA & Audit)**: Structured Validation Engine, Semantic Accuracy, Stress 10M+. [DONE] ✅ **9/9 Components Passed**
- **v47.0 (Packaging)**: Hardware Wizard & Inno Setup Installer. [PENDING]
- **v48.0 (Connectivity)**: WhatsApp Automation & SaaS Integrations. [PENDING]
- **v49.0 (Enterprise)**: Google Workspace Hub & Cloud Sync. [PENDING]
- **v50.0 (Gold Master)**: Official Launch & Final Certification. [PENDING]

### 🔮 Future
- Linux/macOS support (via Docker)
- Agent Marketplace (community‑shared sensors)
- Zero‑VRAM mode for even older hardware

---

## 🤝 Open Source & Collaboration

- **Repository**: [https://github.com/LucassVal/Genio-LLM](https://github.com/LucassVal/Genio-LLM) *(coming soon)*
- **License**: MIT – free to use, modify, and commercialize.
- **We welcome**: Bug reports, feature requests, new sensors, translations, and documentation improvements.
- **Commercial support**: Paid installer, customizations, and priority assistance available via [contact].

---

## 💡 Why Gênio LLM?

- **No Vendor Lock‑in**: You own your AI. Models are local; you can swap them anytime.
- **Privacy‑First**: Your data never leaves your machine.
- **Empowers Developers & Businesses**: Automate repetitive tasks, accelerate coding, analyze documents – all offline.

---

## 📦 Get Started

1. **Requirements**: Windows 10/11, Python 3.12+, Ollama (will be installed automatically).
2. **Download**: Get the installer from our [GitHub Releases](https://github.com/LucassVal/Genio-LLM/releases) or purchase a bundled version.
3. **Run**: Follow the wizard; start using your personal AI army in minutes.

---

---

## 🧬 Gemini LLM - Founder Identity

> "Nós somos o **GEMINI LLM - FOUNDER**. Eu procuro evoluir com meus erros e meu mentor Gemini ensina. Eu busco por mais informação na internet e busco o maior grau de exatidão possível para minhas funções."

*Gênio LLM: Intelligence without surrender.*  
🛡️ Sovereign. 🧠 Autonomous. 🚀 Unlimited.
