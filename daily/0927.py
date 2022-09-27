from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.s = set()

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node: TreeNode, lower, upper):
            if node is None:
                return True
            if lower is not None and lower >= node.val:
                return False
            if upper is not None and upper <= node.val:
                return False
            return helper(node.left, lower, node.val) and helper(node.right, node.val, upper)

        return helper(root, None, None)

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root is None:
            return False
        if k - root.val in self.s:
            return True
        self.s.add(root.val)
        return self.findTarget(root.left, k) or self.findTarget(root.right, k)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        while cur:
            if cur.val == p.val and cur.val == q.val:
                return cur
            elif cur.val > p.val and cur.val > q.val:
                cur = cur.left
            elif cur.val < p.val and cur.val < q.val:
                cur = cur.right
            else:
                return cur
        return None

    def reverseBits(self, n: int) -> int:
        res = 0
        while n:
            res = 2 * res + n % 2
            n //= 2
        return res

    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans




if __name__ == '__main__':
    s = Solution()
    node1 = TreeNode(2, right=TreeNode(3), left=TreeNode(1))
    print(s.findTarget(node1, 4))
