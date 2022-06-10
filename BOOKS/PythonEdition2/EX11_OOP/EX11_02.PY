from Ex11_01 import Tax

price = 200
ans = Tax.caltax(price)
print("ราคาสินค้าเท่ากับ {0:,.2f} บาท".format(price))
print("อัตราภาษีเท่ากับ {0:,.2f} บาท".format(Tax.taxrate))
print("จำนวนเงินภาษีที่ต้องจ่าย {0:,.2f} บาท".format(ans))
