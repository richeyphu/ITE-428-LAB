import sqlite3


def sqlQuery(db, args=[]):
    with (sqlite3.connect(db)) as conn:
        conn.row_factory = sqlite3.Row
        sql_command = '''select CategoryName as cat, count(ProductId) as pd, sum(unitPrice * unitsInStock) as StockValue
        from products
        natural join categories
        group by CategoryId
        having StockValue > ?
        order by 3'''
        cursor = conn.execute(sql_command, args).fetchall()
        display(cursor)


def display(cursor):
    found = len(cursor)
    print("Found {} Category(s)".format(found))
    for i, v in enumerate(cursor):
        print("{:>2}.) {:<20} {:>5} PD. {:>15,.2f} Baht".format(i + 1, v['cat'], v['pd'], v['StockValue']))


if __name__ == '__main__':
    dbname = "myDatabase/Sqlite_Northwind.sqlite3"

    value = [float(input("See Value of Stock by Category > : "))]
    print('\n')

    sqlQuery(dbname, value)
