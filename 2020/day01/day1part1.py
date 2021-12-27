z = open("train1.txt","r") 
a= z.read()
z.close()

b=a.split('\n')
d=0

for i in b:
    for j in b:
        c = int(i)
        d = int(j)
        if c+d == 2020:
            e=c*d

print(e)
