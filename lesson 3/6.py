'''
Пользователь вводит 3 числа, 
найти среднее арифметическое с точность 3 знака после запятой

'''
var_1, var_2, var_3 = int(input()), int(input()), int(input())
average = (var_1 + var_2 + var_3)/3
print(round(average, 3))
