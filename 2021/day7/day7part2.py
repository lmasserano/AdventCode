z = open("train7.txt","r") 
a = z.read()
z.close()

b = a.split(',')

c = {}

for i in b:
    if int(i) in c.keys():
        c[int(i)] += 1
    else:
        c[int(i)] = 1 

min1 = min(c.keys())
max1 = max(c.keys())

tot = max1**5

for i in range(min1,max1):
    tot1 = 0
    step = 0
    l = i
    m = i
    for j in range(1,max1+1):
        l += 1
        m -= 1
        step += j
        if m < min1 and l > max1:
            break
        if l in c.keys():
            tot1 += step*c[l]
        if m in c.keys():
            tot1 += step*c[m]
    if tot1 < tot:
        tot = tot1

print(tot)
