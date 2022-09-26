from typing import List


class TwoSum:

    def __init__(self):
        self.data = []

    def add(self, number: int) -> None:
        self.data.append(number)

    def find(self, value: int) -> bool:
        d = set()
        for num in self.data:
            if value - num in d:
                return True
            else:
                d.add(num)
        return False


class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        n = len(s)
        maxIdx = n - 1
        idx1 = idx2 = -1
        for i in range(n - 1, -1, -1):
            if s[i] > s[maxIdx]:
                maxIdx = i
            elif s[i] < s[maxIdx]:
                idx1, idx2 = i, maxIdx
        if idx1 < 0:
            return num
        s[idx1], s[idx2] = s[idx2], s[idx1]
        return int(''.join(s))

    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        ans = []
        if nums:
            cur = lower
            for num in nums:
                if cur < num:
                    if cur == num - 1:
                        ans.append(str(cur))
                    else:
                        ans.append(f"{cur}->{num-1}")
                cur = max(cur,num + 1)
            if cur <= upper:
                if cur == upper:
                    ans.append(str(cur))
                else:
                    ans.append(f"{cur}->{upper}")
        else:
            if lower == upper:
                ans.append(f"{lower}")
            else:
                ans.append(f"{lower}->{upper}")
        return ans

if __name__ == '__main__':
    print(Solution().findMissingRanges([0, 1, 3, 50, 75], 0, 99))
