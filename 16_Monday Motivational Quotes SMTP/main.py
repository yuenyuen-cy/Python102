import datetime as dt
import smtplib
import random

### Use datetime module to obtain current day of week ##
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 6:

    ### Open quotes ###
    with open("quotes.txt") as file:
        quotes = file.readlines()
    list_of_quotes = [quote.strip() for quote in quotes]

    ### Use random module to pick random quote #
    weekly_quote = random.choice(list_of_quotes)

    ### Use smtplib to send email to yourself ###
    my_email = "myemail@gmail.com" # replace with your email
    password = "1234abcd" # take app password from gmail settings

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="test123@gmail.com", # the email you want to send to
            msg=f"Subject: Monday Motivational Quotes\n\n\n"
                f"{weekly_quote}"
                f"\n\nHave a great week,\nYour favourite girlfriend")