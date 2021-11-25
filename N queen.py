N = 4
result = []


def issafe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solvequeen(board, col):
    if col == N:
        v = []
        for i in board:
            for j in range(len(i)):
                if i[j] == 1:
                    v.append(j+1)
        result.append(v)
        return True
        
    res = False
    for i in range(N):
        if issafe(board, i, col) == True:
            board[i][col] = 1

            res = solvequeen(board, col+1) or res

            board[i][col] = 0

    return res


board = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]

if solvequeen(board, 0):
    print(result)
else:
    print('not possible')
