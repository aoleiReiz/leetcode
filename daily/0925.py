from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rotatedDigits(self, n: int) -> int:
        def rotate_helper(num, di):
            cur = num
            ans = 0
            temp = []
            while cur:
                digit = cur % 10
                if digit not in di:
                    return False
                cur //= 10
                temp.append(di[digit])
            for digit in temp[::-1]:
                ans = ans * 10 + digit
            return ans != num

        d = {
            1: 1,
            0: 0,
            2: 5,
            5: 2,
            6:9,
            8:8,
            9:6
        }
        count = 0
        for num in range(1, n + 1):
            if rotate_helper(num, d):
                count += 1
        return count

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        left = self.invertTree(root.right)
        right = self.invertTree(root.left)
        root.left = left
        root.right = right
        return root


if __name__ == '__main__':
    s = Solution()
    print(s.rotatedDigits(10))


