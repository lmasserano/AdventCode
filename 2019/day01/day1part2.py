z = open("train1.txt","r") 
a= z.read()
z.close()

b=a.split('\n')
summa=0

for i in b:
    fuel = int(i)
    while fuel > 8:
        fuel = int(fuel/3)-2
        summa += fuel

print(summa)
