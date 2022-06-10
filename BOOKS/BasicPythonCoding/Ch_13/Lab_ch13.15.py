from turtle import *
 
bgcolor("black")
colors=["blue","purple","red","yellow","orange","brown"]
tracer(1, 25)
 
for x in range(300):
    color(colors[x%6])
    forward(x)
    left(59)
 
exitonclick()

