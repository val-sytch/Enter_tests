#!/usr/bin/env python3

import cgi
from html import escape

form = cgi.FieldStorage()
Name1 = form.getfirst("YourName", "unnown")
Name1 = escape(Name1)

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Greeting with name</title>
        </head>
        <body>""")

print("<h1>Hello, {}! Nice to meet you!</h1>".format(Name1))


print("""<a href="../index.html">Return to main page</a>
        </body>
        </html>""")
