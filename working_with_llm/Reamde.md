# Working with LLM

A project for exploring and integrating large language models (LLMs) locally.

## Prerequisites

- Python 3.8+
- Ollama (for running LLMs locally)

## Installation

### 1. Install Ollama
Download from [ollama.com/download](https://ollama.com/download) for your platform (Mac, Linux, or Windows).

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

## Quick Start

1. Start Ollama:
   ```bash
   ollama serve
   ```

2. Pull a model:
   ```bash
   ollama pull llama2
   ```

3. Run the project:
   ```bash
   python main.py
   ```

## Usage

Interact with local LLMs through the project's interface. Ollama handles model management and inference.

## Available Models

Check [ollama.com/library](https://ollama.com/library) for available models to pull.