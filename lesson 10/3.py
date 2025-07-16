"""
Написать функцию которая принимает строку в которой есть 
круглые скобки и возвращает True или False анализируя все ли скобки 
являются закрытыми и расставлены в правильном порядке.
Примеры:
    (()()) -> True
    (()()() -> False
    (hello(2)ver()(33)python) -> True
    (hello(2()ver(33)python)) -> True
    (hello(2()ver(33)python) -> False

"""
def check():
    counter = 0  

    def check_count(s):
        nonlocal counter
        for char in s:
            if char == '(':
                counter += 1
            elif char == ')':
                counter -= 1
                if counter < 0:
                    return False
        result = (counter == 0)
        return result

    return check_count
a = check()
print(a('(()()()'))