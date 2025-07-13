"""
Создать класс Student.


Определить атрибуты:
    - surname - фамилия
    - name - имя
    - group - номер группы
    - grads - список оценок

Определить методы:
    - инициализатор __init__
    - Методы __eq__, __ne__, __lt__, __gt__, __le__, __ge__, которые будут сравнивать
    студентов по среднему баллу
    - метод add_grade - добавляет в список оценок одну или несколько оценок от 1 до 10
    - метод average_grade -считает и возвращает среднюю оценку ученика

Создать список из 5 студентов класса и вывести его отсортированным по возрастанию
и убыванию.

Вывести студентов, у которых средний балл больше 8
"""

class Student:
    def __init__(self, surname, name, group):
        self.surname = surname
        self.name = name
        self.group = group
        self.grads = []

    def add_grade(self, *grades):
        for grade in grades:
            if 1 <= grade <= 10:
                self.grads.append(grade)
            else:
                raise ValueError
        
    
    def __len__(self):
        len(self.grads)

    def average_grade(self):
        aver_marks = sum(self.grads)/len(self.grads)
        return aver_marks
    
    
    
    def __eq__(self, other_obj):
        return self.average_grade() == other_obj.average_grade()
    def __ne__(self, other_obj):
        return self.average_grade() != other_obj.average_grade()
    def __lt__(self, other_obj):
        return self.average_grade() < other_obj.average_grade()
    def __le__(self, other_obj):
        return self.average_grade() <= other_obj.average_grade()
    def __gt__(self, other_obj):
        return self.average_grade() > other_obj.average_grade()
    def __ge__(self, other_obj):
        return self.average_grade() >= other_obj.average_grade()
    
    def __str__(self):
        avg = self.average_grade()
        return f"{self.surname} {self.name}, группа {self.group}, средний балл: {avg:.2f}"
    


    
student1 = Student("Петров", "Петр", 141)
student2 = Student("Иванов", "Иван", 151)
student3 = Student("Сидоров", "Константин", 171)
student4 = Student("Иванович", "Олег", 141)
student5 = Student("Тикоцкий", "Федор", 151)

student1.add_grade(6, 8, 9, 10, 7, 6)
student2.add_grade(6, 8, 6, 5, 8, 6)
student3.add_grade(6, 7, 6, 8, 5, 4)
student4.add_grade(10, 9, 10, 10, 10, 9)
student5.add_grade(5, 7, 7, 6, 7, 6)

students = [student1, student2, student3, student4, student5]
students_sort = sorted(students, reverse=True)
print(*students_sort, sep='\n')
#Сортировка по имени
#sorted_name = sorted(students, key=lambda s: s.surname)
#print(*sorted_name, sep='\n')
print('Студенты со средним баллом больше 8:')
print(*(s for s in students if s.average_grade() > 8))





