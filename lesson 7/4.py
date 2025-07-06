'''
Запросить высоту елочки - число от 3 до 20. 
Напечатать на экране елочку где ее высота равна числу строк. 
Пример елочки из 4 строк:
   *
  ***
 *****
*******



* - елочка со снегом
'''
import random

n = 20
a = 1
for i in range(n):
   branch = '*' * a
   no_branch = ' '*((n - 1)- i)
   start_position = random.randint(0, len(no_branch))
   real_branch = no_branch[:start_position] + '.' + no_branch[start_position:] + branch + no_branch[:start_position] + '.'
   print(real_branch)
   a += 2


  