n=int(input("enter the number"))
m=n
o=n
c=0
while(o>0):
    o=o//10
    c=c+1
sum=0
while(n>0):
    lv=n%10
    sum=sum+lv**c
    n=n//10
if(m==sum):
    print("armstrong")
else:
    print("not armstrong")


