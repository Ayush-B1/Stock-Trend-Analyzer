import requests
import pandas as pd

def fetch_stock_data(stock_symbol):
    API_URL = "https://www.alphavantage.co/query"
    API_KEY = ""

    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": stock_symbol,
        "apikey": API_KEY,
        "outputsize": "compact"
    }

    response = requests.get(API_URL, params=params)
    data = response.json()

    # Check if the response contains the expected key
    if "Time Series (Daily)" not in data:
        raise ValueError(f"Failed to fetch data for symbol: {stock_symbol}")

    time_series = data["Time Series (Daily)"]

    # Convert the data into a pandas DataFrame
    stock_data = pd.DataFrame.from_dict(time_series, orient="index", dtype=float)
    stock_data.index = pd.to_datetime(stock_data.index)  # Convert index to datetime
    stock_data = stock_data.rename(columns={
        "1. open": "Open",
        "2. high": "High",
        "3. low": "Low",
        "4. close": "Close",
        "5. volume": "Volume"
    })
    stock_data = stock_data.sort_index()  # Sort by date

    return stock_data
