def calhigh(*arg):
    maxlist = []
    i = 1
    for data in arg:
        maxdata = max(data)
        print("ปริมาณน้ำฝนมากที่สุดของข้อมูลชุดที่", i, "เท่ากับ", maxdata, "มิลลิเมตร")
        maxlist.append(maxdata)
        i += 1
    print("ปริมาณน้ำฝนมากที่สุดของข้อมูลทั้งหมดเท่ากับ", max(maxlist), "มิลลิเมตร")

data1 = 500,  850,  650
data2 = 650,  750
calhigh(data1, data2)
data3 = 875, 620
data4 = 925, 875, 930, 890
calhigh(data1, data2, data3, data4)


