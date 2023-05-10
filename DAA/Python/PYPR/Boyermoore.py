#implement Boyer Moore algorithm
print("=====================================")
print("Welcome to Boyer Moore Algorithm")
print("=====================================")
print("Enter the text:")
text = input()
print("Enter the pattern:")
pattern = input()
print("=====================================")
print("The text is:")
print(text)
print("=====================================")
print("The pattern is:")
print(pattern)
print("=====================================")
print("The pattern is found at:")
n = len(text)
m = len(pattern)
i = 0
while i <= n - m:
    j = m - 1
    while j >= 0 and text[i + j] == pattern[j]:
        j -= 1
    if j == -1:
        print(i)
        i += m
    else:
        if text[i + j] in pattern:
            i += j - pattern.index(text[i + j])
        else:
            i += j + 1
print("=====================================")

#Advantages of Boyer Moore algorithm
# 1. It is faster than other string matching algorithms.
# 2. It is efficient for large alphabets.

#Disadvantages of Boyer Moore algorithm
# 1. It is not efficient for small alphabets.
# 2. It is not efficient for small patterns.
# 3. It is not efficient for patterns with few distinct characters.
# 4. It is not efficient for patterns that contain same character at different positions.
# 5. It is not efficient for patterns that have some common sub-patterns.

#Time complexity of Boyer Moore algorithm
# Best case: O(n/m) explanation: O(n/m) + O(m) = O(n/m)
# Worst case: O(mn)
# where n is the length of the text and m is the length of the pattern

#Space complexity of Boyer Moore algorithm
# O(m) where m is the length of the pattern
