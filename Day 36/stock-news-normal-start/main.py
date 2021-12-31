import requests
from twilio.rest import Client
import os

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

ACCOUNT_SID = "ACe8a33132e138ffa600f277406243884f"
AUTH_TOKEN = "4578cf8cc79fb16c6ba5e369c11bb895"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "9e46a914364c49afaf81a2566c1f40a8"
API_KEY = "NXZ17V2USCUPZ5JU"
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": API_KEY,
}
response = requests.get(url=STOCK_ENDPOINT, params=parameters)
data = response.json()
time_series = data["Time Series (Daily)"]
data_list = [Value for (Name, Value) in time_series.items()]
yesterday_data = data_list[0]
yesterday_closing = yesterday_data["4. close"]
before_yesterday = data_list[1]
before_yesterday_closing = before_yesterday["4. close"]
difference = abs(round(float(yesterday_closing) - float(before_yesterday_closing), 2))
percentage_difference = (float(difference) / float(before_yesterday_closing) * 100)
if percentage_difference > 1:
    news_param = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_param)
    news_data = news_response.json()
    article = news_data["articles"]
    # print the first 3 articles
    first_articles = article[:3]
    print(first_articles)
    # getting individual articles
    news = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in first_articles]
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    for new in news:
        message = client.messages \
            .create(
            body=f"news[0]",
            from_='+13236010511',
            to='+251928315616'
        )
        print(message.status)





