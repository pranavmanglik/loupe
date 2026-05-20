from dotenv import load_dotenv

import os

load_dotenv()

MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "groq/llama-3.3-70b-versatile"
)
