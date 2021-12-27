z = open("train4.txt","r") 
a = z.read()
z.close()

import re

b = a.split('\n')
pick = b[0].split(',')
pointer = int(len(b)/6)
win = 0
draw = []

def ver(raw,draw1):
    win1 = 0
    for column in range(0,5):
        temp = []
        for raw1 in range (0,5):
            temp1 = re.findall('\d+', b[raw*6+2+raw1])
            temp.append(temp1[column])
        win1 = check(temp,draw1)
        if win1 == 1:
            break
    return win1

def check(list2,draw2):
    win2 = 0
    for i in list2:
        if i not in draw2:
            win2 = 0
            break
        win2 = 1
    return win2


for k in pick:
    draw.append(k)
    for i in range(1,len(b)):
        if b[i] != '':
            temp = re.findall('\d+', b[i])
            win = check(temp,draw)
            if win == 1:
                ref = int(i/6)
                break
    if win == 1:
        break
    for i in range(0, pointer):
        win = ver(i,draw)
        if win == 1:
            ref = i
            break
    if win == 1:
        break

res = 0
for i in range (0,5):
    temp = re.findall('\d+', b[ref*6+2+i])
    for j in temp:
        if j not in draw:
            res += int(j)

print(res*int(k))
