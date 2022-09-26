from typing import Optional, List


class Node:

    def __init__(self, val, next=None):
        self.next = next
        self.val = val


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MyLinkedList:

    def __init__(self):
        self.dummy_head = Node(-1)
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        p = self.dummy_head.next
        i = 0
        while i < index:
            p = p.next
            i += 1
        return p.val

    def addAtHead(self, val: int) -> None:
        new_head = Node(val, self.dummy_head.next)
        self.dummy_head.next = new_head
        if self.size == 0 and self.tail is None:
            self.tail = new_head
        self.size += 1

    def addAtTail(self, val: int) -> None:
        if self.size == 0:
            self.addAtHead(val)
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next
            self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.size:
            self.addAtTail(val)
        elif 0 <= index < self.size:
            p = self.dummy_head
            i = 0
            while i < index:
                p = p.next
                i += 1
            node = Node(val, p.next)
            p.next = node
            self.size += 1
        elif index < 0:
            self.addAtHead(val)

    def deleteAtIndex(self, index: int) -> None:

        if 0 <= index < self.size:
            p = self.dummy_head
            i = 0
            while i < index:
                p = p.next
                i += 1
            p.next = p.next.next
            if index == self.size - 1:
                self.tail = p
            self.size -= 1

    def pr(self):
        p = self.dummy_head.next
        count = 0
        while p:
            count += 1
            print(p.val, "->", end="")
            p = p.next
        print(f"size: {count} -> {self.size} ->{self.tail.val}")


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(node, path):
            if node:
                path.append(node.val)
                helper(node.left, path)
                helper(node.right, path)
        ans = []
        helper(root, ans)
        return ans

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(node, path):
            if node:
                helper(node.left, path)
                path.append(node.val)
                helper(node.right, path)
        ans = []
        helper(root, ans)
        return ans

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(node, path):
            if node:
                helper(node.left, path)
                helper(node.right, path)
                path.append(node.val)
        ans = []
        helper(root, ans)
        return ans

    def getDecimalValue(self, head: ListNode) -> int:
        p = head
        ans = 0
        i = 0
        while p:
            ans += p.val * 2 ** i
            i += 1
        return ans

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_max = self.maxDepth(root.left)
        right_max = self.maxDepth(root.right)

        return max(left_max + 1, right_max + 1)

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sum = 0
        if root.left and root.left.left is None and root.left.right is None:
            sum += root.left.val
        elif root.left:
            sum += self.sumOfLeftLeaves(root.left)
        if root.right:
            sum += self.sumOfLeftLeaves(root.right)
        return sum



if __name__ == '__main__':
    pass
