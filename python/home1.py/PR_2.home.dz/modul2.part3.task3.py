# Користувач вводить з клавіатури номер місяця(від 1 до 12).В залежності від цього програма виводить на екран...
x=int(input("x: "))
if (1<=x<=2 or x==12):
    print("winter")
if (3<=x<=5):
    print("spring")
if (6<=x<=8):
    print("summer")
if (9<=x<=11):
    print("autumn")
if (0<x<=12):
    print("ok")
else:
    print("no")


    



