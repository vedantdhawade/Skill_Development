from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]  # Start with the first element
        current_sum = 0  # Keeps track of the current subarray sum
        
        for num in nums:
            if current_sum < 0:
                current_sum = 0  # Reset if the sum becomes negative
            current_sum += num
            max_sum = max(max_sum, current_sum)  # Update max sum
        
        return max_sum
