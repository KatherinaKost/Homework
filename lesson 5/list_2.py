'''
Запросить по очереди у пользователя 5 имен. Добавить все в список. 
Отсортировать. 
Вывести на экран.
Вывести True при наличии в списке имени 'Вася'
'''
names = [input(f"Введите имя {i+1} ") for i in range (5)]
print (names)
print ("Вася" in names)
