# Написать программу подсчета стоимости разговора для разных мобильных операторов....
# t-время разговора (в минутах), a-стоимость 1 минуты разговора (в гривнах).
# 1- звонок с kyivstar, 2- звонок с  vodafon, 3-звонок с life.
choise=int(input("operator: "))
print("1: kyivstar")
print("2: vodafon")
print("3: life")
if choise==1:
    print("kyivstar")
    t=int(input("t: "))
    print("1: kyivstar")
    print("2: vodafon")
    print("3: life")
    choise=int(input("operator"))
    if choise==1:
                print(t*0)
    elif choise==2:
                print(t*0.6)
    else:
                print(t*0.6) 
elif choise==2:
    print("vodafon")
    t=int(input("t: "))
    print("1: kyivstar")
    print("2: vodafon")
    print("3: life")
    choise=int(input("operator"))
    if choise==1:
                print(t*0.69+0.29)
    elif choise==2:
                print(t*1)
    else:
                print(t*0.69+0.29)
else:
    print("life")
    t=int(input("t: "))
    print("t:")
    print("1: kyivstar")
    print("2: vodafon")
    print("3: life")
    choise=int(input("operator"))
    if choise==1:
            print(t*1.05+1.05)
    elif choise==2:
            print(t*1.05+1.05)
    else:
            print(t*0)

# данные о стоимости звонков взяла в интернете.

