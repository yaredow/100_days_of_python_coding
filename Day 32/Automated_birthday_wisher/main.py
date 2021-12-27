import smtplib

my_email = "yaredyilma11@gmail.com"
password = "dopellex11"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email, to_addrs="yaredyilma2020@outlook.com",
                        msg="Subject:Hello\n\nHey Yared the greatest of all time"
    )
