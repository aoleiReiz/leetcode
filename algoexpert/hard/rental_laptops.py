def laptopRentals(times):
    # Write your code here.
    ans = 0
    times = sorted(times)
    min_heap = MinHeap([])
    for time_interval in times:
        if len(min_heap.heap) == 0 or min_heap.peek()[1] > time_interval[0]:
            min_heap.insert(time_interval)
        else:
            min_heap.remove()
            min_heap.insert(time_interval)
        ans = max(ans, len(min_heap.heap))
    return ans


class MinHeap:

    def __init__(self, array) -> None:
        self.heap = self.build_heap(array)

    def compare_func(self, x1, x2):
        if x1[1] < x2[1]:
            return True
        elif x1[1] > x2[1]:
            return False
        else:
            return x1[0] < x2[0]

    def sift_up(self, curr_idx, heap):
        parent_idx = (curr_idx - 1) // 2
        while parent_idx >= 0:
            if self.compare_func(heap[curr_idx], heap[parent_idx]):
                self.swap(parent_idx, curr_idx, heap)
                curr_idx = parent_idx
                parent_idx = (curr_idx - 1) // 2
            else:
                break

    def sift_down(self, curr_idx, heap):
        left_child_idx = 2 * curr_idx + 1
        while left_child_idx < len(heap):
            if left_child_idx + 1 < len(heap) and self.compare_func(heap[left_child_idx+1], heap[left_child_idx]):
                idx_to_swap = left_child_idx + 1
            else:
                idx_to_swap = left_child_idx
            if self.compare_func(heap[idx_to_swap], heap[curr_idx]):
                self.swap(idx_to_swap, curr_idx, heap)
                curr_idx = idx_to_swap
                left_child_idx = 2 * curr_idx + 1
            else:
                break

    def build_heap(self, array):
        first_parent_idx = (len(array) - 2) // 2
        for curr_idx in reversed(range(first_parent_idx + 1)):
            self.sift_down(curr_idx, array)
        return array

    def peek(self):
        return self.heap[0]

    def insert(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1, self.heap)

    def remove(self):
        self.swap(0, len(self.heap)-1, self.heap)
        value = self.heap.pop()
        self.sift_down(0, self.heap)
        return value

    def swap(self, i, j, array):
        array[i], array[j] = array[j], array[i]
s