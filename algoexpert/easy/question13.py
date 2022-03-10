# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    p = linkedList
    while p and p.next:
        if p.value == p.next.value:
            delete_node = p.next
            p.next = delete_node.next
            delete_node.next = None
        p = p.next
    return linkedList


if __name__ == '__main__':
    n1 = LinkedList(1)
    n2 = LinkedList(1)