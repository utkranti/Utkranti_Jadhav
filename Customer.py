from End_to_end_App.Shopping_Cart.Generic import *
from End_to_end_App.Shopping_Cart.Address_Info import *
from End_to_end_App.Shopping_Cart.Account_Info import *

class Customer(Generic):

    def __init__(self,cid,cnm,caddr,cacc):
        self.customerId = cid
        self.customerName = cnm
        self.customerAddress = caddr
        self.customerAccount = cacc

# cust = Customer(cid = 125562,cnm = "ABCD",caddr = adr ,cacc = acc)
# print(cust)