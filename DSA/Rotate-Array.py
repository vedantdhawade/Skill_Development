from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n  # Handle cases where k > n

        # Step 1: Reverse the entire array
        nums.reverse()

        # Step 2: Reverse the first k elements
        nums[:k] = reversed(nums[:k])

        # Step 3: Reverse the remaining n-k elements
        nums[k:] = reversed(nums[k:])
