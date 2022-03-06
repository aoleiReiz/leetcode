# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
    def helper(node, cur_sum, res):
        if node is None:
            return
        cur_sum += node.value
        if node.left is None and node.right is None:
            res.append(cur_sum)
        if node.left:
            helper(node.left, cur_sum, res)
        if node.right:
            helper(node.right, cur_sum, res)
    res = []
    helper(root, 0, res)
    return res
