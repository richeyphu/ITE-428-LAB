#!\xampp\htdocs\basicwebpython\venv\Scripts\python.exe
print("Content-type:text/html; charset=utf-8\n")

import Database
import json

# Service1
db = Database.connectDb()
with db.cursor() as cs:
    sql = "select * from products"
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
