from End_to_end_App.Shopping_Cart.Vendor_DAO_info import VendorDAO
from End_to_end_App.Shopping_Cart.DB_Conn import *

class VendorDAOImpl(VendorDAO):

    conn = None
    def __init__(self):
        VendorDAOImpl.conn = get_connection()
        # self.createTable()

        # print('Database Created')

    def createTable(self):
        SQL = '''
        CREATE TABLE IF NOT EXISTS venproduct_info (
            product_id INT AUTO_INCREMENT,
            product_name VARCHAR(255) NOT NULL,
	        product_price FLOAT NOT NULL,
	        product_cat VARCHAR(255) NOT NULL,
	        product_qty INT NOT NULL,
	        PRIMARY KEY (product_id)
	        )
            '''
        cursor = VendorDAOImpl.conn.cursor()
        cursor.execute(SQL)
        VendorDAOImpl.conn.commit()

    def insert_product(self,pr):
        SQL = 'insert into venproduct_info values('
        SQL += str(pr.productId) + ",'" + pr.productName + "'," + str(pr.productPrice) + ",'" + pr.productCategory + "'," + str(pr.productQuantity) + " " + ")"
        cursor = VendorDAOImpl.conn.cursor()
        cursor.execute(SQL)
        VendorDAOImpl.conn.commit()


    def fetch_product(self,pid):
        SQL = "SELECT * FROM venproduct_info WHERE PRODUCT_ID=" + str(pid)
        cursor = VendorDAOImpl.conn.cursor()
        cursor.execute(SQL)
        return cursor.fetchone()

    def modify_product(self,prod):
        SQL = 'update venproduct_info set '
        SQL += "product_name='" + prod.productName + "',product_price=" + str(prod.productPrice) + ",product_cat='" +\
               prod.productCategory + "',product_qty=" + str(prod.productQuantity) + " where product_id=" + str(prod.productId)
        # SQL += "where product_id =" + str(prod.productId) + ')'
        print(SQL)

        cursor = VendorDAOImpl.conn.cursor()

        cursor.execute(SQL)
        VendorDAOImpl.conn.commit()

    def delete_product(self,pid):
        SQL = ' delete from venproduct_info where product_id=' + str(pid)
        cursor = VendorDAOImpl.conn.cursor()
        cursor.execute(SQL)
        VendorDAOImpl.conn.commit()
        return self.fetch_all_products()

    def fetch_all_products(self):
        SQL = 'select * from venproduct_info'
        cursor = VendorDAOImpl.conn.cursor()
        cursor.execute(SQL)
        return cursor.fetchall()