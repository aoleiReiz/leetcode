
def twoNumberSum(array, targetSum):
    """o(n) speed, o(n) space"""
    s = set()
    for num in array:
        rem = targetSum - num
        if rem in s:
            return [rem , num]
        else:
            s.add(num)
    return []


def twoNumberSum2(array, targetSum):
    array = sorted(array)
    i = 0
    j = len(array) - 1
    while i < j:
        s = array[i] + array[j]
        if s == targetSum:
            return [array[i], array[j]]
        elif s > targetSum:
            j -= 1
        else:
            i += 1
    return []


