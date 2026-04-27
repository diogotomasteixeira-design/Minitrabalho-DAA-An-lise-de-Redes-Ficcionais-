from collections import deque


def bfs(graph, source):
    visited = {}
    dist = {}
    parent = {}

    for v in graph:
        visited[v] = False
        dist[v] = float('inf')
        parent[v] = None

    queue = deque()

    visited[source] = True
    dist[source] = 0
    queue.append(source)

    while queue:
        v = queue.popleft()

        for w in graph[v]:
            if not visited[w]:
                visited[w] = True
                dist[w] = dist[v] + 1
                parent[w] = v
                queue.append(w)

    return visited, dist, parent


graph = {
    "Eddard-Stark": ["Jon-Snow", "Robert-Baratheon", "Catelyn-Stark"],
    "Jon-Snow": ["Eddard-Stark", "Samwell-Tarly"],
    "Robert-Baratheon": ["Eddard-Stark", "Cersei-Lannister"],
    "Catelyn-Stark": ["Eddard-Stark", "Arya-Stark", "Sansa-Stark"],
    "Samwell-Tarly": ["Jon-Snow"],
    "Cersei-Lannister": ["Robert-Baratheon", "Jaime-Lannister"],
    "Jaime-Lannister": ["Cersei-Lannister"],
    "Arya-Stark": ["Catelyn-Stark"],
    "Sansa-Stark": ["Catelyn-Stark"]
}


visited, dist, parent = bfs(graph, "Jon-Snow")

print("=== VISITED ===")
for v in visited:
    print(v, "->", visited[v])

print("\n=== DISTÂNCIAS ===")
for v in dist:
    print(v, "->", dist[v])

print("\n=== PARENTS / CAMINHO ===")
for v in parent:
    print(v, "->", parent[v])




#           Jon-Snow
#          /        \
#   Eddard --------- Samwell
#     |    \
#     |     \
#     |      \
#   Robert  Catelyn
#     |         /   \
#     |        /     \
#   Cersei Arya   Sansa
#     |
#   Jaime
