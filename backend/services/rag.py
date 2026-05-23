from services.docs_graph import (
    build_docs_graph,
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

    print()

    print("Building docs graph...")

    graph = await build_docs_graph(
        url
    )

    print()

    print("Choosing candidate URLs...")

    selected_urls = choose_candidate_urls(
        question,
        graph,
    )

    print()

    print("Initial URLs:")

    for u in selected_urls:
        print(u)

    expanded_urls = expand_neighbors(
        graph,
        selected_urls,
        depth=1,
        max_urls=15,
    )

    selected_urls = list(
        set(
            selected_urls +
            expanded_urls
        )
    )[:10]

    print()

    print("Expanded URLs:")

    for u in selected_urls:
        print(u)

    print()

    print("Fetching pages...")

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

    print()

    print("Chunking content...")

    chunks = chunk_text(
        combined_content
    )

    retriever = Retriever(
        chunks
    )

    print()

    print("Searching relevant chunks...")

    relevant_chunks = retriever.search(
        question,
        n=5,
    )

    print()

    print("Generating answer...")

    for token in stream_answer(
        question,
        relevant_chunks,
    ):

        yield token
