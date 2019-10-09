from End_to_end_App.Shopping_Cart.Vendor_Info import *
from End_to_end_App.Shopping_Cart.Product_Info import *
from End_to_end_App.Shopping_Cart.Account_Info import *
from End_to_end_App.Shopping_Cart.Address_Info import *
from End_to_end_App.Shopping_Cart.Customer import *
from End_to_end_App.Shopping_Cart.Vendor_Ser_Impl import *

if __name__ == '__main__':
    pr = Product(123,'Mobile',12345.56,'AAA',7)
    pr1 = Product(124, 'Mobile12', 12345.56, 'AAA', 7)
    pr2 = Product(125, 'Mobile14', 22345.56, 'BBB', 8)
    pr3 = Product(126, 'Mobile15', 32345.56, 'CCC', 9)
    pr5 = Product(128, 'Mobile17', 54345.56, 'EEE', 30)
    pr6 = Product(129, 'Mobile18', 64345.56, 'FFF', 40)
    pr7 = Product(130, 'Mobile19', 74345.56, 'GGG', 50)

    # print(pr)

    # prod_List = [pr,pr1,pr2,pr3,pr4]
    # Vendor.vendor_ProdList= prod_List
    # adr = Address('Amardeep', 'Balajinagar', 425552, 'MH', 'IND')
    # venadr = Address('GHHHH', 'Ramnagar', 89552, 'MH', 'IND')
    # print(adr,vadr)
    # acc = Account(accn=155672772, atype='Saving', abal=16627772.8)
    # vacc = Account(accn=62777721, atype="Current", abal=76237763.3)
    # print(acc,vacc)
    # v = Vendor(vreg = 178828822,vnm = 'Flipkart',vacc = vacc, vadr = venadr)
    # print(v)
    # v.vendor_ProdList.extend(prod_List)
    # print(v)
    # cust = Customer(cid=125562, cnm="ABCD", caddr=adr, cacc=acc)
    # print(cust)

    vendorservices = VendorSerImpl()
    # vendorservices.add_product(pr7)
    # vendorservices.add_product(pr7)
    # vendorservices.add_product(pr4)
    # a = vendorservices.get_product(125)
    # print(a)
    # b = vendorservices.get_all_products()
    # print(b)
    # print(vendorservices.get_all_products())
    # a=vendorservices.remove_product(127)
    # print(a)

    pr4 = Product(127, 'TV', 42345.56, 'DDEE', 10)

    vendorservices.update_product(pr4)
