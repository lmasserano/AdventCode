z = open("train10.txt","r") 
a = z.read()
z.close()

b = a.split('\n')
tot = []

def check(string1):
    list1 = []
    list2 = []
    score = 0
    counting = 1
    for i in string1:
        if i in ['(','[','{','<']:
            list1.append(i)
        else:
            if len(list1) == 0:
                counting = 0
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
                counting = 0
                break
    if counting == 1:
        while len(list1) != 0:
            if list1[-1] == '(':
                list2.append(')')
            elif list1[-1] == '[':
                list2.append(']')
            elif list1[-1] == '{':
                list2.append('}')
            elif list1[-1] == '<':
                list2.append('>')
            list1.pop()
        for k in list2:
            if k == ')':
                j = 1
            elif k == ']':
                j = 2
            elif k == '}':
                j = 3
            elif k == '>':
                j = 4
            score = score*5 + j
    return(score)

for j in b:
    count = check(j)
    if count != 0:
        tot.append(count)

tot.sort()
print(tot[int((len(tot)-1)/2)])
