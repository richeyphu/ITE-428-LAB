import sqlite3


def sqlQuery(db, args=[]):
    with (sqlite3.connect(db)) as conn:
        conn.row_factory = sqlite3.Row
        sql_command = '''SELECT ProductId, ProductName, UnitPrice, UnitsInStock, Discontinued
                         FROM Products
                         WHERE ProductId = ?'''
        cursor = conn.execute(sql_command, args).fetchall()
        display(cursor)


def display(cursor):
    if len(cursor) == 0:
        print("Product Id not found.")
    else:
        for v in cursor:
            print("Product Name : {}".format(v['ProductName']))
            print("Unit Price\t : {}".format(v['UnitPrice']))
            print("In Stock\t : {}".format(v['UnitsInStock']))


def updateDb(db, args=[]):
    with (sqlite3.connect(db)) as conn:
        sql_command = '''UPDATE Products
                         SET Discontinued = 1
                         WHERE ProductId = ?'''
        conn.execute(sql_command, args)


def line():
    print('-' * 50)


if __name__ == '__main__':
    dbname = "myDatabase/Sqlite_Northwind.sqlite3"

    prodId = [input("Input Product ID : ")]

    line()
    sqlQuery(dbname, prodId)
    line()

    confirm = input("Confirm 'Discontinued' this product? (Y/N) : ").upper()
    if confirm == 'Y':
        updateDb(dbname, prodId)
        print("UPDATED!")
    line()
