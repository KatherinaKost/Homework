"""
Написать функцию (без регулярных выражений), которая принимает текстовую строку 
и возвращает словарь, который содержит информацию о количестве 
символов, слов, строк и предложений в тексте. 
Затем создайте вторую функцию, которая принимает этот словарь, 
и выводит его содержимое в удобном и красивом формате. 

"""


def text_inform(text)->dict:
    keys_text = ['Кол-во символов', 'Кол-во слов', 'Кол-во строк', 'Кол-во предложений']
    normal_text = [part.strip() for part in text.replace('!', '.').replace('?', '.').split('.') if part.strip()]
    values_text = [len(list(text)), len(text.split()), text.count('\n') + 1,len(normal_text)]
    inform = {keys_text:values_text for keys_text, values_text in zip(keys_text, values_text)}
    return inform

def inform_print(inform_dict):
    for key in inform_dict:
        print(key, inform_dict[key])
    
    

inform_print(text_inform('''Предложение 1!
                         предложение 2.
                         предложение 3?
                         предложение 4.'''
))


    

                  

           
