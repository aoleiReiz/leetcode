

def threeNumberSum(array, targetSum):
    # Write your code here.
    array = sorted(array)
    ans = []
    for i in range(len(array) - 2):
        two_sum_ans = twoNumberSum(array[i+1:], targetSum - array[i])
        for r in two_sum_ans:
            ans.append([array[i], *r])
    return ans


def twoNumberSum(array, targetSum):
    left = 0
    right = len(array) - 1
    ans = []
    while left < right:
        if array[left] + array[right] == targetSum:
            ans.append([array[left], array[right]])
            left += 1
            right -= 1
        elif array[left] + array[right] > targetSum:
            right -= 1
        else:
            left += 1
    return ans


def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne = sorted(arrayOne)
    arrayTwo = sorted(arrayTwo)
    idx_one = 0
    idx_two = 0
    smallest = float("inf")
    ans = []
    while idx_one < len(arrayOne) and idx_two < len(arrayTwo):
        first = arrayOne[idx_one]
        second = arrayTwo[idx_two]
        if first > second:
            diff = first - second
            idx_two += 1
        elif first < second:
            diff = second - first
            idx_one += 1
        else:
            return [first, second]
        if diff < smallest:
            smallest = diff
            ans = [first, second]
    return ans


def moveElementToEnd(array, toMove):
    # Write your code here.
    k = 0
    for i in range(len(array)):
        if array[i] != toMove:
            array[k] = array[i]
            k += 1
    for j in range(k, len(array)):
        array[j] = toMove
    return array


def moveElementToEnd(array, toMove):
    # Write your code here.
    i = 0
    j = len(array) - 1
    while i < j:
        while j > i and array[j] == toMove:
            j -= 1
        if array[i] == toMove:
            array[i], array[j] = array[j], array[i]
        i+= 1
    return array


def isMonotonic(array):
    n = len(array)
    if n <= 1:
        return True
    flag = array[n-1] >= array[0]
    for i in range(n-1):
        if flag != (array[i+1] >= array[i]) and array[i+1] != array[i]:
            return False
    return True


def spiralTraverse(array):
    # Write your code here.
    if len(array) == 0:
        return []
    ans = []
    row_start = 0
    row_end = len(array) - 1
    col_start = 0
    col_end = len(array[0]) - 1
    while col_start < col_end and row_start < row_end:
        for col in range(col_start, col_end + 1):
            ans.append(array[row_start][col])
        for row in range(row_start + 1, row_end + 1):
            ans.append(array[row][col_end])
        for col in reversed(range(col_start, col_end)):
            if row_start == row_end:
                break
            ans.append(array[row_end][col])
        for row in reversed(range(row_start+1, row_end)):
            if col_start == col_end:
                break
            ans.append(array[row][col_start])
        row_start += 1
        row_end -= 1
        col_start += 1
        col_end -= 1
    return ans

def spiralTraverse2(array):
    if len(array) == 0:
        return []
    ans = []
    row_start = 0
    row_end = len(array) - 1
    col_start = 0
    col_end = len(array[0]) - 1
    while row_start <= row_end and col_start <= col_end:
        for col in range(col_start, col_end + 1):
            ans.append(array[row_start][col])
        for row in range(row_start+1, row_end + 1):
            ans.append(array[row][col_end])
        for col in reversed(range(col_start, col_end)):
            if row_start == row_end:
                break
            ans.append(array[row_end][col])
        for row in reversed(range(row_start+1, row_end)):
            if col_start == col_end:
                break
            ans.append(array[row][col_start])
        row_start += 1
        row_end -= 1
        col_start += 1
        col_end -= 1
    return ans



if __name__ == '__main__':
    array = [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7]
  ]
    print(spiralTraverse2(array))
    