import sqlite3
import csv
import datetime


def exportToCsv(data):
    currentdate = str(datetime.datetime.now())
    currentdate = currentdate.split('.')[0]
    currentdate = currentdate.replace(':', '-')
    print("{}".format(currentdate))
    with (open(file="Exportdata/mydata{}.csv".format(currentdate), mode='w', encoding='utf8', newline="")) as f:
        fw = csv.writer(f)
        fw.writerow(['Product', 'Price'])
        fw.writerows(data)


def sqlQuery(DB):
    with (sqlite3.connect(DB)) as conn:
        conn.row_factory = sqlite3.Row
        sql_command = '''select productname, unitprice
        from products 
        '''
        cursor = conn.execute(sql_command)
        found = len(conn.execute(sql_command).fetchall())
        print("Found {} Records".format(found))
        print('=' * 50)
        for i, v in enumerate(cursor):
            print("No.         : {}".format(i + 1))
            print("ProductName : {}".format(v['Productname']))
            print("UnitPrice   : {}".format(v['unitprice']))
            print('-' * 50)


def sqlQuery2(DB, params):  # params is list
    with (sqlite3.connect(DB)) as conn:
        conn.row_factory = sqlite3.Row
        sql_command = '''select productname, unitprice
        from products 
        where unitprice between ? and ?
        order by 2 desc'''
        cursor = conn.execute(sql_command, params)
        found = len(conn.execute(sql_command, params).fetchall())
        print("Found {} Records".format(found))
        print('=' * 50)
        for i, v in enumerate(cursor):
            print("No.         : {}".format(i + 1))
            print("ProductName : {}".format(v['ProductName']))
            print("UnitPrice   : {}".format(v['unitPrice']))
            print('-' * 50)
        exportToCsv(conn.execute(sql_command, params))


def manageData(DB):
    with (sqlite3.connect(DB)) as conn:
        sql_command = '''insert into categories
        values ('20','cat','cat cat')'''
        conn.execute(sql_command)
        conn.commit()
        print("Insert Success!")


if __name__ == '__main__':
    dbname = "myDatabase/Sqlite_Northwind.sqlite3"
    p = [50, 100]
    # sqlQuery(dbname)
    sqlQuery2(dbname, p)
    # manageData(dbname)
