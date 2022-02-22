from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        window = defaultdict(lambda :0)
        res = 0
        while right < len(s):
            c = s[right]
            right += 1
            window[c] += 1
            while window[c] > 1:
                window[s[left]] -= 1
                left += 1
            res = max(res, right - left)
        return res



if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring(""))

