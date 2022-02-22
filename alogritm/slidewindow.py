from typing import List

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or s == "": return ""
        window = {}
        need = {}
        for c in t:
            if c in need:
                need[c] += 1
            else:
                need[c] = 1

        left = 0
        right = 0
        valid = 0
        ret = ""
        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                if c in window:
                    window[c] += 1
                else:
                    window[c] = 1
                if window[c] == need[c]:
                    valid += 1

            while valid == len(need):
                if ret == "":
                    ret = s[left:right]
                else:
                    ret = ret if len(ret) < len(s[left:right]) else s[left:right]
                c = s[left]
                left += 1
                if c in window:
                    if window[c] == need[c]:
                        valid -= 1
                    window[c] -= 1
                    if window[c] == 0:
                        window.pop(c)
        return ret




    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        d = {}
        cur_start = 0
        res = 0
        for i, c in enumerate(s):
            if c in d:
                res = max(res, i - cur_start)
                cur_start = max(d[c] + 1, cur_start)
            d[c] = i
        res = max(len(s) - cur_start, res)
        return res

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        cur_sum = 0
        res = float("inf")
        while right < len(nums):
            cur_sum += nums[right]
            right += 1
            while cur_sum >= target:
                res = min(res, right - left)
                cur_sum -= nums[left]
                left += 1
        return 0 if res == float("inf") else res

    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p): return []
        res = []
        need = {}
        for c in t:
            if c in need:
                need[c] += 1
            else:
                need[c] = 1
        window = {}
        left = 0
        right = 0
        valid = 0
        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                if c in window:
                    window[c] += 1
                else:
                    window[c] = 1
                if window[c] == need[c]:
                    valid += 1
            while right - left >= len(p):
                if right - left == len(p) and valid == len(need):
                    res.append(left)
                c = s[left]
                left += 1
                if c in need:
                    if window[c] == need[c]:
                        valid -= 1
                    window[c] -= 1
        return res




if __name__ == '__main__':
    sl = Solution()
    s = "cbaebabacd"
    t = "abc"
    print(sl.findAnagrams(s,t))