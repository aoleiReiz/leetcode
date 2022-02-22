from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        def helper(_nums, left, right):
            if left > right:
                return -1
            mid = (left + right) // 2
            if mid == 0:
                if _nums[mid] != _nums[mid + 1]:
                    return mid
            elif mid == len(_nums) - 1:
                if _nums[mid] != _nums[mid - 1]:
                    return mid
            else:
                if _nums[mid] != _nums[mid - 1] and _nums[mid] != _nums[mid + 1]:
                    return mid

            left_ans = helper(_nums, left, mid - 1)
            right_ans = helper(_nums, mid + 1, right)
            


