a = [1,2,3,4,5] 
b = [1,2,3]
n = len(a)
m = len(b)
res = []

seen = set()

for i in a :
    if i in seen:
        continue
    else:
        seen.add(i)
        res.append(i)

for i in b :
    if i in seen:
        continue
    else:
        seen.add(i)
        res.append(i)

print(res)