import sqlite3


def sqlQuery(db, args=[]):
    with (sqlite3.connect(db)) as conn:
        conn.row_factory = sqlite3.Row
        sql_command = '''select productname, unitprice
        from products 
        natural join categories
        where unitprice between {} and {}
        order by 2 {}, 1'''.format(args[0], args[1], args[2])
        cursor = conn.execute(sql_command).fetchall()
        display(cursor)


def display(cursor):
    found = len(cursor)
    print("Found {} Record(s)".format(found))
    for i, v in enumerate(cursor):
        print("{:>2}.) {:<35} :{:>10.2f} Baht".format(i + 1, v['Productname'], v['UnitPrice']))


if __name__ == '__main__':
    dbname = "myDatabase/Sqlite_Northwind.sqlite3"

    while True:
        start = int(input("Enter start price you want to see : "))
        end = int(input("Enter end price you want to see : "))
        if end > start:
            break
        print(">> End price should be more that Start price <<")

    while True:
        print("Sort price : [1] Ascending  [2] Descending")
        sort = input("Select [1] or [2] : ")
        if sort in ('1', '2'):
            sort = "ASC" if sort == '1' else "DESC"
            break
        print(">> Please select again <<")
    print()

    sqlQuery(dbname, [start, end, sort])
