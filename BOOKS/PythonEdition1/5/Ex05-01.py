sales = float(input("ป้อนข้อมูลยอดขายที่นี่ >>> "))
commission = 1.5/100*sales
print("ยอดขายเท่ากับ", "{:,.2f}".format(sales), "บาท")
print("ค่าคอมมิชชั่นเท่ากับ", "{:,.2f}".format(commission), "บาท")
