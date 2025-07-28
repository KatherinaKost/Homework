from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import add_data, UserDB, Service


# engine = create_engine('E:\\projects_py\\Homework\\lesson 15\\users.db', echo=True)
engine = create_engine('sqlite:///test2.db')
with Session(autoflush=False, bind=engine) as db:
    add_data(engine, db)