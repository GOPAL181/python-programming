a=int(input("enter the value"))
b=int(input("enter the value"))
if(a>b):
    min=b
else:
    min=a
for i in range(min,1,-1):
    if(a%i==0 and b%i==0):
        hcf=i
print("hcf=",hcf)
lcm=a*b//hcf
print("lcm=",lcm)
