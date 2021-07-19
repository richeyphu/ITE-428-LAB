import sqlite3


def sqlQuery(db, args=[]):
    with (sqlite3.connect(db)) as conn:
        conn.row_factory = sqlite3.Row
        sql_command = '''select productId as id, productName, unitPrice * unitsInStock as StockValue
        from products
        where StockValue > ?
        order by 3 desc'''
        cursor = conn.execute(sql_command, args).fetchall()
        display(cursor)


def display(cursor):
    for v in cursor:
        print("ID = {}".format(v['id']))
        print("PRODUCT NAME = {}".format(v['productName']))
        print("STOCK VALUE = {:,.2f}".format(v['StockValue']))
        print('-' * 50)


if __name__ == '__main__':
    dbname = "myDatabase/Sqlite_Northwind.sqlite3"

    value = [float(input("Show only 'Stock Value' more than : "))]
    print()

    sqlQuery(dbname, value)
