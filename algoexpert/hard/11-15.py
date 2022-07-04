def minNumberOfJumps(array):
    # Write your code here.
    if len(array) == 1:
        return 0
    steps = array[0]
    right_most = array[0]
    jumps = 0
    for i in range(1, len(array) - 1):
        right_most = max(right_most, array[i] + i)
        steps -= 1
        if steps == 0:
            jumps += 1
            steps = right_most - i

    return jumps + 1


def longestCommonSubsequence(str1, str2):
    # Write your code here.
    m = len(str1)
    n = len(str2)
    if m == 0 or n == 0:
        return []
    dp = [[[] for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + [str2[j - 1]]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=len)
    return dp[m][n]


def waterArea(heights):
    # Write your code here.
    n = len(heights)
    left_highest = [0 for i in range(n)]
    right_highest = [0 for i in range(n)]
    left_max = 0
    for i in range(n):
        left_highest[i] = left_max
        left_max = max(left_max, heights[i])
    right_max = 0
    for i in range(n):
        right_highest[n - i - 1] = right_max
        right_max = max(right_max, heights[n - i - 1])

    water = []
    for i in range(n):
        water.append(max(min(left_highest[i], right_highest[i]) - heights[i], 0))
    return sum(water)


def knapsackProblem(items, capacity):
    n = len(items)
    dp = [[[0, []] for i in range(capacity + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for c in range(1, capacity + 1):
            value, weight = items[i - 1]
            if c < weight:
                dp[i][c] = dp[i - 1][c]
            else:
                dp[i][c] = max([dp[i - 1][c - weight][0] + value, dp[i - 1][c - weight][1] + [i - 1]
                                ], dp[i - 1][c], key=lambda x: x[0])

    return dp[n][capacity]


def diskStacking(disks):
    # Write your code here.
    disks = sorted(disks, key=lambda disk: disk[2])
    heights = [disk[2] for disk in disks]
    sequences = [None for disk in disks]
    max_height_idx = 0
    for i in range(1, len(disks)):
        current_disk = disks[i]
        for j in range(0, i):
            other_disk = disks[j]
            if areValidDimension(other_disk, current_disk):
                if heights[i] <= heights[j] + current_disk[2]:
                    heights[i] = current_disk[2] + heights[j]
                    sequences[i] = [j]
        if heights[max_height_idx] <= heights[i]:
            max_height_idx = i
    return build_sequences(disks, sequences, max_height_idx)


def build_sequences(disks_, sequences_, current_idx):
    sequence = []
    while current_idx is not None:
        sequence.append(disks_[current_idx])
        current_idx = sequences_[current_idx]
    return sequence[::-1]


def areValidDimension(other_disk, current_disk):
    return other_disk[0] < current_disk[0] and other_disk[1] < current_disk[1] and other_disk[2] < current_disk[2]


if __name__ == '__main__':
    items = [[1, 2], [4, 3], [5, 6], [6, 7]]
    capacity = 10
    print(knapsackProblem(items, capacity))
