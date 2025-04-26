
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
maximum = 0
total_max = 0
start = 0
end = 0
flips = k  # Save original k so we can modify it

while end < len(nums):
    if nums[end] == 1:
        maximum += 1
        end += 1
    else:
        if flips > 0:
            flips -= 1
            maximum += 1
            end += 1
        else:
            if nums[start] == 0:
                flips += 1  # Regain a flip
            maximum -= 1
            start += 1
    total_max = max(total_max, maximum)

print(total_max)
