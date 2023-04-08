# Implementation of memory allocation algorithms like best-fit, first-fit, worst-fit.

def first_fit(blocks, processes, n, m):
    b = blocks.copy()
    p = processes.copy()
    allocation = [-1] * n
    for i in range(n):
        for j in range(m):
            if b[j] >= p[i]:
                allocation[i] = j
                b[j] -= p[i]
                break
    print("Process No.\tProcess Size\tBlock no.")
    for i in range(n):
        print(i + 1, "\t\t\t", p[i], "\t\t\t", end="")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")


def best_fit(blocks, processes, n, m):
    b = blocks.copy()
    p = processes.copy()
    allocation = [-1] * n
    for i in range(n):
        best = -1
        for j in range(m):
            if b[j] >= p[i]:
                if best == -1:
                    best = j
                elif b[best] > b[j]:
                    best = j
        if best != -1:
            allocation[i] = best
            b[best] -= p[i]
    print("Process No.\tProcess Size\tBlock no.")
    for i in range(n):
        print(i + 1, "\t\t\t", p[i], "\t\t\t", end="")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")


def worst_fit(blocks, processes, n, m):
    b = blocks.copy()
    p = processes.copy()
    allocation = [-1] * n
    for i in range(n):
        worst = -1
        for j in range(m):
            if b[j] >= p[i]:
                if worst == -1:
                    worst = j
                elif b[worst] < b[j]:
                    worst = j
        if worst != -1:
            allocation[i] = worst
            b[worst] -= p[i]
    print("Process No.\tProcess Size\tBlock no.")
    for i in range(n):
        print(i + 1, "\t\t\t", p[i], "\t\t\t", end="")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")


print("-----------------------------------------------------")
print("Welcome to Memory Allocation Algorithms")  # by Om Hinge 52 SECA
print("-----------------------------------------------------")
n = int(input("Enter the number of processes:"))
print("-----------------------------------------------------")
m = int(input("Enter the number of memory blocks:"))
print("-----------------------------------------------------")
blocks = list(map(int, input("Enter the size of the memory blocks:").split()))
print("-----------------------------------------------------")
processes = list(map(int, input("Enter the size of the processes:").split()))
print("-----------------------------------------------------")
ch = 0
while ch != 4:
    print("Enter the memory allocation algorithm to be used:")
    print("1. First Fit")
    print("2. Best Fit")
    print("3. Worst Fit")
    print("4. Exit")
    print("-----------------------------------------------------")
    ch = int(input())
    print("-----------------------------------------------------")
    if ch == 1:
        first_fit(blocks, processes, n, m)
    elif ch == 2:
        best_fit(blocks, processes, n, m)
    elif ch == 3:
        worst_fit(blocks, processes, n, m)
    else:
        print("exit")
    print("-----------------------------------------------------")

print("-----------------------------------------------------")
print("Thank you for using the program")
print("-----------------------------------------------------")
