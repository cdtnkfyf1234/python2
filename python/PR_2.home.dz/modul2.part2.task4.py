# Пользователь вводит с клавиатуры размер файла в гигабайтах и скорость интернет соединения в битах.....
a=float(input("file: "))
b=float(input("speed: "))
c=a*1024/((b*1.0e-6)/8)
print(c)
# с- в секундах
min=c/60
hours=c/60/60
print(min)
print(hours)