'''
Дан список содержащий в себе различные типы данных, отфильтровать таким
образом, чтобы 
 - остались только строки.
 - остался только логический тип.
 
'''
a = [1, 'w', False, 23, [1,2], True, 'qwerty']



data_str = list(filter(lambda x: isinstance(x, str), a))
data_bool = list(filter(lambda x: isinstance(x, bool), a))
print(*data_str)
print(*data_bool)



#если одновременно надо вывести
""" def filtr_list(text):
    if isinstance(text,(bool, str)):
        return True """
    

