userList = ("admin;2468", "admin;7531")
uList = []
pList = []
for i in range(0, len(userList)):
    data = userList[i].split(";")
    uList.append(data[0])
    pList.append(data[1])
while True:
    username = input("ป้อนข้อมูลชื่อผู้ใช้ >>> ")
    password = input("ป้อนข้อมูลรหัสผ่าน >>> ")
    data = username+";"+password
    if data in userList:
        print("เข้าสู่ระบบสำเร็จ")
        break
    else:
        if username in uList:
            print("รหัสผ่านไม่ถูกต้อง ลองใหม่อีกครั้ง")
        elif password in pList:
            print("ชื่อผู้ใช้ไม่ถูกต้อง ลองใหม่อีกครั้ง")
        else:
            print("ข้อมูลไม่ถูกต้อง ลองใหม่อีกครั้ง")
