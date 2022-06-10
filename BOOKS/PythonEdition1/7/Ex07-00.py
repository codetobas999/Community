from math import *
from datetime import *


print(factorial(2))
currentdate = date.today()
print(currentdate)
currenttime = datetime.now()
print(currenttime.strftime("%a %d %b, %Y %H:%M:%S"))


# ฟังก์ชัน showvalue1()
def showvalue1():
    print("in showvalue1(), data =", data)


# ฟังก์ชัน showvalue2()
def showvalue2():
    print("in showvalue2(), data =", data)
    showvalue1()    # เรียกฟังก์ชัน showvalue1()


# โปรแกรมหลัก
data = 1
print("in main(), data =", data)
showvalue1()    # เรียกฟังก์ชัน showvalue1()
showvalue2()    # เรียกฟังก์ชัน showvalue2()
print("="*20)


def showdata1():
    global data1
    data1 = 5
    print("in showdata1(), data =", data)
    print("in showdata1(), data1 =", data1)


# ฟังก์ชัน showdata2()
def showdata2():
    print("in showdata2(), data =", data)
    print("in showdata2(), data1 =", data1)
    showdata1()    # เรียกฟังก์ชัน showvalue1()




# โปรแกรมหลัก
data = 1
print("in main(), data =", data)
showdata1()    # เรียกฟังก์ชัน showvalue1()
showdata2()    # เรียกฟังก์ชัน showvalue2()
print("in main(), data1 =", data1)
print("="*20)

# ฟังก์ชัน showdata1()
def showdatas1():
    data1 = 5
    print("in showdata1(), data1 =", data1)
# ฟังก์ชัน showdata2()
def showdatas2():
    data2 = 10
    print("in showdata2(), data2 =", data2)
    showdatas1()    # เรียกฟังก์ชัน showdata1()
# โปรแกรมหลัก
showdatas1()    # เรียกฟังก์ชัน showdata1()
showdatas2()    # เรียกฟังก์ชัน showdata2()
