# Пользователь вводит с клавиатуры два числа. В зависимости от выбора пользователя надо показать сумму, разницу, произведение и среднеарифметическое двух чисел.
a=int(input("input number"))
b=int(input("input number"))
print("vybor")
print("1 sum: ")
print("2 differ: ")
print("3 mult: ")
print("4 arithm: ")
choise=int(input("vas vybor"))
if choise==1:
    print(a+b)
elif choise==2:
    if a>b:
        print(a-b)
    else:
        print(b-a)
elif choise==3:
    print(a*b)
else:
    print((a+b)/2)