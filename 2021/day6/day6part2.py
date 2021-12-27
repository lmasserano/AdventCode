z = open("train6.txt","r") 
a = z.read()
z.close()

b = a.split(',')

c = {}
for i in range(0,9):
    c[i] = 0

for i in b:
    c[int(i)] += 1

def day(e):
    d = {}
    d[0] = e[1]
    d[1] = e[2]
    d[2] = e[3]
    d[3] = e[4]
    d[4] = e[5]
    d[5] = e[6]
    d[6] = e[7] + e[0]
    d[7] = e[8]
    d[8] = e[0]
    return d


timer = 256
while timer >0:
    temp = day(c)
    c = temp.copy()
    timer -= 1

counter = sum(i for i in c.values())
print(counter)
