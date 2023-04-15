#Задание 5 Користувач вводить з клавіатури кількість годин.Коли отримане значення знаходиться у діапазоні від 0 до 6.....
x=int(input("x: "))
if (0<=x<=24):
    print("ok")
    if (0<=x<6 or x==24):
        print("good night")
    elif (6<=x<13):
        print("good morning")
    elif (13<=x<17):
        print("good day")
    elif (17<=x<24):
        print("good evening")
else:
    print("no")




