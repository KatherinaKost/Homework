'''
Написать функцию, которая вычисляет  факториал переданного в нее числа без рекурсии.

'''
def factorial(n:int):
    if n <= 0:
        raise ValueError ('Значение должно быть больше 0')
    else:
        a = 1
        if True:
            for i in range (1, n+1):
                a *= i
    return a
    
print(factorial(3))


        

    
