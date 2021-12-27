z = open("train5.txt","r") 
a= z.read()
z.close()

position=a.split('\n')
people = []

for man in position:
    raw = 0
    column = 
    for letter in man:
        if letter == 'B':
            raw += 2**(6-counter)
        if letter == 'R':
            column += 2**(9-counter)
        counter += 1
    people.append(raw*8 + column)

me = 0

for person in people:
    if person +2 in people and person +1 not in people:
        me = person+1

print(me)
