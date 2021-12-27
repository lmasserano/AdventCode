z = open("train14.txt","r") 
a = z.read()
z.close()

b = a.split('\n')

pol = b[0]
law = {}
count = {}

for i in range(2,len(b)):
    j = b[i].split(' -> ')
    law[j[0]] = j[1]

for i in range(0,10):
    pol_temp = [pol[0]]
    for j in range(0,len(pol)-1):
        temp = pol[j] + pol[j+1]
        if temp in law.keys():
            pol_temp.append(law[temp])
        pol_temp.append(pol[j+1])
    pol = ''.join(pol_temp)

for i in pol:
    if i not in count.keys():
        count[i] = 1
    else:
        count[i] += 1

d = max(count.values()) - min(count.values())

print(d)
