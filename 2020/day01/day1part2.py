z = open("train1.txt","r") 
a= z.read()
z.close()

b=a.split('\n')
d=0

for i in b:
    for j in b:
        for k in b:
            c = int(i)
            d = int(j)
            e =int(k)
            if c+d+e == 2020:
                f=c*d*e

print(f)
