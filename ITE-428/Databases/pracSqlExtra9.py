import sqlite3


def sqlQuery(db, args=[]):
    with (sqlite3.connect(db)) as conn:
        conn.row_factory = sqlite3.Row
        sql_command = '''SELECT OrderId, OrderDate, Customer, ProductName, Price, CompanyName
        FROM Invoices
        WHERE OrderId = ?
        ORDER BY 4'''
        cursor = conn.execute(sql_command, args).fetchall()
        display(cursor)


def display(cursor):
    print("Order ID   : {}".format(cursor[0]['OrderId']))
    print("Order Date : {}".format(cursor[0]['OrderDate']))
    print("Customer   : {}".format(cursor[0]['Customer']))
    print('-' * 50)

    total_price = 0
    for i, v in enumerate(cursor):
        print("{}.) {:<35}{:>9,.2f}".format(i + 1, v['ProductName'], v['Price']))
        total_price += v['Price']
    vat = total_price * 7 / 100

    print('-' * 50)
    print("{:<24}{:<11} : {:>10,.2f}".format("", "TOTAL PRICE", total_price))
    print("{:<24}{:<11} : {:>10,.2f}".format("", "VAT (7%)", vat))
    print("{:<24}{:<11} : {:>10,.2f}".format("", "NET PRICE", total_price + vat))
    print('-' * 50)


if __name__ == '__main__':
    dbname = "myDatabase/Sqlite_Northwind.sqlite3"

    orderId = [input("กรุณากรอก Order ID ที่ต้องการดูข้อมูล : ")]
    print()

    try:
        sqlQuery(dbname, orderId)
    except IndexError:
        print("ไม่พบข้อมูล")
