# import smtplib

# my_email = "appbreweryinfo@gmail.com"
# password = "abcd1234()"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="appbrewerytesting@yahoo.com",
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )


import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=1995, month=12, day=15)
print(date_of_birth)