#!\xampp\htdocs\basicwebpython\venv\Scripts\python.exe
import pymysql

print("Context-type:text/html\n")


def connectDB():
    mydatabase = pymysql.connect(host="localhost",
                                 port=3306,
                                 user="root",
                                 passwd="",
                                 cursorclass=pymysql.cursors.DictCursor,
                                 database="northwind_mysql_python")
    return mydatabase


if __name__ == '__main__':
    db = connectDB()
    with db.cursor() as cs:
        sql = """select ProductName, UnitPrice, UnitsInStock
                 from products
                 where UnitPrice > 50
                 order by UnitPrice"""
        cs.execute(sql)
        result = cs.fetchall()

    print("<html>")
    print("""<head>
             <meta charset='UTF-8'>
             <title>My Products</title>
             </head>""")
    print("<body>")

    print("<table border='5'>")
    print("""<tr>
             <td>No.</td>
             <td>ProductName</td>
             <td>UnitPrice</td>
             <td>UnitsInStock</td>
             <td>ValueInStock</td>
             </tr>""")
    for i, v in enumerate(result):
        ProductName = v['ProductName']
        UnitPrice = v['UnitPrice']
        UnitsInStock = v['UnitsInStock']
        ValueInStock = UnitPrice * UnitsInStock
        print(f"""<tr>
                 <th>{i + 1}</th>
                 <th>{ProductName}</th>
                 <th>{UnitPrice:,.2f}</th>
                 <th>{UnitsInStock}</th>
                 <th>{ValueInStock:,.2f}</th>
                 </tr>""")
    print("</table>")

    print("</body>")
    print("</html>")

