heights = [0,1,0,2,1,0,1,3,2,1,2,1]
l = 0
r = len(heights)-1
water_trapped = 0
while l < r :
    max_l = heights[l]
    max_r = heights[r]
    if heights[l] < heights[r]:
        if heights[l] > max_l:
            max_l = heights[l]
        else:
            water_trapped = max_l - heights[l]
        l = l + 1
    else:
        if heights[r] > max_r:
            max_r = heights[r]
        else:
            water_trapped = max_r - heights[r]
        r = r - 1

    print(water_trapped)

        