"""
дан словарь
d = {'one':11, 'two':22, 'hello':'python', True:False}
запросить номер элемента и удалить его из словаря с помощью del.


"""

d = {'one':11, 'two':22, 'hello':'python', True:False}
a = input("Введите номер элемента ")
if a in d:
    del d[a]
print(d)