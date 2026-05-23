def score_url(
    question,
    url,
    title,
):
    score = 0

    q = question.lower()

    url = url.lower()

    title = title.lower()

    keywords = [
        "model",
        "query",
        "queryset",
        "orm",
        "database",
        "migration",
        "field",
    ]

    for keyword in keywords:

        if keyword in q:

            if keyword in url:
                score += 5

            if keyword in title:
                score += 3

    return score


def choose_candidate_urls(
    question,
    graph,
    top_k=5,
):
    scored = []

    for url, node in graph.items():

        score = score_url(
            question,
            url,
            node["title"],
        )

        scored.append(
            (
                score,
                url,
            )
        )

    scored.sort(
        reverse=True
    )

    return [
        url
        for _, url in scored[:top_k]
    ]
