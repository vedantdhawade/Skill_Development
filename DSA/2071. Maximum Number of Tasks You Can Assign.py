tasks = [10,15,30]
workers = [0,10,10,10,10]
pills = 3
strength = 10
tasks.sort()
workers.sort()
p1 , p2 ,count = 0 , 0 , 0 

while (p1 < len(tasks) and p2 < len(workers)):
    if workers[p2] < tasks[p1]:
        if pills != 0:
            if workers[p2] + strength >= tasks[p1]:
                pills -= 1
                p1 += 1
                p2 += 1
                count += 1
            else:
                p1 += 1
                p2 += 1
        else:
            p1 += 1
            p2 += 1
    else :
        count += 1
        p1 += 1
        p2 += 1

print(f"count ----> {count}")