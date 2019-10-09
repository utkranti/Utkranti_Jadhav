from End_to_end_App.Shopping_Cart.Product_Info import *
from End_to_end_App.Shopping_Cart.Vendor_Ser_Info import *
from End_to_end_App.Shopping_Cart.Vendor_DAO_Impl import *

class VendorSerImpl(Vendor_Service):

    dao = None
    def __init__(self):
        VendorSerImpl.dao = VendorDAOImpl()

    def add_product(self,prodlist):
        if type(prodlist) == list:
            for prod in prodlist:
                self.product_add(prod)
        else:
            self.product_add(prodlist)

    def product_add(self,prod):

        if type(prod) == Product:
            if prod.productId > 0:
                if prod.productPrice >= 500:
                    if prod.productQuantity > 0:
                        if self.get_product(prod.productId):
                            print('Duplicate product...!')
                        else:
                            VendorSerImpl.dao.insert_product(prod)
                            print('Product saved successfully.....!')
                    else:
                        print('Invalid product quantity...!')
                else:
                    print('Invalid product price...!')
            else:
                print('Invalid product id...!')
        else:
            print('Invalid product... cannot proceed...!')

    def get_product(self,pid):
        if pid > 0:
            row = VendorSerImpl.dao.fetch_product(pid)
            return self.convert_rows_to_products(row)
            #     print(self.convert_rows_to_products(row))
        #     print(row)
        else:
            print('invalid product id....!')

    def update_product(self,prod):

        if type(prod) == Product:
            if prod.productQuantity > 1:
                if prod.productPrice >= 500:
                    if self.get_product(prod.productId):
                        VendorSerImpl.dao.modify_product(prod)
                    else:
                        print('Duplicate product...Cannot insert again...!!!!')
                else:
                    print('Invalid product price...!')
            else:
                print('Invalid product quantity....')
        else:
            print('Invalid Product...Cannot update....')


    def remove_product(self,pid):

        if pid > 0:
            if self.get_product(pid):
                rows = VendorSerImpl.dao.delete_product(pid)
                return self.convert_rows_to_products(rows)

            else:
                print('Product not available...')
        else:
            print('Invalid product id...!')

    def get_all_products(self):
        rows = VendorSerImpl.dao.fetch_all_products()
        return self.convert_rows_to_products(rows)

    def convert_rows_to_products(self,rows):

        listofProducts = []
        if rows:
            # print(type(rows[0]))
            if type(rows[0]) == tuple:
                for row in rows:
                    listofProducts.append(Product(pid = row[0], pnm = row[1], pprice = row[2], pcat = row[3], pqty= row[4]))
                return listofProducts
            else:
                return Product(pid = rows[0], pnm = rows[1], pprice = rows[2], pcat = rows[3], pqty = rows[4])
        else:
            print('No record exists...')
            # print('Deleted...')
            # return listofProducts



a = VendorSerImpl()
# b=a.get_all_products()
# print(b)
# print(a.get_all_products())