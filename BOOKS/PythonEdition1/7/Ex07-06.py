def calwage(hr, rate):
    global total
    total = (40 * rate) + (hr - 40) * (1.5 * rate)

h = 50
r = 100
calwage(h, r)
print("จำนวนชั่วโมงทำงาน เท่ากับ {:,d} ชั่วโมง".format(h))
print("อัตราค่าแรง เท่ากับ {:,.2f} บาทต่อชั่วโมง".format(r))
print("ค่าแรงรวม เท่ากับ {:,.2f} บาท".format(total))
