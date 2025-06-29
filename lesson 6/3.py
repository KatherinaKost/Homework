'''
Запросить 3 числа. Вывести наибольшее  из них. Решить используя if.
'''
b, c, d = int(input("Введите число: ")), int(input("Введите число: ")), int(input("Введите число: "))

if b > c > d:
    print(b)
elif c > b > d:
    print(c)
else:
    print(d)





