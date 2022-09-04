def min_heap_func(a, b):
    return a < b


def max_heap_func(a, b):
    return a > b


class Heap:
    def __init__(self, compare_func, array):
        self.compare_func = compare_func
        self.heap = self.build_heap(array)
        self.length = len(self.heap)

    def build_heap(self, array):
        first_parent_idx = (len(array) - 2) // 2
        for cur_idx in reversed(range(first_parent_idx + 1)):
            self.sift_down(cur_idx, len(array) - 1, array)
        return array

    def sift_up(self, idx, heap):
        parent_idx = (idx - 1) // 2
        while idx > 0:
            if self.compare_func(heap[idx], heap[parent_idx]):
                self.swap(idx, parent_idx, heap)
                idx = parent_idx
                parent_idx = (idx - 1) // 2
            else:
                return

    def sift_down(self, idx, end_idx, heap):
        left_child_idx = 2 * idx + 1
        while left_child_idx <= end_idx:
            right_child_idx = left_child_idx + 1
            if right_child_idx <= end_idx and self.compare_func(heap[right_child_idx], heap[left_child_idx]):
                idx_to_swap = right_child_idx
            else:
                idx_to_swap = left_child_idx
            if self.compare_func(heap[idx_to_swap], heap[idx]):
                self.swap(idx_to_swap, idx, heap)
                idx = idx_to_swap
                left_child_idx = 2 * idx + 1
            else:
                return

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, self.length - 1, self.heap)
        value_to_remove = self.heap.pop()
        self.length -= 1
        self.sift_down(0, self.length - 1, self.heap)
        return value_to_remove

    def insert(self, value):
        self.heap.append(value)
        self.length += 1
        self.sift_up(self.length - 1, self.heap)

    def swap(self, i, j, array):
        array[i], array[j] = array[j], array[i]


class ContinuousMedianHandler:
    def __init__(self):
        self.lowers = Heap(max_heap_func, [])
        self.greaters = Heap(min_heap_func, [])
        self.median = None

    def insert(self, number):
        # Write your code here.
        if not self.lowers.length or number < self.lowers.peek():
            self.lowers.insert(number)
        else:
            self.greaters.insert(number)
        self.re_balance()
        self.update_median()

    def re_balance(self):
        if self.lowers.length - self.greaters.length == 2:
            self.greaters.insert(self.lowers.remove())
        elif self.greaters.length - self.lowers.length == 2:
            self.lowers.insert(self.greaters.remove())

    def update_median(self):
        if self.lowers.length == self.greaters.length:
            self.median = (self.lowers.peek() + self.greaters.peek()) / 2
        elif self.lowers.length > self.greaters.length:
            self.median = self.lowers.peek()
        else:
            self.median = self.greaters.peek()

    def getMedian(self):
        return self.median


c = ContinuousMedianHandler()
c.insert(5)
c.insert(10)
print(c.getMedian())
c.insert(100)
print(c.getMedian())