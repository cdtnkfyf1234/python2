# Зарплата менеджера составляет 200$ + процент от продаж,продажи от 500-3%, от 500 до 1000-5%....
a=int(input("sale1: "))
b=int(input("sale2: "))
c=int(input("sale3: "))
salary=200
if a<500:
    zp1=a+a*0.03
    print(zp1)
elif a>1000:
    zp1=a+a*0.08
    print(zp1)
else:
    zp1=a+a*0.05
    print(zp1)
    if b<500:
        zp2=b+b*0.03
        print(zp2)
    elif b>1000:
        zp2=b+b*0.08
        print(zp2)
    else:
        zp2=b+b*0.05
        print(zp2)
        if c<500:
            zp3=c+c*0.03
            print(zp3)
        elif c>1000:
            zp3=c+c*0.08
            print(zp3)
        else:
            zp3=c+c*0.05
            print(zp3)
if zp1>zp2 and zp1>zp3:
                print("manager1-best")
                print(zp1+200)
elif zp2>zp1 and zp2>zp3:
                print("manager2-best")
                print(zp2+200)
else:
                print("manager3-best")
                print(zp3+200)
