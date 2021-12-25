z = open("train1.txt","r") 
a = z.read()
z.close()

b = a.split('\n')
c = 0
d = int(b[0])

for i in b:
    if int(i) > d:
        c += 1
    d = int(i)

print(c)
