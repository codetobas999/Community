from turtle import *

bgcolor("white") 
bgpic("python_logo.png")

penup()
setx(-350)
sety(-200)
pendown()
shape("circle")
shapesize(2)
pensize(10)

for red in range(4):
    for green in range(4):
        for blue in range(4):
            pencolor(red / 4.0, green / 4.0, blue / 4.0)
            forward(10)
