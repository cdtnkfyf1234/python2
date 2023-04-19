n=int(input("n="))
a=n%10
n//=10
print(n)
b=n%10
n//=10
print(b)
c=n%10
n//=10
print(c)
d=n%10
n//=10
print(d)
e=n%10
n//=10
print(e)
f=n%10
n//=10
print(f)
print(f, e, d, c, b,a)
if (f+e+d == c+b+a):
    print("lucky")
else:
    print("no lucky")
