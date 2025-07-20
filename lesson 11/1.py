"""
Создать класс Phone, у которого будут следующие атрибуты:

Определить атрибуты:

- brand - бренд
- model - модель
- issue_year - год выпуска

Определить методы:

- инициализатор __init__
- receive_call, который принимает имя звонящего и выводит на экран: 
        <Бренд-Модель> - Звонит {name}
- get_info, который будет возвращать кортеж (brand, model, issue_year)
- метод __str__, который выводит на экран информацию об устройстве:
Бренд: {}
Модель: {}
Год выпуска: {}

"""

class Phone:
        def __init__(self, brand, model, issue_year):
                self.brand = brand
                self.model = model
                self.issue_year = issue_year
        
        def receive_call(self, name) -> tuple:
                print (f'{self.brand}-{self.model} - звонит {name}')

        def get_info(self):
                return self.brand, self.model, self.issue_year
        
        def __str__(self):
                return f'Бренд: {phone1.brand}\nМодель: {phone1.model}\nГод выпуска: {phone1.issue_year}'
        
phone1 = Phone('iPhone', '13', 2021)

phone1.receive_call('Катя')
print(*phone1.get_info())
print(str(phone1))        

        