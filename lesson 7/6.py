"""
1. Запросить у пользователей имя и отзыв о магазине. 
Программа должна запрашивать данные пока не введено слово "stop". 
Все данные сложить в словарь.
    -распечатать количество отзывов
    -распечатать отдельно имена пользователей
    -распечатать отдельно отзывы

"""
dict_review ={}
while True:
    name = input('имя: ')
    if name  == 'stop':
        break
    review = input('отзыв: ')    
    dict_review[name] = review
 
    
    
print(f' кол-во отзывов - {len(dict_review)}')
for name in dict_review.keys():
    print(f"- {name}")
print("\nОтзывы:")
for review in dict_review.values():
    print(f"- {review}")

