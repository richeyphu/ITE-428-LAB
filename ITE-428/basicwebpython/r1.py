#!\xampp\htdocs\basicwebpython\venv\Scripts\python.exe
print("Content-type:text/html; charset=utf-8\n")

import requests
import json
import cgi

# Request1
url = "http://localhost/basicwebpython/s1.py"
r = requests.get(url)
data = json.loads(r.content)

print("<html>")
print("<head><title>Find Products</title></head>")
print("<body>")
print("Your DATA = <br>{}".format(data))
print("</body>")
print("</html>")
