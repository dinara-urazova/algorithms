# more optimized version of early termination in case of a sorted array
from typing import List


class Solution:
    def bubbleSort(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cf = 0
        for i in range(n - 1):
            swaps = 0
            for j in range(n - 1 - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    cf += 1  # to see that in case of the sorted array no swaps have been done
                    swaps = 1
            if swaps == 0:
                break
        # print(nums, cf)
        return nums


s = Solution()
assert s.bubbleSort([1, 3, 5, 6, 8, 10]) == [1, 3, 5, 6, 8, 10]
assert s.bubbleSort([10, 9, 5, 3, 2, 1]) == [1, 2, 3, 5, 9, 10]
