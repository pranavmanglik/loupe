from collections import deque


def expand_neighbors(
    graph,
    start_urls,
    depth=2,
):
    visited = set()

    queue = deque()

    for url in start_urls:
        queue.append((url, 0))

    expanded = []

    while queue:

        current, current_depth = (
            queue.popleft()
        )

        if current in visited:
            continue

        visited.add(current)

        expanded.append(current)

        if current_depth >= depth:
            continue

        node = graph.get(current)

        if not node:
            continue

        for neighbor in node["links"]:

            queue.append(
                (
                    neighbor,
                    current_depth + 1,
                )
            )

    return expanded
