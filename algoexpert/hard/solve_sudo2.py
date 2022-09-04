def is_valid(i, j, num, board):
    row_valid = num not in board[i]
    col_valid = num not in [board[c][j] for c in range(9)]
    if not row_valid or not col_valid:
        return False
    row_start = (i // 3) * 3
    col_start = (j // 3) * 3
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if board[r][c] == num:
                return False
    return True


def try_digit_at_position(cur_row, cur_col, board):
    for num in range(1, 10):
        if is_valid(cur_row, cur_col, num, board):
            board[cur_row][cur_col] = num
            if solve_partial_sudoku(cur_row, cur_col + 1, board):
                return True
    board[cur_row][cur_col] = 0
    return False


def solve_partial_sudoku(row, col, board):
    cur_row = row
    cur_col = col
    if col == 9:
        cur_row += 1
        cur_col = 0
        if cur_row == 9:
            return True
    if board[cur_row][cur_col] == 0:
        return try_digit_at_position(cur_row, cur_col, board)
    return solve_partial_sudoku(cur_row, cur_col + 1, board)


def solveSudoku(board):
    # Write your code here.
    solve_partial_sudoku(0, 0, board)
    return board