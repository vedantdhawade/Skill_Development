from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0  # Edge case: Empty list
        
        k = 0  # Pointer for unique elements
        for i in range(1, len(nums)):
            if nums[i] != nums[k]:  # Found a new unique element
                k += 1
                nums[k] = nums[i]  # Move it to the front
        
        return k + 1  # Number of unique elements
