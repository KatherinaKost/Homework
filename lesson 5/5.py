"""
Запросить фразу 
    - вывести на экран количество уникальных символов
    - вывести на экран количество уникальных слов
    -* вывести символ который встречался чаще всего

"""
from collections import Counter
a = input()
b = set(a)
с = a.split()
d = set(с)
e = Counter(a)
f = e.most_common(1)
print(
    f'Исходная фраза -{a}\n'
    f'Количество уникальных символов - {len(b)}\n'
    f'Количество уникальных слов {len(d)}\n'
    f'Часто встречающийся символ {f[0][0]}'
)



