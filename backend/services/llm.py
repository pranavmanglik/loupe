import os

from litellm import completion


MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "groq/llama-3.3-70b-versatile",
)


def stream_answer(
    question: str,
    chunks: list[str],
):

    context = "\n\n".join(chunks)

    prompt = f"""
You are a helpful RAG assistant.

Answer ONLY using the provided context.

If the answer is not present in the context,
say you could not find it.

Context:
{context}

Question:
{question}
"""

    response = completion(
        model=MODEL_NAME,

        api_key=os.getenv(
            "OPENAI_API_KEY"
        ),

        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],

        stream=True,
    )

    for chunk in response:

        delta = (
            chunk.choices[0]
            .delta
            .content
        )

        if delta:

            yield delta
