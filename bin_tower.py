
n=int(input())
d=bin(n+1)
d=d.replace("0b","")
e=len(d)
for i in range(n+1):
    c=bin(i)
    c= c.replace('0b', '')
    if(e>len(c)):
        for j in range(e-len(c)):
            c=" "+c
    print(c)