from typing import List
import math
from collections import deque


class Solution:
    def isUnique(self, astr: str) -> bool:
        if len(astr) <= 1: return True
        count = [0] * 52
        for c in astr:
            if 'a' <= c <= 'z':
                idx = ord(c)-ord('a')
                count[idx] += 1
                if count[idx] > 1:
                    return False
            if 'A' <= c <= 'Z':
                idx = ord(c)-ord('A') + 26
                count[idx] += 1
                if count[idx] > 1:
                    return False
        return True

    def CheckPermutation(self, s1: str, s2: str) -> bool:
        """https://leetcode-cn.com/problems/check-permutation-lcci/"""
        return sorted([c for c in s1]) == sorted([c for c in s2])

    def replaceSpaces(self, S: str, length: int) -> str:
        ret = ["%20" if S[i] == ' ' else S[i] for i in range(length)]
        return "".join(ret)

    def canPermutePalindrome(self, s: str) -> bool:
        count =  dict()
        for c in s:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        values = [v % 2 for v in count.values()]
        if len(s) % 2 == 0:
            return sum(values)==0
        else:
            return sum(values) == 1

    def oneEditAway(self, first: str, second: str) -> bool:
        if abs(len(first) - len(second)) > 1: return False
        chars="abcdefghijklmnopqrstuvwxyz"
        s = set()
        #插入一个字符
        for i in range(len(first)+1):
            for c in chars:
                s.add(first[:i] + c + first[i:])
                s.add(first[:i] + chr(ord(c)-32) + first[i:])
        #删除一个字符
        for i in range(len(first)):
            s.add(first[:i] + first[i+1:])
        #替换一个字符
        for i in range(len(first)):
            for c in chars:
                s.add(first[:i] + c + first[i+1:])
                s.add(first[:i] + chr(ord(c) - 32) + first[i+1:])
        return second in s

    def nthUglyNumber(self, n: int) -> int:
        dp = [1] * n
        a, b, c = 0, 0, 0

        for i in range(1, n):
            n1 = dp[a] * 2
            n2 = dp[b] * 3
            n3 = dp[c] * 5

            _n = min([n1, n2, n3])
            dp[i] = _n

            if n1 == _n:
                a += 1
            if n2 == _n:
                b += 1
            if n3 == _n:
                c += 1
        return dp[n-1]

    def translateNum(self, num: int) -> int:
        x = 1
        y = 1
        num_str = str(num)
        for i in range(2, len(num_str)+1):
            s = num_str[i-2: i]
            z = x
            if 25 >= int(s) >= 10:
                z = x + y
            y = x
            x = z
        return x

    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1: return 0
        dp = [0] * len(prices)
        cur_min = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > cur_min:
                dp[i] = prices[i] - cur_min
            elif prices[i] < cur_min:
                cur_min = prices[i]
        return max(dp)

    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        n =len(dominoes)
        s = set()
        count = 0
        for i in range(n-1):
            m = 1
            if i in s:
                continue
            for j in range(i+1,n):
                if j in s:
                    continue
                if (dominoes[i][0] == dominoes[j][0] and dominoes[i][1] == dominoes[j][1])or(dominoes[i][1] == dominoes[j][0] and dominoes[i][0] == dominoes[j][1]):
                    m += 1
                    s.add(j)
            if m > 1:
                count += (m - 1) * m //2
        return count

    def removeDuplicates(self, S: str) -> str:
        l = list()
        for ch in S:
            if l and ch == l[-1]:
                l.pop()
            else:
                l.append(ch)
        return "".join(l)

    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        pre_sign = '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if not s[i].isdigit() and s[i] != ' ' or i == len(s) - 1:
                if pre_sign == '+':
                    stack.append(num)
                elif pre_sign == "-":
                    stack.append(-num)
                elif pre_sign == "*":
                    stack[-1] = stack[-1] * num
                elif pre_sign == '/':
                    stack[-1] = math.trunc(stack[-1] / num)
                pre_sign = s[i]
                num = 0
        ans = 0
        for n in stack:
            ans += n
        return ans

    def evalRPN(self, tokens: List[str]) -> int:
        q = deque()
        for t in tokens:
            if t == "+":
                n1 = q.pop()
                n2 = q.pop()
                q.append(n1 + n2)
            elif t == "-":
                n1 = q.pop()
                n2 = q.pop()
                q.append(n2 - n1)
            elif t == "/":
                n1 = q.pop()
                n2 = q.pop()
                q.append(math.trunc(n2 / n1))
            elif t == "*":
                n1 = q.pop()
                n2 = q.pop()
                q.append(n1 * n2)
            else:
                q.append(int(t))
        return q[0]

    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        d = {}
        cur_start = 0
        res = 0
        for i,c in enumerate(s):
            if c in d:
                res = max(res, i - cur_start)
                cur_start = max(d[c] + 1,cur_start)
            d[c] = i
        res = max(len(s)-cur_start, res)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abba"))
