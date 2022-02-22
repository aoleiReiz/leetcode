from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    #从前序与中序遍历序列构造二叉树
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def recur(pre_start, pre_end, in_start, in_end, in_map):
            if pre_start > pre_end or in_start > in_end :
                return
            in_root = in_map[preorder[in_start]]
            num_left = in_root - in_start
            root = TreeNode(preorder[pre_start])
            root.left = recur(pre_start + 1, pre_start + num_left, in_start, in_root, in_map)
            root.right = recur(pre_start + num_left + 1, pre_end, in_root + 1, in_end, in_map)
            return root
        in_map = {v : i for i,v in enumerate(inorder)}
        return  recur(0, len(preorder)-1, 0, len(inorder)-1, in_map)

    #从中序与后序遍历序列构造二叉
    def buildTree2(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def recur(in_start, in_end, in_map):
            if in_start > in_end:
                return
            val = postorder.pop()
            in_root = in_map[val]
            node = TreeNode(val)
            node.right = recur(in_root + 1, in_end, in_map)
            node.left = recur(in_start, in_root - 1, in_map)
            return node
        in_map = {v : i for i,v in enumerate(inorder)}
        return recur(0, len(inorder) - 1, in_map)

    #前序遍历构造二叉搜索树
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def helper(lower = float('-inf'), upper = float('inf')):
            nonlocal idx
            if idx == n:
                return None
            val = preorder[idx]
            if val < lower or val > upper:
                return None
            idx += 1
            root = TreeNode(val)
            root.left = helper(lower, val)
            root.right = helper(val, upper)
            return root

        idx = 0
        n = len(preorder)
        return helper()

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def is_valid(i, j, num):
            # check row
            n = len(board)
            for c in range(n):
                if j != c and board[i][c] == num:
                    return False
            # check col
            for r in range(n):
                if r != i and board[r][j] == num:
                    return False
            # check square
            row_start = i // 3
            col_start = j // 3
            for r in range(row_start * 3, row_start * 3 + 3):
                for c in range(col_start * 3 , col_start * 3 + 3):
                    if (r != i or j != c) and board[r][c] == num:
                        return False
            return True

        def find_next_coord():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        return (i, j)
            return None

        def helper():
            pos = find_next_coord()
            if pos is not None:
                i, j = pos
                for n_str in '123456789':
                    if is_valid(i, j, n_str):
                        board[i][j] = n_str
                        if helper():
                            return True
                        board[i][j] = '.'
                return False
            return True

        helper()

    def generateParenthesis(self, n: int) -> List[str]:
        def helper(left, right, cur):
            if len(cur) == 2 * n:
                res.append("".join(cur))
                return
            if left < n:
                cur.append("(")
                helper(left + 1, right, cur)
                cur.pop()
            if right < left:
                cur.append(")")
                helper(left, right + 1, cur)
                cur.pop()
        res = []
        helper(0, 0, [])
        return res

    def letterCombinations(self, digits: str) -> List[str]:
        def helper(start, cur, res):
            if start == len(digits):
                res.append("".join(cur[:]))
                return
            for c in m[digits[start]]:
                cur.append(c)
                helper(start + 1, cur, res)
                cur.pop()

        m = {'2':'abc', '3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv',9:'wxyz'}
        res = []
        helper(0,[],res)
        return res

    def letterCasePermutation(self, S: str) -> List[str]:
        def helper(start, cur, res):
            if start == len(S):
                if len(cur) > 0:
                    res.append("".join(cur[:]))
                return
            for c in m[S[start]]:
                cur.append(c)
                helper(start + 1, cur, res)
                cur.pop()
        m = {}
        for i in '0123456789':
            m[i] = [i]
        for c in 'abcdefghijklmnopqrstuvwxyz':
            m[c] = [c,chr(ord(c) - 32)]
            m[chr(ord(c) - 32)] = [c,chr(ord(c) - 32)]
        res = []
        helper(0, [], res)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.letterCasePermutation("3z4"))

