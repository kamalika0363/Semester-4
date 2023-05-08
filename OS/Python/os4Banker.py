p = int(input("Enter the no of processes: "))
r = int(input("Enter the no of resources: "))

max_matrix = []
alloc_matrix = []
need_matrix = []
completed = [False] * p
safe_sequence = []
available = []

# input the Max Matrix
print("Enter the Max Matrix: ")
for i in range(p):
    print(f"For process {i+1}: ", end="")
    max_matrix.append(list(map(int, input().split())))

# input the Allocation Matrix
print("Enter the Allocation Matrix: ")
for i in range(p):
    print(f"For process {i+1}: ", end="")
    alloc_matrix.append(list(map(int, input().split())))

# input the Available Resources
print("Enter the Available Resources: ", end="")
available = list(map(int, input().split()))

# calculate the Need Matrix
for i in range(p):
    row = []
    for j in range(r):
        row.append(max_matrix[i][j] - alloc_matrix[i][j])
    need_matrix.append(row)

# find a safe sequence
while len(safe_sequence) < p:
    found = False
    for i in range(p):
        if not completed[i]:
            if all(available[j] >= need_matrix[i][j] for j in range(r)):
                completed[i] = True
                safe_sequence.append(i+1)
                available = [available[j] + alloc_matrix[i][j] for j in range(r)]
                found = True
    if not found:
        break

if len(safe_sequence) == p:
    print("The system is in a safe state!")
    print("Safe Sequence: <", end=" ")
    for i in range(p):
        print(safe_sequence[i], end=" ")
    print(">")
else:
    print("The system is in an unsafe state!")
