from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        n = len(nums)
        nums = sorted(nums)
        if nums[0] >= n:
            return n
        for i, num in enumerate(nums):
            if num >= n - i and not (i > 0 and nums[i - 1] >= n - i):
                return n - i
        return -1

    def minCostToMoveChips(self, position: List[int]) -> int:
        odd = 0
        even = 0
        for num in position:
            if num % 2 == 0:
                even += 1
            else:
                odd += 1
        return min(odd, even)

    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # https://leetcode.cn/problems/word-subsets/
        ans = []
        count_dicts = []
        for word in words1:
            d = {}
            for c in word:
                if c not in d:
                    d[c] = 0
                d[c] += 1
            count_dicts.append(d)
        query_dict = {}
        for word in words2:
            d = {}
            for c in word:
                if c not in d:
                    d[c] = 0
                d[c] += 1
            for c in d:
                query_dict[c] = max(query_dict.get(c, 0), d[c])
        for i, cd in enumerate(count_dicts):
            flag = True
            for c, v in query_dict.items():
                if c not in cd or v > cd[c]:
                    flag = False
                    break
            if flag:
                ans.append(words1[i])
        return ans

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sum = 0

        if root.left and root.left.left is None and root.left.right is None:
            sum += root.left.val
        if root.left:
            sum += self.sumOfLeftLeaves(root.left)
        if root.right:
            sum += self.sumOfLeftLeaves(root.right)
        return sum



if __name__ == '__main__':
    node1 = TreeNode(-9)
    node2 = TreeNode(-3)
    node3 = TreeNode(2)
    node4 = TreeNode(4)
    node5 = TreeNode(4)
    node6 = TreeNode(0)
    node7 = TreeNode(-6)
    node8 = TreeNode(-5)
    node1.left = node2
    node1.right = node3
    node2.right = node4
    node3.left = node5
    node3.right = node6
    node4.left = node7
    node5.left = node8

    print(Solution().sumOfLeftLeaves(node1))
