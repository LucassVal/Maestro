# Contributing to Gênio LLM 🤝🪐

First off, thank you for considering contributing to Gênio LLM! It's people like you who make the project better.

## 🚀 How Can I Contribute?

### Reporting Bugs
- Use the **GitHub Issues** template.
- Describe the hardware you are using (VRAM, RAM, CPU).
- Include the log from `.panda/logs/genio_session.log`.

### Suggesting Enhancements
- If you have an idea for a new **Sensor** or **Agent**, open a Feature Request.
- Follow the `_GL` naming convention for all new modules.

### Pull Requests
1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## 🧬 Coding Standards
- **Language**: All code and strings must be in **US English**.
- **No Emojis**: Use ASCII markers like `[OK]`, `[ERR]`, `[WARN]`.
- **Absolute Imports**: Always use `src.agentes.passivos...` style.

## 🛠️ Development Setup
1. Ensure Python 3.12 is installed.
2. Set `PYTHONIOENCODING='utf-8'`.
3. Run the Mist stress test locally: `python scripts/genio_master_init_GL.py --test mist`.

---
*Thank you for being part of the SOTA Evolution!*
