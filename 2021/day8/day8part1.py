z = open("train8.txt","r") 
a = z.read()
z.close()

b = a.split('\n')

counter = 0

for i in b:
    c = i.split('|')
    d = c[1].split(' ')
    for j in d:
        if len(j) == 2 or len(j) == 3 or len(j) == 4 or len(j) == 7:
            counter += 1

print(counter)
