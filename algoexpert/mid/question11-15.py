# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BST(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self


def validateBst(tree):
    # Write your code here.
    def helper(node, min_node, max_node):
        if node is None:
            return True
        if min_node and node.value < min_node.value:
            return False
        if max_node and node.value >= max_node.value:
            return False

        return helper(node.left, min_node, node) and  helper(node.right, node, max_node)
    return helper(tree, None, None)


def validateBst2(tree):
    # Write your code here.
    def helper(node, min_value, max_value):
        if node is None:
            return True
        if node.value < min_value or node.value >= max_value:
            return False
        return helper(node.left, min_value, node.value) and  helper(node.right, node.value, max_value)
    return helper(tree, float("-inf"), float("inf"))


def inOrderTraverse(tree, array):
    # Write your code here.
    def helper(node, array):
        if node is None:
            return
        helper(node.left, array)
        array.append(node.value)
        helper(node.right, array)
    helper(tree, array)
    return array


def preOrderTraverse(tree, array):
    # Write your code here.
    def helper(node, array):
        if node is None:
            return
        array.append(node.value)
        helper(node.left, array)
        helper(node.right, array)
    helper(tree, array)
    return array


def postOrderTraverse(tree, array):
    # Write your code here.
    def helper(node, array):
        if node is None:
            return
        helper(node.left, array)
        helper(node.right, array)
        array.append(node.value)
    helper(tree, array)
    return array

def minHeightBst(array):
    def helper(arr, start_index, end_index):
        if start_index > end_index:
            return None
        mid = (start_index + end_index)//2
        value = arr[mid]
        node = BST(value)
        node.left = helper(arr, start_index, mid - 1)
        node.right = helper(arr, mid + 1, end_index)
        return node
    return helper(array, 0, len(array) - 1)


class TreeInfo:
    def __init__(self, numberOfNodesVisited, lastVisitedValue):
        self.num_of_nodes_visited = numberOfNodesVisited
        self.last_visited_value = lastVisitedValue


def reverse_search(tree_info_, node, k):
    if node is None and tree_info_.num_of_nodes_visited >= k:
        return
    reverse_search(tree_info_, node.right, k)
    if tree_info_.num_of_nodes_visited < k:
        tree_info_.num_of_nodes_visited += 1
        tree_info_.last_visited_value = node.value
        reverse_search(tree_info_, node.left, k)


def findKthLargestValueInBst(tree, k):
    # Write your code here.
    tree_into = TreeInfo(0, -1)
    reverse_search(tree_into, tree, k)
    return tree_into.last_visited_value


class TreeIndexInfo:
    def __init__(self, root_index):
        self.root_index = root_index


def reconstructBst(preOrderTraversalValues):
    # Write your code here.
    def helper(lower_bound, upper_bound, pre_order_values, curr_tree_index_info):
        if curr_tree_index_info.root_index >= len(pre_order_values):
            return None
        root_value = pre_order_values[curr_tree_index_info.root_index]
        if  root_value < lower_bound or root_value >= upper_bound:
            return None
        curr_tree_index_info.root_index += 1
        bst = BST(root_value)
        bst.left = helper(lower_bound, root_value, pre_order_values, curr_tree_index_info)
        bst.right = helper(root_value, upper_bound, pre_order_values, curr_tree_index_info)
        return bst

    tree_index_info = TreeIndexInfo(0)
    return helper(float("-inf"), float("inf"), preOrderTraversalValues, tree_index_info)

