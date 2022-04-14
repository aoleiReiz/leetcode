# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def invertBinaryTree(tree):
    # Write your code here.
    def swap_node(node):
        node.left, node.right = node.right, node.left
    queue = [tree]
    while tree:
        current = queue.pop(0)
        if current:
            swap_node(current)
            queue.append(current.left)
            queue.append(current.right)

def invertBinaryTree2(tree):
    # Write your code here.
    def swap_node(node):
        node.left, node.right = node.right, node.left
    if tree is None:
        return
    swap_node(tree)
    invertBinaryTree2(tree.left)
    invertBinaryTree2(tree.right)


def binaryTreeDiameter(tree):
    # Write your code here.
    return getTreeInfo(tree).diameter


def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(0, 0)
    left_tree_info = getTreeInfo(tree.left)
    right_tree_info = getTreeInfo(tree.right)
    longest_path_through_root = left_tree_info.height + right_tree_info.height
    max_dia_meter = max(left_tree_info.diameter, right_tree_info.diameter)
    curr_diameter = max(longest_path_through_root, max_dia_meter)
    curr_height = 1 + max(left_tree_info.height, right_tree_info.height)
    return TreeInfo(curr_diameter, curr_height)


class TreeInfo:
    def __init__(self, diameter, height):
        self.diameter = diameter
        self.height = height


def maxSubsetSumNoAdjacent(array):
    n = len(array)
    if n == 0:
        return 0
    if n == 1:
        return array[0]
    prev = array[0]
    curr = max(array[0], array[1])
    for i in range(2, n):
        prev, curr = curr, max(prev + array[i], curr)
    return curr