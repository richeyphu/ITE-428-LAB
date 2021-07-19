import sqlite3


def sqlQuery(db, args=[]):
    with (sqlite3.connect(db)) as conn:
        conn.row_factory = sqlite3.Row
        sql_command = '''SELECT p.ProductId, ProductName, count(p.ProductId) as NoSales
                         FROM Products p
                         JOIN OrdersDetails o ON p.ProductId = o.ProductId
                         GROUP BY p.ProductId
                         HAVING NoSales > ?'''
        cursor = conn.execute(sql_command, args).fetchall()
        display(cursor)


def display(cursor):
    print("Found = {}".format(len(cursor)))
    line()
    print("รหัส สินค้า")
    line()
    for v in cursor:
        print("{:<3} {}".format(v['ProductId'], v['ProductName']))


def line():
    print('-' * 50)


if __name__ == '__main__':
    dbname = "myDatabase/Sqlite_Northwind.sqlite3"

    sales = [int(input("กรอกจำนวนที่สินค้าขายได้มากกว่ากี่ครั้ง : "))]

    sqlQuery(dbname, sales)
