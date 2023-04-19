# Пользователь вводит с клавиатуры диаметр окружности. В зависимости от выбора пользователя посчитать площадь или периметр окружности.
d=float(input("diameter: "))
r=float(d//2)
if d>0:
    print("ok")
choise=int(input("vybor: "))
print("1: circumference L: ")
print("2: circumference area of a circle S: ")
if choise==1:
             print(2*3.14*r)
elif choise==2:
             print(3.14*r*r)
else: d<=0
print("no")









  





