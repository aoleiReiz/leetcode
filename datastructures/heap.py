class MinHeap:

    def __init__(self):
        self._data = []

    def insert(self, value):
        self._data.append(value)
        self._shift_up(len(self._data) - 1)

    def _shift_up(self, k):
        parent = (k - 1) // 2
        while parent >= 0 and self._data[parent] > self._data[k]:
            self._data[parent], self._data[k] = self._data[k], self._data[parent]
            k = parent
            parent = (k - 1) // 2

    def _shift_down(self, k):
        left_child = 2 * k + 1
        while left_child < len(self._data):
            if left_child + 1 < len(self._data) and self._data[left_child + 1] < self._data[left_child]:
                left_child += 1
            if self._data[left_child] < self._data[k]:
                self._data[left_child], self._data[k] = self._data[k], self._data[left_child]
                k = left_child
                left_child = 2 * k + 1
            else:
                break

    def heapify(self, array):
        self._data = array[:]
        k = (len(self._data) - 2) // 2
        for i in range(k, -1, -1):
            self._shift_down(i)

    def extract_min(self):
        if self._data:
            val = self._data[0]
            self._data[0] = self._data[-1]
            self._data.pop()
            self._shift_down(0)
            return val


if __name__ == '__main__':
    import random

    # random.seed(42)
    arr = []
    mh = MinHeap()
    for i in range(10):
        arr.append(random.randint(1, 100))
    mh.heapify(arr)
    for i in range(10):
        print(mh.extract_min(), end=" ")
    print()
