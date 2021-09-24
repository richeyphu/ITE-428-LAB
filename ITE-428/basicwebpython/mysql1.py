#!\xampp\htdocs\basicwebpython\venv\Scripts\python.exe
import pymysql

print("Context-type:text/html\n")


def connectDB():
    mydatabase = pymysql.connect(host="localhost",
                                 port=3306,
                                 user="root",
                                 passwd="",
                                 cursorclass=pymysql.cursors.DictCursor,
                                 database="northwind_mysql_python")
    return mydatabase


if __name__ == '__main__':
    db = connectDB()
    with db.cursor() as cs:
        sql = """select *
                 from products
                 order by unitprice"""
        cs.execute(sql)
        result = cs.fetchall()
        for i in result:
            print("{}".format(i['ProductName']))
            print("{:,.2f}".format(i['UnitPrice']))
            print('-' * 30)
