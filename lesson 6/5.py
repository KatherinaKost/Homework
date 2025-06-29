'''
Запросить число от 1 до 12. 
Если ввели другое число сообщить об ошибке. 
Если ввели не число сообщить об ошибке. 
Когда введут допустимое число - вывести на экран соответствующее 
название месяца, пору года и сколько дней в данном месяце.

'''
import calendar
from datetime import datetime

a = input()

if not a.isdigit():
    print("Ошибка: введите целое число")
    exit()

a = int(a)

if 1 <= a <= 12:
    print(calendar.month_name[a])
    print(calendar.monthrange(datetime.now().year, a)[1])
    print('winter' if a in [12, 1, 2] else
          'spring' if a in [3, 4, 5] else
          'summer' if a in [6, 7, 8] else 'autumn')
else:
    print('Error')



