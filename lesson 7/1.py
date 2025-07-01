"""
Запросить у учителя оценки ученика по одной до тех пор пока он не введет 0. 
Выдать средний бал ученика.
"""

mark = int(input('Введите оценку: '))
marks = []
while mark != 0:
    marks.append(mark)
    mark = int(input('Введите оценку: '))
    if mark == 0:
        break
    
print(f'Средний бал {sum(marks)/len(marks)}')
    
