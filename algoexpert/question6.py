def findClosestValueInBst(tree, target):
    def helper(node, t, closest):
        if not node:
            return closest
        if abs(t - closest) > abs(node.value - t):
            closest = node.value
        if node.value > target:
            return helper(node.left, t, closest)
        elif node.value < target:
            return helper(node.right, t, closest)
        return closest
    return helper(tree, target, tree.value)



# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


if __name__ == '__main__':
    node1 = BST(1)
    node2 = BST(2)
    node3 = BST(5)
    node4 = BST(10)
    node5 = BST(13)
    node6 = BST(14)
    node7 = BST(15)
    node8 = BST(22)
    node9 = BST(5)

    node4.left = node9
    node4.right = node7
    node9.left = node2
    node9.right = node3
    node2.left = node1
    node7.left = node5
    node7.right = node8
    node5.right = node6

    print(findClosestValueInBst(node4,12))