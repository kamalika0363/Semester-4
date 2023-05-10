def selectionSort(ar):
    for i in range(len(ar)):
        mini = i
        for j in range(i + 1, len(ar)):
            if ar[mini] > ar[j]:
                mini = j
        ar[i], ar[mini] = ar[mini], ar[i]
    return ar


print("=====================================")
print("Welcome to Selection Sort")
print("=====================================")
n = int(input("Enter the number of elements:"))
print("Enter the elements:")
arr = []
for k in range(n):
    arr.append(int(input()))
print("The unsorted array is:")
print(arr)
print("The sorted array is:")
print(selectionSort(arr))
print("=====================================")

# Time Complexity: O(n^2) because of the nested loops
# Space Complexity: O(1) because of the in-place sorting
