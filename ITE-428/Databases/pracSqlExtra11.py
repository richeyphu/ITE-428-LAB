import sqlite3


def sqlQuery(db, args=[]):
    with (sqlite3.connect(db)) as conn:
        conn.row_factory = sqlite3.Row
        sql_command = '''SELECT ProductId, ProductName, UnitPrice, 
                         UnitPrice - (SELECT avg(UnitPrice)
                                      FROM Products) as PriceDiff
                         FROM Products
                         WHERE UnitPrice > (SELECT avg(UnitPrice)
                                            FROM Products)
                         ORDER BY 3 DESC'''
        cursor = conn.execute(sql_command).fetchall()
        display(cursor)


def display(cursor):
    line()
    print("รหัส สินค้า\t\t\t\t\t\t\t\t\t\tราคาสินค้า\t\t\t ราคาสูงกว่าราคาเฉลี่ย")
    line()
    for v in cursor:
        print("{:<3} {:<40} {:>10,.2f} {:>20,.2f}".format(v['ProductId'],
                                                          v['ProductName'],
                                                          v['UnitPrice'],
                                                          v['PriceDiff']))
    line()


def line():
    print('-' * 80)


if __name__ == '__main__':
    dbname = "myDatabase/Sqlite_Northwind.sqlite3"

    sqlQuery(dbname)
