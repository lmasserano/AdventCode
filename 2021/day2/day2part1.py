z = open("train2.txt","r") 
a = z.read()
z.close()

b = a.split('\n')
hor = 0
dep = 0

for i in b:
    c = i.split(' ')
    if c[0] == 'forward':
        hor += int(c[1])
    elif c[0] == 'down':
        dep += int(c[1])
    elif c[0] == 'up':
        dep -= int(c[1])

print(dep*hor)
