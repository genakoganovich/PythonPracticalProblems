#!/usr/bin/env python3
import cgi
import html

print("Content-type: text/html\n")
print("""<html>
        <body>""")


print("<table>")

for i in range(1, 11):
    print("<tr>")
    for j in range(1, 11):
        print(f"<td>{i * j}</td>")

    print("</tr>")

print("</table>")

print("""</body>
        </html>""")