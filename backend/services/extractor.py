import trafilatura


def extract_content(html: str):
    content = trafilatura.extract(html)

    return content or ""
