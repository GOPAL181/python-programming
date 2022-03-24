lst=eval(input("enter value"))
l=len(lst)
s=s1=c=0
for i in range(l):
    s=s+lst[i]
    print(s)
    s1=0
    for j in range(i+1,l):
        s1=s1+lst[j]
        print(s1)
    if(s==s1):
        c=c+1
if(c==1):
    print("yes balanced")
else:
    print("not balanced")


    


