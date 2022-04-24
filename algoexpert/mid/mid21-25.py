def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
    ways = [0 for _ in range(n+1)]
    for denom in denoms:
        for amount in range(1, n+1):
            if denom <= amount:
                ways[amount] += ways[amount - denom]
    return ways[n]

def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
    dp = [n+1 for _ in range(n+1)]
    dp[0] = 0
    for denom in denoms:
        for amount in range(n + 1):
            if denom <= amount:
                dp[amount] = min(dp[amount], 1 + dp[amount - denom])
    return  -1 if (dp[n]==n + 1) else dp[n]


def numberOfWaysToMakeChange2(n, denoms):
    # Write your code here.
    ways = [0 for _ in range(n+1)]
    for denom in denoms:
        for amount in range(1, n+1):
            if denom <= amount:
                if ways[amount - denom] > 0:
                    ways[amount] += 1 + ways[amount - denom]
    return ways[n]

def levenshteinDistance(str1, str2):
    # Write your code here.
    m = len(str1)
    n = len(str2)
    dp = [[ 0 for _ in range(n+1)]for _ in range(m + 1)]
    for i in range(1, m+1):
        dp[i][0] = i
    for j in range(1, n+1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + 1)
    return dp[-1][-1]

def levenshteinDistance2(str1, str2):
    def dp(i, j, memo):
        if (i,j) in memo:
            return memo[(i,j)]
        if i == -1:
            return j + 1
        if j == -1:
            return i + 1
        if str1[i] == str2[j]:
            memo[(i,j)] = dp(i-1, j -1, memo)
        else:
            memo[(i, j)] = min(dp(i, j-1, memo) + 1, dp(i-1, j, memo) + 1, dp(i - 1, j-1, memo) + 1)

        return memo[(i,j)]

    return dp(len(str1) -1 , len(str2) -1, {})


def numberOfWaysToTraverseGraph(width, height):
    # Write your code here.
    if width == 1 or height == 1:
        return 1
    return numberOfWaysToTraverseGraph(width-1, height) + numberOfWaysToTraverseGraph(width, height - 1)


def numberOfWaysToTraverseGraph1(width, height):
    def dp(w, h, memo):
        if (w,h) in memo:
            return memo[(w,h)]
        if w == 1 or h == 1:
            return 1
        else:
            memo[(w,h)] = dp(w-1, h, memo) + dp(w, h -1, memo)
        return memo[(w,h)]
    return dp(width, height, {})


def numberOfWaysToTraverseGraph2(width, height):
    dp = [ [ 0 for _ in range(width + 1)] for _ in range(height + 1)]
    for i in range(1, height+1):
        dp[i][1] = 1
    for j in range(1, width + 1):
        dp[1][j] = 1
    for i in range(2, height + 1):
        for j in range(2, width + 1):
            dp[i][j] = dp[i-1][j] + dp[i][j - 1]
    return dp[height][width]


def kadanesAlgorithm(array):
    # Write your code here.
    ans = float("-inf")
    if array:
        ans = array[0]
        dp = array[0]
        for num in array[1:]:
            dp = max(num, num + dp)
            ans = max(ans, dp)
    return ans

if __name__ == '__main__':
    print(kadanesAlgorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]))