import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 1.352083
MY_LONG = 103.819839
MY_EMAIL = "your_email@gmail.com"
PASSWORD = "pass1234"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

longitude = float(data["iss_position"]["longitude"])
latitude = float(data["iss_position"]["latitude"])

#Your position is within +/- 5 degree of the ISS position

range_degrees = 5

lat_start = latitude - range_degrees
lat_stop = latitude + range_degrees
long_start = longitude - range_degrees
long_stop = longitude + range_degrees

iss_close =  lat_start <= MY_LAT <= lat_stop and long_start <= MY_LONG <= long_stop

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid": "Asia/Singapore"
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params = parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
hour_now = time_now.hour

sky_is_dark = hour_now < sunrise or hour_now > sunset


#If the ISS is close to my current position & it is currently dark, email me to look up
if iss_close and sky_is_dark:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject: Look up!\n\nThe ISS is above you in the sky.")
