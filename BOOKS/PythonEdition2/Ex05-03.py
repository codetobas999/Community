a = int(input("ป้อนข้อมูล a >>> "))
b = int(input("ป้อนข้อมูล b >>> "))
if a < b:
    print(a, "น้อยกว่า", b)
else:
    temp = a
    a = b
    b = temp
    print(a, "และ", b, "สลับค่ากันแล้ว")
print(a, ",", b)


