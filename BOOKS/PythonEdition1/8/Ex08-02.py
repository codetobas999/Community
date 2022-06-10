try:
    data1 = float(input("ข้อมูลตัวเลขที่ 1 >>> "))
    data2 = float(input("ข้อมูลตัวเลขที่ 2 >>> "))
    print("ข้อมูลคือ", data1, data2, end=" => ")
    print("แปลงชนิดข้อมูลได้สำเร็จ")
except ValueError as e:
        print("ไม่สามารถแปลงชนิดข้อมูลได้")
        print("เกิดข้อผิดพลาดของ Value Error >>> ", e)

