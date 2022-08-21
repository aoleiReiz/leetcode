from typing import List






class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def is_valid(i, j, num_str, bo):
            row_valid = num_str not in bo[i]
            col_valid = num_str not in [bo[r][j] for r in range(9)]
            if not row_valid or not col_valid:
                return False
            row_start = i // 3 * 3
            col_start = j // 3 * 3
            for r in range(row_start, row_start + 3):
                for c in range(col_start, col_start + 3):
                    if bo[r][c] == num_str:
                        return False
            return True

        def try_num_str_at_position(i, j, bo):
            for num in range(1, 10):
                num_str = str(num)
                if is_valid(i, j, num_str, bo):
                    bo[i][j] = num_str
                    if solve_partial_soduku(i, j + 1, bo):
                        return True
            bo[i][j] = "."
            return False

        def solve_partial_soduku(i, j, bo):
            curr_row = i
            curr_col = j
            if curr_col == 9:
                curr_row += 1
                curr_col = 0
                if curr_row == 9:
                    return True
            if bo[curr_row][curr_col] == ".":
                return try_num_str_at_position(curr_row, curr_col, bo)
            return solve_partial_soduku(curr_row, curr_col + 1, bo)

        solve_partial_soduku(0, 0, board)


if __name__ == '__main__':
    s = Solution()
    b = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    s.solveSudoku(b)
    print(b)

