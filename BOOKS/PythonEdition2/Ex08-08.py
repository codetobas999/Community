data1 = 111
data2 = 2222
try:
    print("ข้อมูลตัวเลขที่ 1 มีจำนวน",  len(data1), "หลัก")
    print("ข้อมูลตัวเลขที่ 2 มีจำนวน",  len(data2), "หลัก")
except TypeError as e:
        print("ไม่สามารถแสดงผลจำนวนหลักของตัวเลขได้")
        print("เกิดข้อผิดพลาดของ Type Error >>> ", e)
finally:
    print("ข้อมูลตัวเลขที่ 1 มีจำนวน",  len(str(data1)), "หลัก")
    print("ข้อมูลตัวเลขที่ 2 มีจำนวน",  len(str(data2)), "หลัก")







