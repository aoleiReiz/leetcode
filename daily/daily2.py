from typing import List
from collections import  defaultdict


class Solution:
    def isUgly(self, n: int) -> bool:
        def divide(num, base):
            while num % base == 0:
                num = num // base
            return num
        if n <= 3: return True
        r = divide(n, 2)
        if r == 1: return True
        r = divide(r, 3)
        if r == 1: return True
        r = divide(r, 5)
        if r == 1: return True
        return False

    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * (n + 1)
        p2 = p3 = p5 = 1
        dp[1] = 1
        for i in range(2, n+1):
            num2 = dp[p2] * 2
            num3 = dp[p3] * 3
            num5 = dp[p5] * 5
            dp[i] = min(min(num2, num3), num5)
            if num2 == dp[i]: p2 += 1
            if num3 == dp[i]: p3 += 1
            if num5 == dp[i]: p5 += 1

        return dp[n]

    def leastBricks(self, wall: List[List[int]]) -> int:
        d= {}
        for w in wall:
            size = len(w)
            cur = 0
            for i in range(size - 1):
                cur += w[i]
                d[cur] = d.get(cur, 0) + 1
        return len(wall) - max(d.values()) if d else len(wall)



if __name__ == '__main__':
    s = Solution()
    wall = [[1],[1],[1]]
    print(s.leastBricks(wall))



