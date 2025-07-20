'''
Добавить несколько черепах 
    - или сразу 
    * или в течении игры по одной через определенное количество кликов
    - на каждой забиндить клик через одну и туже функцию cath

'''
  
import turtle
from turtle import *
from random import randint

screen = turtle.Screen()
screen.colormode(255)

ts = []
count_click = 0
max_click = 3

def new_turtle():
    r = randint(0, 255)
    g = randint(0, 255) 
    b = randint(0, 255)  
    t = Turtle()
    t.color(r, g, b)
    t.speed(1)
    t.shape("turtle")
    t.penup()
    t.goto(0, 0)
    t.pendown()
    ts.append(t)
    click_turtle(t)   
    return t

def click_turtle(t):
    def catch(x,y):
        global count_click
        t.goto(0,0)
        t.right(randint(0,120))               
        count_click += 1    
        if count_click % max_click == 0:
            new_turtle()
    t.onclick(catch)
    

t1 = new_turtle()

while 1:
    for t in ts:
        t.forward(3)
mainloop()