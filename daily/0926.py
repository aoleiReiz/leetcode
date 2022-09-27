from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        n = len(nums)
        ans = []
        cur = 1
        idx = 0
        while idx < n:
            if cur == nums[idx]:
                idx += 1
                cur += 1
            elif cur < nums[idx]:
                ans.append(cur)
                cur += 1
            else:
                ans.append(cur)
                idx += 1
        if cur == n + 3 or len(ans) == 2:
            return ans
        elif cur < n + 3:
            while cur < n + 3:
                ans.append(cur)
                cur += 1
        return ans

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None
        elif root.val == val:
            return root
        elif root.val < val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        elif root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        prev = 0
        cur = nums[0]
        for i in range(1, len(nums)):
            prev, cur = cur, max(cur, prev + nums[i])

        return cur

    def isPowerOfTwo(self, n: int) -> bool:
        while n:
            digit = n % 2
            if digit == 1:
                return False
            n //= 2
        return True

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [0 for _ in range(n + 1)]
        for i in range(n-1, -1, -1):
            for j in range(0, i + 1):
                dp[j] = min(dp[j] , dp[j+1]) + triangle[i][j]
        return dp[0]



if __name__ == '__main__':
    s = Solution()
    print(s.missingTwo([2, 3]))