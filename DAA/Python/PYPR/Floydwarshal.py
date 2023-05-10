print("=====================================")
print("Welcome to Floyd Warshall Algorithm")  # by Om Hinge 52 SECA
print("=====================================")
print("Enter the number of vertices:")
n = int(input())
print("Enter the adjacency matrix:")
adj = []
for i in range(n):
    adj.append(list(map(int, input().split())))
print("The adjacency matrix is:")
for i in range(n):
    for j in range(n):
        print(adj[i][j], end=" ")
    print()
print("=====================================")
print("The shortest path matrix is:")
for k in range(n):
    for i in range(n):
        for j in range(n):
            adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])
for i in range(n):
    for j in range(n):
        print(adj[i][j], end=" ")
    print()
print("=====================================")

# Time Complexity: O(n^3) because of the nested loops
# Space Complexity: O(n^2) because of the adjacency matrix

