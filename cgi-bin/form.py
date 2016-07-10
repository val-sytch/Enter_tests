#!/usr/bin/env python3
import cgi

form = cgi.FieldStorage()
Name1 = form.getfirst("Name", "не задано")

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Greeting with name</title>
        </head>
        <body>""")

print("<p>Hello, {}! Nice to meet you</p>".format(Name1))


print("""</body>
        </html>""")
