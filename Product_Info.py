from End_to_end_App.Shopping_Cart.Generic import *

class Product(Generic):

    def __init__(self,pid,pnm,pprice,pcat,pqty):
        self.productId = pid
        self.productName = pnm
        self.productPrice = pprice
        self.productCategory = pcat
        self.productQuantity = pqty


# p1 = Product(123,'Mobile',12345.56,'AAA',7)
# p2 = Product(124,'Laptop',54666.6,'BBB',12)
# p3 = Product(125,'Fridge',24899,'CCC',8)
#
# prod_list = [p1,p2,p3]
# print(prod_list)

