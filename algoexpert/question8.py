def nodeDepths(root):
    # Write your code here.
    def helper(node, depth):
        if node is None:
            return 0
        return depth + helper(node.left, depth + 1) + helper(node.right, depth + 1)
    return helper(root, 0)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
