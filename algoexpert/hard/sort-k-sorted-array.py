class MinHeap:

    def __init__(self, array):
        self.heap = self.build_heap(array[:])

    def build_heap(self, array):
        first_parent_idx = (len(array) - 2) // 2
        for current_idx in reversed(range(first_parent_idx + 1)):
            self.sift_down(current_idx, array)
        return array

    def sift_down(self, current_idx, heap):
        left_child_idx = 2 * current_idx + 1
        while left_child_idx < len(heap):
            if left_child_idx + 1 < len(heap) and heap[left_child_idx + 1] < heap[left_child_idx]:
                idx_to_swap = left_child_idx + 1
            else:
                idx_to_swap = left_child_idx
            if heap[idx_to_swap] < heap[current_idx]:
                self.swap(idx_to_swap, current_idx, heap)
                current_idx = idx_to_swap
                left_child_idx = 2 * current_idx + 1
            else:
                break

    def sift_up(self, current_idx, heap):
        parent_idx = (current_idx - 1) // 2
        while parent_idx >= 0:
            if heap[current_idx] < heap[parent_idx]:
                self.swap(current_idx, parent_idx, heap)
                current_idx = parent_idx
                parent_idx = (current_idx - 1) // 2
            else:
                break

    def insert(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1, self.heap)

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, len(self.heap)-1, self.heap)
        value_to_remove = self.heap.pop()
        self.sift_down(0, self.heap)
        return value_to_remove

    def swap(self, i, j, array):
        array[i], array[j] = array[j], array[i]


def sortKSortedArray(array, k):
    # Write your code here.
    insert_idx = 0
    min_heap = MinHeap(array[:k+1])
    for idx in range(k+1, len(array)):
        value = min_heap.remove()
        min_heap.insert(array[idx])
        array[insert_idx] = value
        insert_idx += 1

    while min_heap.heap:
        value = min_heap.remove()
        array[insert_idx] = value
        insert_idx += 1
    return array



if __name__ == '__main__':
    a = [3, 2, 1, 5, 4, 7, 6, 5]
    print(sortKSortedArray(a, 3))
