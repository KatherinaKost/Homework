'''

Дан списк:
['qwertyu','asdfggh','zxcvbnm','yuiop[]','hjklasd','mnbvnbv']
Для каждого элемента в списке 
    - вывести на экран сначала номер элемента 
    - сам элемент 
    - символ данного элемента, соответствующий номеру его позиции в списке. 
Образец:
1 - qwertyu - q
2 - asdfggh - s
3 - zxcvbnm - c
и так далее...


'''
list1 = ['qwertyu','asdfggh','zxcvbnm','yuiop[]','hjklasd','mnbvnbv']
a = 1
for i in list1:
    print(f'{a} - {i} - {i[a-1]}')
    a+=1