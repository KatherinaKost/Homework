"""
Создать класс BookCard, в классе должны быть:

- private атрибут author - автор (тип str)
- private атрибут title - название книги (тип str)
- private атрибут year - год издания (тип int)
- магический метод __init__, который принимает author, title, year
- магические методы сравнения для сортировки книг по году издания
- сеттеры и геттеры к атрибутам author, title (len<50), year. В сеттерах сделать проверку
  на тип данных, если тип данных не подходит, то бросить ValueError. Для года
  издания дополнительно проверить на валидность (> 0, <= текущего года).

Аксессоры реализоваться через property.
"""

from datetime import date
CURRENT_YEAR = date.today().year

class BookCard:
   
    def __init__(self,  author, title, year):
        self.author = author
        self.title = title
        self.year = year
    
             
    def __le__(self, other):
        return self.year <= other.year

    def __eq__(self, other):
        return self.year == other.year

    def __ne__(self, other):
        return self.year != other.year

    def __gt__(self, other):
        return self.year > other.year

    def __ge__(self, other):
        return self.year >= other.year
        
    @property
    def author(self):
        return self.__author
    @author.setter
    def author(self, value: str):
      if not isinstance(value, str):
          raise ValueError("Тип данных должен быть str")
      self.__author = value   
    
    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, value: str):
      if not isinstance(value, str) or len(value) >= 50:
          raise ValueError("Неверные данные")
      self.__title = value   
    
    @property
    def year(self):
        return self.__year
    @year.setter
    def year(self, value: int):
        if not isinstance(value, int):
            raise ValueError("Год должен быть целым числом")
        if not (0 < value <= CURRENT_YEAR):
            raise ValueError(f"Год должен быть от 1 до {CURRENT_YEAR}")
        self.__year = value 

books =[
    BookCard('Франсуа Мориак', 'Тереза Дескейру', 1927),
    BookCard('Ульям Коллинз', 'Мертвая комната', 1856),
    BookCard('Федор Михайлович Достоевский', 'Униженные и оскорбленные', 1861)    
]

book_sort =sorted(books)
for book in book_sort:
    print(f'{book.author} {book.title} {book.year}')

   
      
      

