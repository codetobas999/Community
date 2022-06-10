def calwage(hr, rate):
    total = []
    total1 = 40 * rate
    total2 = (hr - 40) * (1.5 * rate)
    total.append(total1)
    total.append(total2)
    total.append(total1+total2)
    return total

h = 50
r = 100
result = calwage(h, r)
result1 = result[0]
result2  = result[1]
result3  = result[2]
print("จำนวนชั่วโมงทำงาน เท่ากับ {:,d} ชั่วโมง".format(h))
print("อัตราค่าแรง เท่ากับ {:,.2f} บาทต่อชั่วโมง".format(r))
print("ค่าแรง 40 ชั่วโมง เท่ากับ {:,.2f} บาท".format(result1))
print("ค่าแรงที่เกินจาก 40 ชั่วโมง เท่ากับ {:,.2f} บาท".format(result2))
print("ค่าแรงรวม เท่ากับ {:,.2f} บาท".format(result3))

