from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()  # Using a set for faster lookups
        for n in nums:
            if n in seen:
                return True  # Return True when a duplicate is found
            seen.add(n)
        return False  # Return False if no duplicates exist
