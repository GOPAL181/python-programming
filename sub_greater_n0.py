x=int(input("enter the value"))
y=int(input("enter the value"))
if(x>y):
    s=x-y
    print("greater=", x)
    print("smaller=", y)
elif(y>x):
    print("greater=", y)
    print("smaller=", x)
    s=y-x
else:
    print("both are equal")
    s=x-y
print ("after subtracting",s)
