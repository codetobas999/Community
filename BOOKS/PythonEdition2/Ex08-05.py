try:
    data1 = float(input("ข้อมูลตัวเลขที่ 1 >>> "))
    data2 = float(input("ข้อมูลตัวเลขที่ 2 >>> "))
except ValueError as e:
        print("ไม่สามารถแปลงชนิดข้อมูลได้")
        print("เกิดข้อผิดพลาดของ Type Error >>> ", e)
else:
    print("ข้อมูลคือ", data1, data2, end=" => ")
    print("แปลงชนิดข้อมูลได้สำเร็จ")
    try:
        if data1 > data2:
            data = [data2, data1]
        print("ข้อมูลที่เรียงลำดับแล้วคือ", data)
        print("ข้อมูลได้รับการจัดเรียงลำดับแล้ว")
    except NameError as e:
        print("ไม่สามารถแสดงผลข้อมูลที่เรียงลำดับได้")
        print("เกิดข้อผิดพลาดของ Name Error >>> ", e)
    else:
        data = data1/data2
        print("ผลหารของ", data1, "/", data2, "เท่ากับ", data)
