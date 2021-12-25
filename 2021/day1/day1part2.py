z = open("train1.txt","r") 

with open("train1.txt", "r"):
    a = z.read()
    

b = a.split('\n')
c = 0
d = []

for i in b:
    d.append(int(i))
    if len(d) < 4:
        continue
    n1 = sum(d) - d[0]
    n2 = sum(d) - d[3]
    if n1-n2 > 0:
        c += 1
    d.pop(0)

print(c)
