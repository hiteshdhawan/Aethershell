
# AetherShell
![GitHub stars](https://img.shields.io/github/stars/hiteshdhawan/Aethershell?style=social)

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

[![Releases](https://img.shields.io/github/v/release/hiteshdhawan/Aethershell?label=Latest%20Release)](https://github.com/hiteshdhawan/Aethershell/releases)


AetherShell is an AI-native Linux assistant that understands high-level natural language tasks and autonomously plans, executes, and validates actions using a local LLM (Mistral) without internet dependency.

It bridges the gap between natural language and real-time shell execution in a fully isolated, self-contained environment.

---

## Features

- Natural language command understanding
- Local LLM integration via `llama-cpp`
- Dynamic multi-step action planning and execution
- Memory persistence (JSON-based context)
- Offline capability (Works completely offline using local model.)
- Optional cloud fallback support (WIP)
- Secure Sandbox (WIP)

---

## Quick Start

### Requirements

- Python 3.8+
- `curl`
- Linux OS (Debian-based recommended)
- At least 6 GB RAM for LLM execution
  
## Prerequisites

Before running `setup.sh`, ensure the following tools are installed on your system:

- `curl` – for downloading the model
- `python3` and `venv` – for setting up the environment

You can install them on Debian/Ubuntu systems using:

```bash
sudo apt update
sudo apt install curl python3 python3-venv
```
---
### Installation

```bash
git clone https://github.com/hiteshdhawan/Aethershell.git
cd Aethershell
bash setup.sh
```


---
## Execution

```
source venv/bin/activate
python assistant.py
```


## Folder Structure
```aethershell/
├── assistant.py
├── action_planner.py
├── step_executor.py
├── executor.py
├── memory.py
├── prompt_engine.py
├── system_context.py
├── requirements.txt
├── setup.sh
├── models/                # Stores downloaded GGUF model
├── aether_memory.json     # Stores task memory/logs
└── venv/                  # Virtual environment (ignored)
```

## Model
This project uses the following model via llama-cpp-python:
mistral-7b-instruct-v0.1.Q4_K_M.gguf (Auto downloaded using setup.sh)

## How to Fork and Contribute

1. **Fork** this repository by clicking the "Fork" button on the top right.
2. **Clone** your fork locally:

   ```bash
   git clone https://github.com/your-username/Aethershell.git
   cd Aethershell
   ```
3. Create a **branch** for your feature or fix:
   
   ```bash
   git checkout -b your-feature-name
   ```
4. Make your changes, commit, and push:

   ```bash
   git add .
   git commit -m "Your message"
   git push origin your-feature-name
   ```

5. Open a Pull Request on GitHub and wait for review.

##  Author

Built and maintained by [Hitesh Dhawan](https://github.com/hiteshdhawan)

## Acknowledgements

Thanks to the open-source LLM and Python communities for providing the resources.

## Feedback

Have ideas, suggestions, or found a bug?  
Please open an [Issue](https://github.com/hiteshdhawan/Aethershell/issues) or start a [Discussion](https://github.com/hiteshdhawan/Aethershell/discussions) — your feedback is welcome!
