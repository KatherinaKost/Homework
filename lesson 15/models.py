from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Float
from sqlalchemy.orm import relationship, DeclarativeBase
import re
import datetime
import random
import string


class Base (DeclarativeBase):
    pass
    


class UserDB(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    login = Column(String(50), nullable=False, unique=True)
    is_blocked = Column(Boolean, nullable=False)
    #subscription_mode = Column(String, nullable=False)
    subscription_date = Column(String)
    services = relationship('Service', back_populates='user')


    def __init__(self, name, login, password = None, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        if not re.fullmatch(r'^[а-яА-ЯёЁ]+$', name):
            raise ValueError("неверное имя")
        self.login = login
        if not re.fullmatch(r'[a-zA-z0-9_]{6,}', login):
           raise ValueError("неверный логин")
        if password is None:
            self.password = self.generate_password()
            #print(f"Сгенерированный пароль: {self.password}")
        else:
            if not self.validate_password():
                raise ValueError("Пароль не соответствует условию")
            self.password = password   
        
        self.start_date = datetime.now()

    def bloc(self, value:bool):
        self.is_blocked = value
    
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

class Service(Base):
    __tablename__ = 'services'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    type = Column(Boolean,nullable=False)
    cost = Column(Float)
    period_days = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('UserDB', back_populates='services')

    def __init__(self, title:str, type:bool, cost:float = None, period_days:int = 30, **kw):
        super().__init__(**kw)
        self.title = title
        self.type = type
        self.cost = cost if type else None
        self.period_days = period_days
        self.start_date = datetime.now()
        self.end_data = self.start_date +datetime.timedelta(days=period_days)

    def extend_time(self, val):
        if self.end_data < datetime.now():
            raise ValueError("услуга истекла")
        self.end_data += datetime.timedelta(days=val)

 


def add_data(engine, db):
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    users = [
        UserDB(name = 'Катя', login =  "Kat_1236"),  
        UserDB(name = 'Петя', login = 'Petr123')      
    ]
    servisec =[
        Service(title = "type1", type=False, period_days=15, user=users[0]),
        Service(title = "type1", type=True, cost = 123, period_days=30, user=users[1])
    ]      
    db.add_all(users+servisec)
    db.commit()
