import sqlite3


def sqlQuery(db, args=[]):
    with (sqlite3.connect(db)) as conn:
        conn.row_factory = sqlite3.Row
        sql_command = '''select productname, unitprice
                         from products 
                         natural join categories
                         where lower(categoryname) = lower(?)
                         order by 1'''
        cursor = conn.execute(sql_command, args).fetchall()
        found = len(cursor)
        print("{} Found {} Record(s)".format(args[0].title(), found))
        for i, v in enumerate(cursor):
            print("{:>2}.) {:<35} :{:>10.2f} Baht".format(i + 1, v['Productname'], v['UnitPrice']))


if __name__ == '__main__':
    dbname = "myDatabase/Sqlite_Northwind.sqlite3"

    cat = [input("Enter your category name to see : ")]
    print()

    sqlQuery(dbname, cat)
