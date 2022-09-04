from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """https://leetcode.cn/problems/binary-tree-maximum-path-sum/"""
        ans = float("-inf")
        def max_side_path_sum(node:TreeNode):
            if node is None:
                return 0
            left_path_max = max(0, max_side_path_sum(node.left))
            right_path_max = max(0, max_side_path_sum(node.right))
            nonlocal ans
            ans = max(ans, left_path_max + right_path_max + node.val)
            return max(left_path_max, right_path_max) + node.val
        max_side_path_sum(root)
        return ans