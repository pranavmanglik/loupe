def chunk_text(
    text: str,
    chunk_size: int = 1000
):
    paragraphs = text.split("\n")

    chunks = []
    current = ""

    for para in paragraphs:

        if len(current) + len(para) < chunk_size:
            current += "\n" + para

        else:
            chunks.append(current)
            current = para

    if current:
        chunks.append(current)

    return chunks
