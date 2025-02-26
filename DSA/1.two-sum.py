#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
from typing import List

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if(complement in hash_table):
                return [hash_table[complement],i]
            hash_table[nums[i]] = i
        
# @lc code=end

