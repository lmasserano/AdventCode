z = open("train14.txt","r") 
a = z.read()
z.close()

b = a.split('\n')

pol = b[0]
law = {}
count = {}
count2 = {}

count2[pol[-1]] = 1

for i in range(2,len(b)):
    j = b[i].split(' -> ')
    law[j[0]] = j[1]

for i in range(0,len(pol)-1):
    temp = pol[i] + pol[i+1]
    if temp not in count.keys():
        count[temp] = 1
    else:
        count[temp] += 1

for i in range(0,40):
    temp = []
    for j in count.keys():
        temp.append(j)
    count3 = {}
    for j in temp:
        if j[0] + law[j] not in count3.keys():
            count3[j[0] + law[j]] = count[j]
        else:
            count3[j[0] + law[j]] = count3[j[0] + law[j]] + count[j]
        if law[j] + j[1] not in count3.keys():
            count3[law[j] + j[1]] = count[j]
        else:
            count3[law[j] + j[1]] = count3[law[j] + j[1]] + count[j]
    count = count3.copy()



for i in count.keys():
    if i[0] not in count2.keys():
        count2[i[0]] = count[i]
    else:
        count2[i[0]] += count[i]

d = max(count2.values()) - min(count2.values())

print(d)
