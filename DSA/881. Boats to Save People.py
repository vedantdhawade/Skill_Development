people = [3,5,3,4]
people.sort()
limit = 5
boat = 0
l = 0
r = len(people) - 1

while l <= r:
    if people[l] + people[r] <= limit:
        l += 1  # lightest person is placed
    # In both cases, heaviest person goes, so move right pointer
    r -= 1
    boat += 1

print(boat)
