# kruskals algorithm
print("===========================================")
v = int(input("Enter the number of vertices: "))  # By Om Hinge 52 SECA
print("===========================================")
e = int(input("Enter the number of edges: "))
print("===========================================")
edges = []
print("Enter the edges and their weights:")
for i in range(e):
    edges.append(list(map(int, input().split())))
edges.sort(key=lambda x: x[2])
parent = [i for i in range(v)]
rank = [0 for i in range(v)]
print("===========================================")
print("The edges in the graph are:")
print("===========================================")
for i in range(e):
    print(edges[i][0], edges[i][1], edges[i][2])

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if rank[x] > rank[y]:
        parent[y] = x
    elif rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[y] = x
        rank[x] += 1


mst = []
for i in range(e):
    if find(edges[i][0]) != find(edges[i][1]):
        union(edges[i][0], edges[i][1])
        mst.append(edges[i])
print("===========================================")
print("The edges in the minimum spanning tree are:")
print("===========================================")
for i in range(len(mst)):
    print(mst[i][0], mst[i][1], mst[i][2])
print("===========================================")
