# Пользователь вводит с клавиатуры длину и ширину прямоугольника. Требуется отобразить на экран неза-
n=int(input("Введите ширину прямоугольника"))
h=int(input("Введите высоту прямоугольника"))
for i in range(n):
    for j in range(h):
        if i == 0 or j == 0 or i == n-1 or j == h-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")