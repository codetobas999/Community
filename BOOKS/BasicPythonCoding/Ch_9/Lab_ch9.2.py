import random

num = random.randint(1, 3)
c = int(input("ป้อนตัวเลขของคุณ = "))
if (c == num):
    print("คุณชนะ")
if (c != num):
    print("คอมชนะ")
