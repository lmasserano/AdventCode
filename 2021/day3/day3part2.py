z = open("train3.txt","r") 
a = z.read()
z.close()

b = a.split('\n')
oxygen = a.split('\n')
co2 = a.split('\n')
n = len(b[0])

for i in range (0,n):
    zero = 0
    uno = 0
    for j in oxygen:
        if j[i] == '0':
            zero += 1
        elif j[i] == '1':
            uno += 1
    if uno >= zero:
        temp = '1'
    elif uno < zero:
        temp = '0'
    temp1 = []
    for j in oxygen:
        if j[i] == temp:
            temp1.append(j)
    oxygen = temp1.copy()
    if len(oxygen)==1:
        break

for i in range (0,n):
    zero = 0
    uno = 0
    for j in co2:
        if j[i] == '0':
            zero += 1
        elif j[i] == '1':
            uno += 1
    if uno >= zero:
        temp = '0'
    elif uno < zero:
        temp = '1'
    temp1 = []
    for j in co2:
        if j[i] == temp:
            temp1.append(j)
    co2 = temp1.copy()
    if len(co2)==1:
        break

g = int(''.join(oxygen),2)
e = int(''.join(co2),2)

print(e*g)
