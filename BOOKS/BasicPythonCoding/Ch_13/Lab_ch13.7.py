from turtle import *

lineLen = inc = 10    
max = 200             
      
while lineLen <= max:
    forward(lineLen)
    right (90)
    lineLen += inc
for i in range(20):
    undo()
