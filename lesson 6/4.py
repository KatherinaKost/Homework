'''
Запросить у пользователя число
    - если число менее 20 -  вывести на экран сколько чисел 
        в диапазоне от 0 до этого числа делится без остатка на 7. 
    - если более 20 - вывести на экран сколько чисел 
        в диапазоне от 0 до этого числа делится без остатка на 11.
'''

a = int(input())

if a < 20:
    print(a // 7 + 1)
else:
    print(a // 11 + 1)