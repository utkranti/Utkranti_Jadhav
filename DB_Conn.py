import  pymysql

conn = None
def get_connection():
    global conn
    if conn == None:

        conn = pymysql.connect('localhost','root','chiu','DB_persist')

    return conn
    # print(conn)

# a = get_connection()
# print(a)