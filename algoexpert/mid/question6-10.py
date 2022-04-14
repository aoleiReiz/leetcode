def longestPeak(array):
    # Write your code here.哦；pj'pk【。】
    ans = 0
    n = len(array)
    if n <= 2:
        return ans
    i = 1
    while i < n - 1:
       is_peak = array[i-1] < array[i] > array[i + 1]
       if is_peak:
           temp_ans = 3
           j = i - 1
           while j > 0 and array[j] > array[j - 1]:
               temp_ans += 1
               j -= 1
           j = i + 1
           while j < n - 1 and array[j] > array[j+1]:
               j += 1
               temp_ans += 1
           ans = max(ans, temp_ans)
       i += 1
    return ans

def arrayOfProducts(array):
    # Write your code here.
    n = len(array)
    if n < 2:
        return []
    output = []
    left_prd = []
    right_prd = []
    cur = 1
    for i in range(n):
        left_prd.append(cur)
        cur *= array[i]
    cur = 1
    for i in reversed(range(n)):
        right_prd.append(cur)
        cur *= array[i]
    for i in range(n):
        output.append(left_prd[i] * right_prd[n - 1 - i])

    return output


def firstDuplicateValue(array):
    for i, value in enumerate(array):
         value = abs(value)
         index = value - 1
         if arr[index] < 0:
             return value
         else:
             array[index] *= -1

    return -1


def mergeOverlappingIntervals(intervals):
    ans = []
    if intervals:
        intervals = sorted(intervals)
        cur_interval = intervals[0]
        for interval in intervals[1:]:
            if interval[0] > cur_interval[1]:
                ans.append(cur_interval)
                cur_interval = interval
            else:
                cur_interval[1] = max(cur_interval[1], interval[1])
        ans.append(cur_interval)
    return ans


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        if value >= self.value:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        elif value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        return self

    def contains(self, value):
        # Write your code here.
        if value == self.value:
            return True
        elif value > self.value:
            if self.right is None:
                return False
            return self.right.contains(value)
        else:
            if self.left is None:
                return False
            return self.left.contains(value)

    def remove(self, value, parent=None):
        # Write your code here.
        # Do not edit the return statement of this method.
        if value < self.value:
            if self.left is not None:
                self.left.remove(value, self)
        elif value > self.value:
            if self.right is not None:
                self.right.remove(value, self)
        else:
            if self.left is not None and self.right is not None:
                self.value = self.right.get_min()
                self.right.remove(self.value, self)
            elif parent is None:
                if self.left is not None:
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                elif self.right is not None:
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
                else:
                    pass
            elif parent.left == self:
                parent.left = self.left if self.left is not None else self.right
            elif parent.right == self:
                parent.right = self.left if self.left is not None else self.right
        return self

    def get_min(self):
        if self.left is None:
            return self.value
        return self.left.get_min()

if __name__ == '__main__':
    arr = [
    [1, 2],
    [3, 5],
    [4, 7],
    [6, 8],
    [9, 10]
  ]
    print(mergeOverlappingIntervals(arr))