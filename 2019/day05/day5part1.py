z = open("train5.txt","r") 
a= z.read()
z.close()

b=a.split(',')
1
step = 0

for i in range(0,len(b)):
    if step > 1:
        step -= 1
        continue
    j = int(b[i])
    if j < 0:
        continue
    E = j%10
    D = int((j/10)%10)
    C = int((j/100)%10)
    B = int((j/1000)%10)
    A = int((j/10000)%10)
    case = D*10 + E
    if case == 1:
        add1 = int(b[i+1])
        add2 = int(b[i+2])
        pos = int(b[i+3])
        if C == 0:
            x = int(b[add1])
        else:
            x = add1
        if B == 0:
            y = int(b[add2])
        else:
            y = add2
        summa = x + y
        b[pos] = summa
        step = 4
    if case == 2:
        pro1 = int(b[i+1])
        pro2 = int(b[i+2])
        pos = int(b[i+3])
        if C == 0:
            x = int(b[pro1])
        else:
            x = pro1
        if B == 0:
            y = int(b[pro2])
        else:
            y = pro2
        product = x * y
        b[pos] = product
        step = 4
    if j == 3:
        val = input('Enter instruction: ')
        pos = int(b[i+1])
        b[pos] = val
        step = 2
    if j == 4:
        pos = int(b[i+1])
        print(b[pos])
        step = 2
    if j == 99:
        break
