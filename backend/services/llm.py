from litellm import completion

from core.config import (
    OLLAMA_BASE_URL,
    MODEL_NAME,
)


async def stream_answer(
    question: str,
    chunks: list[str],
):

    context = "\n\n".join(chunks)

    prompt = f"""
You are Loupe.

You are a grounded AI assistant.

Answer ONLY using the provided context.

Be:
- concise
- conversational
- accurate

If information is missing,
say so clearly.

QUESTION:
{question}

CONTEXT:
{context}
"""

    response = completion(
        model=MODEL_NAME,
        api_base=OLLAMA_BASE_URL,
        stream=True,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    for chunk in response:

        delta = (
            chunk.choices[0]
            .delta
            .content
        )

        if delta:
            yield delta
