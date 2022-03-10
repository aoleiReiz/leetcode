

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


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15]
    print(threeNumberSum(arr, 32))
    