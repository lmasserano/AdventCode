z = open("train10.txt","r") 
a = z.read()
z.close()

b = a.split('\n')
tot = 0

def check(string1):
    list1 = []
    save1 = ''
    for i in string1:
        if i in ['(','[','{','<']:
            list1.append(i)
        else:
            if len(list1) == 0:
                break
            elif i == ')' and list1[-1] == '(':
                list1.pop()
            elif i == ']' and list1[-1] == '[':
                list1.pop()
            elif i == '}' and list1[-1] == '{':
                list1.pop()
            elif i == '>' and list1[-1] == '<':
                list1.pop()
            else:
                save1 = i
                break
    return(save1)

for j in b:
    count = check(j)
    if count == '':
        continue
    elif count == ')':
        tot += 3
    elif count == ']':
        tot += 57
    elif count == '}':
        tot += 1197
    elif count == '>':
        tot += 25137

print(tot)
