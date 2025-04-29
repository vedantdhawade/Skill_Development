target = 7
nums = [2,3,1,2,4,3]
start = 0
end = 0
window_sum = 0
min_length = float('inf')

while end < len(nums):
    window_sum += nums[end]
    
    while window_sum >= target:
        min_length = min(min_length, end - start + 1)
        window_sum -= nums[start]
        start += 1
    
    end += 1

print(min_length if min_length != float('inf') else 0)
