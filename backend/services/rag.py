from services.docs_graph import (
    build_docs_graph,
)

from services.agent import (
    choose_relevant_pages,
)

from services.crawler import (
    fetch_pages,
)

from services.extractor import (
    extract_content,
)

from services.planner import (
    choose_candidate_urls,
)

from services.explorer import (
    expand_neighbors,
)

from services.chunker import (
    chunk_text,
)

from services.retrieval import (
    Retriever,
)

from services.llm import (
    stream_answer,
)


async def run_rag(
    url: str,
    question: str,
):

    graph = await build_docs_graph(
        url
    )

    selected_urls = choose_candidate_pages(
        question,
        graph,
    )

    expanded_urls = expand_neighbors(
        graph,
        selected_urls,
        depth=2,
    )
    
    selected_urls = list(
        set(
            selected_urls +
            expanded_urls
        )
    )

    pages = await fetch_pages(
        selected_urls
    )

    all_content = []

    for page in pages:

        content = extract_content(
            page["html"]
        )

        all_content.append(
            content
        )

    combined_content = "\n\n".join(
        all_content
    )

    chunks = chunk_text(
        combined_content
    )

    retriever = Retriever(
        chunks
    )

    relevant_chunks = retriever.search(
        question,
        n=5,
    )

    for token in stream_answer(
        question,
        relevant_chunks,
    ):

        yield token
