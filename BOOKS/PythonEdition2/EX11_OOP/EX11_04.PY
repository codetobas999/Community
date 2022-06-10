class Tax:
    taxrate = 0.07

    def __init__(self):
        pass

    @staticmethod
    def caltax(productprice):
        return Tax.taxrate * productprice

price = 200
ans = Tax.caltax(price)
print("ราคาสินค้าเท่ากับ {0:,.2f} บาท".format(price))
print("อัตราภาษีเท่ากับ {0:,.2f} บาท".format(Tax.taxrate))
print("จำนวนเงินภาษีที่ต้องจ่าย {0:,.2f} บาท".format(ans))
