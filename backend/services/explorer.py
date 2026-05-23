from collections import deque


def expand_neighbors(
    graph,
    start_urls,
    depth=1,
    max_urls=15,
):
    visited = set()

    queue = deque()

    for url in start_urls:
        queue.append((url, 0))

    expanded = []

    while queue:

        if len(expanded) >= max_urls:
            break

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

            if neighbor not in visited:

                queue.append(
                    (
                        neighbor,
                        current_depth + 1,
                    )
                )

    return expanded
