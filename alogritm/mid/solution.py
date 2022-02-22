

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_str = ""
        temp_str = ""
        d = {}
        for i, c in enumerate(s):
            if c not in temp_str:
                temp_str += c
                d[c] = i
            else:
                if len(temp_str) > len(longest_str):
                    longest_str = temp_str
                new_start = d[c] + 1
                temp_str = s[new_start: i + 1]
                d[c] = i

        if len(temp_str) > len(longest_str):
            longest_str = temp_str
        return len(longest_str)


if __name__ == '__main__':
    s = Solution()
    print (s.lengthOfLongestSubstring("abba"))

