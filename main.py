import smtplib
import datetime as dt
import random

my_email = 'pythonmaven29@gmail.com'
my_pass = 'pxuadatgwkvfjeot'

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 1:
    with open('quotes.txt') as file:
        all_quotes = file.readlines()
        quotes = random.choice(all_quotes)

        with smtplib.SMTP('smtp.gmail.com') as conn:
            conn.starttls()
            conn.login(user=my_email, password=my_pass)
            conn.sendmail(
                from_addr=my_email,
                to_addrs='pycharmist.py@gmail.com',
                msg=f'Subject: Quote of the day\n\n {quotes}'
            )

