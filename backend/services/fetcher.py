import httpx


def normalize_url(url: str):

    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    return url


async def fetch_url(url: str):

    url = normalize_url(url)

    async with httpx.AsyncClient() as client:

        response = await client.get(
            url,
            timeout=20,
            follow_redirects=True
        )

    return response.text
