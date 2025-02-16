# Project Name

## Introduction
This project is designed to utilize the capabilities of the `smolagents` package to create and manage agents that can perform various tasks such as web searches and code generation. The project leverages the `LiteLLMModel` for language model operations and integrates tools like `DuckDuckGoSearchTool` and custom tools for enhanced functionality.

## Prerequisit

Install Ollama in local

pull model

```bash
ollama pull deepseek-r1:7b
```

make sure is running

```bash
ollama list
ollama run deepseek-r1:7b ""
```

check running
http://localhost:11434

## Installation
To install and set up the project, follow these steps:

1. Clone the repository:
    ```bash
    cd my-ai-agents
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
To run the project, execute the `main.py` script:

```bash
python.exe main.py
```

now visit http://127.0.0.1:7860/ to chat with your agent!