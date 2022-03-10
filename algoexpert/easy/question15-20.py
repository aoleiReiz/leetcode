def productSum(array):
    # Write your code here.
    def helper(inner_array, depth):
        cur_sum = 0
        for ele in inner_array:
            if isinstance(ele, list):
                cur_sum += (depth + 1) * helper(ele, depth + 1)
            else:
                cur_sum += ele
        return cur_sum

    return helper(array, 1)


def binarySearch(array, target):
    # Write your code here.
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] > target:
            right = mid - 1
        elif array[mid] < target:
            left = mid + 1
        else:
            return mid
    return -1


def findThreeLargestNumbers(array):
    # Write your code here.
    first = float("-inf")
    second = float("-inf")
    third = float("-inf")
    for e in array:
        if e > first:
            third = second
            second = first
            first = e
        elif e > second:
            third = second
            second = e
        elif e > third:
            third = e
    return third


def bubbleSort(array):
    # Write your code here.
    n = len(array)
    for i in range(n):
        flag = False
        for j in range(n - 1, 0, -1):
            if array[j] < array[j - 1]:
                tmp = array[j]
                array[j] = array[j - 1]
                array[j - 1] = tmp
                flag = True
        if not flag:
            break


def insertionSort(array):
    # Write your code here.
    n = len(array)
    for i in range(1, n):
        e = array[i]
        while array[i-1] > e and i > 0:
            array[i] = array[i-1]
            i -= 1
        array[i] = e
    return  array


def selectionSort(array):
    n = len(array)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if array[j] < array[min_idx]:
                min_idx = j
        tmp = array[min_idx]
        array[min_idx] = array[i]
        array[i] = tmp
    return array



if __name__ == '__main__':
    arr = [5, 2, 7, -1, 3, 61, -13, 8, 4]
    print(selectionSort(arr))
