'''
Дан список
['samsung', 'lg', 'xerox', 'bosch']
Удалить элемент с именем 'xerox'
Добавить элемент на 2 место 'indesit'

'''
a = ['samsung', 'lg', 'xerox', 'bosch']
a.remove('xerox')
a.insert(2, 'indesit')
print(a)