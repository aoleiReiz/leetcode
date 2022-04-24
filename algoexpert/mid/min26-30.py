def hasSingleCycle(array):
    # Write your code here.
    def index_jump(i, jump, n):
        return (i + jump) % n
    n_visited = 0
    n = len(array)
    curr = 0
    while n < n_visited:
        if curr == 0 or n_visited > 0:
            return False
        next_index = index_jump(curr, array[curr], n)
        n_visited += 1
        curr = next_index
    return curr == 0


# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    curr = descendantOne
    visited = {curr}
    while curr.ancestor:
        curr = curr.ancestor
        visited.add(curr)
    curr = descendantTwo
    if curr in visited:
        return curr
    while curr.ancestor:
        curr = curr.ancestor
        if curr in visited:
            return curr
    return topAncestor


def getYoungestCommonAncestor1(topAncestor, descendantOne, descendantTwo):
    depthOne = getDescendantTreeDepth(descendantOne, topAncestor)
    depthTwo = getDescendantTreeDepth(descendantTwo, topAncestor)
    if depthOne > descendantTwo:
        return backtrackAncestorTree(descendantOne, descendantTwo, depthOne - depthTwo)
    else:
        return backtrackAncestorTree(descendantTwo, descendantOne, depthTwo - depthOne)


def getDescendantTreeDepth(descendant, topAncestor):
    depth = 0
    while descendant != topAncestor:
        depth += 1
        descendant = descendant.ancestor
    return depth


def backtrackAncestorTree(lowerDescendant, higherDescendant, diff):
    while diff > 0:
        lowerDescendant = lowerDescendant.ancestor
        diff -= 1
    while lowerDescendant != higherDescendant:
        lowerDescendant = lowerDescendant.ancestor
        higherDescendant = higherDescendant.ancestor
    return lowerDescendant