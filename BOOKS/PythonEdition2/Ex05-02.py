key = int(input("ต้องการคำนวณคะแนนร้อยละ กด 1 >>> "))
if key == 1:
    score = float(input("ป้อนข้อมูลคะแนนที่นี่ >>> "))
    percent = score/35*100
    print("คะแนนเท่ากับ %.1f คะแนน\nคิดเป็น %.1f%%" %
          (score, percent))
print("แล้วเจอกันใหม่!")


