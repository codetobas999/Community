class Tax:
    taxrate = 0.07

    def caltax(self, productprice):
        return Tax.taxrate * productprice
