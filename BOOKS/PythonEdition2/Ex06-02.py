key = 1
passList = ["236428", "339212", "326224", "818339", "111212"]
while (key > 0) and (key < 4):
    print("เมนูหลัก")
    print("1.ดูข้อมูลคนที่สอบผ่าน")
    print("2.ค้นหาข้อมูลผลสอบ")
    key = int(input("เลือกเมนูที่ต้องการ >>> "))
    if key == 1:
        print(passList)
    if key == 2:
        studentID = input("ป้อนข้อมูลเลขที่ผู้สมัคร >>> ")
        if studentID in passList:
            idx = passList.index(studentID)
            print("คุณสอบได้เป็นลำดับที่", idx + 1)
        else:
            print("คุณสอบไม่ผ่าน เจอกันใหม่รอบหน้า")
