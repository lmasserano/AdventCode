z = open("train5.txt","r") 
a= z.read()
z.close()

position=a.split('\n')
maxy = 0

for man in position:
    raw = 0
    column = 0
    counter = 0
    for letter in man:
        if letter == 'B':
            raw += 2**(6-counter)
        if letter == 'R':
            column += 2**(9-counter)
        counter += 1
    new_max = raw*8 + column
    if new_max > maxy:
        maxy = new_max

print(maxy)
