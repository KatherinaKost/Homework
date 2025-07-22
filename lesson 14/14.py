"""
Используя класс из пред.урока обеспечить хранение и сохранение любых изменений в базе 
данных. Для этого можно к примеру добавить в класс метод save который будет сохранять или 
создавать пользователя в базе данных и использовать его при любых изменениях.


* в базе данных создать таблицу предоставляемых услуг со след полями
	название
	тип (1 - платная 0 - бесплатная)
	стоимость 
	период в днях
** в класс пользователя добавить методы:
	добавить услугу (услуг у одного пользователя может быть несколько)
	продлить услугу (продлить можно если услуга еще не закончена, иначе добавить)
	удалить услугу
*** создать консольное или оконное приложение которое показывает меню и отрабатывает выбранный пункт.
	Меню:
		1 - показать пользователей
		2 - информация о пользователе (в т.ч. и подключенные услуги)
		3 - список услуг		
		4 - показать пользователей с определенной услугой
		5 - показать пользователей у которых за прошедший месяц окончился период хоть одной услуги 
 
	
 
"""

import sqlite3

con = sqlite3.connect('E:\\projects_py\\Homework\\lesson 14\\users.db')
cur = con.cursor()

sql =\
"""CREATE TABLE IF NOT EXISTS users(
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         name TEXT,
         login TEXT,
         is_blocked BOOLEAN,
         subscription_date TEXT,
         subscription_mode TEXT);
"""
cur.execute(sql)
con.commit()
con.close()


import re
import datetime
import random
import string

class User:

    def __init__(self, name, login, password = None, user_id = None):
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
        self.id = user_id   
        self.is_blocked = False
        self.subscription_date = datetime.date.today() + datetime.timedelta(days=30)
        self.subscription_mode = "free" 
        
    def bloc(self, value:bool):
        self.is_blocked = value
        self.save()
    
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
        self.save()

    def save(self):
        con = sqlite3.connect(r'E:\projects_py\Homework\lesson 14\users.db')
        cur = con.cursor()
        if self.id is None:   
            sql =\
            """INSERT INTO users (
            name, 
            login, 
            is_blocked, 
            subscription_date, 
            subscription_mode)  VALUES (?,?,?,?,?)
            """
            cur.execute(
                sql,[self.name, self.login, self.is_blocked, self.subscription_date,
                self.subscription_mode]
            )
            self.id = cur.lastrowid
        else:
            sql =\
            """UPDATE users SET name = ?, login = ?, is_blocked = ?, 
            subscription_date = ?, subscription_mode =?
            WHERE id = ?
            """
            cur.execute(sql,(self.name, self.login, self.is_blocked, self.subscription_date,
                self.subscription_mode, self.id))
            
        con.commit()
        con.close()

    

        
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



def check_login(login):
    con = sqlite3.connect(r'E:\projects_py\Homework\lesson 14\users.db')
    cur = con.cursor()
    cur.execute("SELECT 1 FROM users WHERE login = ?", (login,))
    result = cur.fetchone()
    con.close()
    return result is not None 


        
user1 = User("Иван", "ivan_123")
if not check_login(user1.login):
    user1.save()
    print("Пользователь создан")
else:
    print(f"пользователь с логином {user1.login} существует")


user1.save()
#user1.get_info()
