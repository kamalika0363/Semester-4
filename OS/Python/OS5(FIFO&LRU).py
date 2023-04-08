def fifo(ref, n, m):
    frames = []
    page_faults = 0
    for i in range(m):
        if ref[i] not in frames:
            if len(frames) < n:
                frames.append(ref[i])
            else:
                frames.pop(0)
                frames.append(ref[i])
            page_faults += 1
    print("Page Faults using FIFO:", page_faults)


def lru(ref, n, m):
    frames = []
    page_faults = 0
    for i in range(m):
        if ref[i] not in frames:
            if len(frames) < n:
                frames.append(ref[i])
            else:
                frames.pop(0)
                frames.append(ref[i])
            page_faults += 1
        else:
            frames.pop(frames.index(ref[i]))
            frames.append(ref[i])
    print("Page Faults using LRU:", page_faults)


print("--------------------------------------------------------")
print("Program to implement LRU & FIFO page Replacement Policies")  # By Om Hinge SECA 52
print("--------------------------------------------------------")
n = int(input("Enter the number of frames:"))
print("--------------------------------------------------------")
m = int(input("Enter the number of pages:"))
print("--------------------------------------------------------")
print("Enter the page reference string:")
ref = list(map(int, input().split()))
while True:
    print("Enter the page replacement algorithm to be used:")
    print("1. FIFO")
    print("2. LRU")
    print("3. Exit")
    ch = int(input())
    print("--------------------------------------------------------")
    if ch == 1:
        fifo(ref, n, m)
    elif ch == 2:
        lru(ref, n, m)
    else:
        break

print("--------------------------------------------------------")
