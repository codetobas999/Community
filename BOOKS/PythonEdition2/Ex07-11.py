# from wage import calfirst, calextra, calwage
from wage import *
h = 50
r = 100
print("จำนวนชั่วโมงทำงาน เท่ากับ {:,d} ชั่วโมง".format(h))
print("อัตราค่าแรง เท่ากับ {:,.2f} บาทต่อชั่วโมง".format(r))
print("ค่าแรง 40 ชั่วโมง เท่ากับ {:,.2f} บาท".format(calfirst(r)))
print("ค่าแรงที่เกินจาก 40 ชั่วโมง เท่ากับ {:,.2f} บาท".format(calextra(h, r)))
print("ค่าแรงรวม เท่ากับ {:,.2f} บาท".format(calwage(h, r)))
