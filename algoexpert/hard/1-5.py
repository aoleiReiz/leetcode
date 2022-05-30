def subarraySort(array):
    # Write your code here.
    def is_out_of_order(idx, arr):
        if idx == 0:
            return arr[idx] > arr[idx + 1]
        elif idx == len(arr) - 1:
            return arr[idx] < arr[idx - 1]
        else:
            return arr[idx - 1] > arr[idx] or  arr[idx] > arr[idx + 1]

    min_out_of_order = float("inf")
    max_out_of_order = float("-inf")
    i = 0
    while i < len(array):
        if is_out_of_order(i, array):
            min_out_of_order = min(array[i], min_out_of_order)
            max_out_of_order = max(array[i], max_out_of_order)
        i += 1
    if min_out_of_order == float("-inf"):
        return [-1, -1]
    left_idx = 0
    while array[left_idx] <= min_out_of_order:
        left_idx += 1
    right_idx = len(array) - 1
    while array[right_idx] >= max_out_of_order:
        right_idx -= 1
    return [left_idx, right_idx]


def largestRange(array):
    if len(array) == 1:
        return [array[0], array[0]]
    array = sorted(array)
    cur_largest_range = float("-inf")
    cur_range = []
    cur_start = 0
    for i in range(1, len(array)):
        if array[i] == array[i-1] + 1 or array[i] == array[i-1]:
            if i == len(array) - 1:
                if array[i] - array[cur_start] > cur_largest_range:
                    cur_range = [array[cur_start], array[i]]
        else:
            if array[i-1] - array[cur_start] > cur_largest_range:
                cur_range = [array[cur_start], array[i-1]]
                cur_largest_range = array[i-1] - array[cur_start]
                cur_start = i

    return cur_range


def largestRange2(array):
    s = {}
    for num in array:
        s[num] = False
    curr_longest = float("-inf")
    longest_range = []
    for num in array:
        if s[num]:
            continue
        left = num
        right = num
        while left in s:
            s[left] = True
            left -= 1
        while right in s:
            s[right] = True
            right += 1
        if right - left > curr_longest:
            curr_longest = right - left
            longest_range=[left+1, right - 1]
    return longest_range


def minRewards(scores):
    # Write your code here.
    rewards = [1 for _ in scores]
    for i in range(1, len(scores)):
        if scores[i] > scores[i-1]:
            rewards[i] = rewards[i - 1] + 1
    for i in reversed(range(len(scores) - 1)):
        if scores[i] > scores[i+1]:
            rewards[i] = max(rewards[i + 1] + 1, rewards[i])
    return sum(rewards)


def zigzagTraverse(array):
    # Write your code here.
    ans = []
    if array:
        m = len(array)
        n = len(array[0])
        flag = True
        for i in range(m + n - 1):
            temp = []
            for j in range(min(i+1, m)):
                if i - j >= n:
                    continue
                temp.append(array[j][i - j])
            if temp:
                if flag:
                    ans.extend(temp)
                else:
                    ans.extend(reversed(temp))
            flag = not flag

    return ans


if __name__ == '__main__':
    print(zigzagTraverse([
  [1, 3, 4, 10],
  [2, 5, 9, 11],
  [6, 8, 12, 15],
  [7, 13, 14, 16]
]))


