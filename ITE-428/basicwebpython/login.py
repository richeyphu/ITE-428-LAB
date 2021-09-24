#!\xampp\htdocs\basicwebpython\venv\Scripts\python.exe
import cgi
from datetime import datetime
import sqlite3
from hashlib import md5

formdata = cgi.FieldStorage()
user = formdata.getvalue('user')
pwd = formdata.getvalue('pass')
pwd_hashed = md5(pwd.encode()).hexdigest()
dbname = "Databases/practice.sqlite3"

with (sqlite3.connect(dbname)) as conn:
    conn.row_factory = sqlite3.Row
    sql_command = '''SELECT username, password, name, lastname
                     FROM users
                     WHERE username = ? AND password = ?'''
    cursor = conn.execute(sql_command, [user, pwd_hashed]).fetchall()
    found = len(cursor)
    if found:
        AUTH = True
        name = cursor[0]['name']
        lastname = cursor[0]['lastname']
        sql_command = '''UPDATE users
                         SET lastaccess = ?
                         WHERE username = ?'''
        conn.execute(sql_command, [datetime.now(), user])
    else:
        AUTH = False

print("Context-type:text/html\n")

print("<html>")
print("""<head>
         <meta charset='UTF-8'>
         <title>Login Welcome</title>
         </head>""")
print("<body>")
if AUTH:
    print("<h1>Hello, {} {}!</h1>".format(name, lastname))
else:
    print("<h1>ERROR: <i>Username or Password INCORRECT</i></h1>")
print("</body>")
print("</html>")
