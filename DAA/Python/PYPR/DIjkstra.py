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

# Time Complexity: O(V^2) where V is the number of vertices in the given graph. because of the nested loops
# Space Complexity: O(V) because of the dist and prev array

# advantages of Dijkstra’s algorithm:
# 1. It is used in GPS devices to find the shortest path between the current location and the destination.
# 2. It is used in network routing protocols like IGRP, OSPF, BGP etc.
# 3. It is used in driving directions applications such as Google Maps, Mapquest, Open Street Maps etc.
# 4. It is used in E-commerce applications for shipping the products from the source to the destination.
# 5. It is used in video games where we want to reach the target with minimum possible cost.
# 6. It is used in airlines ticketing systems to find the shortest path between source city and the destination city.

# disadvantages of Dijkstra’s algorithm:
# 1. It is used only when all the weights of the graph are positive.
# 2. It does not give the correct results for graphs with negative edges.
# 3. It is a greedy algorithm and does not guarantee the optimal solution.
# 4. It does not work for undirected graphs with cycles.
# 5. It does not work for graphs with loops.
# 6. It is not used when the graph is dynamic because it is computationally expensive.
