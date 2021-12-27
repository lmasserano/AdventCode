z = open("train2.txt","r") 
a= z.read()
z.close()

b=a.split(',')

def check(x):
    for i in range(0,len(x),4):
        if int(x[i]) == 1:
            add1 = int(x[i+1])
            add2 = int(x[i+2])
            summa = int(x[add1]) + int(x[add2])
            pos = int(x[i+3])
            x[pos] = summa
        if int(x[i]) == 2:
            pro1 = int(x[i+1])
            pro2 = int(x[i+2])
            product = int(x[pro1]) * int(x[pro2])
            pos = int(x[i+3])
            x[pos] = product
        if int(x[i]) == 99:
            break
    return x[0]

for i in range(0,99):
    for j in range(0,99):
        b[1]=i
        b[2]=j
        x = b.copy()
        result = check(x)
        if result == 19690720:
            z = 100*i+j
            print(z)
