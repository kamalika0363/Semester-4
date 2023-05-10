print("===========================================")
print("KMP String Matching")
print("===========================================")

def computeLPSArray(pattern, M):
    lps = [0] * M
    len = 0
    i = 1
    while i < M:
        if pattern[i] == pattern[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def KMPSearch(pattern, text):
    M = len(pattern)
    N = len(text)
    lps = computeLPSArray(pattern, M)
    j = 0
    output = []
    i = 0
    while i < N:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == M:
            output.append(i - j)
            j = lps[j - 1]
        elif i < N and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    if len(output) > 0:
        print("Found pattern at indices: {}".format(output))
        print("Pattern occurred {} times".format(len(output)))
    else:
        print("Pattern not found in text.")
    print("===========================================")

text = input("Enter the text: ")
pattern = input("Enter the pattern: ")
KMPSearch(pattern, text)


# Advantages of KMP over Naive:
# 1. Time complexity of KMP is O(m + n) while that of Naive is O(mn).
# 2. KMP is efficient for large alphabets.
# 3. KMP is efficient for large patterns.
# 4. KMP is efficient for patterns with few distinct characters.
# 5. KMP is efficient for patterns that contain same character at different positions.
# 6. KMP is efficient for patterns that have some common sub-patterns.

# Disadvantages of KMP over Naive:
# 1. KMP is inefficient for small alphabets.
# 2. KMP is inefficient for small patterns.
# 3. KMP is inefficient for patterns with large number of distinct characters.
# 4. KMP is inefficient for patterns that contain same character at different positions.
# 5. KMP is inefficient for patterns that have no common sub-patterns.

# Time complexity of KMP:
# O(m + n) where m is the length of the pattern and n is the length of the text.

# Space complexity of KMP:
# O(m) where m is the length of the pattern.
