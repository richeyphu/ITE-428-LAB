#!\xampp\htdocs\basicwebpython\venv\Scripts\python.exe
print("Context-type:text/html\n")

print("<html>")
print("<head><title>My First Python Web</title></head>")
print("<body>")

print("<table border='5'>")
rows, cols = (10, 10)
for i in range(rows):
    print("<tr bgcolor='{}'>".format("Chocolate" if i % 2 == 0 else "Salmon"))
    for j in range(cols):
        print("<td align='center'>")
        print("<b><i><u>PHURIT</b></i></u>")
        print("</td>")
    print("</tr>")
print("</table>")

print("</body>")
print("</html>")
