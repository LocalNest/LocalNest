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

        +-------------------+         +-------------------+         +---------------------+
        |                   |         |                   |         |                     |
        |  Devices/Sensors  +-------> |   LocalNest AI    +-------> |    n8n Workflows    |
        |  (Cameras, IoT,   | Events |   Assistant/API    |  Calls |   Orchestration &    |
        |  SmartPlugs, etc) |        |                   |         |     Automation      |
        +-------------------+        +-------------------+         +---------------------+
                 |                            ^                               ^
                 |                            |                               |
                 +--------- Automation <-------+                    Event Triggers

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

## Credits

> **n8n** ([n8n.io](https://n8n.io)) is the backbone for workflow logic, event routing, and device integration.

## License

MIT License (see `LICENSE.txt`).

***

**Ready to take control? Build, contribute, and make your home truly intelligent with LocalNest!**

***
