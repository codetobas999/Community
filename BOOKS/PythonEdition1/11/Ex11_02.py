from Ex10_01 import Tax

mytax = Tax()
price = 200
ans = mytax.caltax(price)
print("ราคาสินค้าเท่ากับ {0:,.2f} บาท".format(price))
print("อัตราภาษีเท่ากับ {0:,.2f} บาท".format(mytax.taxrate))
print("จำนวนเงินภาษีที่ต้องจ่าย {0:,.2f} บาท".format(ans))
