def searchForRange(array, target):
    # Write your code here.
    left = 0
    right = len(array) - 1
    left_index = -1
    right_index = -1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            left_index = mid
            right = mid - 1
        elif array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            right_index = mid
            left = mid + 1
        elif array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return [left_index, right_index]


print(searchForRange([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], 45))
