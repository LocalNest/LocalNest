# LocalNest: Open Source Intelligent Home Automation

**LocalNest delivers next-generation, AI-powered home automation—all running securely on your own hardware, orchestrated visually with n8n.**

## Features

- **Local Intelligence:** Bring smart home logic, vision, and automation fully under your control.
- **Visual Automation:** Build flexible device workflows with [n8n](https://n8n.io)’s open-source drag-and-drop engine.
- **Device Integration:** Connect cameras, sensors, lights, locks, appliances, and more.
- **Private & Secure:** Data and automations stay in your home, with optional cloud intelligence.
- **Scalable Memory:** Redis + FAISS for rich, persistent context and smarter automations.
- **Remote Access:** Easily integrate your favorite VPN, Meshnet, or local dashboard for control from anywhere.

## Architecture
```
+---------------------+       +---------------------+       +----------------------+
|   Devices/Sensors   | ----> |    LocalNest AI     | ----> |     n8n Workflows    |
| (Cameras, IoT, etc) |       | Assistant / API     |       | Orchestration & Auto |
+---------------------+       +---------------------+       +----------------------+
                                       ^                               ^
                                       |                               |
                                       +--------- Automation <---------+
                                                   Event Triggers
```

- **n8n** triggers all workflows, orchestrates devices, and calls LocalNest for AI-powered decisions and event analysis.
- **LocalNest AI Assistant** parses commands, analyzes camera/sensor feeds, and powers intelligent automations.
- **Full Device Compatibility:** Use dozens of n8n nodes to connect Tuya, Tapo, Zigbee, Philips, smart locks, and more.
- **Memory:** Redis and FAISS provide persistent storage for deep automations and adaptive intelligence.

## Quick Start

1. Clone your repo:  
   `git clone https://github.com/LocalNest/LocalNest.git`
2. Run the setup script or follow install docs to deploy on any modern Linux PC/server.
3. Launch n8n, import sample workflows, and connect your devices.
4. Start building intelligent automations for your home.

***

## AI Model Setup & Platform Notes

- **Recommended Models:**
  - `codellama:7b-code` for code and scripting automations.
  - `llama3:8b` for all conversational AI, assistant, and event analysis workflows (chat/instruct).
- **Platform Compatibility:**
  - Use **Ubuntu Desktop 24.04 LTS (not 25.x) only!**
  - **Pop!_OS is NOT supported** due to NVIDIA driver conflicts and issues initializing GPU acceleration for AI inference.
- **NVIDIA Driver Notes:**
  - Use the latest official NVIDIA driver for your hardware (typically 550+).
  - After install, reboot and confirm GPU support via `nvidia-smi`.
  - Check `ollama system` for model/GPU compatibility.
  - If using Docker: pass-through the GPU, but direct host install is preferred for stability.
- **Ollama Model Storage:**
  - Models are stored in Ollama's system directory (`~/.ollama/models`) by default.
  - **Do NOT create or use a custom models folder** unless you change Ollama's default setting.
- **Troubleshooting:**
  - If the Ollama pull fails with `manifest not found`, check for model name accuracy and verify against the [official model library](https://ollama.com/library).
  - Only use official, supported model tags (`codellama:7b-code`, `llama3:8b`).
  - For conversational/assistant automations, always pull and use `llama3:8b` for best compatibility and speed with consumer-grade GPUs like 3070ti.

## Debug Summary

- Install and test on **Ubuntu 24.04**—Pop!_OS will fail with NVIDIA AI models.
- Use recommended NVIDIA drivers; do not rely on defaults.
- Only pull official models required for code (`codellama:7b-code`) and conversation (`llama3:8b`).
- Models are NOT saved to your project directory—do not expect custom model storage.
- Refer to Ollama's library for latest working model tags.

## Credits

> **n8n** ([n8n.io](https://n8n.io)) is the backbone for workflow logic, event routing, and device integration.

## License

MIT License (see `LICENSE.txt`).

***