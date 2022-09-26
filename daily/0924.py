from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = []
        if k == 0:
            return [0] * n
        elif k > 0:
            for i in range(n):
                cur = 0
                for j in range(i + 1, i + k + 1):
                    cur += code[j % n]
                ans.append(cur)
        else:
            for i in range(n):
                cur = 0
                for j in range(i + k, i):
                    cur += code[j]
                ans.append(cur)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        level_orders = []
        q = [root]
        while q:
            level_vals = []
            temp = []
            for node in q:
                level_vals.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            q = temp
            level_orders.append(level_vals)
        return level_orders

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(node1, node2):
            if node1 is None and node2 is None:
                return True
            elif node1 and node2:
                return node1.val == node2.val and helper(node1.left, node2.right) and helper(node1.right, node2.left)
            else:
                return False

        return helper(root, root)

    def sortByBits(self, arr: List[int]) -> List[int]:
        def bit_1_count(num):
            count = 0
            while num:
                count += num % 2
                num //= 2
            return count
        arr = [(num, bit_1_count(num)) for num in arr]
        arr = sorted(arr, key=lambda x: [x[1],x[0]])
        arr = [t[0] for t in arr]
        return arr

    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(index, path, ans):
            if k - len(path) > n - index + 1:
                print(k - len(path), n - index + 1, f"index: {index}")
                return
            if len(path) == k:
                ans.append(path[:])
                return
            for i in range(index, n + 1):
                path.append(i)
                backtrack(i + 1, path, ans)
                path.pop()

        ans = []
        backtrack(1, [], ans)
        return ans

    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path, ans, used):
            if len(path) == len(nums):
                ans.append(path[:])
                return
            for i, num in enumerate(nums):
                if used[i]:
                    continue
                used[i] = True
                path.append(num)
                backtrack(path, ans, used)
                path.pop()
                used[i] = False
        ans = []
        backtrack([], ans, [False for _ in range(len(nums))])
        return ans

    def letterCasePermutation(self, s: str) -> List[str]:
        def backtrack(idx, path, ans, lows, uppers):
            print(path)
            if idx >= len(s):
                ans.append("".join(path))
                return
            if s[idx] in lows:
                for c in [s[idx], uppers[lows[s[idx]]]]:
                    path.append(c)
                    backtrack(idx + 1, path, ans, lows, uppers)
                    path.pop()
            else:
                path.append(s[idx])
                backtrack(idx + 1, path, ans, lows, uppers)
                path.pop()

        lower_letters = "abcdefghijklmnopqrstuvwxyz"
        upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower_letters_idx = {c:i for i,c in enumerate(lower_letters)}
        s = s.lower()
        ans = []
        backtrack(0, [], ans, lower_letters_idx, upper_letters)
        return ans



if __name__ == '__main__':
    s = Solution()
    print(s.letterCasePermutation("a1b2"))
