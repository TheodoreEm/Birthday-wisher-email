import smtplib
from datetime import datetime
import pandas
import random

MY_EMAIL = "email"
PASSWORD = "password"
# Creating tuple with today's month and date
today = (datetime.now().month, datetime.now().day)

# Reading csv with pandas
data = pandas.read_csv("birthdays.csv")
# Creating a  dictionary with value and key a taple of month and day and content all the row
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# Checking if the today's month and day is in the birth_dictionary
if today in birthday_dict:
    # To get the person's row we create a variable from the dictionary with key and value the tuple 'today'
    birthday_person = birthday_dict[today]
    # Creating a variable to get the path for the files with the wishes.
    # Also with the random module picking a random  from the letters
    filepath = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(filepath) as letter_file:
        contents = letter_file.read()
        # With replace method replace the space of '[Name]' with the persons name from the
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday\n\n{contents}"
        )



