height = [1,1]
l = 0
r = len(height) - 1
area = 0

if len(height) < 3:
    area = min(height)
    print(area)

else :
    while l < r :
        if height[l] < height[r]:
            area = max(area , height[l] * (r - l))
            l = l + 1
        elif height[r] <  height[l]:
            area = max(area,height[r] * (r - l)) 
            r = r - 1
        else :
            area = max(area , height[l] * (r - l))
            if height[l+1] < height[r-1]:
                l = l + 1
            else :
                r = r - 1
    print(area)            
 
