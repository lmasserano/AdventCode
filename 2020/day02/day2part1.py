z = open("train2.txt","r") 
a= z.read()
z.close()
ok = 0
b=a.split("\n")
for i in b:
    if ':' in i:
        m=i.split()
        n=m[0].split('-')
        min=int(n[0])
        max=int(n[1])
        x = m[1][0]
        word= m[2]
        counter = word.count(x)
        if counter >= min and counter <= max:
            ok += 1

print(ok)
