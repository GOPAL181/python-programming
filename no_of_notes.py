n=int(input("enter the value"))
th=n//2000
n%=2000
fh=n//500
n%=500
twh=n//200
n%=200
h=n//100
n%=100
f=n//50
n%=50
twe=n//20
n%=20
ten=n//10
n%=10
print("no of notes of 2000",th)
print("no of notes of 500",fh)
print("no of notes of 100",h)
print("no of notes of 50",f)
print("no of notes of 20",twe)
print("no of notes of 10",ten)
print("no of coins of 1 rupee",n)
