import asyncio

from services.docs_graph import (
    build_docs_graph,
)


async def main():

    graph = await build_docs_graph(
        "https://fastapi.tiangolo.com/"
    )

    for url, meta in graph.items():

        print()

        print(meta["title"])

        print(url)


asyncio.run(main())
