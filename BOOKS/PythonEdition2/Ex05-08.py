total = 0
data = 1
msg = ""
while data > 0:
    data = int(input("ป้อนข้อมูลตัวเลข  >>> "))
    if data > 0:
        total += data
        print('ข้อมูลถูกต้อง')
        msg += str(data) + " "
else:
    print("ข้อมูลไม่ถูกต้อง... เป็นค่าลบ ...")
msg = "ผลรวมของ " + msg + " เท่ากับ " + str(total)
print(msg)


