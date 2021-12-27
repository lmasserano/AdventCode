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

eye = ['amb','blu','brn','gry','grn','hzl','oth']

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
    if len(dic)!=correct:
        continue
    if int(dic["byr"]) < 1920 or int(dic["byr"]) > 2002:
        continue
    if int(dic["iyr"]) < 2010 or int(dic["iyr"]) > 2020:
        continue
    if int(dic["eyr"]) < 2020 or int(dic["eyr"]) > 2030:
        continue
    if 'in' not in dic["hgt"] and 'cm' not in dic["hgt"]:
        continue
    else:
        height = re.findall(r'[a-z]+|\d+', dic["hgt"])
        if height[1]=='cm':
            if  int(height[0]) < 150 or int(height[0]) > 193:
                continue
        else:
            if  int(height[0]) < 59 or int(height[0]) > 76:
                continue
    if len(dic["hcl"]) != 7 or dic["hcl"][0] != '#' or dic["hcl"][1:6].isalnum == False:
        continue
    if dic["ecl"] not in eye:
        continue
    if len(dic["pid"]) != 9 or dic["pid"].isdigit == False:
        continue
    count += 1

print(count)
