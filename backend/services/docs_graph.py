from urllib.parse import (
    urljoin,
    urlparse,
)

import httpx

from bs4 import BeautifulSoup


async def build_docs_graph(
    root_url: str,
    max_pages=25,
):
    graph = {}

    discovered = set()

    queue = [root_url]

    async with httpx.AsyncClient(
        timeout=10,
        follow_redirects=True,
    ) as client:

        while queue:

            if len(discovered) >= max_pages:
                break

            current_url = queue.pop(0)

            if current_url in discovered:
                continue

            discovered.add(current_url)

            print(
                f"Crawling: {current_url}"
            )

            try:

                response = await client.get(
                    current_url
                )

                soup = BeautifulSoup(
                    response.text,
                    "html.parser",
                )

                graph.setdefault(
                    current_url,
                    {
                        "title": (
                            soup.title.string
                            if soup.title
                            else current_url
                        ),
                        "links": [],
                        "visited": False,
                        "content": None,
                    },
                )

                for link in soup.find_all(
                    "a",
                    href=True,
                ):

                    href = link["href"]

                    absolute = urljoin(
                        current_url,
                        href,
                    )

                    parsed_root = urlparse(
                        root_url
                    ).netloc

                    parsed_absolute = urlparse(
                        absolute
                    ).netloc

                    if (
                        parsed_root
                        != parsed_absolute
                    ):
                        continue

                    if "#" in absolute:
                        continue

                    if absolute.endswith(
                        (
                            ".png",
                            ".jpg",
                            ".svg",
                            ".pdf",
                            ".zip",
                        )
                    ):
                        continue

                    graph[current_url][
                        "links"
                    ].append(absolute)

                    if (
                        absolute
                        not in discovered
                    ):
                        queue.append(
                            absolute
                        )

            except Exception as e:

                print(
                    f"Graph error: {current_url}",
                    e,
                )

    return graph
