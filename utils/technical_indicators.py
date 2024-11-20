import pandas as pd

def calculate_technical_indicators(stock_data):
    try:
        if 'Close' not in stock_data.columns:
            raise KeyError("'Close' column is required in the stock data.")

        stock_data['Moving_Avg'] = stock_data['Close'].rolling(window=20).mean()

        delta = stock_data['Close'].diff(1)
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)
        avg_gain = gain.rolling(window=14).mean()
        avg_loss = loss.rolling(window=14).mean()
        rs = avg_gain / avg_loss
        stock_data['RSI'] = 100 - (100 / (1 + rs))

        return stock_data

    except Exception as e:
        raise RuntimeError(f"Error calculating technical indicators: {e}")
