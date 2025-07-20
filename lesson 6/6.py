"""
Даны 4 переменные - a1, a2, a3, a4.
1 - вывести True если все они дробные числа
2 - вывести True если одна из них строка
3 - вывести True если  одна пара переменных является целочисленным типом. 
    Пары могут образовать только следующие переменные - a1-a3, a2-a4, a3-a4"
"""
a1, a2, a3, a4 = 1, 2, 3, 4
a = [a1, a2, a3, a4]
print (all(isinstance(i, float) for i in a))
print (any(isinstance(i, str) for i in a))
b = [(a1, a3), (a2, a3), (a3,a4)]
print (any((isinstance(i, int) for i in x) for x in b))
