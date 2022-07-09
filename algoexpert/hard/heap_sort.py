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
        for i in range(k, -1, 0):
            self._shift_down(i)


    def extract_min(self):
        if self._data:
            val = self._data[0]
            self._data[0] = self._data[-1]
            self._data.pop()
            self._shift_down(0)
            return val


def heapSort(array):
    min_heap = MinHeap()
    min_heap.heapify(array)
    for i in range(len(array)):
        array[i] = min_heap.extract_min()
    return array


def shift_down(arr, k, end_idx):
    while 2 * k + 1 <= end_idx:
        left_child = 2*k + 1
        if left_child + 1 <= end_idx and arr[left_child + 1] > arr[left_child]:
            left_child += 1
        if arr[left_child] > arr[k]:
            arr[left_child], arr[k] = arr[k], arr[left_child]
            k = left_child
        else:
            break

def heapify(arr):
    for i in range((len(arr) - 2)//2, -1, -1):
        shift_down(arr, i, len(arr) - 1)


def heapSort2(array):
    heapify(array)

    for e_idx in range(len(array) - 1, 0, -1):
        array[e_idx], array[0] = array[0], array[e_idx]
        shift_down(array, 0, e_idx - 1)
    return array


if __name__ == '__main__':
    print(heapSort2([1, 2, 3]))