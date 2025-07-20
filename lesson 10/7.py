"""
**
задание для самых  любопытных ))

сделать анимацию снежинок елки с выводом в консоль
образец и описание в файле example\elka_animate.py

"""
import random
from random import Random
from rich.console import Console

random = Random()
console = Console()

#елка вне сильный ветер

def c_tree(n):  
    tree = []
    a = 1
    for i in range(n):
        branch = '*' * a
        no_branch = ' '*((n - 1)- i)
        pos = random.randint(0, len(no_branch))
        left = no_branch[:pos]
        right =no_branch[pos:]
        line = f"{left}.o{right}{branch}{right}.o{left}"
        tree.append(line)    
        a += 2 
    return tree
        
import time
while True:
    print("\033[H\033[J", end="")  
    christmas_tree = c_tree(20)
    for line in christmas_tree:
        print(line)
    time.sleep(0.1)         