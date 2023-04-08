print("Welcome to Quick Sort machine")


def qs(arr):
    if len(arr) <= 1:
        return arr
    else:
        temp = arr[0]
        low = [x for x in arr[1:] if x <= temp]
        high = [x for x in arr[1:] if x > temp]
        return qs(low) + [temp] + qs(high)


n = (int(input("Enter the size of array:")))
print("Enter the array elements:")
array = []
for i in range(n):
    array.append(int(input()))
print("Unsorted array", array)
sorted_array = qs(array)
print("sorted array", sorted_array)
