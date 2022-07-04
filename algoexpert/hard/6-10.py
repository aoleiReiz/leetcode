def sameBsts(arrayOne, arrayTwo):
    # Write your code here.
    if len(arrayOne) != len(arrayTwo):
        return False

    if len(arrayOne) == 0 and len(arrayTwo) == 0:
        return True

    if arrayOne[0] != arrayTwo[0]:
        return False

    left_one = get_smaller(arrayOne)
    left_two = get_smaller(arrayTwo)

    right_one = get_bigger_or_equal(arrayOne)
    right_two = get_bigger_or_equal(arrayTwo)

    return sameBsts(left_one, left_two) and sameBsts(right_one, right_two)


def get_smaller(array):
    smaller = []
    for i in range(1, len(array)):
        if array[i] < array[0]:
            smaller.append(array[i])
    return smaller


def get_bigger_or_equal(array):
    bigger_or_equal = []
    for i in range(1, len(array)):
        if array[i] >= array[0]:
            bigger_or_equal.append(array[i])
    return bigger_or_equal


# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    # Write your code here.

    return (search(nodeOne, nodeTwo) and search(nodeTwo, nodeThree)) or (
            search(nodeThree, nodeTwo) and search(nodeTwo, nodeOne))


def search(rootNode: BST, target: BST):
    if rootNode is None:
        return False
    if rootNode.value == target.value:
        return True
    if rootNode.value < target.value:
        return search(rootNode.right, target)
    elif rootNode.value > target.value:
        return search(rootNode.left, target)


def maxPathSum(tree):
    _, max_path_sum = find_max_sum(tree)
    return max_path_sum


def find_max_sum(tree):
    if tree is None:
        return 0, float("-inf")
    left_max_branch_sum, left_max_path_sum = find_max_sum(tree.left)
    right_max_branch_sum, right_max_path_sum = find_max_sum(tree.right)
    max_child_branch_sum = max(left_max_branch_sum, right_max_branch_sum)

    value = tree.value
    max_branch_sum = max(max_child_branch_sum + value, value)
    max_sum_as_root_node = max(left_max_branch_sum + value + right_max_branch_sum, max_branch_sum)
    max_path_sum = max(left_max_path_sum, right_max_path_sum, max_sum_as_root_node)

    return max_branch_sum, max_path_sum


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findNodesDistanceK(tree, target, k):
    node_to_parents = {}
    populate_nodes_to_parent(tree, node_to_parents)
    target_node = get_node_from_value(target, tree, node_to_parents)
    return bfs_node_k_distance(target_node, node_to_parents, k)


def bfs_node_k_distance(target_node: BinaryTree, node_to_parents: dict, k: int):
    queue = [(target_node, 0)]
    seen = {target_node.value}
    while len(queue) > 0:
        current_node, distance_from_target = queue.pop(0)
        if distance_from_target == k:
            node_distance_k = [node.value for node, _ in queue]
            node_distance_k.append(current_node.value)
            return node_distance_k
        connected_nodes = [current_node.left, current_node.right, node_to_parents[current_node.value]]
        for node in connected_nodes:
            if node is None:
                continue
            if node.value in seen:
                continue
            seen.add(node.value)
            queue.append((node, distance_from_target + 1))
    return []


def get_node_from_value(value, node: BinaryTree, node_to_parents: dict):
    if node.value == value:
        return node
    node_parent = node_to_parents[value]
    if node_parent.left is not None and node_parent.left.value == value:
        return node_parent.left
    return node.right


def populate_nodes_to_parent(node: BinaryTree, node_to_parent: dict, parent: BinaryTree = None):
    if node is not None:
        node_to_parent[node.value] = parent
        populate_nodes_to_parent(node.left, node_to_parent, node)
        populate_nodes_to_parent(node.right, node_to_parent, node)



