import random

ran = random.randint(-1,1)
num = int(input("Enter your number [-1, 0, 1]:"))
if ran == num:
    print("You won!")
else:
    print("You lost!")

