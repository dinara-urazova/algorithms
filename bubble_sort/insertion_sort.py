from typing import List


class Solution:
    def insertion_sort(self, arr: List[int]) -> List[int]:  # Added 'self'
        swaps = 0
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:  # Fixed condition to include the first element
                arr[j + 1] = arr[j]  # Move the element one position ahead
                j -= 1
            arr[j + 1] = key  # Insert the key at the correct position
        print(arr)
        return arr


s = Solution()
assert s.insertion_sort([2, 5, 1, 8, 15, 3]) == [1, 2, 3, 5, 8, 15]
