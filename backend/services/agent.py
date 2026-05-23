import json

from services.llm import client


def choose_relevant_pages(
    question: str,
    graph: dict,
):

    pages = []

    for url, meta in graph.items():

        title = meta.get(
            "title",
            ""
        )

        pages.append(
            f"{title} -> {url}"
        )

    docs_map = "\n".join(
        pages
    )

    prompt = f"""
    You are a documentation navigation agent.
    
    Choose the most relevant documentation URLs
    for answering the question.
    
    Rules:
    - Return ONLY valid JSON
    - Output MUST be a JSON array
    - No markdown
    - No explanation
    - Maximum 5 URLs
    
    Example output:
    [
      "https://example.com/page1",
      "https://example.com/page2"
    ]
    
    Question:
    {question}
    
    Documentation Pages:
    {docs_map}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],

        temperature=0,
    )

    content = (
        response
        .choices[0]
        .message
        .content
    )

    try:

        urls = json.loads(
            content
        )

        if isinstance(
            urls,
            list,
        ):

            return urls

    except Exception:

        pass

    return []
