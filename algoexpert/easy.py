


def isValidSubsequence(array, sequence):
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(sequence)


def tournamentWinner(competitions, results):
    # Write your code here.
    score_dict = {}
    for i, competition in enumerate(competitions):
        if results[i] == 1:
            score_dict[competition[0]] = score_dict.get(competition[0], 0) + 3
        else:
            score_dict[competition[1]] = score_dict.get(competition[1], 0) + 3
    max_score = -1
    winner = ""
    for k,v in score_dict.items():
        if v > max_score:
            winner = k
            max_score = v
    return winner


def nonConstructibleChange(coins):
    # Write your code here.
    coins = sorted(coins)
    current_change = 0
    for coin in coins:
        if coin > current_change + 1:
            return current_change + 1
        current_change += coin

    return current_change + 1


def findClosestValueInBst(tree, target):
    # Write your code here.
    def search_small_closest_node(node, t, cur_small):
        if node is None:
            return cur_small
        if node.value < t:
            cur_small = max(node.value, curr_small)
            return search_small_closest_node(node.right, t, cur_small)
        elif node.value > t:
            return search_small_closest_node(node.left, t, cur_small)
        else:
            return node.value

    def search_large_closest_node(node, t, cur_large):
        if node is None:
            return cur_large
        if node.value > t:
            cur_large = min(node.value, curr_large)
            return search_large_closest_node(node.left, t, cur_large)
        elif node.value < t:
            return search_large_closest_node(node.right, t, cur_large)
        else:
            return node.value

    if tree is None:
        return 0
    curr_small = -float("inf")
    curr_large = float("inf")
    curr_small = search_small_closest_node(tree, target, curr_small)
    curr_large = search_large_closest_node(tree, target, curr_large)
    if abs(curr_large - target) <= abs(curr_small - target):
        return curr_large
    else:
        return curr_small




# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def findClosestValueInBst_v2(tree, target):
    def helper(node, t, closest):
        if node is None:
            return closest
        if abs(t - closest) > abs(node.value - t):
            closest = node.value
        if node.value > target:
            return helper(node.left, t, closest)
        elif node.value < target:
            return helper(node.right, t, closest)
        else:
            return closest
    return helper(tree, target, tree.value)


# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
    def helper(node, res, cur_sum):
        if node is None:
            return
        cur_sum += node.value
        if node.left is None and node.right is None:
            res.append(cur_sum)
        helper(node.left, res, cur_sum)
        helper(node.right, res, cur_sum)
    ans = []
    helper(root, ans, 0)
    return ans


def nodeDepths(root):
    # Write your code here.
    def helper(node, depth):
        if node is None:
            return 0
        return depth + helper(node.left, depth + 1) + helper(node.right, depth + 1)
    return helper(root, 0)


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # Write your code here.
        def helper(node):
            array.append(node.name)
            for child in node.children:
                helper(child)
        helper(self)


def test_bst_closest():
    node1 = BST(10)
    node2 = BST(5)
    node3 = BST(2)
    node4 = BST(1)
    node5 = BST(15)
    node6 = BST(13)
    node7 = BST(22)
    node8 = BST(14)
    node9 = BST(5)

    node1.left = node2
    node1.right = node5
    node2.left = node3
    node2.right = node9
    node3.left = node4
    node5.left= node6
    node5.right = node7
    node6.right = node8

    print(findClosestValueInBst(node1,12))


def test_branch_sums():
    node1 = BinaryTree(1)
    node2 = BinaryTree(2)
    node3 = BinaryTree(3)
    node4 = BinaryTree(4)
    node5 = BinaryTree(5)
    node6 = BinaryTree(6)
    node7 = BinaryTree(7)
    node8 = BinaryTree(8)
    node9 = BinaryTree(9)
    node10 = BinaryTree(10)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    node4.left = node8
    node4.right = node9
    node5.left = node10

    print(branchSums(node1))


if __name__ == '__main__':
    test_branch_sums()


