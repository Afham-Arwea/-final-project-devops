# Local AI Agent Orchestration & LLM Benchmark Lab

A comprehensive DevOps and Local AI laboratory project demonstrating the end-to-end containerized deployment of an autonomous AI Agent framework (`OpenClaw`) integrated with a private `Ollama` LLM inference engine.

## Overview & Key Highlights
* **Multi-Container Orchestration:** Manages both OpenClaw Gateway and the Ollama LLM engine inside a unified `docker-compose.yml` stack using service dependency rules.
* **Complete Privacy & Cost Control:** Inferences run locally on GPU/CPU with zero data leakage or per-token API costs.
* **Persistent Model Storage:** Dedicated Docker volume management ensures model weights persist across container restarts.

## Quick Start Guide

### 1. Running the Local AI Stack (Docker Compose)
Ensure Docker Desktop is running, then execute:

```bash
# 1. Launch both Ollama and OpenClaw services simultaneously
docker-compose up -d

# 2. Pull the target benchmark models into the Ollama container
docker exec -it openclaw-ollama-1 ollama run qwen3:8b
docker exec -it openclaw-ollama-1 ollama run glm4:9b
```

### 2. Running the Python Benchmark Games
```bash
# Run implementations directly
python Model1-GLM/main.py   # Run GLM-4 Endless Runner Game (Pygame)
python Model2-QWEN/main.py   # Run Qwen 3 Endless Runner Game (Tkinter)
```
