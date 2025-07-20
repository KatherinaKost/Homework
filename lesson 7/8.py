"""
*
Написать программу калькулятор которая предлагает 
ввести пример для решения пока пользователь не введет команду "стоп"
Программа должна решить пример и запросить следующий.
При вводе команды "стоп" программа завершается.
Поддерживаемые операции: + - * ** /
Пример:
    Введите пример или 'стоп' для завершения: 2 + 2
    Ответ: 4
    Введите пример или 'стоп' для завершения: 16 / 8
    Ответ: 2
    Введите пример или 'стоп' для завершения: 1651+
    Неправильный формат. Пример: '2 + 4'

"""
while True:
    
    a = input("Введите пример или 'стоп' для завершения: ").lower().strip()
    if a == 'стоп':
        print("работа окончена")
        break
    
    try:
        if '+' in a:
            list1 = a.split('+')
            list1 = [float(i) for i in list1]
            print('ответ:', sum(list1))

        elif '-' in a:
                list1 = a.split('-')
                list1 = [float(i) for i in list1]
                print ('ответ:', list1[0]-list1[1])
        elif '*' in a:
            list1 = a.split('*')
            list1 = [float(i) for i in list1]
            print ('ответ:', list1[0]*list1[1])

        elif '**' in a:
            list1 = a.split('**')
            list1 = [float(i) for i in list1]
            print('ответ:', list1[0]**list1[1])

     
        elif '/' in a:
            list1 = a.split('/')
            list1 = [float(i) for i in list1]
            print (list1[0]/list1[1])
    except ZeroDivisionError:
        print("Ошибка: деление на ноль запрещено")
    except ValueError:
        print("Ошибка: неправильный формат числа. Пример: '2+3'")
    except Exception as e:
        print(f"Произошла ошибка: {e}")   

    




