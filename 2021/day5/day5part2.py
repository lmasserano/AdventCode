z = open("train5.txt","r") 
a = z.read()
z.close()

import re

b = a.split('\n')
c = {}

for i in b:
    temp = re.findall('\d+', i)
    if temp[0] == temp[2]:
        min1 = min(int(temp[1]),int(temp[3]))
        max1 = max(int(temp[1]),int(temp[3]))
        for j in range (min1,max1+1):
            if tuple([int(temp[0]), j]) not in c.keys():
                c[tuple([int(temp[0]), j])] = 1
            else:
                c[tuple([int(temp[0]), j])] += 1
    elif temp[1] == temp[3]:
        min1 = min(int(temp[0]),int(temp[2]))
        max1 = max(int(temp[0]),int(temp[2]))
        for j in range (min1,max1+1):
            if tuple([j, int(temp[1])]) not in c.keys():
                c[tuple([j, int(temp[1])])] = 1
            else:
                c[tuple([j, int(temp[1])])] += 1
    elif int(temp[0])-int(temp[2]) == int(temp[1])-int(temp[3]):
        x = min(int(temp[0]),int(temp[2]))
        y = min(int(temp[1]),int(temp[3]))
        max1 = abs((int(temp[0])-int(temp[2])))
        for j in range (0,max1+1):
            if tuple([x+j, y+j]) not in c.keys():
                c[tuple([x+j, y+j])] = 1
            else:
                c[tuple([x+j, y+j])] += 1
    elif int(temp[0])+int(temp[1]) == int(temp[2])+int(temp[3]):
        x = min(int(temp[0]),int(temp[2]))
        y = max(int(temp[1]),int(temp[3]))
        max1 = abs((int(temp[0])-int(temp[2])))
        for j in range (0,max1+1):
            if tuple([x+j, y-j]) not in c.keys():
                c[tuple([x+j, y-j])] = 1
            else:
                c[tuple([x+j, y-j])] += 1

d = sum(i >=2 for i in c.values())
print(d)
