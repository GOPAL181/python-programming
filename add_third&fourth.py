n=int(input("enter value"))
m=n
while(n>1000):
    n=n//10
    l=n%10
while(m>10000):
    m=m//10
    v=m%10
c=l*v
print(c)