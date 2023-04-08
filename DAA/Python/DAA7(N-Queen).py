#  n queen problem using backtracking
print("===========================================")
n = int(input("Enter the number of queens: "))
print("===========================================")
board = [[0 for i in range(n)] for j in range(n)]
print("===========================================")
print("The board is:")
print("===========================================")
for i in range(n):
    print(board[i])
print("===========================================")


def queen(board, col):
    if col >= n:
        return True
    for i in range(n):
        if is_safe(board, i, col):
            board[i][col] = 1
            if queen(board, col + 1):
                return True
            board[i][col] = 0
    return False


def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


if queen(board, 0):
    print("===========================================")
    print("The solution is:")
    print("===========================================")
    for i in range(n):
        print([board[i][j])
    print("===========================================")
else:
    print("===========================================")
    print("No solution exists")
    print("===========================================")
