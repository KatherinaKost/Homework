"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
а возвращает список из Yes или No для каждого элемента, 
Yes - если число уже встречалось и No, если нет
[1,2,3,1,4] => [no, no, no, yes, no]

если в списке не все целые числа вернуть False.

"""



def yes_or_no(*n):
    if not all(isinstance(i, int) for i in n):
        return False

    b = []
    c = set()
    for i in n:
        if i in c:
            b.append('Yes')
        else:
            b.append('no')
            c.add(i)
    return b
    

print(yes_or_no(1, 2, 2.5, 2, 3))




    

