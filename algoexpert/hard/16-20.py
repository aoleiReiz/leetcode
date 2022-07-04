def numbersInPi(pi, numbers):
    # Write your code here.
    numbers = set(numbers)
    min_space = get_min_spaces(pi, numbers, {}, 0)
    return -1 if min_space == float("inf") else min_space


def get_min_spaces(pi, numbers, cache, idx):
    if idx == len(pi):
        return -1
    if idx in cache:
        return cache[idx]
    min_spaces = float("inf")
    for i in range(idx, len(pi)):
        prefix = pi[idx: i + 1]
        if prefix in numbers:
            min_spaces_suffix = get_min_spaces(pi, numbers, cache, i + 1)
            min_spaces = min(min_spaces_suffix + 1, min_spaces)
    cache[idx] = min_spaces
    return cache[idx]


def maximumSumSubmatrix(matrix, size):
    # Write your code here.
    m = len(matrix)
    n = len(matrix[0])
    ans = float("-inf")
    col_start = 0
    dp = [sum(matrix[i][:size]) for i in range(m)]
    while col_start + size <= n:
        if col_start != 0:
            dp = [cur_row_sum - matrix[i][col_start - 1] + matrix[i][col_start + size - 1] for i, cur_row_sum in
                  enumerate(dp)]
        row_start = 0
        dp_sum_from_row_start = sum(dp[:size])
        while row_start + size <= m:
            if row_start == 0:
                ans = max(dp_sum_from_row_start, ans)
            else:
                dp_sum_from_row_start = dp_sum_from_row_start - dp[row_start - 1] + dp[row_start + size - 1]
                ans = max(dp_sum_from_row_start, ans)
            row_start += 1
        col_start += 1
    return ans


def maximizeExpression(array):
    # Write your code here.
    if len(array) < 4:
        return 0
    max_of_a = [array[0]]
    max_of_a_minus_b = [float("-inf")]
    max_of_a_minus_b_plus_c = [float("-inf"), float("-inf")]
    max_of_a_minus_b_plus_c_minus_d = [float("-inf"), float("-inf"), float("-inf")]

    for i in range(1, len(array)):
        current_max = max(max_of_a[i-1], array[i])
        max_of_a.append(current_max)

    for i in range(1, len(array)):
        current_max = max(max_of_a_minus_b[i-1], max_of_a[i - 1] - array[i])
        max_of_a_minus_b.append(current_max)

    for i in range(2, len(array)):
        current_max = max(max_of_a_minus_b_plus_c[i-1], max_of_a_minus_b[i-1] + array[i])
        max_of_a_minus_b_plus_c.append(current_max)

    for i in range(3, len(array)):
        current_max = max(max_of_a_minus_b_plus_c_minus_d[i-1], max_of_a_minus_b_plus_c[i-1] - array[i])
        max_of_a_minus_b_plus_c_minus_d.append(current_max)

    return max_of_a_minus_b_plus_c_minus_d[-1]






if __name__ == '__main__':
    ma = [
        [2, 4],
        [5, 6],
        [-3,2]
    ]

    print(maximizeExpression([3, 6, 1, -3, 2, 7]))