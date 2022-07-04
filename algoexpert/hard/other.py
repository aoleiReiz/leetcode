def quickSort(array):
    # Write your code here.
    quick_sort(0, len(array) - 1, array)


def quick_sort(left, right, array):
    if left > right:
        return
    p1, p2 = partition(left, right, array)
    quick_sort(left, p1, array)
    quick_sort(p2, right, array)


def partition(left, right, array):
    e = array[left]
    i = left
    k = left - 1
    j = right
    while i <= j:
        if array[i] < e:
            k += 1
            array[k], array[i] = array[i], array[k]
            i += 1
        elif array[i] == e:
            i += 1
        else:
            array[i], array[j] = array[j], array[i]
            j -= 1
    return k, i


def multiStringSearch(bigString, smallStrings):
    # Write your code here.
    tabu = {}
    for i, c in enumerate(bigString):
        if c == " ":
            continue
        if c not in tabu:
            tabu[c] = []
        tabu[c].append(i)
    ans = []
    for string in smallStrings:
        if string[0] not in tabu:
            ans.append(False)
        else:
            flag = False
            for start_index in tabu[string[0]]:
                if bigString[start_index: start_index + len(string)] == string:
                    ans.append(True)
                    flag = True
                    break
            if not flag:
                ans.append(False)
    return ans


if __name__ == '__main__':
    print(multiStringSearch("this is a big string", ["this", "yo", "is", "a", "bigger", "string", "kappa"]))
