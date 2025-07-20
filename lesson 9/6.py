"""
Дан словарь наблюдения за температурой 
{"day1":18, "day2":22, "day3":7, "day4":11, "day5":14}. 
Отсортировать словарь по температуре в порядке возрастания и обратно.

"""
a = {"day1":18, "day2":22, "day3":7, "day4":11, "day5":14}

a_sort1 = dict(sorted(a.items(), key = lambda item:item[1]))
a_sort2 = dict(sorted(a.items(), key = lambda item:item[1], reverse = True))

print(a_sort1, a_sort2, sep= '\n')
