'''
Написать функцию count_char, которая принимает строковое значение,
из которого создает и возвращает словарь, следующего вида:
{'буква': 'количество-вхождений-в-строку'}
Нельзя пользоваться collections.Counter!


'''


def count_char(word:str):
    b = {}
    word = word.lower()
    for letter in word:
        if letter not in b:
            b[letter] = 1
        else:
            b[letter] += 1
    return b

print(count_char('трпаррп'))

