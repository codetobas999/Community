loginList = "87654321"
checkList = loginList[0:len(loginList):2]
check = False
while not check:
    password = input("ป้อนข้อมูลรหัสผ่าน >>> ")
    if password == checkList:
        print("เข้าสู่ระบบสำเร็จ")
        break
    else:
        print("ข้อมูลไม่ถูกต้อง ลองใหม่อีกครั้ง")
