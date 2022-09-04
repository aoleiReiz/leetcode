def is_valid(i, j, num, board):
    # check row
    for col in range(9):
        if col != j and board[i][col] == num:
            return False
    # check col
    for row in range(9):
        if row != i and board[row][j] == num:
            return False
    # check subs
    row_start = i // 3
    col_start = j // 3
    for r in range(3 * row_start, 3 * row_start + 3):
        for c in range(3 * col_start, 3 * col_start + 3):
            if (r != i or j != c) and board[r][c] == num:
                return False
    return True


def find_next_position(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


def helper(board):
    postion = find_next_position(board)
    if postion is not None:
        i, j = postion
        for num in range(1, 10):
            if is_valid(i, j, num, board):
                board[i][j] = num
                if helper(board):
                    return True
                board[i][j] = 0
        return False
    return True


def solveSudoku(board):
    # Write your code here.
    helper(board)
    return board


b = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
  ]

print(solveSudoku(b))