z = open("train01.txt","r") 
a= z.read()
z.close()

b=a.split('\n')
summa=0

for i in b:
    summa += int(int(i)/3)-2

print(summa)
