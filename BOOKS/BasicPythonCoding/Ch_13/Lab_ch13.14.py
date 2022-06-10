from turtle import *

bgcolor("black")
color("orange")
pensize(5)
 
def DrawCircle(x, y):
     circle(60)

def DrawGoto(x,y):
    goto(x,y)
 
onclick(DrawCircle)
ondrag(DrawGoto)
