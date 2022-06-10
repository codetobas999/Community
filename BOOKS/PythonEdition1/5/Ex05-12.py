count = 1
while count <= 5:
    score = float(input("คะแนนสอบของนิสิตคนที่ " + str(count) + "  >>> "))
    if score < 0 or score > 100:
        print("ข้อมูลคะแนนไม่ถูกต้อง")
        continue
    print("ข้อมูลคะแนนถูกต้อง")
    count += 1


