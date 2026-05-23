import os

from dotenv import load_dotenv

from groq import Groq


load_dotenv()


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def stream_answer(
    question: str,
    chunks: list[str],
):

    context = "\n\n".join(chunks)

    prompt = f"""
Use the context below to answer the question.

Context:
{context}

Question:
{question}
"""

    stream = client.chat.completions.create(
        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],

        temperature=0.4,

        stream=True,
    )

    for chunk in stream:

        content = (
            chunk.choices[0]
            .delta
            .content
        )

        if content:

            yield content
