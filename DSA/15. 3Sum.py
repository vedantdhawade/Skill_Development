nums = [-1,0,1,2,-1,-4]
nums.sort()
print(len(nums))
for i in range(len(nums)-2):
    target = -nums[i]
    left = i + 1
    right = len(nums) - 1
    print(f"target - {target} left {left} right {right}")