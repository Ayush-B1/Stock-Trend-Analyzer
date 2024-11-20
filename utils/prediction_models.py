import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

def train_price_prediction_model(stock_data):
    try:
        if 'Close' not in stock_data.columns:
            raise KeyError("'Close' column is required in the stock data.")

        stock_data['Day'] = np.arange(len(stock_data))
        X = stock_data[['Day']].values
        y = stock_data['Close'].values

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = LinearRegression()
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        predictions = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})

        return model, predictions

    except Exception as e:
        raise RuntimeError(f"Error training prediction model: {e}")
