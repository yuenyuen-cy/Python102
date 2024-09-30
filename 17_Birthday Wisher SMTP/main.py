import pandas as pd
import datetime as dt
import smtplib
import random

my_email = "youremail@gmail.com"
password = "pass1234"

data = pd.read_csv("birthdays.csv")

now = dt.datetime.now()
day = now.day
month = now.month
year = now.year

birthday = data[(data["day"] == day) & (data["month"] == month)]

for index, row in birthday.iterrows():
    birthday_name = row["name"]
    birthday_email = row["email"]

random_letter = f"letter_templates/letter_{random.randint(1,3)}.txt"
with open (random_letter, 'r') as letter_text:
    letter = letter_text.read()
    name_letter = letter.replace("[NAME]", birthday_name)

if  not birthday.empty:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_email,
            msg=f"Subject: Happy Birthday, {birthday_name}!!!\n\n{name_letter}")
