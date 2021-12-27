z = open("train4.txt","r") 
a= z.read()
z.close()

import re

dict = {
    "byr":"",
    "iyr":"",
    "eyr":"",
    "hgt":"",
    "hcl":"",
    "ecl":"",
    "pid":"",
}

correct = len(dict)
people=a.split('\n''\n')

count = 0

for man in people:
    dic = {}
    data = re.split(' |\n', man)
    for info in data:
        info1 = info.split(':')
        dic[info1[0]] = info1[1]
    if "cid" in dic.keys():
        dic.pop('cid')
    if len(dic)==correct:
        count += 1

print(count)
