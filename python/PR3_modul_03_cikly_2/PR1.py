# Пользователь вводит с клавиатуры два числа. Нужно посчитать сумму чисел в указанном дыапазоне а также среднеарифметическое.
a=int(input("a= "))
b=int(input("b= "))
a0=a
i=0
# i+=a
s=0
while a<=b:
    s+=a
    a+=1
    i+=1
print("sum= ", s)
# print("sr= ",s/(b-a0+1))
print("sr= ",s/i)

    
    
 
