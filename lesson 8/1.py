"""
Написать функцию  которая принимает фамилию имя и отчество одной стройкой, 
а возвращает в виде краткого формата. 
Функция должна содержать необязательный параметр в виде логического значения 
и в зависимости от него возвращала ФИО в двух следующих форматах:
 -  Николаев И.С. 
 -  И.С.Николаев


"""



def short_name(text:str,revers=False):
    format_name = text.split()
   
    if (len(format_name)) != 3:
        raise ValueError("Должны быть только фамилия, имя и отчество!")

    if revers != True:
        return f'{format_name[0]} {format_name[1][0]}. {format_name[2][0]}.'
    else:
        return f'{format_name[0][0]}. {format_name[1][0]}. {format_name[2]}'
    
print(short_name('Иванов Иван Иванович'))
print(short_name('Иван Иванович Иванов', True))



