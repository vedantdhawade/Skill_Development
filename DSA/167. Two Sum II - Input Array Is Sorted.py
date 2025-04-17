numbers = [-1,0]
target  = -1
l = 0
r = len(numbers) - 1
arr2 = []
while l < r :
    if numbers[l] + numbers[r] > target:
        r = r - 1
    elif numbers[l] + numbers[r] < target:
        l = l + 1
    else:
        arr2.append(l+1)
        arr2.append(r + 1)
        break
print(arr2)