#!\xampp\htdocs\basicwebpython\venv\Scripts\python.exe
import cgi

formdata = cgi.FieldStorage()
cols = int(formdata.getvalue('cols'))
rows = int(formdata.getvalue('rows'))
msg = formdata.getvalue('msg')

print("Context-type:text/html\n")

print("<html>")
print("<head>"
      "<meta charset='UTF-8'>"
      "<title>My First Python Web</title>"
      "</head>")
print("<body>")

print("<table border='5'>")
# rows, cols = (10, 10)
# msg = "PHURIT"
for i in range(rows):
    print("<tr bgcolor='{}'>".format("Chocolate" if i % 2 == 0 else "Salmon"))
    for j in range(cols):
        print("<td align='center'>")
        if i == j:
            print("<a href='https://www.tni.ac.th/' target='_blank'>"
                  "<img src='image/tni.png' alt='TNI Logo' height='50'></a>")
        else:
            print("<b><i><u>{}</b></i></u>".format(msg))
        print("</td>")
    print("</tr>")
print("</table>")

print("</body>")
print("</html>")
