def searchInSortedMatrix(matrix, target):
    # Write your code here.
    ans = [-1, -1]
    if matrix:
        m = len(matrix)
        n = len(matrix[0])
        i = m - 1
        j = 0
        while i >= 0 and j < n:
            if matrix[i][j] == target:
                return [i, j]
            elif matrix[i][j] > target:
                i -= 1
            else:
                j += 1
    return ans


def threeNumberSort(array, order):
    # Write your code here.
    i = -1
    k = 0
    j = len(array) - 1
    while k <= j:
        if array[k] == order[0]:
            i += 1
            array[k], array[i] = array[i], array[k]
            k += 1
        elif array[k] == order[1]:
            k += 1
        else:
            array[k], array[j] = array[j], array[k]
            j -= 1


def sunsetViews(buildings, direction):
    # Write your code here.
    ans = []
    n = len(buildings)
    cur_max = float("-inf")
    if direction == "EAST":
        for i in reversed(range(n)):
            if buildings[i] > cur_max:
                ans.append(i)
                cur_max = buildings[i]
        ans = ans[::-1]
    elif direction == "WEST":
        for i in range(n):
            if buildings[i] > cur_max:
                ans.append(i)
                cur_max = buildings[i]

    return ans


def sortStack(stack):
    # Write your code here.
    def helper(s, value):
        if len(s) == 0 or s[-1] <= value:
            s.append(value)
            return
        temp = s.pop()
        helper(s, value)
        s.append(temp)
    if len(stack) == 0:
        return
    top = stack.pop()
    sortStack(stack)
    helper(stack, top)
    return stack


def nextGreaterElement(array):
    # Write your code here.
    n = len(array)
    stack = []
    ans = [-1] * n
    for i in range(2*n - 1, -1, -1):
        if len(stack) > 0 and stack[-1] <= array[i % n]:
            stack.pop()
        ans[ i % n] = stack[-1] if len(stack) > 0 else -1
        stack.append(array[i % n])
    return ans


def longestPalindromicSubstring(string):
    def getLongestPalindromicFrom(left_index, right_index, s):
        while left_index >= 0 and right_index < len(s):
            if s[left_index] != s[right_index]:
                break
            left_index -= 1
            right_index += 1
        return left_index + 1, right_index

    curr_longest = [0, 1]
    for i in range(1, len(string)):
        even = getLongestPalindromicFrom(i - 1, i, string)
        odd = getLongestPalindromicFrom(i-1, i + 1, string)
        curr_longest = max(curr_longest, even, odd, key=lambda x: x[1] - x[0])
    return string[curr_longest[0]: curr_longest[1]]


def groupAnagrams(words):
    # Write your code here.
    if len(words) == 0:
        return []
    aux_words = [("".join(sorted([w for w in word])), i) for i, word in enumerate(words)]
    aux_words = sorted(aux_words, key=lambda x: x[0])
    ans = []
    cur_word = aux_words[0][0]
    cur_list = [words[aux_words[0][1]]]
    for aux_word in aux_words[1:]:
        if aux_word[0] == cur_word:
            cur_list.append(words[aux_word[1]])
        else:
            ans.append(cur_list)
            cur_word = aux_word[0]
            cur_list = [ words[aux_word[1]]]
    if cur_list:
        ans.append(cur_list)
    return ans


if __name__ == '__main__':
    words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
    print(groupAnagrams(words))