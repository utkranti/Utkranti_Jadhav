from End_to_end_App.Shopping_Cart.Generic import *

class Account(Generic):

    def __init__(self,accn,atype,abal):
        self.accountNumber = accn
        self.accountType = atype
        self.accountBalance = abal

acc = Account(accn = 155672772,atype = 'Saving',abal = 16627772.8)

vacc = Account(accn=62777721,atype="Current",abal=76237763.3)