from urllib.parse import (
    urljoin,
    urlparse,
)

import httpx

from bs4 import BeautifulSoup


async def build_docs_graph(
    root_url: str,
    max_links: int = 100,
):

    graph = {}

    domain = urlparse(root_url).netloc

    async with httpx.AsyncClient(
        timeout=20,
        follow_redirects=True,
    ) as client:

        response = await client.get(root_url)

        soup = BeautifulSoup(
            response.text,
            "html.parser",
        )

        links = soup.find_all("a")

        discovered = set()

        for link in links:

            href = link.get("href")

            text = (
                link.get_text(strip=True)
            )

            if not href:
                continue

            absolute = urljoin(
                root_url,
                href,
            )

            parsed = urlparse(
                absolute
            )

            if parsed.netloc != domain:
                continue

            if "#" in absolute:
                continue

            if absolute in discovered:
                continue

            discovered.add(absolute)

            graph[absolute] = {
                "title": text,
            }

            if len(graph) >= max_links:
                break

    return graph
