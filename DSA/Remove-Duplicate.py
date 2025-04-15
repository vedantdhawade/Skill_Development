nums = [0,0,1,1,1,2,2,3,3,4]
seen = set()
l = 0
r = 0
if not nums:
    print(0)
else :
    for num in nums:
        if num in seen:
            if r < len(nums):
                r += 1
            
        else:
            seen.add(num)
            nums[l] = nums[r]
            r =  r + 1 
            l = l + 1
    print(nums)
