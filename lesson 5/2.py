"""
2. Создать структуру данных сотрудников фирмы с 
    тремя сотрудниками. каждый сотрудник должен иметь:
        ФИО, 
        должность, 
        год рождения, 
        список навыков, 
        список детей с их именем и годом рождения. 
    
    Запросить ФИО сотрудника и вывести по нему информацию.
"""
import pprint
employees = {
    "Ivanov Ivan Ivanovich": {
        "position": "manager",
        "year_of_birth": 1990,
        "skills": [{"Python":{'навык':85}}, {"SQL":{'навык':90}}],
        "children": [
            {"name": "Sergey Ivanovich", "year_of_birth": 2010},
            {"name": "Maria Ivanovna", "year_of_birth": 2015}
        ]
    },
    "Petrov Petr Petrovich": {
        "position": "engineer",
        "year_of_birth": 1985,
        "skills": [{"Java":{'навык':70}}, {"C++":{'навык':87}}],
        "children": [
            {"name": "Dmitry Petrovich", "year_of_birth": 2008}
        ]
    },
    "Sidorov Sergey Sidorovich": {
        "position": "HR specialist",
        "year_of_birth": 1995,
        "skills": [{"Recruitment":{'навык':87}}],
        "children": []
    }
}
name = input('Введите фио: ')
if name in employees:
    pprint.pprint(employees[name])