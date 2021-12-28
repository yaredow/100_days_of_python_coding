import smtplib
import random
import datetime as dt

my_email = "yaredyilma11@gmail.com"
password = "dopellex11"
# opening the text file
with open("quotes.txt") as file:
    file_list = file.readlines()
daily_quote = random.choice(file_list)
# obtaining the current day of the week
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    # sending the email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="yaredyilma2020@outlook.com",
            msg=f"Subject:Monday Motivation\n\n{daily_quote}"
        )
