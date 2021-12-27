z = open("train6.txt","r") 
a = z.read()
z.close()

b = a.split(',')

c = {}
counter = 0
for i in b:
    c[counter] = int(i)
    counter += 1

timer = 80
while timer >0:
    temp = []
    for i in c.keys():
        c[i] -= 1
        if c[i] == -1:
            temp.append(i)
    if len(temp) > 0:
        for j in temp:
            c[j] = 6
            counter += 1
            c[counter] = 8
    timer -= 1

print(counter)
