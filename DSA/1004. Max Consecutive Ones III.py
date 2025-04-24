nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

start = 0
max_len = 0

for end in range(len(nums)):
    # If we flip a 0, decrease k
    if nums[end] == 0:
        k -= 1

    # If k < 0, move the start pointer forward to regain a flip
    while k < 0:
        if nums[start] == 0:
            k += 1  # Regain a flip
        start += 1  # Shrink window

    # Update max_len
    max_len = max(max_len, end - start + 1)

print(max_len)
