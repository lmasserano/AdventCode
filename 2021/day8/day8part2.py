z = open("train8.txt","r") 
a = z.read()
z.close()

b = a.split('\n')
result = 0

for i in b:
    c = i.split('|')
    d = c[0].split(' ')
    e = {}
    e5 = []
    e6 = []
    for k in d:
        k1 = list(k)
        k1.sort()
        j = ''.join(k1)
        if len(j) == 2:
            e[j] = 1
        elif len(j) == 3:
            seven = j
            e[j] = 7
        elif len(j) == 4:
            four = j
            e[j] = 4
        elif len(j) == 7:
            eight = j
            e[j] = 8
        elif len(j) == 5:
            e5.append(j)
        elif len(j) == 6:
            e6.append(j)
    for j in e6:
        if all(elem in j for elem in four) and all(elem in eight for elem in j):
            nine = j
            e[j] = 9
        elif all(elem in j for elem in seven):   
            e[j] = 0
        else:
            six = j
            e[j] = 6
    for j in e5:
        if all(elem in six for elem in j):
            e[j] = 5
        elif all(elem in nine for elem in j):   
            e[j] = 3
        else:
            e[j] = 2
    d1 = c[1].split(' ')
    for i in range(1,len(d1)):
        temp = list(d1[i])
        temp.sort()
        result += e[''.join(temp)]*10**(4-i)
        
print(result)
