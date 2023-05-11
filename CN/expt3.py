def calcRedundantBits(m):
    for i in range(m):
        if 2 ** i >= m + i + 1:
            return i


def posRedundantBits(data, r):
    j = 0
    k = 1
    m = len(data)
    res = ''

    for i in range(1, m + r + 1):
        if i == 2 ** j:
            res = res + '0'
            j += 1
        else:
            res = res + data[-1 * k]
            k += 1

    return res[::-1]


def calcParityBits(arr, r):
    n = len(arr)

    for i in range(r):
        val = 1
        for j in range(1, n + 1):

            if j & (2 ** i) == (2 ** i):
                val = val ^ int(arr[-1 * j])

        arr = arr[:n - (2 ** i)] + str(val) + arr[n - (2 ** i) + 1:]
    return arr


def detectError(arr, nr):
    n = len(arr)
    res = 1

    for i in range(nr):
        val = 1
        for j in range(1, n + 1):
            if j & (2 ** i) == (2 ** i):
                val = val ^ int(arr[-1 * j])

        res = res + val * (10 ** i)

    return int(str(res), 2)


print("*****************************************")
print("Welcome to Hamming Code Machine")  # by Om Hinge 52 SECA
print("*****************************************")
data = input("Enter the data to be transmitted:")
print("*****************************************")

m = len(data)
r = calcRedundantBits(m)

arr = posRedundantBits(data, r)

arr = calcParityBits(arr, r)

print("Data transferred is " + arr)
print("*****************************************")

arr = input("Enter the received data:")
print("*****************************************")
print("Error Data is " + arr)
correction = detectError(arr, r)
if correction == 0:
    print("There is no error in the received message.")
else:
    print("The position of error is ", len(arr) - correction + 2, "from the left")
    print("The corrected message is ", arr[:len(arr) - correction] + str((int(arr[len(arr) - correction]) + 2) % 2) + arr[len(arr) - correction + 1:])
print("*****************************************")
