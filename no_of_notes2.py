n=int(input("enter the value"))
n=n-100
th=n//2000
n%=2000
fh=n//500
n%=500
twh=n//200
n%=200
h=n//100
print("no of notes of 2000",th)
print("no of notes of 500",fh)
print("no of notes of 100",h+1)
