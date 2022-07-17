def indexEqualsValue(array):
    # Write your code here.
    for i, num in enumerate(array):
        if i == num:
            return i
    return -1


def indexEqualsValue2(array):
    # Write your code here.
    left = 0
    right = len(array) - 1
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == mid:
            right = mid - 1
            ans = mid
        elif array[mid] >= mid:
            right = mid - 1
        else:
            left = mid + 1
    return ans

print(indexEqualsValue2([-12, 1, 2, 3, 12]))