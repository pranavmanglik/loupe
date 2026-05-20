from litellm import completion

from core.config import MODEL_NAME


def stream_answer(
    question: str,
    chunks: list[str],
):

    context = "\n\n".join(chunks)

    prompt = f"""
You are Loupe.

Answer ONLY using the provided context.

QUESTION:
{question}

CONTEXT:
{context}
"""

    response = completion(
        model=MODEL_NAME,
        stream=True,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    for chunk in response:

        try:

            delta = (
                chunk.choices[0]
                .delta
                .content
            )

            if delta:
                yield delta

        except:
            pass
