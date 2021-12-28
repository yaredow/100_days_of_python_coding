from datetime import *
import pandas
import random
import smtplib

now = datetime.now()
day = now.day
month = now.month
today = (month, day)
email = "yaredyilma11@gmail.com"
password = "dopellex11"
# reading the csv
data = pandas.read_csv("birthdays.csv")
new_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today in new_dict:
    birthday_person = new_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as textFile:
        letter = textFile.read()
        new_letter = letter.replace("[NAME]", birthday_person["name"])
        final_letter = new_letter.replace("Angela", "Yared")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Birthday Wish\n\n{final_letter}")
