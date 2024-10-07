import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

#API keys and phone numbers redacted

STOCK_API = "12345678"
NEWS_API = "12345678"
TWILIO_SID = "12345678"
TWILIO_AUTH = "12345678"

FROM_PHONE = "12345678"
TO_PHONE = "12345678"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol":"TSLA",
    "apikey": STOCK_API,
}

stock_response = requests.get(url="https://www.alphavantage.co/query", params=stock_parameters)
stock_data = stock_response.json()

time_series = stock_data['Time Series (Daily)']
dates = list(time_series.keys())
close_tdy = float(time_series[dates[0]]['4. close'])
close_ytd = float(time_series[dates[1]]['4. close'])

diff_percentage = (close_tdy - close_ytd) / close_ytd * 100

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

date_tdy = dates[0]
date_ytd = dates[1]

news_parameters = {
    "qInTitle":COMPANY_NAME,
    "apiKey":NEWS_API,
    "from": date_ytd,
    "to": date_tdy,
    "language": "en",
    "sortBy": "popularity",
    "pageSize": 3,
}

news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
news_data = news_response.json()

## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.

if diff_percentage >= 0:
    direction = "🔺"

else:
    direction = "🔻"


if abs(diff_percentage) >= 5:
    client = Client(TWILIO_SID, TWILIO_AUTH)
    for news in news_data['articles']:
        headline = news['title']
        brief = news['description']
        content = (f"{STOCK}: {direction}{abs(round(diff_percentage,2))}\n"
                   f"Headline: {headline}\n"
                   f"Brief: {brief}"
                   )

        message = client.messages.create(
            body=content,
            from_=FROM_PHONE,
            to=TO_PHONE,
        )

        print(message.status)
