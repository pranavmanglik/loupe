from litellm import completion


async def generate_answer(
    question: str,
    chunks: list[str]
):

    context = "\n\n".join(chunks)

    prompt = f"""
You are Loupe, an AI research assistant.

Answer the user's question ONLY using the provided context.

Provide:
- a clean
- concise
- well-structured answer

Do NOT dump raw text.

If information is missing, say so clearly.

QUESTION:
{question}

CONTEXT:
{context}
"""

    response = completion(
        model="ollama/deepseek-r1:1.5b",
        api_base="http://localhost:11434",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
