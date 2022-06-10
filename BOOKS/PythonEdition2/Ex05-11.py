while True:
    ch = input("ป้อนข้อมูลตัวอักขระ  >>> ")
    if 'a' <= ch <= 'z':
        print(ch,  "เป็นตัวอักษรในภาษาอังกฤษ")
    elif 'A' <= ch <= 'Z':
        print(ch,  "เป็นตัวอักษรในภาษาอังกฤษ")
    else:
        print(ch,  "ไม่ใช่ตัวอักษรในภาษาอังกฤษ")
        break
