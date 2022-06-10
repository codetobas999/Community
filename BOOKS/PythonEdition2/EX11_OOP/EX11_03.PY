class Tax:
    taxrate = 0.07

    def __init__(self, productprice, taxrate=None):
        self.productprice = productprice
        if taxrate is None:
            self.taxrate = Tax.taxrate
        else:
            self.taxrate = taxrate

    def caltax(self):
        return self.taxrate * self.productprice

price = 200
mytax1 = Tax(price)
ans1 = mytax1.caltax()
print("ราคาสินค้าเท่ากับ {0:,.2f} บาท".format(price))
print("อัตราภาษีเท่ากับ {0:,.2f} บาท".format(mytax1.taxrate))
print("จำนวนเงินภาษีที่ต้องจ่าย {0:,.2f} บาท".format(ans1))

newrate = 0.05
mytax2 = Tax(price, newrate)
ans2 = mytax2.caltax()
print("อัตราภาษีใหม่เท่ากับ {0:,.2f} บาท".format(mytax2.taxrate))
print("จำนวนเงินภาษีที่ต้องจ่าย {0:,.2f} บาท".format(ans2))

