# Пользователь вводит с клавиатуры число в диапазоне от 1 до 100.Если число кратно 3 то нужно вывести слово Fizz......
a=int(input("input number: "))
if 0<=a<=100:
    print("ok")
else: 
    print("false")
if a%3==0:
    print("fizz")
if  a%5==0:
     print("buzz")
elif a%3==0 and a%5==0:
    print("fizz, buzz")
elif a%3!=0 and a%5!=0:
    print(a)


  

