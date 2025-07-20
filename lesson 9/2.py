'''
Написать рекурсивную функцию, которая вычисляет  
факториал переданного в нее числа.

'''

def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Факториал определяется для неотрицательных чисел")
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

    
        
    
        
print(factorial(5))

