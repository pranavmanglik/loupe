from services.fetcher import fetch_url
from services.extractor import extract_content
from services.chunker import chunk_text
from services.retrieval import Retriever
from services.llm import stream_answer


async def run_rag(
    url: str,
    question: str,
):

    html = await fetch_url(url)

    content = extract_content(html)

    chunks = chunk_text(content)

    retriever = Retriever(chunks)

    relevant_chunks = retriever.search(
        question,
        n=5
    )

    for token in stream_answer(
        question,
        relevant_chunks
    ):

        yield token
