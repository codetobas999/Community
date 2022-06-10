class Tax:
    taxrate = 0.07

    @staticmethod
    def caltax(productprice):
        return Tax.taxrate * productprice
