a=1
while(a<5000):
    if(a%7==0 and a%6==1 and a%5==1 and a%4==1 and a%3==1 and a%2==1):
        print(a)
        break
    a=a+1
'''       OR
a=1
while(a<5000):
    if(a%7==0 and a%60==1):  /BY TAKING LCM /
        print(a)
        break
    a=a+1
'''

