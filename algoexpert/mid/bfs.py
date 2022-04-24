class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        # Write your code here.
        queue = [self]
        ans = []
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                ans.append(node.name)
                for child in node.children:
                    queue.append(child)
        return ans

