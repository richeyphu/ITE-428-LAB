import sqlite3


def sqlQuery(db, args=[]):
    with (sqlite3.connect(db)) as conn:
        conn.row_factory = sqlite3.Row
        sql_command = '''SELECT CompanyName as name, CategoryName as cat, count(ProductId) as noProd, avg(UnitPrice) as avgPrice
        FROM Suppliers
        NATURAL JOIN Categories
        NATURAL JOIN Products
        GROUP BY SupplierId, CategoryId
        ORDER BY 1'''
        cursor = conn.execute(sql_command).fetchall()
        display(cursor)


def display(cursor):
    found = len(cursor)
    print("Result: {} rows returned\n".format(found))
    for v in cursor:
        print("{} ({}) No. of Product = {} (Average price = {:.2f})".format(v['name'],
                                                                            v['cat'],
                                                                            v['noProd'],
                                                                            v['avgPrice']))


if __name__ == '__main__':
    dbname = "myDatabase/Sqlite_Northwind.sqlite3"

    sqlQuery(dbname)
