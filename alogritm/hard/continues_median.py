import random


def max_compare_func(a, b):
    return a > b


def min_compare_func(a, b):
    return a < b


class Heap:
    def __init__(self, compare_func, array):
        self.compare_func = compare_func
        self.heap = self.build_heap(array[:])

    def build_heap(self, array):
        first_parent_idx = (len(array) - 2) // 2
        for curr_idx in reversed(range(first_parent_idx + 1)):
            self.sift_down(curr_idx, array)
        return array

    def sift_up(self, curr_idx, heap):
        parent_idx = (curr_idx - 1) // 2
        while curr_idx > 0:
            if self.compare_func(heap[curr_idx], heap[parent_idx]):
                self.swap(curr_idx, parent_idx, heap)
                curr_idx = parent_idx
                parent_idx = (curr_idx - 1) // 2
            else:
                break

    def sift_down(self, curr_idx, heap):
        left_child_idx = 2 * curr_idx + 1
        while left_child_idx <= len(heap) - 1:
            right_child_idx = left_child_idx + 1
            if right_child_idx < len(heap) and self.compare_func(heap[right_child_idx], heap[left_child_idx]):
                idx_to_swap = right_child_idx
            else:
                idx_to_swap = left_child_idx
            if self.compare_func(heap[idx_to_swap], heap[curr_idx]):
                self.swap(idx_to_swap, curr_idx, heap)
                curr_idx = idx_to_swap
                left_child_idx = 2 * curr_idx + 1
            else:
                break

    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        value_to_remove = self.heap.pop()
        self.sift_down(0, self.heap)
        return value_to_remove

    def insert(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1, self.heap)

    def peek(self):
        return self.heap[0]

    def swap(self, i, j, array):
        array[i], array[j] = array[j], array[i]


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lowers = Heap(max_compare_func, [])
        self.biggers = Heap(min_compare_func, [])
        self.median = None

    def addNum(self, num: int) -> None:
        if len(self.lowers.heap) == 0 or num < self.lowers.peek():
            self.lowers.insert(num)
        else:
            self.biggers.insert(num)
        self._re_balance()
        self.update_median()

    def _re_balance(self):
        if len(self.lowers.heap) - len(self.biggers.heap) == 2:
            self.biggers.insert(self.lowers.remove())
        elif len(self.biggers.heap) - len(self.lowers.heap) == 2:
            self.lowers.insert(self.biggers.remove())

    def update_median(self):
        if len(self.lowers.heap) == len(self.biggers.heap):
            self.median = (self.lowers.peek() + self.biggers.peek()) / 2
        elif len(self.lowers.heap) > len(self.biggers.heap):
            self.median = self.lowers.peek()
        else:
            self.median = self.biggers.peek()

    def findMedian(self) -> float:
        return self.median


if __name__ == '__main__':
    c = MedianFinder()
    c.addNum(1)
    c.addNum(2)
    print(c.findMedian())

