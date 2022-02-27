

def sortedSquaredArray(array):
    ans = [0 for _ in range(len(array))]
    left = 0
    right = len(array) - 1
    for i in range(len(array)-1, -1, -1):
        left_value = array[left]
        right_value = array[right]
        if abs(left_value) > abs(right_value):
            ans[i] = left_value ** 2
            left += 1
        else:
            ans[i] = right_value ** 2
            right -= 1
    return ans
