z = open("train3.txt","r") 
a= z.read()
z.close()

b=a.split('\n')
counter = 0
position = 0
max = len(b[0])
for i in b:
    if i[position] == '#':
        counter +=1
    position +=3
    if position >= max:
        position -= max
print(counter)
