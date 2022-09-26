from typing import List

class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        n = len(nums)
        ans = []
        cur = 1
        idx = 0
        while idx < n:
            if cur == nums[idx]:
                idx += 1
                cur += 1
            elif cur < nums[idx]:
                ans.append(cur)
                cur += 1
            else:
                ans.append(cur)
                idx += 1
        if cur == n + 3 or len(ans) == 2:
            return ans
        elif cur < n + 3:
            while cur < n + 3:
                ans.append(cur)
                cur += 1
        return ans



if __name__ == '__main__':
    s = Solution()
    print(s.missingTwo([2, 3]))