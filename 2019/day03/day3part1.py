z = open("train3.txt","r") 
a= z.read()
z.close()

b=a.split('\n')
save = []

def line(tr):
    d = [(0, 0)]
    for j in tr:
        temp = d[-1]
        if j[0] == 'R':
            for i in range(1,int(j[1:])+1):
                e = (temp[0]+i,temp[1])
                d.append(e)
        if j[0] == 'L':
            for i in range(1,int(j[1:])+1):
                e = (temp[0]-i,temp[1])
                d.append(e)
        if j[0] == 'U':
            for i in range(1,int(j[1:])+1):
                e = (temp[0],temp[1]+i)
                d.append(e)
        if j[0] == 'D':
            for i in range(1,int(j[1:])+1):
                e = (temp[0],temp[1]-i)
                d.append(e)
    return(d)



for wire in b:
    track = wire.split(',')
    x = line(track)
    save.append(x)

max = 10000

common = list(set(save[0]).intersection(save[1]))

for i in common:
    new = abs(i[0])+abs(i[1])
    if new < max and new > 0:
        max = new

print(max)
