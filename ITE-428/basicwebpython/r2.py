#!\xampp\htdocs\basicwebpython\venv\Scripts\python.exe
print("Content-type:text/html; charset=utf-8\n")

import requests
import json
import cgi

# Request2
form = cgi.FieldStorage()
search_id = form.getvalue("product_ID")
url = "http://localhost/basicwebpython/s2.py"
mypara = {"ID": "{}".format(search_id)}
r = requests.get(url, params=mypara)
data = json.loads(r.content)

print("<html>")
print("<head><title>Find Products</title></head>")
print("<body>")
print("Your DATA = {}".format(data))
print("</body>")
print("</html>")
