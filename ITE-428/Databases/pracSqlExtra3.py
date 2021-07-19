import sqlite3


def sqlQuery(db, args=[]):
    with (sqlite3.connect(db)) as conn:
        conn.row_factory = sqlite3.Row
        sql_command = '''select upper(country) as c, count(country) as noc
        from suppliers 
        group by country
        order by 2 desc, 1'''
        cursor = conn.execute(sql_command).fetchall()
        display(cursor)


def display(cursor):
    for v in cursor:
        print("{:<38} {}".format(v['c'], v['noc']))


if __name__ == '__main__':
    dbname = "myDatabase/Sqlite_Northwind.sqlite3"

    print("Supplier From\t\t\t\t\t No. of Company")
    print('-' * 50)
    sqlQuery(dbname)
