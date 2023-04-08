def split(matrix):
    n = len(matrix)
    mid = n // 2
    a = [[matrix[i][j] for j in range(mid)] for i in range(mid)]
    b = [[matrix[i][j] for j in range(mid, n)] for i in range(mid)]
    c = [[matrix[i][j] for j in range(mid)] for i in range(mid, n)]
    d = [[matrix[i][j] for j in range(mid, n)] for i in range(mid, n)]
    return a, b, c, d

def add_matrices(a, b):
    n = len(a)
    C = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = a[i][j] + b[i][j]
    return C

def subtract_matrices(a, b):
    n = len(a)
    c = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            c[i][j] = a[i][j] - b[i][j]
    return c

def strassen(a, b):
    n = len(a)
    if n == 1:
        return [[a[0][0] * b[0][0]]]

    a11, a12, a21, a22 = split(a)
    b11, b12, b21, b22 = split(b)

    p1 = strassen(a11, subtract_matrices(b12, b22))
    p2 = strassen(add_matrices(a11, a12), b22)
    p3 = strassen(add_matrices(a21, a22), b11)
    p4 = strassen(a22, subtract_matrices(b21, b11))
    p5 = strassen(add_matrices(a11, a22), add_matrices(b11, b22))
    p6 = strassen(subtract_matrices(a12, a22), add_matrices(b21, b22))
    p7 = strassen(subtract_matrices(a11, a21), add_matrices(b11, b12))

    c11 = add_matrices(subtract_matrices(add_matrices(p5, p4), p2), p6)
    c12 = add_matrices(p1, p2)
    c21 = add_matrices(p3, p4)
    c22 = subtract_matrices(subtract_matrices(add_matrices(p5, p1), p3), p7)

    c = [[0 for j in range(n)] for i in range(n)]
    for i in range(n // 2):
        for j in range(n // 2):
            c[i][j] = c11[i][j]
            c[i][j + n // 2] = c12[i][j]
            c[i + n // 2][j] = c21[i][j]
            c[i + n // 2][j + n // 2] = c22[i][j]
    return c


print("=====================================================")
print("Welcome to Strassen's Matrix Multiplication Algorithm")
print("=====================================================")
print("Enter the elements of the first matrix: ")
mat1 = [[int(input()) for j in range(2)] for i in range(2)]
print("Enter the elements of the second matrix: ")
mat2 = [[int(input()) for j in range(2)] for i in range(2)]
print("The first matrix is: ")
for row in mat1:
    print(row)
print("The second matrix is: ")
for row in mat2:
    print(row)
print("=====================================================")
print("The result of matrix multiplication is: ")
print("=====================================================")
c = strassen(mat1, mat2)
for row in c:
    print(row)
print("=====================================================")
