#!\xampp\htdocs\basicwebpython\venv\Scripts\python.exe
import Database
import cgi

print("Content-type:text/html; charset=utf-8\n")


if __name__ == '__main__':
    formData = cgi.FieldStorage()
    start_price = float(formData.getvalue('start'))
    end_price = float(formData.getvalue('end'))
    order_by = formData.getvalue('sort')
    param = [start_price, end_price]

    db = Database.connectDb()
    with db.cursor() as cs:
        sql = """select ProductName, UnitPrice, UnitsInStock
                 from products
                 where UnitPrice between %s and %s
                 order by UnitPrice {}""".format(order_by)
        cs.execute(sql, param)
        result = cs.fetchall()

    print("<html>")
    print("<head><title>Find Products</title></head>")
    print("<body>")
    print("<table border='5' align='center'>")
    print("""<tr>
             <th>No.</th>
             <th>ProductName</th>
             <th>UnitPrice</th>
             <th>UnitsInStock</th>
             <th>ValueInStock</th>
             </tr>""")
    for i, v in enumerate(result):
        ProductName = v['ProductName']
        UnitPrice = v['UnitPrice']
        UnitsInStock = v['UnitsInStock']
        ValueInStock = UnitPrice * UnitsInStock
        print(f"""<tr>
                  <td>{i + 1}</td>
                  <td>{ProductName}</td>
                  <td>{UnitPrice:,.2f}</td>
                  <td>{UnitsInStock}</td>
                  <td>{ValueInStock:,.2f}</td>
                  </tr>""")
    print("</table>")

    print("</body>")
    print("</html>")
