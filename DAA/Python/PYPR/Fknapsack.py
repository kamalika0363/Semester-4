# Implement Fractional Knapsack Problem
print("=====================================")
print("Welcome to Fractional Knapsack Problem")
print("=====================================")
print("Enter the number of items:")
n = int(input())
print("Enter the capacity of knapsack:")
c = int(input())
print("Enter the weights of items:")
w = list(map(int, input().split()))
print("Enter the profits of items:")
p = list(map(int, input().split()))
print("=====================================")
print("The weights & Profits of items are:")
print("Weights:", end=" ")
print("Profits:")
for i in range(n):
    print(w[i],"\t\t", p[i])
print("=====================================")
print("The ratio of profits to weights are:")
r = []
for i in range(n):
    r.append(p[i] / w[i])
for i in range(n):
    print(r[i], end=" ")
print()
print("=====================================")
print("The sorted ratio of profits to weights are:")
for i in range(n):
    for j in range(n - i - 1):
        if r[j] < r[j + 1]:
            r[j], r[j + 1] = r[j + 1], r[j]
            p[j], p[j + 1] = p[j + 1], p[j]
            w[j], w[j + 1] = w[j + 1], w[j]
for i in range(n):
    print(r[i], end=" ")
print()
print("=====================================")
print("The sorted weights of items are:")
for i in range(n):
    print(w[i], end=" ")
print()
print("The sorted profits of items are:")
for i in range(n):
    print(p[i], end=" ")
print()
print("=====================================")
print("The maximum profit is:")
profit = 0
for i in range(n):
    if w[i] <= c:
        profit += p[i]
        c -= w[i]
    else:
        profit += c * r[i]
        break
print(profit)
print("=====================================")

# Time Complexity: O(n^2) because of the nested loops
# Space Complexity: O(n) because of the ratio array


