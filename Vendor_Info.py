from End_to_end_App.Shopping_Cart.Generic import *
from End_to_end_App.Shopping_Cart.Product_Info import *

class Vendor(Generic):

    def __init__(self,vreg,vnm,vacc,vadr):
        self.vendorRegid = vreg
        self.vendorName = vnm
        self.vendorAccount = vacc
        self.vendorAddress = vadr
        self.vendor_ProdList = []




# v = Vendor(12222,'Flipkart','Saving',344555.7)
# v.vendor_ProdList.extend(['a','b'])
#
# print(v)