customers = [1, 0, 1, 2, 1, 1, 7, 5]
grumpy =    [0, 1, 0, 1, 0, 1, 0, 1]
minutes = 3

# Step 1: satisfied by default (owner not grumpy)
base_satisfied = 0
for i in range(len(customers)):
    if grumpy[i] == 0:
        base_satisfied += customers[i]

# Step 2: Find max additional satisfied in any 'minutes' window
extra = 0
max_extra = 0
for i in range(len(customers)):
    if grumpy[i] == 1:
        extra += customers[i]
    if i >= minutes:
        if grumpy[i - minutes] == 1:
            extra -= customers[i - minutes]
    max_extra = max(max_extra, extra)

# Final answer
total_satisfied = base_satisfied + max_extra
print(total_satisfied)
