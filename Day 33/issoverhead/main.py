import requests
from datetime import datetime
import smtplib
import time

USER = "yaredyilma11@gmail.com"
PASS = "dopellex11"
MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758  # Your longitude


def is_iss_overhead():
    response1 = requests.get(url="http://api.open-notify.org/iss-now.json")
    response1.raise_for_status()
    data1 = response1.json()

    iss_latitude = float(data1["iss_position"]["latitude"])
    iss_longitude = float(data1["iss_position"]["longitude"])
    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT <= iss_longitude - 5 <= iss_longitude + 5 and MY_LONG <= iss_longitude - 5 <= iss_longitude + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    # check if it is night
    if sunset <= time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.google.com") as connection:
            connection.starttls()
            connection.login(user=USER, password=PASS)
            connection.sendmail(
                from_addr=USER,
                to_addrs=USER,
                msg="Subject: Look Up\n\nthe ISS is above you in the sky")
