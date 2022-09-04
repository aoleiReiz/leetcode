from typing import List


class Solution:

    def solve_partial_sudoku(self, row, col, board):
        print(board)
        cur_row = row
        cur_col = col
        if col == len(board):
            cur_row += 1
            cur_col = 0
            if cur_row == len(board):
                return True
        if board[cur_row][cur_col] == ".":
            return self.try_digit_at_position(cur_row, cur_col, board)
        return self.solve_partial_sudoku(cur_row, cur_col + 1, board)

    def is_valid(self, row, col, num_str, board):
        row_valid = num_str not in board[row]
        col_valid = num_str not in [board[r][col] for r in range(len(board))]
        if not row_valid or not col_valid:
            return False
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        for r in range(row_start + 3):
            for c in range(col_start + 3):
                if board[r][c] == num_str:
                    return False
        return True

    def try_digit_at_position(self, row, col, board):
        for num_str in "123456789":
            if self.is_valid(row, col, num_str, board):
                board[row][col] = num_str
                if self.solve_partial_sudoku(row, col + 1, board):
                    return True
        board[row][col] = "."
        return False

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve_partial_sudoku(0, 0, board)


b = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

s = Solution()
s.solveSudoku(b)
print(b)
