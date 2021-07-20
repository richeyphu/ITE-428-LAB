import sqlite3


def sqlQuery(db, args=[]):
    with (sqlite3.connect(db)) as conn:
        conn.row_factory = sqlite3.Row
        sql_command = '''select firstname || ' ' || lastname || ' , ' || TitleOfCourtesy as name, count(orderId) as 'order'
                         from employees
                         natural join orders
                         group by employeeId
                         order by 2'''
        cursor = conn.execute(sql_command).fetchall()
        display(cursor)


def display(cursor):
    for i, v in enumerate(cursor):
        print("{}.) {:<30} {:>5}".format(i + 1, v['name'].upper(), v['order']))


if __name__ == '__main__':
    dbname = "myDatabase/Sqlite_Northwind.sqlite3"

    sqlQuery(dbname)
