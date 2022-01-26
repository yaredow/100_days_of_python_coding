from bs4 import BeautifulSoup
import requests
import smtplib
import os

headers = {
    "User_Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
}
url = "https://www.amazon.ae/Samsung-Galaxy-128GB-International-Version/dp/B088KP19HP/ref=sr_1_5?crid=1VMMG0N9XWTMG&keywords=samsung%2Bs10%2B&qid=1643183088&sprefix=samsung%2Bs10%2Bplus%2Caps%2C608&sr=8-5&th=1"
response = requests.get(url, headers=headers)
amazon_data = response.content
soup = BeautifulSoup(amazon_data, "html.parser")
price = soup.find(class_="a-price-whole").get_text()
final_price = price.split(".")[1]

# sending email when the price is below 1000
my_email = os.environ.get("MY_EMAIL")
my_password = os.environ.get("MY_PASSWORD")

if final_price < 1000:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="yaredyilma2020@gmail.com",
            msg=f"Subject:Hello Yared\n\nThe price of samsung galaxy is below {final_price}. go and grab one king")



