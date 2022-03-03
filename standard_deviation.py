a=(1,2,3,4,5)
n=len(a)
sum=0
sum2=0
for i in range(0,n+1):
    sum=sum+i
print(sum)
avg=sum/n
print(avg)
for j in a:
    
    p=(j-avg)**2
    print(p)
    sum2=sum2+p
d=sum2/n
s=d**0.5
print("standard deviation=",s)