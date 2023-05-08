print("===========================================")
print("Welcome to Disk Scheduling FCFS & SSTF")
print("===========================================")

# take user input
n = int(input("Enter the number of requests: "))
req = list(map(int, input("Enter the requests: ").strip().split()))[:n]
head = int(input("Enter the head position: "))

print("===========================================")
print("The requests are: ", req)
print("The head position is: ", head)
print("===========================================")

# FCFS algorithm
fcfs_head_movement = 0
prev = head
for r in req:
    fcfs_head_movement += abs(r - prev)
    prev = r

print("The Head Movement in FCFS disk scheduling algorithm is: ", fcfs_head_movement)
print("===========================================")

# SSTF algorithm
sstf_head_movement = 0
visited = [False] * n
for i in range(n):
    min_dist = float('inf')
    min_idx = -1
    for j in range(n):
        if not visited[j] and abs(req[j] - head) < min_dist:
            min_dist = abs(req[j] - head)
            min_idx = j
    visited[min_idx] = True
    sstf_head_movement += min_dist
    head = req[min_idx]

print("The Head Movement in SSTF disk scheduling algorithm is: ", sstf_head_movement)
print("===========================================")
