# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, is_balanced, height):
        self.is_balanced = is_balanced
        self.height = height


def heightBalancedBinaryTree(tree):
    # Write your code here.

    return getTreeInfo(tree).is_balanced


def getTreeInfo(node):
    if node is None:
        return TreeInfo(True, -1)
    left_tree_info = getTreeInfo(node.left)
    right_tree_info = getTreeInfo(node.right)
    is_balanced = (left_tree_info.is_balanced and right_tree_info.is_balanced and abs(left_tree_info.height - right_tree_info.height) <= 1)
    height = max(left_tree_info.height, right_tree_info.height) + 1
    return TreeInfo(is_balanced, height)
