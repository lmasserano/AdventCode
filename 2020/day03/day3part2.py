z = open("train3.txt","r") 
a= z.read()
z.close()

b=a.split('\n')
counter = 0
tot = []
position = 0
max = len(b[0])
c = [1, 3, 5, 7, 1]
d = [1, 1, 1, 1, 2]
jump = 1
for j,k in zip(c,d):
    for i in b:
        if i[position] == '#' and jump == 1:
            counter +=1
        if k > 1:
            if jump > 1:
                jump -= 1
            else:
                jump = k
                position += j
        else:
            position += j
        if position >= max:
            position -= max
    tot.append(counter)
    counter = 0
    position = 0

totale = 1
for m in tot:
    totale *= m

print(totale)
