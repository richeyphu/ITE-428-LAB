#!\xampp\htdocs\basicwebpython\venv\Scripts\python.exe
print("Content-type:text/html; charset=utf-8\n")

import Database
import json
import cgi

# Service2
db = Database.connectDb()
form = cgi.FieldStorage()
search_id = form.getvalue('ID')

with db.cursor() as cs:
    sql = """select * 
             from products
             where productid = {}""".format(search_id)
    cs.execute(sql)
    rows = cs.fetchall()
    # json -> list of dictionary [{},{},...]
    result = []
    for i in rows:
        data = {"id": "{}".format(i['ProductID']),
                "name": "{}".format(i['ProductName']),
                "price": "{}".format(i['UnitPrice']),
                }
        result.append(data)

    print(json.dumps(result))
