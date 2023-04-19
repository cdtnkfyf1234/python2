n=int(input("n="))
a=n%10
n//=10
# print(n)
b=n%10
n//=10
# print(b)
c=n%10
n//=10
# print(c)
d=n%10
n//=10
# print(d)
e=n%10
n//=10
# print(e)
f=n%10
n//=10
if(f==0 or n):
    print("No")
else:
    a,f = f,a
    b,e = e,b
    print(f*100000+e*10000+d*1000+c*100+b*10+a)


