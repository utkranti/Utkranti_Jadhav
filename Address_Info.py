from End_to_end_App.Shopping_Cart.Generic import *

class Address(Generic):

    def __init__(self,soc,area,pin,stat,coun):
        self.addressArea = area
        self.addressSoc = soc
        self.addressPin = pin
        self.addressState = stat
        self.addressCountry = coun

adr = Address('Amardeep','Balajinagar',425552,'MH','IND')
vadr = Address('GHHHH','Ramnagar',89552,'MH','IND')
