"""
Дан список пользователей след. формата: 
[{"name":"some_name", "login":"some_login", "password":"some_password" },
 ...
]

Отфильтровать используя функцию filter() список на предмет паролей 
которые менее 5 символов.

*Отфильтровать используя функцию filter() список на предмет валидных логинов. 
Валидный логин должен содержать только латинские буквы, цифры и черту подчеркивания. 
Каждому пользователю с плохим логином вывести текст 
"Уважаемый user_name, ваш логин user_login не является корректным."

"""


def filter_pass(text):
    if len(text['password']) < 5:
        return True
    
def valid_login(text:dict):
    
    if all ((i.isalpha() or i.isdigit() or i == '_') for i in text['login']):
        return True
    else:
        print(f"Уважаемый {text['name']}, ваш логин {text['login']} не является корректным")
    
users = [{'name':'Katya', 'login':'belka2156', 'password':'qwer'},
         {'name':'Oleg', 'login':'oleg!123', 'password':'12345678'},
         {'name':'Violetta', 'login':'vile@b96', 'password':'lebed12'},
         {'name':'Inna', 'login':'inna40', 'password':'0368'}
]   

users_2 = filter(valid_login, users)
users_1 = filter (filter_pass, users)

print('пароль содержит менее 5 символов:',*users_1, sep='\n')
print('Валидный логин ',*users_2, sep='\n')

