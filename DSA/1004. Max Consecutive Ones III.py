nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
max = 0
total_max = 0
start = 0
end = 0
while end < len(nums):
    if nums[end] == 1:
        end = end + 1
        max = max + 1
        total_max = max(total_max,max)
    else:
        if k != 0:
            end = end + 1
            max = max + 1 
            k = k - 1
            total_max = max(total_max,max)
        else:
            if nums[start] == 1:
                start = start + 1
                max = max - 1
                total_max = max(total_max,max)
            else :
                flip = flip + 1
                start = start + 1
                total_max = max(total_max,max)
print(total_max)
            