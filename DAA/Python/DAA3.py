def dijkstra(graph_, src):
    dist = {}
    prev = {}
    for node in graph_:
        dist[node] = float('inf')
        prev[node] = None
    dist[src] = 0
    Q = set(graph_.keys())
    while Q:
        u = min(Q, key=lambda x: dist[x])
        Q.remove(u)
        for v in graph_[u]:
            alt = dist[u] + graph_[u][v]
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
    return prev, dist


print("=====================================================")
print("welcome to the Dijkstra’s algorithm using Greedy method and analyze it. ")
print("=====================================================")
graph = {
    'A': {'A': 0, 'B': 10, 'C': 5, 'D': 40},
    'B': {'D': 10, 'E': 40},
    'C': {'B': 5, 'E': 60},
    'D': {'E': 50},
    'E': {'E': 0}
}
print("=====================================================")
print("The graph is:")
print(graph)
print("=====================================================")
start = (input("Enter The starting Node:"))
print(dijkstra(graph, start))
print("=====================================================")
