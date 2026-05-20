from dotenv import load_dotenv

import os

load_dotenv()

OLLAMA_BASE_URL = os.getenv(
    "OLLAMA_BASE_URL",
    "http://localhost:11434"
)

MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "ollama/llama3.2"
)
