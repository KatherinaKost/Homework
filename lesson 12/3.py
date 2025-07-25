"""
в файле hero1 добавить следующий функционал
        - добавить несколько классов других героев унаследовав их от Hero.
        - Каждому герою добавить уникальное свойство-спец.очки (мана, ярость, и т.п. ) и 
                и свойство cо значением урона от спец.атаки.
        - Создать метод атаки special_attack которая возможна только если количество 
                спец.очков более 0.
        - Добавить метод attack который при атаке с вероятностью 25% будет использовать 
                спец.способность героя если у него остались спец.очки. 
                При спец атаке вычитать из очков 1. Если вероятность пришлась на
                остальные 75% - выполнить обычную атаку. Вывести сообщение в консоль 
                о типе и результате атаки.

добавить класс Arena:
        - атрибут warriors - все воины на арене (тип list)
        - магический метод __init__, который принимает необязательный аргумент warriors.
                Если был передан список warriors, та заполняет им атрибут. Если нет, то заполняет
                пустым списком.
        - метод add_warrior, который принимает аргумент warrior и добавляет его к warriors.
                Если данный воин уже есть в списке, то бросить исключение ValueError("Воин уже на арене").
                Если нет, то добавить воина к списку warriors и вывести сообщение на экран
                "{warrior.name} участвует в битве"
        - метод choose_warrior, который не принимает аргументов и возвращает случайного
                воина из warriors
        - метод battle, который не принимает аргументов и симулирует битву. Сперва 
                должна пройти проверка, что воинов на арене больше 1. Если меньше, то бросить
                исключение ValueError("Количество воинов на арене должно быть больше 1").
                Битва продолжается, пока на арене не останется только один воин. Сперва
                в случайном порядке выбираются атакующий и защищающийся. Атакующий ударяет
                защищающегося. Если у защищающегося осталось 0 health_points, то удалить его
                из списка воинов и вывести на экран сообщение "{name} пал в битве".
                Когда останется только один воин, то вывести сообщение "Победил воин: {name}".
                Вернуть данного воина из метода battle.
                
                
Создать несколько воинов используя разные классы, добавить их на арену и запустить битву. 
Выжить должен только один.

"""

