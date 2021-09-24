#!\xampp\htdocs\basicwebpython\venv\Scripts\python.exe
import cgi
from datetime import datetime
import sqlite3
from hashlib import md5

formdata = cgi.FieldStorage()
user = formdata.getvalue('user')
pwd = formdata.getvalue('pass')
name = formdata.getvalue('name')
lname = formdata.getvalue('lname')
pwd_hashed = md5(pwd.encode()).hexdigest()
param = [user, pwd_hashed, name, lname, datetime.now(), datetime.now()]

dbname = "Databases/practice.sqlite3"

with (sqlite3.connect(dbname)) as conn:
    conn.row_factory = sqlite3.Row
    sql_command = '''insert into users
                     values (?, ?, ?, ?, ?, ?)'''
    conn.execute(sql_command, param)
    conn.commit()

print("Context-type:text/html\n")

print("<html>")
print("""<head>
         <meta charset='UTF-8'>
         <title>Registration</title>
         </head>""")
print("<body>")
print("<h1>Registration Complete!</h1>")
print("<h2>Welcome, {} {}!</h2>".format(name, lname))
print("</body>")
print("</html>")
