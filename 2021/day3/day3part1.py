z = open("train3.txt","r") 
a = z.read()
z.close()

b = a.split('\n')
n = len(b[0])
gamma = ['0']*n
epsilon = ['0']*n
uno = [0]*n
zero = [0]*n

for i in b:
    k = 0
    for j in i:
        if j == '0':
            zero[k] += 1
        elif j == '1':
            uno[k] += 1
        k += 1

k = 0
for i,j in zip(uno, zero):

    if i > j:
        gamma[k] = '1'
    elif i <j:
        epsilon[k] = '1'
    k += 1

g = int(''.join(gamma),2)
e = int(''.join(epsilon),2)

print(e*g)
