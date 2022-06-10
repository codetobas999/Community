from turtle import *

title("Turtle Python") 
bgcolor("green") 
screensize(600,800) 

shape("turtle") 
pensize(3) 

s = 0
for c in ['red', 'black', 'yellow', 'blue']: 
    color(c) 
    speed(s + 5)
    forward(90) 
    left(90) 
    stamp()
