
"""
Написать генератор factorial, который возвращает подряд значения факториала

Например:

factorial_gen = factorial()

next(factorial_gen) -> 1
next(factorial_gen) -> 2
next(factorial_gen) -> 6
next(factorial_gen) -> 24
"""
def factorial():
    n = 1000
    a = 1    
    for i in range(1, n+1):
        a *= i
        yield a
    
factorial_gen = factorial()
print(next(factorial_gen))
print(next(factorial_gen))
print(next(factorial_gen))
print(next(factorial_gen))
   

        


