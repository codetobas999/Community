result = lambda hour, rate: (hour - 40) * (1.5 * rate)
h = 45
r = 120
print("จำนวนชั่วโมงทำงาน เท่ากับ {:,d} ชั่วโมง".format(h))
print("อัตราค่าแรง เท่ากับ {:,.2f} บาทต่อชั่วโมง".format(r))
print("ค่าแรงรวม เท่ากับ {:,.2f} บาท".format(result(h, r)))
