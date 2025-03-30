from typing import List


class Solution:
    def bubbleSort(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        # print(nums)
        return nums


s = Solution()
assert s.bubbleSort([1, 3, 5, 6, 8, 10]) == [1, 3, 5, 6, 8, 10]
assert s.bubbleSort([10, 9, 5, 3, 2, 1]) == [1, 2, 3, 5, 9, 10]
