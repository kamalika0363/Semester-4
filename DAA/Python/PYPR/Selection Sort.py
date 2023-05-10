def selectionSort(arr):
    for i in range(len(arr)):
        mini = i
        for j in range(i + 1, len(arr)):
            if ar[mini] > arr[j]:
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]
    return arr


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
