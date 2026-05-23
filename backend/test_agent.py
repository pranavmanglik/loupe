import asyncio

from services.agent import (
    choose_relevant_pages,
)

from services.docs_graph import (
    build_docs_graph,
)


QUESTION = """
How does dependency injection work in FastAPI?
"""


async def main():

    graph = await build_docs_graph(
        "https://fastapi.tiangolo.com/"
    )

    urls = choose_relevant_pages(
        QUESTION,
        graph,
    )

    print()

    print("Selected URLs:")

    print()

    for url in urls:

        print(url)


asyncio.run(main())
