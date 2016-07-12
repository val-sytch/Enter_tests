#!/usr/bin/env python3

import cgi
from html import escape

form = cgi.FieldStorage()
ticketNumb = form.getfirst("ticket_number","none")
ticketNumb = escape(ticketNumb)

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Lucky ticket</title>
        </head>
        <body>""")

def check_for_correct_input(ticketNumb):
    correct = True
    ticketNumb = ticketNumb.strip()
    while correct:
        for digit in ticketNumb:
            if digit not in "0123456789":
                correct = False
        break
    return correct        

def checking_ticket_for_lucky(ticketNumb):
    first_3_Numb=int(ticketNumb[0])+int(ticketNumb[1])+int(ticketNumb[2])
    second_3_Numb=int(ticketNumb[3])+int(ticketNumb[4])+int(ticketNumb[5])
    if first_3_Numb==second_3_Numb:
        print('<h2>Congratulations!Your ticket is lucky</h2>')
    else:
        print('<h2>Sorry, this ticket is not lucky. Try next time</h2>')

if check_for_correct_input(ticketNumb) ==True:
    checking_ticket_for_lucky(ticketNumb)
else:
    print("<h2>Oops! Inputed number isn't correct. Please try again!</h2>")

print("""<a href="../index.html">Return to main page</a>
        </body>
        </html>""")
