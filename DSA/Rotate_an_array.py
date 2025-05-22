arr = [ 1 , 2 , 3 , 4 , 5,6,7,8,9,10]

element = arr[0]

for i in range(len(arr)-1):
    arr[i+1],element = element , arr[i+1]
arr[0] = element
print(arr)