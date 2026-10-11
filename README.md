# Local AI Agent Orchestration & LLM Benchmark Lab

A comprehensive DevOps and Local AI laboratory project demonstrating the end-to-end containerized deployment of an autonomous AI WebUI framework (`Open WebUI`) integrated with a private `Ollama` LLM inference engine.

## System Architecture

```text
+-----------------------------------------------------------------------+

|                             Host Machine                              |
|                                                                       |
|   +-------------------+               +-------------------+           |
|   |  Browser (User)   |               |   Docker Engine   |           |
|   +---------+---------+               +---------+---------+           |
|             |                                   |                     |
|             | (Port 18789)                      v                     |
|             v                                                         |
|   +---------------------------------------------------------------+   |
|   | Container: openclaw-openclaw-gateway-1                        |   |
|   | - Enterprise Web Workspace UI Dashboard (Open WebUI)          |   |
|   | - Enterprise RAG & Multi-User Governance Engine               |   |
|   +-------------------------------+-------------------------------+   |
|                                   |                                   |
|                                   | (Shared Docker Bridge Network)    |
|                                   v                                   |
|   +---------------------------------------------------------------+   |
|   | Container: openclaw-ollama-1                                  |   |
|   | - Local LLM Inference Daemon (Port 11434)                     |   |
|   | - Volume: ollama_data:/root/.ollama                           |   |
|   +-------------------------------+-------------------------------+   |
|                                   |                                   |
|                                   v                                   |
|                   +-------------------------------+                   |
|                   |      Model Weights (Local)    |                   |
|                   |      - qwen2.5:1.5b (986 MB)  |                   |
|                   |      - glm4:9b-q4 (5.5 GB)    |                   |
|                   +-------------------------------+                   |
+-----------------------------------------------------------------------+
```

## Repository Structure

```text
devops/
├── .github/
│   └── workflows/
│       └── ci.yml               # GitHub Actions CI workflow (Docker & Python tests)
├── Model1-GLM/
│   ├── main.py                  # Model 1 Implementation (GLM-4 9B) - Endless Runner Game
│   └── requirements.txt         # Pygame-ce dependency
├── Model2-QWEN/
│   ├── main.py                  # Model 2 Implementation (Qwen 2.5) - Endless Runner Game
│   └── requirements.txt         # Standard library documentation fallback
├── docker-compose.yml           # Multi-container orchestration definition
├── .env.example                 # Template for environment variables and secrets
├── .gitignore                   # Excludes virtual environments, caches, and secrets
├── README.md                    # Project landing page and architectural documentation
└── result.md                    # Comparative benchmark evaluation report
```

## LLM Benchmark: Qwen 2.5 (1.5B) vs. GLM-4 (9B)

Both models were independently prompted with the exact same natural language specification:

> **Benchmark Prompt:**
> "สร้างเกมวิ่ง (Endless Runner) ด้วย Python พร้อมหน้าจอ GUI และปุ่มเริ่มเกม"
> *(English: "Create an Endless Runner Game using Python with a GUI window and a game start loop.")*

Below is the comparative evaluation based on core game mechanics and architectural choices from `result.md`:

*   **GUI Framework**
    *   **Model 1: GLM-4 (9B):** Pygame
    *   **Model 2: Qwen 2.5 (1.5B):** Tkinter (Standard Library)
*   **Jump Physics**
    *   **Model 1: GLM-4 (9B):** Constant frame polling with kinetic velocity updates.
    *   **Model 2: Qwen 2.5 (1.5B):** Event-driven interval execution via native `.after()` scheduling.
*   **Collision Logic**
    *   **Model 1: GLM-4 (9B):** Leverages automated boundary boxes via `pygame.Rect.colliderect()`.
    *   **Model 2: Qwen 2.5 (1.5B):** Implements manual dynamic coordinate boundaries evaluation mapping.
*   **External Dependencies**
    *   **Model 1: GLM-4 (9B):** Requires external installation of `pygame-ce`.
    *   **Model 2: Qwen 2.5 (1.5B):** Zero external dependencies (runs out of the box).

Detailed analysis and code snippets are available in `result.md`.

## Quick Start Guide

### 1. Running the Local AI Stack (Docker Compose)
Ensure Docker Desktop is running, then execute:

```bash
# 1. Launch both Ollama and Open WebUI services simultaneously
docker-compose up -d

# 2. Pull the target benchmark models into the Ollama container
docker exec -it openclaw-ollama-1 ollama run qwen2.5:1.5b
docker exec -it openclaw-ollama-1 ollama run glm4:9b-q4_K_M
```

### 2. Running the Python Benchmark Games
```bash
# Run implementations directly
python Model1-GLM/main.py   # Run GLM-4 Endless Runner Game (Pygame)
python Model2-QWEN/main.py   # Run Qwen 3 Endless Runner Game (Tkinter)
```

## DevOps Design Decisions

1. **Service Decoupling:** Decoupled the LLM inference engine (Ollama) from the web application interface layer (Open WebUI) into isolated containers. If the WebUI gateway crashes or restarts, loaded model memory in Ollama remains intact.
2. **Infrastructure as Code (IaC):** Configured the entire multi-service lifecycle inside a single `docker-compose.yml`, reducing cluster startup to a single `docker-compose up -d` command.
3. **Compatibility-Engineered Dependencies:** Standardized on `pygame-ce` across `requirements.txt` to guarantee cross-compatibility across modern Python versions (3.11 - 3.14+) on Windows, Linux, and macOS.
4. **Security by Default:** Enforces local dashboard admin accounts authentication and isolates container networks to prevent unauthorized remote code execution.
