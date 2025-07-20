"""

Описать класс Counter, реализующий целочисленный счетчик.
который может увеличивать или уменьшать свое значение (атрибут value)
на единицу в заданном диапазоне.

Предусмотреть инициализацию счетчика значениями по умолчанию и произвольными значениями.

Определить атрибуты(свойства):
    - value - текущее значение счетчика
    ...

Определить методы:
    - инициализатор __init__, который устанавливает значение счетчика или 0 по умолчанию
    - increase(num=1), увеличивает счетчик на заданную величину или 1 по умолчанию
    - decrease(num=1), уменьшает счетчик на заданную величину или 1 по умолчанию
    - reset, сбрасывает значение счетчика на стартовое    
    - метод __iter__
    - метод __next__
    
    * - stat, возвращает среднее количество изменений счетчика в секунду

"""
import time 

class Counter:
    def __init__(self, val = 3, min_val = 0, max_val = 15):
        self.val = val
        self.min_val = min_val
        self.max_val = max_val

    def increase(self, num = 1):
        new_val = self.val + num
        self.val = new_val
        if self.val > self.max_val:
            raise StopIteration
    def decrease(self, num = 1):
        new_val = self.val - num
        self.val = new_val
        if self.val < self.max_val:
            raise StopIteration
    def reset(self, val = 3):
        self.val = val
    def __iter__(self):        
        self.current = self.val
        return self
    def __next__(self):
        if self.current > self.max_val:
            raise StopIteration  
        value = self.current
        self.current += 1
        return value
    
    
a = Counter(3, 1, 10)
for i in a:
    print(i)  
a.increase(3)
for i in a:
    print(i)



           
