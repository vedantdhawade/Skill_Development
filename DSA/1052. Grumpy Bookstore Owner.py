customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
minutes = 3
satsfied = 0
n = len(customers) - minutes
print(n)
for i,customer in enumerate(customers):
    if i <= len(customers) - minutes:
        if grumpy[i] == 1:
            continue
        else:
            satsfied = satsfied + int(customer)
    else:
        satsfied = satsfied + int(customer)
print(satsfied)