'''
Запросить любое число. Заменить каждую цифру этого числа буквой, 
у которой номер в алфавите равен этой цифре. 
Например: 1352=aceb.
'''

num = '1234'
num_list = [int(i) for i in num]
char_list = [chr(96 + i) for i in num_list]
print (f'{num}={''.join(char_list)}')