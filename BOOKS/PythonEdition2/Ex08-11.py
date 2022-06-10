booklist = [111122, 222128, 222115]
bookname = {111122:"Technology for Life", 222128:"Good Mood Good Health", 222115:"Food for Health"}
try:
    for i in range(0, len(booklist)+1):
        print("รหัสหนังสือเล่มที่", (i+1), "คือ",  booklist[i])
except IndexError as e:
        print("ไม่สามารถแสดงผลข้อมูลรหัสหนังสือเล่มตัวที่", (i+1))
        print("เกิดข้อผิดพลาดของ Index Error >>> ", e)
finally:
    try:
        data = int(input("ป้อนข้อมูลรหัสหนังสือที่ต้องการค้นหา >>> "))
        print("ชื่อหนังสือที่ต้องการค้นหาคือ", bookname[data])
    except KeyError as e:
        print("ไม่สามารถแสดงผลข้อมูลรหัสหนังสือที่ต้องการค้นหา", data)
        print("เกิดข้อผิดพลาดของ Key Error >>> ", e)
