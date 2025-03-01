class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        a = 0
        count = 0
        for i , element in enumerate(nums):
            if element == val:
                continue
            else:
                nums[a] = element
                a = a + 1
                count = count + 1
        return count

            
        