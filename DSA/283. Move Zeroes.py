nums = [0]
l = 0 
r = 0
while r < len(nums):
    if nums[r] != 0:
        nums[l] , nums[r] = nums[r] , nums[l]
        l = l + 1
    r = r + 1
print(nums)    