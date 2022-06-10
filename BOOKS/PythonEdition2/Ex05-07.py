import random

guess = random.randint(0, 9)
print("เลขที่สุ่มได้คือ", guess)
count = 0
while True:
    data = int(input("ป้อนข้อมูลตัวเลข [0 ถึง 9] ที่ต้องการทาย >>> "))
    if data == guess:
        print('ถูกต้อง')
        break
    else:
        count = count + 1
        if count < 4:
            print("ลองใหม่อีกครั้ง")
        else:
            print("ทายผิดเกิน 3 ครั้ง... จบการทำงาน ...")
            break

