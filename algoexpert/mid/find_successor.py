# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    # Write your code here.
    if node.right is not None:
        return getLeftMostChild(node.right)
    return getRightMostParent(node)


def getLeftMostChild(node):
    curr_node = node
    while curr_node.left is not None:
        curr_node = curr_node.left
    return curr_node


def getRightMostParent(node):
    curr_node = node
    while curr_node.parent is not None and curr_node.parent.right == curr_node:
        curr_node = curr_node.parent
    return curr_node.parent
