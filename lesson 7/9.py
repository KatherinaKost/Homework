'''
*
В структуре данных из 5 урока задание №2 каждому сотруднику 
добавить к параметру "навык" параметр "мастерство" измеряемый от 0 до 100

Написать программу которая анализирует всю структуру данных и выводит сотрудников
с наибольшим параметром "мастерство" для каждого существующего навыка.
Пример вывода:
    1. Python - Иванов - 98
    2. JS - Петров  - 74     
    3. Базы данных - Николаев - 87     
    ...


** Пример вывода (перед выводам отсортировать по убыванию "мастерства"):
    
    --------------------------------------------------
    | № |   Навык     |       ФИО       | Мастерство |
    ==================================================
    | 1 | Python      | Иванов Н.С.     |     98     |
    | 2 | JS          | Петров В.В.     |     87     |
    | 3 | Базы данных | Николаев Е.Н.   |     74     |
    ...

 

'''

employees = {
    "Ivanov Ivan Ivanovich": {
        "position": "manager",
        "year_of_birth": 1990,
        "skills": [{"Python":{'мастерство':85}}, {"SQL":{'мастерство':90}}],
        "children": [
            {"name": "Sergey Ivanovich", "year_of_birth": 2010},
            {"name": "Maria Ivanovna", "year_of_birth": 2015}
        ]
    },
    "Petrov Petr Petrovich": {
        "position": "engineer",
        "year_of_birth": 1985,
        "skills": [{"Java":{'мастерство':70}}, {"C++":{'мастерство':87}}],
        "children": [
            {"name": "Dmitry Petrovich", "year_of_birth": 2008}
        ]
    },
    "Sidorov Sergey Sidorovich": {
        "position": "HR specialist",
        "year_of_birth": 1995,
        "skills": [{"Recruitment":{'мастерство':87}}],
        "children": []
    }
}

import pandas as pd
from tabulate import tabulate

skills_list = []
a = 1
for surname_full, data in employees.items():
   
    surname = surname_full
    
    
    for skill_dict in data["skills"]:
        for skill_name, skill_data in skill_dict.items():
            skills_list.append(
                (skill_name, surname, skill_data["мастерство"])
            )
    
skills_list.sort(key=lambda x:x[2], reverse=True)
for i in range(len(skills_list)):
    skills_list[i] = (i+1,) + skills_list[i]
headers_list = ["№","Skill", "Name", "mastery"]
print(tabulate(skills_list, headers_list, tablefmt='grid'))

#печатает просто списком 
""" for i, (skill, surname, level) in enumerate(skills_list, 1):
    print(f"{i}. {skill} - {surname} - {level}") """
#Печатает без рамок в табл. форме
""" df = pd.DataFrame(skills_list, columns=headers_list)
print(df) """