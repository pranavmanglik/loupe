import httpx


async def fetch_url(url: str):

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    async with httpx.AsyncClient(
        follow_redirects=True,
        timeout=30,
    ) as client:

        response = await client.get(
            url,
            headers={
                "User-Agent": "Mozilla/5.0",
            },
        )

        response.raise_for_status()

        return response.text
