from turtle import *

for angle in range(0, 360, 10):
    setheading(angle)
    forward(100)
    write(str(angle) + '°')
    backward(100)
