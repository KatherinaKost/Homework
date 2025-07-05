'''
Написать функцию которая принимает 2 стороны прямоугольника 
и возвращает либо площадь либо периметр в зависимости от дополнительного параметра.

'''


def a1(a:int, b:int, operation='per' or 'sqr'):
    if isinstance(a, int) and isinstance(b, int):  
        if operation == 'per':
            return (a + b) * 2
        elif operation == 'sqr':
            return a * b
    else:
        raise TypeError('Значения должны быть числами')
    
print(a1(2, 10, operation='per'))