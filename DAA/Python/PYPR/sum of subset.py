#Implement Sum of Subset Problem
print("=====================================")
print("Welcome to Sum of Subset Problem")
print("=====================================")
print("Enter the number of elements:")
n = int(input())
print("Enter the elements:")
s = list(map(int, input().split()))
print("Enter the sum:")
sum = int(input())
print("=====================================")
print("The elements are:")
for i in range(n):
    print(s[i], end=" ")
print()
print("=====================================")
print("The sum is:")
print(sum)
print("=====================================")
print("The solution is:")
dp = [[False for i in range(sum + 1)] for j in range(n + 1)]
for i in range(n + 1):
    dp[i][0] = True
for i in range(1, n + 1):
    for j in range(1, sum + 1):
        if j < s[i - 1]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = dp[i - 1][j] or dp[i - 1][j - s[i - 1]]
print("=====================================")
if dp[n][sum]:
    print("The solution exists")
    print("=====================================")
else:
    print("The solution does not exist")
    print("=====================================")
print("The solution subsets for the given sum({}) is:".format(sum))
i = n
j = sum
while i > 0 and j > 0:
    if dp[i][j] == dp[i - 1][j]:
        i -= 1
    else:
        print(s[i - 1], end=" ")
        j -= s[i - 1]
        i -= 1
print()
print("=====================================")

# Time Complexity: O(n*sum) because we are using a nested loop.
# Space Complexity: O(n*sum) because we are using a 2D array to store the values.
