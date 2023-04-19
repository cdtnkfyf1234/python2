# Користувач вводить з клавіатури номер місяця(від 1 до 12).В залежності від цього програма виводить на екран...
x=int(input("x: "))
if (0<x<=12):
        print("ok")
        if (1<=x<=2 or x==12):
            print("winter")
        elif (3<=x<=5):
            print("spring")
        elif (6<=x<=8):
            print("summer")
        elif (9<=x<=11):
            print("autumn")
# if (0<x<=12):
    # print("ok")
else:
    print("no")

 
          



    



