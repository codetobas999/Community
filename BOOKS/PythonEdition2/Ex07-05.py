def calwage():
    global total
    total = (40 * r) + (h - 40) * (1.5 * r)

h = 50
r = 100
calwage()
print("จำนวนชั่วโมงทำงาน เท่ากับ {:,d} ชั่วโมง".format(h))
print("อัตราค่าแรง เท่ากับ {:,.2f} บาทต่อชั่วโมง".format(r))
print("ค่าแรงรวม เท่ากับ {:,.2f} บาท".format(total))
