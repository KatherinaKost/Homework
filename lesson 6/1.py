"""
Запросить у пользователя год рождения и в соответствии с его возрастом 
охарактеризовать пользователя - 
ребенок, подросток, юноша, в расцвете сил, пожилой, старик.
"""
import time

c_time = time.localtime()
c_year = c_time.tm_year

year = input('Введите год рождения')
age = c_year - int(year)

if 0 >= int(age) < 14:
    print("ребенок")
elif 14 >= int(age) < 18:
    print("подросток")
elif 18 <= int(age) < 25:
    print("юноша")
elif 25 <= int(age) < 55:
    print ("в расцвете сил")
elif 55 <= int(age) < 70:
    print ("пожилой")
else:
    print("старик")   


'''
print ("Ребенок" if 0 >= a < 14 else
       "Подросток" if 14 >= a < 18 else
       "Юноша" if 18 <= a < 25 else
       "в расцвете сил" if 25 <= a < 55 else
       "пожилой" if 55 <= a < 70 else "Старик"
)
'''
