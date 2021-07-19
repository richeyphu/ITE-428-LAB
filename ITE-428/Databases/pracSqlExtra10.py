import sqlite3


def sqlQuery(db, args=[]):
    with (sqlite3.connect(db)) as conn:
        conn.row_factory = sqlite3.Row
        sql_command = '''SELECT Country, count(OrderId) as 'NoOrder', 
                                sum(UnitPrice * Quantity - UnitPrice * Quantity * Discount) * 1.07 as 'NetPrice', 
                                avg(UnitPrice * Quantity - UnitPrice * Quantity * Discount) * 1.07 as 'Price/Order'
                         FROM Orders
                         NATURAL JOIN OrdersDetails
                         NATURAL JOIN Customers
                         GROUP BY Country
                         ORDER BY 4 DESC'''
        cursor = conn.execute(sql_command).fetchall()
        display(cursor)


def display(cursor):
    print(" Show Customers by Sales")
    print('-' * 60)
    print(" Country\t\tNo.Of Order\t\tNET Price\t\tPrice/Order")
    print('-' * 60)
    for v in cursor:
        print(" {:<15} {:>5} {:>19,.2f} {:>14,.2f}".format(v['Country'], v['NoOrder'], v['NetPrice'], v['Price/Order']))


if __name__ == '__main__':
    dbname = "myDatabase/Sqlite_Northwind.sqlite3"

    sqlQuery(dbname)
