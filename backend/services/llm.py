import os

from litellm import completion


MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "groq/llama-3.3-70b-versatile"
)


def stream_answer(
    question: str,
    chunks: list[str],
):

    context = "\n\n".join(chunks)

    prompt = f"""
Use the provided context to answer the question.

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
