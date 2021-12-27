z = open("train7.txt","r") 
a = z.read()
z.close()

b = a.split(',')

c = []

for i in b:
    c.append(int(i))

min1 = min(c)
max1 = max(c)

tot = max1*len(c)

for i in range(min1,max1):
    tot1 = sum(abs(d-i) for d in c)
    if tot1 < tot:
        tot = tot1

print(tot)
