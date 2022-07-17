import random

def quickselect(array, k):
    # Write your code here.
    return quick_select(array, 0, len(array) - 1, k)

def quick_select(array, left, right, k):
    if left > right:
        return
    p1, p2 = way_3_sort(array, left, right)
    if k > p1 + 1 and k < p2 + 1:
        return array[p1 + 1]
    elif k <= p1 + 1:
        return quick_select(array, left, p1, k)
    else:
        return quick_select(array, p2, right, k)


def way_3_sort(array, left, right):
    t = left - 1
    i = left
    j = right
    e = array[left]
    while i <= j:
        if array[i] < e:
            t += 1
            array[t], array[i] = array[i], array[t]
            i += 1
        elif array[i] == e :
            i += 1
        else:
            array[i], array[j] = array[j], array[i]
            j-= 1
    return t, i


print(quickselect([102, 41, 58, 81, 2, -5, 1000, 10021, 181, -14515, 25, 15], 5))

