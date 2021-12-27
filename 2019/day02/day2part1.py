z = open("train2.txt","r") 
a= z.read()
z.close()

b=a.split(',')

for i in range(0,len(b),4):
    if int(b[i]) == 1:
        add1 = int(b[i+1])
        add2 = int(b[i+2])
        summa = int(b[add1]) + int(b[add2])
        pos = int(b[i+3])
        b[pos] = summa
    if int(b[i]) == 2:
        pro1 = int(b[i+1])
        pro2 = int(b[i+2])
        product = int(b[pro1]) * int(b[pro2])
        pos = int(b[i+3])
        b[pos] = product
    if int(b[i]) == 99:
        break

print(b[0])
