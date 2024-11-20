import streamlit as st
import pandas as pd
from utils.data_fetching import fetch_stock_data
from utils.technical_indicators import calculate_technical_indicators
from utils.prediction_models import train_price_prediction_model
from utils.sentiment_analysis import analyze_sentiment
from utils.visualization import plot_stock_data, plot_predictions, plot_technical_indicators
from utils.notifications import send_sms

st.title("Stock Trend Analyzer")

# Input for stock symbol
stock_symbol = st.text_input("Enter Stock Symbol (e.g., AAPL, MSFT):", "AAPL")
phonenumber = st.text_input("Enter your phone number (with country code, e.g., +1234567890)")
send_sms_option = st.checkbox("Send SMS Report")

# Check for valid phone number format
def validate_phone_number(number):
    if number.startswith("+") and len(number) >= 10:
        return True
    return False

if st.button("Analyze"):
    try:
        # Step 1: Fetch stock data
        st.subheader("Fetching Stock Data...")
        stock_data = fetch_stock_data(stock_symbol)

        if stock_data.empty or not isinstance(stock_data, pd.DataFrame):
            st.error("Failed to fetch valid stock data. Please check the stock symbol and try again.")
        else:
            st.success("Data fetched successfully!")
            st.write("Stock Data Sample", stock_data.head())

            # Step 2: Display stock data
            st.subheader("Stock Price Chart")
            plot_stock_data(stock_data)

            # Step 3: Add and display technical indicators
            st.subheader("Technical Indicators")
            stock_data = calculate_technical_indicators(stock_data)

            if "Moving_Avg" in stock_data.columns and "RSI" in stock_data.columns:
                plot_technical_indicators(stock_data)
                st.write("Technical Indicators Sample", stock_data.head())
            else:
                st.error("Failed to calculate technical indicators.")

            # Step 4: Train and visualize predictions
            st.subheader("Stock Price Prediction")
            try:
                model, predictions = train_price_prediction_model(stock_data)
                st.write("Predictions Sample", predictions.head())
                st.line_chart(predictions)
            except Exception as e:
                st.error(f"Error in prediction model: {e}")

            # Step 5: Perform sentiment analysis
            st.subheader("Sentiment Analysis")
            try:
                sentiment_score = analyze_sentiment(stock_symbol)
                st.write(f"Sentiment Score: {sentiment_score}")
            except Exception as e:
                st.error(f"Error in sentiment analysis: {e}")

            # Step 6: Optional SMS Report
            if send_sms_option:
                if validate_phone_number(phonenumber):
                    st.subheader("Sending SMS Report")
                    try:
                        sms_status = send_sms(phonenumber, stock_data, stock_symbol)
                        st.success(sms_status)
                    except Exception as e:
                        st.error(f"Failed to send SMS: {e}")
                else:
                    st.error("Please enter a valid phone number (with country code).")

    except Exception as main_error:
        st.error(f"An unexpected error occurred: {main_error}")
