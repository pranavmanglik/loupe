import httpx


async def fetch_pages(
    urls: list[str],
):

    pages = []

    async with httpx.AsyncClient(
        timeout=20,
        follow_redirects=True,
    ) as client:

        for url in urls:

            try:

                response = await client.get(
                    url
                )

                pages.append(
                    {
                        "url": url,
                        "html": response.text,
                    }
                )

            except Exception as e:

                print(
                    f"crawl error: {url}",
                    e,
                )

    return pages
