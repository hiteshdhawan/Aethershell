
# AetherShell

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

[![Releases](https://img.shields.io/github/v/release/hiteshdhawan/Aethershell?label=Latest%20Release)](https://github.com/hiteshdhawan/Aethershell/releases)


AetherShell is an AI-native Linux assistant that understands high-level natural language tasks and autonomously plans, executes, and validates actions using a local LLM (Mistral) without internet dependency.

It bridges the gap between natural language and real-time shell execution in a fully isolated, self-contained environment.

---

## Features — Smarter, Safer, AI-Enhanced Terminal

### 1. Natural Language Shell Commands
Interact with your Linux terminal in plain English:

> “Create a folder called `test` and open it.”

AetherShell understands and converts it to:

```bash
mkdir test && cd test
```

- Skip memorizing complex syntax  
- Ideal for both beginners and advanced users  
- Fast, intuitive command translation

---

### 2. Local AI Integration (LLM-powered)
Powered by `llama-cpp` and Mistral-7B, AetherShell runs entirely offline on your machine.

> “List the 10 biggest files in this directory.”

AetherShell understands and converts it to:
```bash
du -ah | sort -rh | head -n 10
```

- No internet required  
- Maximum privacy and performance  
- Works on air-gapped systems

---

### 3. Dynamic Multi-Step Execution
AetherShell understands and executes multi-step tasks intelligently.

> “Install Python, create a virtual environment, and activate it.”

```bash
sudo apt install python3
python3 -m venv venv
source venv/bin/activate
```

- Automates routine tasks  
- Reduces manual effort  
- Task planning handled by AI

---

### 4. Memory Persistence
AetherShell saves session history and context in a structured format (`aether_memory.json`).

- Maintains task continuity  
- Remembers prior commands  
- Enables contextual conversations

---

### 5. Offline Capability
All features work without an internet connection.

- Fully self-contained  
- No external API calls  
- Perfect for private, secure environments

---

### 6. Optional Cloud Fallback (WIP)
Future support for hybrid execution using cloud models when needed.

- Seamless switch to cloud using claude, gemini, etc. 
- Useful for low-end systems  
- Still prioritizes local-first privacy
- This feature will only be executed, if allowed by the user.

---

### 7. Secure Execution Sandbox (WIP)
AetherShell will feature isolated environments to run commands securely.

- Limits system-level access  
- Helps prevent accidental damage  
- Ideal for testing and sandboxed execution
- Ideal for script development.

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
