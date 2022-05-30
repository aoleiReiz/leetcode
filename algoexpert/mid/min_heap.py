class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        # Write your code here.
        first_parent_idx = (len(array) - 2) // 2
        for idx in reversed(range(first_parent_idx + 1)):
            self.siftDown(idx, len(array) - 1, array)
        return array


    def siftDown(self, idx, end_idx, heap):
        # Write your code here.
        left_child_idx = idx * 2 + 1
        while left_child_idx <= end_idx:
            right_child_idx = idx * 2 + 2 if idx * 2 + 2 <= end_idx else -1
            if right_child_idx != -1 and heap[right_child_idx] < heap[left_child_idx]:
                idx_to_swap = right_child_idx
            else:
                idx_to_swap = left_child_idx
            if heap[idx_to_swap] < heap[idx]:
                self.swap(idx, idx_to_swap, heap)
                idx = idx_to_swap
                left_child_idx = idx * 2 + 1
            else:
                return

    def siftUp(self, idx, heap):
        # Write your code here.
        parent_idx = (idx - 1) // 2
        while idx > 0 and heap[idx] < heap[parent_idx]:
            self.swap(idx, parent_idx, heap)
            idx = parent_idx
            parent_idx = (idx - 1) // 2

    def peek(self):
        # Write your code here.
        return self.heap[0]

    def remove(self):
        # Write your code here.
        self.swap(0, len(self.heap)-1, self.heap)
        value_to_remove = self.heap.pop()
        self.siftDown(0, len(self.heap)-1, self.heap)
        return value_to_remove

    def insert(self, value):
        # Write your code here.
        self.heap.append(value)
        self.siftUp(len(self.heap)- 1, self.heap)

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]
