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
        par1 = int(b[i+1])
        par2 = int(b[i+2])
        pos = int(b[i+3])
        if C == 0:
            x = int(b[par1])
        else:
            x = par1
        if B == 0:
            y = int(b[par2])
        else:
            y = par2
        summa = x + y
        b[pos] = summa
        step = 4
    if case == 2:
        par1 = int(b[i+1])
        par2 = int(b[i+2])
        pos = int(b[i+3])
        if C == 0:
            x = int(b[par1])
        else:
            x = par1
        if B == 0:
            y = int(b[par2])
        else:
            y = par2
        product = x * y
        b[pos] = product
        step = 4
    if j == 3:
        val = input('Enter instruction: ')
        pos = int(b[i+1])
        b[pos] = val
        step = 2
    if case == 4:
        pos = int(b[i+1])
        if C == 0:
            x = int(b[pos])
        else:
            x = pos
        print(x)
        step = 2
    if case == 5:
        par1 = int(b[i+1])
        par2 = int(b[i+2])
        if C == 0:
            x = int(b[par1])
        else:
            x = par1
        if B == 0:
            y = int(b[par2])
        else:
            y = par2
        if x != 0:
            step = y-i
        else:
            step = 3
    if case == 6:
        par1 = int(b[i+1])
        par2 = int(b[i+2])
        if C == 0:
            x = int(b[par1])
        else:
            x = par1
        if B == 0:
            y = int(b[par2])
        else:
            y = par2
        if x == 0:
            step = y-i
        else:
            step = 3
    if case == 7:
        par1 = int(b[i+1])
        par2 = int(b[i+2])
        pos = int(b[i+3])
        if C == 0:
            x = int(b[par1])
        else:
            x = par1
        if B == 0:
            y = int(b[par2])
        else:
            y = par2
        if x < y:
            b[pos] = 1
        else:
            b[pos] = 0
        step = 4
    if case == 8:
        par1 = int(b[i+1])
        par2 = int(b[i+2])
        pos = int(b[i+3])
        if C == 0:
            x = int(b[par1])
        else:
            x = par1
        if B == 0:
            y = int(b[par2])
        else:
            y = par2
        if x == y:
            b[pos] = 1
        else:
            b[pos] = 0
        step = 4
    if j == 99:
        break
