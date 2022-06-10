class Tax:
    taxrate = 0.07

    def __init__(self, productprice):
        self.productprice = productprice
        self.taxrate = Tax.taxrate

    def caltax(self):
        return self.taxrate * self.productprice

    def caltotal(self, tax):
        return self.productprice + tax

price = 200
mytax = Tax(price)
ans1 = mytax.caltax()
ans2 = mytax.caltotal(ans1)
print("ราคาสินค้าเท่ากับ {0:,.2f} บาท".format(price))
print("อัตราภาษีเท่ากับ {0:,.2f} บาท".format(mytax.taxrate))
print("จำนวนเงินภาษีที่ต้องจ่าย {0:,.2f} บาท".format(ans1))
print("จำนวนเงินรวมที่ต้องจ่าย {0:,.2f} บาท".format(ans2))


