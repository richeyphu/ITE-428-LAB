import sqlite3


def sqlQuery(db, args=[]):
    with (sqlite3.connect(db)) as conn:
        # conn.row_factory = sqlite3.Row
        sql_command = '''SELECT CustomerId
                         FROM Customers'''
        cursor = conn.execute(sql_command, args).fetchall()
        return cursor


def line():
    print('-' * 50)


def inputData():
    line()
    print("ADD NEW CUSTOMER")
    line()

    compName = input("Company Name  : ")
    while compName == "":
        compName = input("Input Company Name, again : ")
    contName = getDataOrNull(input("Contact Name  : "))
    contTitle = getDataOrNull(input("Contact Title : "))
    addr = getDataOrNull(input("Address\t\t  : "))
    city = getDataOrNull(input("City\t\t  : "))
    region = getDataOrNull(input("Region\t\t  : "))
    postCode = getDataOrNull(input("Postal Code   : "))
    country = getDataOrNull(input("Country\t\t  : "))
    phone = getDataOrNull(input("Phone\t\t  : "))
    fax = getDataOrNull(input("FAX\t\t\t  : "))
    line()

    return [getId(compName), compName, contName, contTitle, addr, city, region, postCode, country, phone, fax]


def getId(name):
    id = ''.join(x.upper() for x in name if x.isalpha())
    if len(id) < 5:
        id += 'X' * (5 - len(id))
    else:
        id = id[0:5]
    num = 2
    while True:
        if idDuplicatedId(id):
            id = id[0:5] + str(num)
            num += 1
            continue
        return id


def idDuplicatedId(id):
    idList = sqlQuery(dbname)
    return (id,) in idList


def getDataOrNull(data):
    return data if data != "" else None


def insertDb(db, args=[]):
    with (sqlite3.connect(db)) as conn:
        sql_command = '''INSERT INTO CUSTOMERS
                         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        conn.execute(sql_command, args)


if __name__ == '__main__':
    dbname = "myDatabase/Sqlite_Northwind.sqlite3"

    while True:
        data = inputData()

        confirm = input("Confirm adding? (Y/N) : ").upper()
        if confirm == 'Y':
            insertDb(dbname, data)
            print("NEW CUSTOMER ADDED!")
        else:
            print("CANCELED!")
        line()

        loop = input("Input more customer? (Y/N) : ").upper()
        if loop != 'Y':
            break
        print()
