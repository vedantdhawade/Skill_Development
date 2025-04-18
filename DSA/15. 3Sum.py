nums = [-1,0,1,2,-1,-4]
nums.sort()
print(nums)
arr = []
for i in range(len(nums)-2):
    target = -nums[i]
    print(target)
    left = i + 1
    right = len(nums) - 1
    while left < right :
        if nums[left] + nums[right] == target:
            arr.append([target , nums[left] , nums[right]])
            print(arr)
        elif nums[left] + nums[right] < target:
            left = left + 1
        else:
            right = right + 1
        left += 1
        right -= 1
