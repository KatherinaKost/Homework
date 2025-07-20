"""
Создать класс User с атрибутами:

Свойства:
	- name - имя - содержит только буквы русского алфавита 
	- login - логин - может содержать  только латинские буквы цифры и черту подчеркивания быть не менее 6 символов
	- password - пароль - может содержать  только латинские буквы цифры. Обязательные условия: 
                содержит менее шести символов
                содержит строчную букву
                содержит заглавную букву
                содержит число
	- is_blocked - заблокирован
	- subscription_date - дата до какой действует подписка
	- subscription_mode - вид подписки (free, paid)


Методы:
	- bloc - принимает логическое значение и помечает пользователя заблокированным 
	- check_subscr - может принимать аргумент в виде даты. Проверяет действует ли подписка на определенную дату. 
						Если дата не передана значит на дату проверки. 
						Возвращает  действует ли подписка, ее вид и сколько осталось дней.
	- change_pass - смена пароля и присваивание его в качестве действующего. 
						Пароль должен пройти валидацию. 
						Если пароль не был передан сгенерировать по правилам и вывести в консоль.
	- get_info - выводит информацию о пользователе если заблокирован то сообщает об этом.



Создание объекта должно происходить  при передаче обязательных аргументов имя и логин и необязательного - пароль. Логин и пароль должны быть проверен на валидность.
Если пароль в конструктор не был передан он должен сгенерироваться на основании правил, и должен быть выведен на экран(консоль).
При создании пользователя ему предоставляется пробная подписка сроком на 30 дней.
При изменении даты подписки  вид подписки меняется на платный.
Валидацию данных сделать через регулярные выражения
"""

import re
import datetime
import random
import string

class User:
    def __init__(self, name, login, password = None):
        self.name = name
        if not re.fullmatch(r'^[а-яА-ЯёЁ]+$', name):
            raise ValueError("неверное имя")
        self.login = login
        if not re.fullmatch(r'[a-zA-z0-9_]{6,}', login):
           raise ValueError("неверный логин")
        if password is None:
            self.password = self.generate_password()
            print(f"Сгенерированный пароль: {self.password}")
        else:
            if not self.validate_password():
                raise ValueError("Пароль не соответствует условию")
            self.password = password   
        
        self.is_blocked = False
        self.subscription_date = datetime.date.today() + datetime.timedelta(days=30)
        self.subscription_mode = "free" 
        
    def bloc(self, value:bool):
        self.is_blocked = value
    
    def check_subscr(self, date = None):
        if date is None:
            date = datetime.date.today()
        is_active = date <= self.subscription_date
        if is_active:
            days_left = (self.subscription_date - date).days
        else:
            days_left = 0

        return {
            'is_active': is_active,
            'mode': self.subscription_mode,
            'days_left': days_left
        }
    def set_subscription_date(self, new_date):
        self.subscription_date = new_date
        self.subscription_mode = "paid"  
        
    @staticmethod
    def validate_password(password):
        return (len(password) >= 6 and
                re.search(r'[a-z]', password) and  
                re.search(r'[A-Z]', password) and  
                re.search(r'[0-9]', password) and  
                re.fullmatch(r'^[a-zA-Z0-9]+$', password))
    
    def generate_password(self):       
        lower = random.choice(string.ascii_lowercase)
        upper = random.choice(string.ascii_uppercase)
        digit = random.choice(string.digits)        
        remaining = ''.join(random.choices(
            string.ascii_letters + string.digits,
            k=random.randint(3, 10)
        ))
        password = (lower + upper + digit + remaining)
        password = ''.join(random.sample(password, len(password)))    
        return password
    
    def change_pass(self, new_pass=None):
        if new_pass is not None:
            if not self.validate_password(new_pass):
                raise ValueError(
                    "Пароль должен содержать:\n"
                    "- 6+ символов\n"
                    "- латинские буквы (A-Z, a-z)\n"
                    "- хотя бы одну заглавную и строчную букву\n"
                    "- хотя бы одну цифру\n"
                    "- без спецсимволов"
                )
            self.password = new_pass
        else:
            new_pass = self.generate_password()
            print(f"Сгенерирован новый пароль: {new_pass}")
            self.password = new_pass
    
    def get_info(self):
        info = f'Имя {self.name}, логин {self.login}\n'
        if self.is_blocked:
            info += "пользователь заблокирован\n"
        else:
            info += 'пользователь активен\n'
        sub_info = self.check_subscr()
        info += (f"Подписка: {sub_info['mode']}, "
            f"{'активна' if sub_info['is_active'] else 'not_active'}, "
            f"осталось дней: {sub_info['days_left']}\n")
        print(info)
        
user1 = User("Иван", "ivan_123")
user1.get_info()

    
               
               
                              
        
        
        
		
