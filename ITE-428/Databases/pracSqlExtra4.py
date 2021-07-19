import sqlite3


def sqlQuery(db, args=[]):
    with (sqlite3.connect(db)) as conn:
        conn.row_factory = sqlite3.Row
        sql_command = '''select region, count(distinct country) as noc, count(distinct city) as ncity
        from customers
        group by region
        order by 3 desc, 1'''
        cursor = conn.execute(sql_command).fetchall()
        display(cursor)


def display(cursor):
    for v in cursor:
        try:
            print(" {:<30}{:>5}{:>12}".format(v['region'], v['noc'], v['ncity']))
        except TypeError:
            pass


if __name__ == '__main__':
    dbname = "myDatabase/Sqlite_Northwind.sqlite3"

    print('-' * 50)
    print(" Region\t\t\t\t\t\t\tCountry\t\tCity")
    print('-' * 50)
    sqlQuery(dbname)
