min1 = 387638
max1 = 919123

a = range(min1,max1+1)
count = 0

for i in a:
    a1 = i%10
    b1 = int((i/10)%10)
    c1 = int((i/100)%10)
    d1 = int((i/1000)%10)
    e1 = int((i/10000)%10)
    f1 = int((i/100000)%10)
    if a1 < b1 or b1 < c1 or c1 < d1 or d1 < e1 or e1 < f1:
        continue
    g = [a1, b1, c1, d1, e1, f1]
    h = dict((x, g.count(x)) for x in set(g))
    if 2 not in h.values():
        continue
    count += 1

print(count)
