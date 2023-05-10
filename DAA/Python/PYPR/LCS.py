# Longest common subsequence
print("===========================================")
s1 = input("Enter the first string: ")
print("===========================================")
s2 = input("Enter the second string: ")
print("===========================================")
m = len(s1)
n = len(s2)
dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
for i in range(m + 1):
    for j in range(n + 1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif s1[i - 1] == s2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
i = m
j = n
s = ""
while i > 0 and j > 0:
    if s1[i - 1] == s2[j - 1]:
        s += s1[i - 1]
        i -= 1
        j -= 1
    elif dp[i - 1][j] > dp[i][j - 1]:
        i -= 1
    else:
        j -= 1
print("===========================================")
print("The length of the longest common subsequence is:", dp[m][n])
print("===========================================")
print("The longest common subsequence is:", s[::-1])
print("===========================================")

#Time Complexity: O(m*n)
#Space Complexity: O(m*n)
