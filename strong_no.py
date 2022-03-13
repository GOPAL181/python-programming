n=int(input("enter the value"))
f=1
m=n
sum=0
while(n>0):
    lv=n%10
    for i in range(1,lv+1):
        f=f*i
    print(f)
    sum=sum+f
    f=1
    n=n//10
if(sum==m):
    print("strong number")
else:
    print("not strong")





